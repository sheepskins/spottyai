'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.04623, "gpt-4-0613": {"cost": 0.04623, "prompt_tokens": 1391, "completion_tokens": 75, "total_tokens": 1466}}, "usage_excluding_cached_inference": {"total_cost": 0.04623, "gpt-4-0613": {"cost": 0.04623, "prompt_tokens": 1391, "completion_tokens": 75, "total_tokens": 1466}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

pose(0, 0, 0, 0.1)  # Adjusts the pose to make the user comfortable
say("Let's take a little break. I adjusted my pose to help you rest.")
