import os
import autogen
from autogen import ConversableAgent, GroupChatManager, GroupChat
from autogen.coding import LocalCommandLineCodeExecutor
import tempfile

#find system prompts
script_dir = os.path.dirname(os.path.abspath(__file__))
coder_relative_file = 'knowledge/coder_prompt.xml'
coder_path = os.path.join(script_dir, coder_relative_file)

with open(coder_path, 'r') as file: 
    coder_prompt = file.read()

reviewer_relative_file = 'knowledge/review_prompt.xml'
reviewer_path = os.path.join(script_dir, reviewer_relative_file)

with open(reviewer_path, 'r') as file: 
    reviewer_prompt = file.read()

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
    description="Executes code and reports the results to the coder"
    human_input_mode="ALWAYS" #always request human input before executing
)

Coder = ConversableAgent(
    name="Coder AI",
    system_message=coder_prompt,
    description="Writes executable code to run on the robot, code needs to be reviewed by reviewer before execution"
    llm_config=llm_config,
    code_execution_config=False
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)

Reviewer = ConversableAgent(
    name="Reviewer AI",
    system_message=reviewer_prompt,
    description="reviews all code written by the coder for safety and functionality before execution",
    llm_config=llm_config,
    code_execution_config=False
)


group_chat = GroupChat(
    agents=[code_executor, Coder, Reviewer],
    messages=[],
    max_round=6,
    send_introductions=True,
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config = llm_config
)

if __name__ == "__main__":
    while True:
        task = input("What would you like spot to do?")
        if task:
            chat = code_executor.initiate_chat(GroupChatManager, message=task)
        else:
            break


