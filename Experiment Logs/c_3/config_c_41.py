'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.94428, "gpt-4-0613": {"cost": 0.94428, "prompt_tokens": 29248, "completion_tokens": 1114, "total_tokens": 30362}}, "usage_excluding_cached_inference": {"total_cost": 0.94428, "gpt-4-0613": {"cost": 0.94428, "prompt_tokens": 29248, "completion_tokens": 1114, "total_tokens": 30362}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Detect fridge's position
fridge_pos = detect('refrigerator')
if not isinstance(fridge_pos, pd.DataFrame):
    say("Fridge not found, please ensure it's within view or try again.") 
# Move to the fridge
move_result = move_to(fridge_pos['x'][0], fridge_pos['y'][0])
# Ensure moving to fridge was successful
if not move_result.success:
    say("Failed to reach the fridge, please clear the path and try again.")

# Ask user to notify when ready
say("Please tell me when you are ready to go to the microwave.")
ask("Are you ready to go to the microwave?")

# Detect microwave's position
microwave_pos = detect('microwave')
if not isinstance(microwave_pos, pd.DataFrame):
    say("Microwave not found, please ensure it's within view or try again.") 

# Move to the microwave
move_result = move_to(microwave_pos['x'][0], microwave_pos['y'][0])
# Ensure moving to microwave was successful
if not move_result.success:
    say("Failed to reach the microwave, please clear the path and try again.")