'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.96261, "gpt-4-0613": {"cost": 0.96261, "prompt_tokens": 29027, "completion_tokens": 1530, "total_tokens": 30557}}, "usage_excluding_cached_inference": {"total_cost": 0.96261, "gpt-4-0613": {"cost": 0.96261, "prompt_tokens": 29027, "completion_tokens": 1530, "total_tokens": 30557}}}'''
from ai import detect, move_to, say
import rospy
import time

rospy.init_node('SPOTTYAI')

# First, we attempt to detect a person
say("Searching for a person to alert.")
person_detection = detect('person')

# If a person is detected in the field of view
if person_detection is not None:
    # Get the index of the closest person
    closest_person_index = (person_detection['x']**2 + person_detection['y']**2).idxmin()

    # Get the row corresponding to the closest person
    closest_person = person_detection.loc[closest_person_index]

    if closest_person['label'] == 'person':
        # Calculate the direction vector towards the person
        dir_vector = [closest_person['x'] / ((closest_person['x']**2 + closest_person['y']**2)**0.5),
                      closest_person['y'] / ((closest_person['x']**2 + closest_person['y']**2)**0.5)]

        # Move towards the person, but stop at a safe distance, 0.5 meters away, applying the direction vector
        move_to(dir_vector[0] * 0.5, dir_vector[1] * 0.5) 

        for _ in range(3):
            # Get the person's attention 
            say('Person ahead. I am trying to get their attention.')
            
            time.sleep(2)  # Wait for a couple of seconds before trying again

    else:
        # If the closest detected object is not a person, inform the person
        say("I'm sorry, I cannot find a person. The closest entity is a {}.".format(closest_person['label']))

else:
    # If no person is detected, inform the user
    say("No person detected in the area.")