'''take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.27426, "gpt-4-0613": {"cost": 0.27426, "prompt_tokens": 8492, "completion_tokens": 325, "total_tokens": 8817}}, "usage_excluding_cached_inference": {"total_cost": 0.27426, "gpt-4-0613": {"cost": 0.27426, "prompt_tokens": 8492, "completion_tokens": 325, "total_tokens": 8817}}}'''
from ai import detect, move_to, say
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Detect the nearest chair.
detections = detect('chair')
if isinstance(detections, pd.DataFrame) and not detections.empty:
    # The nearest chair is the one with the smallest Euclidean distance.
    detections['distance'] = detections.apply(lambda row: row['x']**2 + row['y']**2, axis=1)
    nearest_chair = detections.loc[detections['distance'].idxmin()]
    say('Moving to the nearest chair.')
    move_to(nearest_chair['x'], nearest_chair['y'])
elif detections is None:
    say('No chair detected.')
elif detections is False:
    say('Failed to detect objects.')