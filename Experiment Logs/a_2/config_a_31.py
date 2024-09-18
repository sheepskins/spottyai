'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.0561, "gpt-4-0613": {"cost": 0.0561, "prompt_tokens": 1392, "completion_tokens": 239, "total_tokens": 1631}}, "usage_excluding_cached_inference": {"total_cost": 0.0561, "gpt-4-0613": {"cost": 0.0561, "prompt_tokens": 1392, "completion_tokens": 239, "total_tokens": 1631}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# ask the user the food category
food_category = ask('What type of food are you feeling like?')

# try to detect this category. spot has food categories like apple, sandwich, pizza, hotdog and more
detection_result = detect(food_category)

# if detection_result is a DataFrame, then we have food detected of the requested category!
if isinstance(detection_result, pd.DataFrame):
    # let's move to the nearest detected food item
    nearest_food_item = detection_result.sort_values(by=['x', 'y']).iloc[0]
    move_to(nearest_food_item.x, nearest_food_item.y)
    say('I have located your desired food. Please reach out to grab it.')
    
elif detection_result == False:
    # detection failed
    say('Sorry, I was unable to perform the detection. Please try again later.')

else:
    # no food of this category detected
    say(f'Sorry, I could not find any {food_category} near you.')
