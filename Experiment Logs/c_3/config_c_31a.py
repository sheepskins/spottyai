'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.48917999999999995, "gpt-4-0613": {"cost": 0.48917999999999995, "prompt_tokens": 16136, "completion_tokens": 85, "total_tokens": 16221}}, "usage_excluding_cached_inference": {"total_cost": 0.48917999999999995, "gpt-4-0613": {"cost": 0.48917999999999995, "prompt_tokens": 16136, "completion_tokens": 85, "total_tokens": 16221}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

user_preference = ask('Would you prefer to order food or navigate to the kitchen?')