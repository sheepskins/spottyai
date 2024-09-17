'''take me to the oven, but if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.056670000000000005, "gpt-4-0613": {"cost": 0.056670000000000005, "prompt_tokens": 1405, "completion_tokens": 242, "total_tokens": 1647}}, "usage_excluding_cached_inference": {"total_cost": 0.056670000000000005, "gpt-4-0613": {"cost": 0.056670000000000005, "prompt_tokens": 1405, "completion_tokens": 242, "total_tokens": 1647}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Attempt to detect a person around oven
person_near_oven = detect('person,oven')

if isinstance(person_near_oven, pd.DataFrame):
    # If a person is detected near the oven
    for index, row in person_near_oven.iterrows():
        if row['label'] == 'person':
            say("There's a person near the oven. Taking you to the microwave instead.")
            microwave_location = detect('microwave')
            if isinstance(microwave_location, pd.DataFrame):
                microwave_location = microwave_location.loc[microwave_location['label'] == 'microwave'].iloc[0]
                move_to(microwave_location['x'], microwave_location['y'])
else:
    # If no person is detected near the oven
    oven_location = detect('oven')
    if isinstance(oven_location, pd.DataFrame):
        oven_location = oven_location.loc[oven_location['label'] == 'oven'].iloc[0]
        move_to(oven_location['x'], oven_location['y'])
