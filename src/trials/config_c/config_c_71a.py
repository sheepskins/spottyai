'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.93411, "gpt-4-0613": {"cost": 0.93411, "prompt_tokens": 28951, "completion_tokens": 1093, "total_tokens": 30044}}, "usage_excluding_cached_inference": {"total_cost": 0.93411, "gpt-4-0613": {"cost": 0.93411, "prompt_tokens": 28951, "completion_tokens": 1093, "total_tokens": 30044}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import numpy as np

rospy.init_node('SPOTTYAI')

# Step 1: Detect oven
oven = detect('oven')

if oven is not None:

    oven_location = {'x': np.mean(oven.x), 'y': np.mean(oven.y)} # averaging detected coordinates

    # Step 2: Detect person
    person = detect('person')

    if person is not None:

        person_location = {'x': np.mean(person.x), 'y': np.mean(person.y)} # averaging detected coordinates

        # check if person is near the oven (within a range of 1 meter for this example)
        if np.sqrt((person_location['x'] - oven_location['x'])**2 + (person_location['y'] - oven_location['y'])**2) <= 1:

            say('A person is detected near the oven.')
            # Step 3: If person detected near oven, detect microwave
            microwave = detect('microwave')     
                
            if microwave is not None:

                microwave_location = {'x': np.mean(microwave.x), 'y': np.mean(microwave.y)} # averaging detected coordinates

                # lower body position for safety before moving
                pose(0, 0, 0, -0.1)

                # Step 3b: Move to microwave
                move_to(microwave_location['x'], microwave_location['y'])

            else:
                # No microwave detected
                say('Sorry, I was unable to locate the microwave.')
        else:

            # lower body position for safety before moving
            pose(0, 0, 0, -0.1)

            # No person detected near the oven, move to the oven
            move_to(oven_location['x'], oven_location['y'])

    else:

        # lower body position for safety before moving
        pose(0, 0, 0, -0.1)

        # No person detected, move to the oven
        move_to(oven_location['x'], oven_location['y'])

else:
    # No oven detected 
    say('Sorry, I was unable to locate the oven.')