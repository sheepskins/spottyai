'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.6245699999999998, "gpt-4-0613": {"cost": 0.6245699999999998, "prompt_tokens": 18467, "completion_tokens": 1176, "total_tokens": 19643}}, "usage_excluding_cached_inference": {"total_cost": 0.6245699999999998, "gpt-4-0613": {"cost": 0.6245699999999998, "prompt_tokens": 18467, "completion_tokens": 1176, "total_tokens": 19643}}}'''
from ai import detect, move_to, say
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Safe distance definition
safe_distance = 2  # You will need to define what is a safe distance.

# Look for the oven in the environment.
oven = detect('oven')
if oven is not False and oven is not None and not oven.empty:
    oven_location = oven.iloc[0]  # Assume the first detected oven is the desired one.

    # Look for people near the oven.
    people = detect('person')
    if people is not False and people is not None and not people.empty:
        # Assume the first detected person is the one to consider.
        person_location = people.iloc[0]

        # Calculate the distance between the person and the oven.
        distance = ((oven_location['x'] - person_location['x'])**2 + (oven_location['y'] - person_location['y'])**2)**0.5

        # If there's no one near the oven, move to the oven.
        if distance > safe_distance:
            say(f"Taking you to the oven at location {oven_location['x']}, {oven_location['y']}")
            move_to(oven_location['x'], oven_location['y'])  
        else:
            # If there's someone near the oven, move to the microwave.
            microwave = detect('microwave')
            if microwave is not False and microwave is not None and not microwave.empty:
                microwave_location = microwave.iloc[0]
                say(f"Taking you to the microwave at location {microwave_location['x']}, {microwave_location['y']}")
                move_to(microwave_location['x'], microwave_location['y'])  
            else:
                say("I'm sorry, I cannot find a microwave.")
    else:
        say(f"Taking you to the oven at location {oven_location['x']}, {oven_location['y']}")
        move_to(oven_location['x'], oven_location['y'])
else:
    say("I'm sorry, I cannot find an oven.")