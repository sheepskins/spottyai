'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 0.25788, "gpt-4-0613": {"cost": 0.25788, "prompt_tokens": 8346, "completion_tokens": 125, "total_tokens": 8471}}, "usage_excluding_cached_inference": {"total_cost": 0.25788, "gpt-4-0613": {"cost": 0.25788, "prompt_tokens": 8346, "completion_tokens": 125, "total_tokens": 8471}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("Attempting to find people nearby for help.")
result = detect('person')
if not result.empty:
    say("I detected someone around. Try to call for their help!")
else:
    say("Unfortunately, I couldn't find anyone nearby. Let's try to get to the nearest populated area.")
