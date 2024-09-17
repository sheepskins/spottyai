'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.05259, "gpt-4-0613": {"cost": 0.05259, "prompt_tokens": 1393, "completion_tokens": 180, "total_tokens": 1573}}, "usage_excluding_cached_inference": {"total_cost": 0.05259, "gpt-4-0613": {"cost": 0.05259, "prompt_tokens": 1393, "completion_tokens": 180, "total_tokens": 1573}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# Detect person category object
detected_person = detect('person')

# Check if person detection was successful
if detected_person is not False and detected_person is not None:
    # Get the first person's position
    person_x, person_y = detected_person.iloc[0][['x', 'y']]

    # Move to the detected person
    move_result = move_to(person_x, person_y)

    if move_result:
        # Notify user that person has been located
        say("A person has been nudged to get their attention.")
    else:
        # Unable to move towards person
        say("I was unable to move towards the person.")
else:
    # No persons were detected
    say("No persons were detected.")
