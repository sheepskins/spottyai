'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.58389, "gpt-4-0613": {"cost": 0.58389, "prompt_tokens": 18003, "completion_tokens": 730, "total_tokens": 18733}}, "usage_excluding_cached_inference": {"total_cost": 0.58389, "gpt-4-0613": {"cost": 0.58389, "prompt_tokens": 18003, "completion_tokens": 730, "total_tokens": 18733}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

say("Alright, let's find some food. Let me look around.")
items_detected = detect('banana,apple,sandwich,orange,broccoli,carrot,hot dog,pizza,donut,cake')

if isinstance(items_detected, pd.DataFrame):
    # get the nearest food item
    nearest_item = items_detected.loc[items_detected['y'].idxmin()]
    
    say(f"I found a {nearest_item['label']}. Let's move towards it.")
    reach_result = move_to(nearest_item['x'], nearest_item['y'])
    if reach_result.successful:
        say("We have reached the food item.")
    else:
        say("Sorry, we couldn't reach the food item. Let's try again.")
else:
    say("I could not find any food items in the vicinity. Let's try another location.")
    # move the robot to another location and repeat the process