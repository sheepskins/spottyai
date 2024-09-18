'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.055170000000000004, "gpt-4-0613": {"cost": 0.055170000000000004, "prompt_tokens": 1393, "completion_tokens": 223, "total_tokens": 1616}}, "usage_excluding_cached_inference": {"total_cost": 0.055170000000000004, "gpt-4-0613": {"cost": 0.055170000000000004, "prompt_tokens": 1393, "completion_tokens": 223, "total_tokens": 1616}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# Detect if a person is in sight.
person = detect('person')

# If a person was detected, move towards them.
if person is not None:
    # Get the coordinates of the nearest person.
    x = person['x'].min()
    y = person['y'].min()

    # Inform the user of the robot's intentions.
    say("I see a person. I will move towards them to get their attention.")

    # Move towards the person.
    move_to(x, y)

    # A gentle nudge to get their attention
    pose(0, 20, 0, 0.1)

elif person is False:
    # Inform the user that there was an error in the detection process.
    say("I am sorry, but I am having trouble detecting people right now.")
else:
    # Inform the user that no people were detected.
    say("I am sorry, but I do not see any people right now.")
