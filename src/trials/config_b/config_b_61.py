'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.57246, "gpt-4-0613": {"cost": 0.57246, "prompt_tokens": 17632, "completion_tokens": 725, "total_tokens": 18357}}, "usage_excluding_cached_inference": {"total_cost": 0.57246, "gpt-4-0613": {"cost": 0.57246, "prompt_tokens": 17632, "completion_tokens": 725, "total_tokens": 18357}}}'''
from ai import detect, move_to, say
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Inform the user of the action
say("Scanning for the nearest person.")

# Use detect function to find people
people = detect('person')

# Check if people were detected
if isinstance(people, pd.DataFrame):
    # Sort people by distance
    people = people.sort_values(by=['x'])

    # Select the closest person
    closest_person = people.iloc[0]

    # Get the x, y coordinates of the closest person
    x, y = closest_person['x'], closest_person['y']

    # Subtract 1 meter from the person's x and y coordinate
    target_x = x - 1
    target_y = y - 1

    # Make sure target_x and target_y are not less than 0
    target_x = max(target_x, 0)
    target_y = max(target_y, 0)

    # Inform the user we're moving toward the person
    say(f"Moving towards the person at ({target_x}, {target_y}).")

    # Move to the person
    move_to(target_x, target_y)
    
    # Inform user that action is completed
    say("Person nudged.")

else:
    # Inform user no people were detected
    say("No people detected.")
