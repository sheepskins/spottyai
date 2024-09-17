'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.27, "gpt-4-0613": {"cost": 0.27, "prompt_tokens": 8500, "completion_tokens": 250, "total_tokens": 8750}}, "usage_excluding_cached_inference": {"total_cost": 0.27, "gpt-4-0613": {"cost": 0.27, "prompt_tokens": 8500, "completion_tokens": 250, "total_tokens": 8750}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

food_categories = 'banana,apple,sandwich,orange,broccoli,carrot,hot dog,pizza,donut,cake'
food = detect(food_categories)

if not food.empty:
    say("I have detected some food nearby. I will guide you to it.")
    x, y = food.iloc[0]['x'], food.iloc[0]['y']
    move_to(x, y)
else:
    say("I'm sorry, I couldn't detect any food nearby.")