import os
import autogen
from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor
import tempfile
import re
import json

#find system prompts
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
coder_relative_file = 'knowledge/coder_prompt.xml'
coder_path = os.path.join(script_dir, coder_relative_file)

with open(coder_path, 'r') as file: 
    system_prompt = file.read()

#set up coder LLM
print(os.environ["OPENAI_API_KEY"])
llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"], "cache_seed": None}

# Create a local command line code executor.
temp_dir = tempfile.TemporaryDirectory() # temp directory for the code exector
executor = LocalCommandLineCodeExecutor(
    timeout=600,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name
)

code_executor = ConversableAgent(
    "code_executor_agent",
    llm_config=False, 
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS" #always request human input before executing
)

Coder = ConversableAgent(
    name="Spotty_ai",
    system_message=system_prompt,
    llm_config=llm_config,
    code_execution_config=False,
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower(),
)

def main(task):
    path = os.path.dirname(os.path.abspath(__file__))
    dir_path = path + "/trials/config_a"
    prompt = ""
    if task is not None:
        prompt = task
    else:
        prompt = input("Prompt: ")
    chat = code_executor.initiate_chat(Coder, message=prompt, summary_method="last_msg")

    file_num = len([name for name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, name))])
    trial, repeat = divmod(file_num,7)
    file_name = "config_a_" + str(repeat+1) + str(trial+1) + ".py"
    full_path = os.path.join(dir_path, file_name)
    with open(full_path, "w") as file: 
        file.write("'''")  
        file.write(task)
        file.write("'''")
        file.write("'''")  
        json.dump(chat.cost,file)
        file.write("'''")
        file.write(re.search(r'```(.*?)```', chat.summary, re.S).group(1))

if __name__ == "__main__":
    main()


