import sys
import subprocess
import pandas as pd
import speech_recognition as sr
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QTabWidget, QTableWidget, QTableWidgetItem, QSizePolicy
)

# ----------------------------
# Header Section
# ----------------------------
class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignLeft)
        
        # App Logo
        self.logo = QLabel()
        
        # App Name
        self.app_name = QLabel("Request a dance from SPOT!")
        self.app_name.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.app_name)
        
        self.layout.addStretch()
        self.setLayout(self.layout)

# ----------------------------
# Speech Recognition Worker
# ----------------------------
class SpeechWorker(QObject):
    result = pyqtSignal(str)
    finished = pyqtSignal()
    
    def __init__(self, recognizer, microphone):
        super().__init__()
        self.recognizer = recognizer
        self.microphone = microphone
        self._is_running = True
    
    def run(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self._is_running:
                try:
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
                    text = self.recognizer.recognize_google(audio)
                    self.result.emit(text)
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    self.result.emit("Speech not recognized.")
                except sr.RequestError:
                    self.result.emit("Could not request results from service.")
        self.finished.emit()
    
    def stop(self):
        self._is_running = False

# ----------------------------
# Speech Recognition Section
# ----------------------------
class SpeechRecognitionSection(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        
        # Detected Speech Display
        self.detected_speech = QTextEdit()
        self.detected_speech.setReadOnly(False)
        self.detected_speech.setFixedHeight(self.detected_speech.fontMetrics().height() * 2)  # Fixed height for 2 lines
        self.layout.addWidget(QLabel("Detected Speech:"))
        self.layout.addWidget(self.detected_speech)
        
        # Buttons
        self.button_layout = QHBoxLayout()
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_text)
        self.button_layout.addWidget(self.clear_button)
        
        self.push_to_talk_button = QPushButton("Push to Talk")
        self.push_to_talk_button.setEnabled(False)
        self.push_to_talk_button.setCheckable(True)
        self.push_to_talk_button.pressed.connect(self.start_listening)
        self.push_to_talk_button.released.connect(self.stop_listening)
        self.button_layout.addWidget(self.push_to_talk_button)
        
        # New "Send to Robot" Button
        self.send_to_robot_button = QPushButton("Send to Robot")
        self.send_to_robot_button.clicked.connect(self.send_to_robot)
        self.button_layout.addWidget(self.send_to_robot_button)
        
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)
        
        # Speech Recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.listening = False
        self.audio_thread = None
    
    def clear_text(self):
        self.detected_speech.clear()
    
    def start_listening(self):
        if not self.listening:
            self.listening = True
            self.audio_thread = QThread()
            self.worker = SpeechWorker(self.recognizer, self.microphone)
            self.worker.moveToThread(self.audio_thread)
            self.audio_thread.started.connect(self.worker.run)
            self.worker.result.connect(self.update_text)
            self.worker.finished.connect(self.audio_thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.audio_thread.finished.connect(self.audio_thread.deleteLater)
            self.audio_thread.start()
    
    def stop_listening(self):
        if self.listening:
            self.listening = False
            self.worker.stop()
    
    def update_text(self, text):
        self.detected_speech.append(text)
        self.detected_speech.verticalScrollBar().setValue(self.detected_speech.verticalScrollBar().maximum())  # Auto-scroll to the bottom
    
    def send_to_robot(self):
        text = self.detected_speech.toPlainText().strip()
        if text:
            # Emit a signal or directly call the planner function
            # Here, we'll emit a signal to be handled by the HomeTab
            self.parent().send_text_to_planner(text)
        else:
            # Optionally, show a message that there's no text to send
            pass

# ----------------------------
# Robot Script Worker
# ----------------------------
class RobotScriptWorker(QObject):
    output = pyqtSignal(str)
    finished = pyqtSignal()
    go_button_enable = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.process = None
        self._is_running = True
    
    def run(self):
        self.process = subprocess.Popen(
            ["python", "src/coder_reviewer_dance.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1  # Line-buffered
        )
        
        for line in iter(self.process.stdout.readline, ''):
            if not self._is_running:
                break
            self.output.emit(line.strip())
            if "Next speaker: code_executor_agent" in line:
                self.go_button_enable.emit()

    def send_input(self, input_text):
        if self.process and self.process.stdin:
            self.output.emit("sending: " + input_text)
            self.process.stdin.write(input_text + '\n')
            self.process.stdin.flush()

    def stop(self):
        self.finished.emit()
        self._is_running = False
        if self.process:
            self.process.terminate()

class RobotThinkingSection(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Allow expansion
        self.console.setMinimumHeight(1000)  # Adjust as necessary
        self.layout.addWidget(QLabel("Robot Thoughts:"))
        self.layout.addWidget(self.console)

        self.layout.addStretch()

        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("background-color: red; color: white; font-size: 16px; padding: 10px;")
        self.reset_button.clicked.connect(self.reset_worker)
        self.layout.addWidget(self.reset_button)


        self.setLayout(self.layout)
        self.thread = None
        self.worker = None


    def reset_worker(self):
        # Clear previous instances
        self.console.clear()
        
        if self.thread:
            self.worker.stop()
            self.thread.quit()
            self.thread.wait()  # Ensure the thread is done before we delete it
        self.thread = None
        self.worker = None

        # Create a new QThread and RobotScriptWorker
        self.thread = QThread()
        self.worker = RobotScriptWorker()
        self.worker.moveToThread(self.thread)

        # Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.output.connect(self.update_thoughts)

        parent = self.parent()  # Get the parent widget

        # Check if parent is valid before trying to access its attributes
        if isinstance(parent, HomeTab):
            self.worker.go_button_enable.connect(parent.execution_section.enable_go_button)
            parent.execution_section.disable_go_button()
        else:
            print("Warning: Parent is not HomeTab or is None")

        # Cleanup when finished
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # Start the thread
        self.thread.start()

    def update_thoughts(self, text):
        self.console.append(text)
        self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())  # Auto-scroll to the bottom

    def planner(self, recognized_text):
        if self.worker is None:
            self.reset_worker()
        
        self.worker.send_input(recognized_text)
        
        
    def send_enter_key(self):
        if self.worker:
            self.worker.send_input("\n")

# ----------------------------
# Execution Section
# ----------------------------
class ExecutionSection(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        
        self.go_button = QPushButton("Go")
        self.go_button.setEnabled(False)
        self.go_button.setStyleSheet("background-color: grey; color: white; font-size: 16px; padding: 10px;")
        self.go_button.clicked.connect(self.execute_plan)
        self.layout.addStretch()
        self.layout.addWidget(self.go_button)
        self.layout.addStretch()
        
        self.setLayout(self.layout)

    def enable_go_button(self):
        """Enable Go button and change its color to green"""
        self.go_button.setEnabled(True)
        self.go_button.setStyleSheet("background-color: green; color: white; font-size: 16px; padding: 10px;")

    def disable_go_button(self):
        """Enable Go button and change its color to green"""
        self.go_button.setEnabled(False)
        self.go_button.setStyleSheet("background-color: grey; color: white; font-size: 16px; padding: 10px;")
    
    def execute_plan(self):
        # Access the RobotThinkingSection to send 'Enter' key
        parent = self.parent()
        while parent and not isinstance(parent, HomeTab):
            parent = parent.parent()
        if parent:
            robot_section = parent.robot_thinking_section
            speech_section = parent.speech_section
            speech_section.clear_text()
            robot_section.send_enter_key()

# ----------------------------
# Home Tab
# ----------------------------
class HomeTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        
        # Speech Recognition Section
        self.speech_section = SpeechRecognitionSection()
        self.layout.addWidget(self.speech_section)
        
        # Robot Thinking Section
        self.robot_thinking_section = RobotThinkingSection()
        self.layout.addWidget(self.robot_thinking_section)
        
        # Execution Section
        self.execution_section = ExecutionSection()
        self.layout.addWidget(self.execution_section)
        
        self.layout.addStretch()
        self.setLayout(self.layout)
    
    def send_text_to_planner(self, text):
        self.robot_thinking_section.planner(text)

# ----------------------------
# Main Window
# ----------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Request a dance from SPOT!")
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        
        # Header
        self.header = Header()
        self.main_layout.addWidget(self.header)
        
        # Tabs
        self.tabs = QTabWidget()
        self.home_tab = HomeTab()
        self.tabs.addTab(self.home_tab, "Home")
        self.main_layout.addWidget(self.tabs)
        
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)




# ----------------------------
# Main Execution
# ----------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Optional: Apply a dark theme or custom styles
    app.setStyleSheet("""
        QMainWindow {
            background-color: #2b2b2b;
            color: #ffffff;
        }
        QPushButton {
            background-color: #3c3f41;
            border: none;
            padding: 10px;
            color: #ffffff;
        }
        QPushButton:hover {
            background-color: #484a4c;
        }
        QTextEdit {
            background-color: #3c3f41;
            color: #ffffff;
            border: 1px solid #555555;
        }
        QLabel {
            color: #ffffff;
        }
    """)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
