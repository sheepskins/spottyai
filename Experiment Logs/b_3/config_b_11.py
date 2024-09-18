'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.29097, "gpt-4-0613": {"cost": 0.29097, "prompt_tokens": 8485, "completion_tokens": 607, "total_tokens": 9092}}, "usage_excluding_cached_inference": {"total_cost": 0.29097, "gpt-4-0613": {"cost": 0.29097, "prompt_tokens": 8485, "completion_tokens": 607, "total_tokens": 9092}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import numpy as np
import pandas as pd

rospy.init_node('SPOTTYAI')

say("Searching for the nearest chair.")
detected_objects = detect("chair")

if detected_objects is False:
    say("Failed to detect any chairs.")
elif detected_objects is None:
    say("No chairs detected.")
else:
    # Calculate distances
    detected_objects["distance"] = np.sqrt(detected_objects["x"]**2 + detected_objects["y"]**2)
    chair_locations = detected_objects.loc[detected_objects['label'] == 'chair']

    if chair_locations.empty:
        say("No chairs detected.")
    else:
        nearest_chair = chair_locations.loc[chair_locations['distance'].idxmin()]
        say("Moving to the nearest chair.")
        move_to(nearest_chair['x'], nearest_chair['y'])
        say("You have been moved to the nearest chair.")
