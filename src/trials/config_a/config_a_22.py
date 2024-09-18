'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.05217, "gpt-4-0613": {"cost": 0.05217, "prompt_tokens": 1393, "completion_tokens": 173, "total_tokens": 1566}}, "usage_excluding_cached_inference": {"total_cost": 0.05217, "gpt-4-0613": {"cost": 0.05217, "prompt_tokens": 1393, "completion_tokens": 173, "total_tokens": 1566}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# Inform the user about the action
say("Attempting to find the nearest person to nudge them.")

# Detect people
persons = detect('person')

# If any person is detected
if persons is not None:
    # Find the nearest person
    nearest_person = persons.loc[persons['distance'].idxmin()]

    # Go to the nearest person
    result = move_to(nearest_person['x'], nearest_person['y'])

    # Check if moving to the person was successful
    if result.success:
        say("Successfully moved near to the person.")
    else:
        say("Failed to move to the person. Trying again.")

# If no person is detected
else:
    say("No person detected.")
