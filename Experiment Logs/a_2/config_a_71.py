'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.06803999999999999, "gpt-4-0613": {"cost": 0.06803999999999999, "prompt_tokens": 1406, "completion_tokens": 431, "total_tokens": 1837}}, "usage_excluding_cached_inference": {"total_cost": 0.06803999999999999, "gpt-4-0613": {"cost": 0.06803999999999999, "prompt_tokens": 1406, "completion_tokens": 431, "total_tokens": 1837}}}'''
from ai import detect, move_to, say
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Detect 'person', 'oven', and 'microwave'
detected_objects = detect('person,oven,microwave')

# If no objects are detected or detection fails, inform the user
if detected_objects is None or detected_objects is False:
    say("I'm sorry, but I cannot detect the locations of the oven, microwave, or any persons.")
else:
    # If 'oven' and 'person' detected near it, move to 'microwave'
    if 'oven' in detected_objects['label'].values and 'person' in detected_objects[detected_objects['label'] == 'oven']['id'].values:
        microwave_location = detected_objects[detected_objects['label'] == 'microwave'].iloc[0]
        say("There is someone near the oven. I will take you to the microwave instead.")
        move_to(microwave_location['x'], microwave_location['y'])
    # If 'oven' detected and no 'person' near it, move to 'oven'
    elif 'oven' in detected_objects['label'].values:
        oven_location = detected_objects[detected_objects['label'] == 'oven'].iloc[0]
        say("Taking you to the oven now.")
        move_to(oven_location['x'], oven_location['y'])
    # If 'oven' not detected, but 'microwave' detected, move to 'microwave'
    elif 'microwave' in detected_objects['label'].values:
        microwave_location = detected_objects[detected_objects['label'] == 'microwave'].iloc[0]
        say("I could not detect the oven. I will take you to the microwave instead.")
        move_to(microwave_location['x'], microwave_location['y'])
    # If neither 'oven' nor 'microwave' is detected, inform the user
    else:
        say("I'm sorry, but I cannot detect the locations of the oven or the microwave.")
