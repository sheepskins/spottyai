import os
import autogen
from autogen import ConversableAgent, GroupChatManager, GroupChat
from autogen.coding import LocalCommandLineCodeExecutor
import tempfile
import re
import json
import csv
    
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
    work_dir= script_dir + '/src'
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
    prompt = ""
    if task is not None:
        prompt = task
    else:
        print("Enter your prompt!")
        prompt = input()
        print(prompt)
    chat = ai.user.initiate_chat(ai.manager, message=prompt, summary_method="last_msg")

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/data')
    file_name = 'usage.csv'
    full_path = os.path.join(path, file_name)
    with open(full_path, "w") as file: 
        # Parse the JSON string
        data = autogen.agentchat.gather_usage_summary([ai.manager, ai.Coder, ai.Reviewer])

        # Extract values from cached inference section
        cached_inference = data['usage_including_cached_inference']['gpt-4-0613']
        cost = cached_inference['cost']
        prompt_tokens = cached_inference['prompt_tokens']
        completion_tokens = cached_inference['completion_tokens']

        # Prepare CSV row
        csv_row = [prompt, cost, prompt_tokens, completion_tokens]
        csv_writer = csv.writer(file)
        csv_writer.writerow(csv_row)


if __name__ == "__main__":
    while True:
      main(None)
    

