'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.30132, "gpt-4-0613": {"cost": 0.30132, "prompt_tokens": 8612, "completion_tokens": 716, "total_tokens": 9328}}, "usage_excluding_cached_inference": {"total_cost": 0.30132, "gpt-4-0613": {"cost": 0.30132, "prompt_tokens": 8612, "completion_tokens": 716, "total_tokens": 9328}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# detect the fridge
fridge_location = detect('refrigerator')
if fridge_location is False or fridge_location is None:
    say("Unable to detect the fridge.")
else:
    # move to the fridge
    fridge_x = fridge_location['x'].values[0]
    fridge_y = fridge_location['y'].values[0]
    move_to(fridge_x, fridge_y)
    say("Reached the fridge, please indicate when you are ready to move to the microwave.")

# wait until the user is ready to move
while True:
    ready = ask("Are you ready to move to the microwave?")
    if ready.lower() in ['yes', 'y', 'sure', 'ready', 'yea', 'yeah']:
        break

# detect the microwave
microwave_location = detect('microwave')
if microwave_location is False or microwave_location is None:
    say("Unable to detect the microwave.")
else:
    # move to the microwave
    microwave_x = microwave_location['x'].values[0]
    microwave_y = microwave_location['y'].values[0]
    move_to(microwave_x, microwave_y)
    say("Reached the microwave.")
