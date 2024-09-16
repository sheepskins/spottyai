'''take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.053910000000000007, "gpt-4-0613": {"cost": 0.053910000000000007, "prompt_tokens": 1389, "completion_tokens": 204, "total_tokens": 1593}}, "usage_excluding_cached_inference": {"total_cost": 0.053910000000000007, "gpt-4-0613": {"cost": 0.053910000000000007, "prompt_tokens": 1389, "completion_tokens": 204, "total_tokens": 1593}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# First, let's try to detect the chair
detected_objects = detect('chair')

# Check if any chair is detected
if detected_objects is not None and not detected_objects.empty:
    # Find the chair with the nearest location
    nearest_chair = detected_objects.loc[detected_objects['distance'].idxmin()]

    # Let the user know the chair has been found
    say("I found a chair. Now I will guide you to it.")

    # Move to the detected chair
    move_result = move_to(nearest_chair['x'], nearest_chair['y'])

    if move_result:
        say('You have reached the chair.')
    else:
        say('Sorry, I am unable to guide you to the chair.')
else:
    say('Sorry, I could not detect any chairs around.')
