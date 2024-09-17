'''Help! I think I've been bitten by a snake''''''{"usage_including_cached_inference": {"total_cost": 0.04848, "gpt-4-0613": {"cost": 0.04848, "prompt_tokens": 1394, "completion_tokens": 111, "total_tokens": 1505}}, "usage_excluding_cached_inference": {"total_cost": 0.04848, "gpt-4-0613": {"cost": 0.04848, "prompt_tokens": 1394, "completion_tokens": 111, "total_tokens": 1505}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("Sit still, I'm searching for the snake")
detected_snake = detect('snake')

if detected_snake:
    say("I have located the snake, I will steer clear from it. Now I am calling for medical assistance")
else:
    say("I can't find the snake but I am still calling for medical assistance")

# Calling for medical assitance logic here
