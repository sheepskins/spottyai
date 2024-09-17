'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.63672, "gpt-4-0613": {"cost": 0.63672, "prompt_tokens": 18674, "completion_tokens": 1275, "total_tokens": 19949}}, "usage_excluding_cached_inference": {"total_cost": 0.63672, "gpt-4-0613": {"cost": 0.63672, "prompt_tokens": 18674, "completion_tokens": 1275, "total_tokens": 19949}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Set predefined default positions for fridge and microwave
default_fridge_pos = (0, 0)
default_microwave_pos = (0, 0)

# Initialize positions to the default values
fridge_pos = default_fridge_pos
microwave_pos = default_microwave_pos

# Detect the fridge and get its coordinates
fridge_loc_df = detect('refrigerator')  # or 'fridge' if that's valid
if isinstance(fridge_loc_df, pd.DataFrame):
    fridge_pos = (fridge_loc_df['x'][0], fridge_loc_df['y'][0])
elif fridge_loc_df is None:
    say("I am unable to detect the fridge in my surroundings, moving to predefined fridge location.")
else:
    say("There was a problem with object detection, moving to predefined fridge location.")

# Move to the fridge
move_to_result = move_to(*fridge_pos)
if move_to_result.success:
    say("We have now arrived at the fridge.")
else:
    say("I am unable to move to the fridge at this time.")

# Ask for user readiness, upto 3 tries
ready = ''
for _ in range(3):
    ready = ask("Are you ready to move to the microwave?")
    if ready.lower() == "yes":
        break
    else:
        rospy.sleep(5)

if ready.lower() != "yes":
    say("Acknowledged. We will remain here until you are ready.")
    
# Detect the microwave and its coordinates
microwave_loc_df = detect('microwave')
if isinstance(microwave_loc_df, pd.DataFrame):
    microwave_pos = (microwave_loc_df['x'][0], microwave_loc_df['y'][0])
elif microwave_loc_df is None:
    say("I am unable to detect the microwave in my surroundings, moving to predefined microwave location.")
else:
    say("There was a problem with object detection, moving to predefined microwave location.")

# Move to the microwave
move_to_result = move_to(*microwave_pos)
if move_to_result.success:
    say("We have now arrived at the microwave.")
else:
    say("I am unable to move to the microwave at this time.")