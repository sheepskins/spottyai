'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.06408, "gpt-4-0613": {"cost": 0.06408, "prompt_tokens": 1406, "completion_tokens": 365, "total_tokens": 1771}}, "usage_excluding_cached_inference": {"total_cost": 0.06408, "gpt-4-0613": {"cost": 0.06408, "prompt_tokens": 1406, "completion_tokens": 365, "total_tokens": 1771}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# First try to locate the oven
detect_result = detect('oven')

# If the oven is detected, we check to see if there are people near it
if detect_result is not False and detect_result is not None:
    oven_coords = detect_result[detect_result['label'] == 'oven'][['x', 'y']]

    # Checking if there is a person near the oven  
    person_near_oven = False
    person_detect_result = detect('person')
    if person_detect_result is not False and person_detect_result is not None:
        for _,person in person_detect_result.iterrows():
            if (abs(person['x'] - oven_coords['x']) < 1) and (abs(person['y'] - oven_coords['y']) < 1):
                person_near_oven = True
    
    if person_near_oven:
        say("There is a person near the oven. Attempting to locate the microwave instead.")
        # If there are people near the oven, we locate the microwave and move there
        detect_result = detect('microwave')
        if detect_result is not False and detect_result is not None:
            microwave_coords = detect_result[detect_result['label'] == 'microwave'][['x', 'y']]
            move_to(microwave_coords['x'], microwave_coords['y'])
        else:
            say("Microwave can't be located. Please manually guide me.")
    else:
        say("No person near the oven. Moving towards the oven.")
        move_to(oven_coords['x'], oven_coords['y'])

else:
    say("Oven can't be located. Please manually guide me.")
