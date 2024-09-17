'''go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.05547, "gpt-4-0613": {"cost": 0.05547, "prompt_tokens": 1393, "completion_tokens": 228, "total_tokens": 1621}}, "usage_excluding_cached_inference": {"total_cost": 0.05547, "gpt-4-0613": {"cost": 0.05547, "prompt_tokens": 1393, "completion_tokens": 228, "total_tokens": 1621}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Detect if there is a person in the vicinity
detected_persons = detect('person')

if isinstance(detected_persons, pd.DataFrame):
    # Get the closest person's position
    nearest_person = detected_persons.loc[detected_persons['x'].idxmin()]
    
    # Inform user before moving
    say("Moving to nearest person to get their attention.")
    
    # Move to the closest person
    move_result = move_to(nearest_person['x'], nearest_person['y'])

    # If move is successful, adjust the body height to nudge the person gently
    if move_result.is_success:
        pose(0, 0, 0, -0.1)  # Lower the body slightly
        pose(0, 0, 0, 0.1)   # Raise the body slightly, creating a nudge
else:
    say("No person detected in the vicinity.")
