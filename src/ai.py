import detection.detector as detector

def say(string):
    print(string)

def ask(string):
    string = string + ": "
    return input(string)