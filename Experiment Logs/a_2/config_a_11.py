'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.04689, "gpt-4-0613": {"cost": 0.04689, "prompt_tokens": 1389, "completion_tokens": 87, "total_tokens": 1476}}, "usage_excluding_cached_inference": {"total_cost": 0.04689, "gpt-4-0613": {"cost": 0.04689, "prompt_tokens": 1389, "completion_tokens": 87, "total_tokens": 1476}}}'''
from ai import detect, move_to, say, ask
import rospy

rospy.init_node('SPOTTYAI')

chair_location = detect('chair')

if chair_location is not None:
    x, y, _, _ = chair_location.iloc[0]
    say("I found a chair, I will guide you there.")
    move_to(x, y)
else:
    say("I could not detect any chairs.")
