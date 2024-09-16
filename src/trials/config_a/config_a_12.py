'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.05007, "gpt-4-0613": {"cost": 0.05007, "prompt_tokens": 1389, "completion_tokens": 140, "total_tokens": 1529}}, "usage_excluding_cached_inference": {"total_cost": 0.05007, "gpt-4-0613": {"cost": 0.05007, "prompt_tokens": 1389, "completion_tokens": 140, "total_tokens": 1529}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

say("Attempting to find the nearest chair.")
result = detect('chair')

if isinstance(result, pd.DataFrame):
    min_distance_index = result.loc[:, 'x':'y'].pow(2).sum(1).idxmin()
    closest_object = result.loc[min_distance_index]
    say("Moving to the chair.")
    move_to(closest_object['x'], closest_object['y'])
elif isinstance(result, bool) and not result:
    say("Detection process has failed.")
else:
    say("No chair detected.")
