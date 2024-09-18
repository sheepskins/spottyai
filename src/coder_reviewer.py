import os
import autogen
from autogen import ConversableAgent, GroupChatManager, GroupChat
from autogen.coding import LocalCommandLineCodeExecutor
import tempfile
import re
import json
    
#find system prompts
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
coder_relative_file = 'knowledge/coder_prompt.xml'
coder_path = os.path.join(script_dir, coder_relative_file)

with open(coder_path, 'r') as file: 
    coder_prompt = file.read()

reviewer_relative_file = 'knowledge/review_prompt.xml'
reviewer_path = os.path.join(script_dir, reviewer_relative_file)

with open(reviewer_path, 'r') as file: 
    reviewer_prompt = file.read()

#set up coder LLM
llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"], 'cache_seed': None}

# Create a local command line code executor.
temp_dir = tempfile.TemporaryDirectory() # temp directory for the code exector
executor = LocalCommandLineCodeExecutor(
    timeout=600,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name
)

class AI():
    def __init__(self):
        self.code_executor = ConversableAgent(
            name="code_executor_agent",
            llm_config=False, 
            code_execution_config={"executor": executor},
            human_input_mode="ALWAYS" #always request human input before executing
        )

        self.Coder = ConversableAgent(
            name="Coder",
            system_message=coder_prompt,
            llm_config=llm_config,
            code_execution_config=False,
        )

        self.Reviewer = ConversableAgent(
            name="Reviewer",
            system_message=reviewer_prompt,
            llm_config=llm_config,
            code_execution_config=False,
            is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
        )
        self.user = ConversableAgent(
            name="visually_impaired_user",
            llm_config=False,
            code_execution_config=False,
        )

        self.allowed_transitions = {
            self.Coder: [self.Reviewer],
            self.Reviewer: [self.Coder, self.code_executor],
            self.code_executor: [self.Reviewer],
            self.user: [self.Coder],
        }

        self.group_chat = GroupChat(
            agents=[self.code_executor, self.Coder, self.Reviewer, self.user],
            allowed_or_disallowed_speaker_transitions=self.allowed_transitions,
            speaker_transitions_type="allowed",
            messages=[],
            max_round=12,
            send_introductions=True,
        )

        self.manager = GroupChatManager(
            groupchat=self.group_chat,
            llm_config = llm_config
        )

def main(task):
    ai = AI()
    path = os.path.dirname(os.path.abspath(__file__))
    dir_path = path + "/trials/config_b"
    prompt = ""
    if task is not None:
        prompt = task
    else:
        prompt = input("Prompt: ")
    chat = ai.user.initiate_chat(ai.manager, message=prompt, summary_method="last_msg")

    file_num = len([name for name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, name))])
    trial, repeat = divmod(file_num,7)
    file_name = "config_b_" + str(repeat+1) + str(trial+1) + ".py"
    full_path = os.path.join(dir_path, file_name)
    with open(full_path, "w") as file: 
        file.write("'''")  
        file.write(prompt)
        file.write("'''")
        file.write("'''")
        print(json.dumps(autogen.agentchat.gather_usage_summary([ai.manager, ai.Coder, ai.Reviewer])))
        json.dump(autogen.agentchat.gather_usage_summary([ai.manager, ai.Coder, ai.Reviewer]),file)
        file.write("'''")
        file.write(re.search(r'```(.*?)```', chat.summary, re.S).group(1))

if __name__ == "__main__":
    main(None)

