'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.050129999999999994, "gpt-4-0613": {"cost": 0.050129999999999994, "prompt_tokens": 1393, "completion_tokens": 139, "total_tokens": 1532}}, "usage_excluding_cached_inference": {"total_cost": 0.050129999999999994, "gpt-4-0613": {"cost": 0.050129999999999994, "prompt_tokens": 1393, "completion_tokens": 139, "total_tokens": 1532}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# Detect the nearest person
nearest_person = detect('person')
if nearest_person is not False and nearest_person is not None:
    # get the x and y coordinates of the nearest person.
    x, y, id, label = nearest_person.iloc[0]
    x = min(x+0.5,1) # Ensure safety by not going too close to the person.

    # Inform the user
    say('Moving towards the nearest person to get their attention.')

    # Move towards the person 
    move_to(x,y) 
