'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.2811, "gpt-4-0613": {"cost": 0.2811, "prompt_tokens": 8610, "completion_tokens": 380, "total_tokens": 8990}}, "usage_excluding_cached_inference": {"total_cost": 0.2811, "gpt-4-0613": {"cost": 0.2811, "prompt_tokens": 8610, "completion_tokens": 380, "total_tokens": 8990}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Detecting the locations of oven, microwave, and person
oven_location = detect('oven')
microwave_location = detect('microwave')
person_location = detect('person')

# If detection of any location fails, inform the user to change the location.
if not oven_location or not microwave_location:
    say("I am unable to detect either the oven or the microwave. Please change to a different location.")
else:
    # If a person is near the oven (within certain x and y coordinates), go to the microwave instead.
    if person_location and ((abs(oven_location['x'] - person_location['x']) <= 1.0) and 
                            (abs(oven_location['y'] - person_location['y']) <= 1.0)):
        say("There is a person near the oven. Taking you to the microwave instead.")
        move_to(microwave_location['x'], microwave_location['y'])
    else:
        # Otherwise, move the user to the oven.
        say("Taking you to the oven.")
        move_to(oven_location['x'], oven_location['y'])