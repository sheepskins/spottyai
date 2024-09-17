'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.04761, "gpt-4-0613": {"cost": 0.04761, "prompt_tokens": 1389, "completion_tokens": 99, "total_tokens": 1488}}, "usage_excluding_cached_inference": {"total_cost": 0.04761, "gpt-4-0613": {"cost": 0.04761, "prompt_tokens": 1389, "completion_tokens": 99, "total_tokens": 1488}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

say('Looking for the nearest chair.')
chairs = detect('chair')

if chairs is not None and not chairs.empty:
    chair = chairs.loc[chairs['distance'].idxmin()]

    say('Found a chair, moving towards it.')
    move_to(chair['x'], chair['y'])
else:
    say('Unable to find a chair.')
