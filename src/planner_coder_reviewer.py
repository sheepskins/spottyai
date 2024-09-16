import os
import autogen
from autogen import ConversableAgent, GroupChatManager, GroupChat
from autogen.coding import LocalCommandLineCodeExecutor
import tempfile
import re
import json

#find system prompts
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

planner_relative_file = 'knowledge/planner_prompt.xml'
planner_path = os.path.join(script_dir, planner_relative_file)

with open(planner_path, 'r') as file: 
    planner_prompt = file.read()

coder_relative_file = 'knowledge/coder_w_planner_prompt.xml'
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
    name="code_executor_agent",
    llm_config=False, 
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS" #always request human input before executing
)

Planner = ConversableAgent(
    name="Planner",
    system_message=planner_prompt,
    llm_config=llm_config,
    code_execution_config=False,
)

Coder = ConversableAgent(
    name="Coder",
    system_message=coder_prompt,
    llm_config=llm_config,
    code_execution_config=False,
)

Reviewer = ConversableAgent(
    name="Reviewer",
    system_message=reviewer_prompt,
    llm_config=llm_config,
    code_execution_config=False,
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)
user = ConversableAgent(
    name="visually_impaired_user",
    llm_config=False,
    code_execution_config=False,
)

allowed_transitions = {
    Planner: [Coder],
    Coder: [Reviewer],
    Reviewer: [Coder, code_executor],
    code_executor: [Reviewer],
    user: [Coder],
}

def speaker_select(last_speaker: autogen.Agent, group_chat: autogen.GroupChat):
    if len(group_chat.messages) <= 1:
        return Planner
    else:
        return "auto"
    
group_chat = GroupChat(
    agents=[code_executor, Planner, Coder, Reviewer, user],
    allowed_or_disallowed_speaker_transitions=allowed_transitions,
    speaker_transitions_type="allowed",
    messages=[],
    max_round=12,
    send_introductions=True,
    speaker_selection_method=speaker_select
)


manager = GroupChatManager(
    groupchat=group_chat,
    llm_config = llm_config
)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    dir_path = path + "/trials/config_c"

    task = input("Prompt: ")
    chat = user.initiate_chat(manager, message=task, summary_method="last_msg")

    file_num = len([name for name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, name))])
    trial, repeat = divmod(file_num,3)
    file_name = "config_c_" + str(trial+1) + str(repeat+1) + ".py"
    full_path = os.path.join(dir_path, file_name)
    with open(full_path, "w") as file: 
        file.write("'''")  
        file.write(task)
        file.write("'''")
        file.write("'''")  
        json.dump(autogen.agentchat.gather_usage_summary([manager, Coder, Reviewer, Planner]),file)
        file.write("'''")
        file.write(re.search(r'```(.*?)```', chat.summary, re.S).group(1))


