'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead''''''{"usage_including_cached_inference": {"total_cost": 0.28109999999999996, "gpt-4-0613": {"cost": 0.28109999999999996, "prompt_tokens": 8590, "completion_tokens": 390, "total_tokens": 8980}}, "usage_excluding_cached_inference": {"total_cost": 0.28109999999999996, "gpt-4-0613": {"cost": 0.28109999999999996, "prompt_tokens": 8590, "completion_tokens": 390, "total_tokens": 8980}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Detect people
people_position = detect('person')

# If people are present
if isinstance(people_position, pd.DataFrame):
    # Detect microwave
    microwave_position = detect('microwave')

    # If microwave is detected
    if isinstance(microwave_position, pd.DataFrame):
        target = microwave_position.loc[0, ['x', 'y']] # assume first detection is the target
        say("Taking you to microwave.")
        move_to( target['x'], target['y'])
    else:
        say("Microwave not found.")

# If no people present
else:
    # Detect the oven
    oven_position = detect('oven')
    
    # If oven is detected
    if isinstance(oven_position, pd.DataFrame):
        target = oven_position.loc[0, ['x', 'y']] # assume first detection is the target
        say("Taking you to oven.")
        move_to( target['x'], target['y'])
    else:
        say("Oven not found.")    