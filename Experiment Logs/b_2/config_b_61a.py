'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.9498, "gpt-4-0613": {"cost": 0.9498, "prompt_tokens": 28758, "completion_tokens": 1451, "total_tokens": 30209}}, "usage_excluding_cached_inference": {"total_cost": 0.9498, "gpt-4-0613": {"cost": 0.9498, "prompt_tokens": 28758, "completion_tokens": 1451, "total_tokens": 30209}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detect the nearest person
nearest_person = detect('person')

if nearest_person is not None and not isinstance(nearest_person, bool):
    # Sort the DataFrame by distance (hypotenuse)
    nearest_person = nearest_person.loc[nearest_person.apply(lambda row: ((row['x']**2) + (row['y']**2))**0.5, axis=1).idxmin()]
    
    # Ensure safe distance for nudging which is more than 0.5 meter
    safe_distance = ((nearest_person['x']**2) + (nearest_person['y']**2))**0.5 
    if safe_distance <= 0.5:
        say("You are too close for a safe nudge. I am adjusting my position.")
        # If the person is too close, the robot will move a bit away but in their direction
        pose(0, 0, 0, -0.2)
        move_to(nearest_person['x']/2, nearest_person['y']/2)
    else:
        say("I am about to nudge you to get your attention.")
        # Move closer to the person to a safe distance to perform a nudge
        x_offset = nearest_person['x'] - 0.5
        y_offset = nearest_person['y'] - 0.5
        move_to(x_offset, y_offset)
        # Tilt the body to a side and back to simulate a nudge
        pose(10, 0, 0, 0) # Tilting a bit
        rospy.sleep(2) # Pausing for a while
        pose(0, 0, 0, 0) # Back to normal position
else:
    say("I'm sorry, I couldn't detect anyone nearby.")