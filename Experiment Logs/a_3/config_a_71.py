'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.060719999999999996, "gpt-4-0613": {"cost": 0.060719999999999996, "prompt_tokens": 1406, "completion_tokens": 309, "total_tokens": 1715}}, "usage_excluding_cached_inference": {"total_cost": 0.060719999999999996, "gpt-4-0613": {"cost": 0.060719999999999996, "prompt_tokens": 1406, "completion_tokens": 309, "total_tokens": 1715}}}'''
from ai import detect, move_to, say
import rospy
import time

rospy.init_node('SPOTTYAI')

# Detect Oven location
oven_detection = detect('oven')

if isinstance(oven_detection, pd.DataFrame):
    oven_x, oven_y = oven_detection.iloc[0][['x', 'y']]
    # Check for persons near the oven
    persons_detection = detect('person')
    if isinstance(persons_detection, pd.DataFrame):
        persons_near_oven = persons_detection[(persons_detection['x']-oven_x)**2 + (persons_detection['y']-oven_y)**2 < 1.0**2]
        if len(persons_near_oven) > 0:
            say('Someone is near the oven, I will take you to the microwave.')
            microwave_detection = detect('microwave')
            if isinstance(microwave_detection, pd.DataFrame):
                # Move to the microwave
                move_to(microwave_detection.iloc[0]['x'], microwave_detection.iloc[0]['y'])
            else:
                say('I am unable to locate a microwave.')
        else:
            # Move to the oven
            say('I am taking you to the oven.')
            move_to(oven_x, oven_y)
    else:
        # If no persons were detected, move to the oven
        say('I am taking you to the oven.')
        move_to(oven_x, oven_y)
else:
    say('I am unable to locate the oven.')
