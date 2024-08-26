import os
import autogen
from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor
import tempfile

#find system prompt
script_dir = os.path.dirname(os.path.abspath(__file__))
coder_relative_file = 'knowledge/coder_prompt.xml'
coder_path = os.path.join(script_dir, coder_relative_file)

with open(coder_path, 'r') as file: 
    system_prompt = file.read()

#set up coder LLM
llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}

# Create a local command line code executor.
temp_dir = tempfile.TemporaryDirectory() # temp directory for the code exector
executor = LocalCommandLineCodeExecutor(
    timeout=600,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name
)

code_executor = ConversableAgent(
    "code_executor_agent",
    llm_config=False, 
    code_execution_config={"exector": executor}
    human_input_mode="ALWAYS" #always request human input before executing
)

Coder = ConversableAgent(
    name="Spotty_ai",
    system_message=system_prompt,
    llm_config=llm_config,
    code_execution_config=False
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)

if __name__ == "__main__":
    while True:
        task = input("What would you like spot to do?")
        if task:
            chat = code_executor.initiate_chat(Coder, message=task)
        else:
            break


