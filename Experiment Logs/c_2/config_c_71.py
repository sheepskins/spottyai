'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.95868, "gpt-4-0613": {"cost": 0.95868, "prompt_tokens": 29424, "completion_tokens": 1266, "total_tokens": 30690}}, "usage_excluding_cached_inference": {"total_cost": 0.95868, "gpt-4-0613": {"cost": 0.95868, "prompt_tokens": 29424, "completion_tokens": 1266, "total_tokens": 30690}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Step 1: Use detect function to find the location of 'oven' and 'person'.
oven_location = detect('oven')
person_location = detect('person')

if oven_location is not None and oven_location is not False:
    oven_x = oven_location.x[0]
    oven_y = oven_location.y[0]
else:
    say("I'm sorry, but I couldn't detect the oven.")
    

if person_location is not None and person_location is not False:
    # Step 2: Check if there is any person within close proximity of the oven.
    for index, person in person_location.iterrows():
        if abs(oven_x - person.x) < 1.5 and abs(oven_y - person.y) < 1.5 :
            # Step 4: Use detect function to find the location of 'microwave'.
            microwave_location = detect('microwave')
            if microwave_location is not None and microwave_location is not False:
                microwave_x = microwave_location.x[0]
                microwave_y = microwave_location.y[0]
                say("There is a person near the oven. Taking you to the microwave instead.")
                
                # Step 5: Use move_to function to take the user to the microwave.
                move_to(microwave_x, microwave_y)
            break
    else:
        # Step 3: Use move_to function to take the user to the oven.
        say("Taking you to the oven.")
        move_to(oven_x, oven_y)
else:
    say("Feel free to approach the oven, as there is no one there.")
    # Step 3: Use move_to function to take the user to the oven.
    move_to(oven_x, oven_y)