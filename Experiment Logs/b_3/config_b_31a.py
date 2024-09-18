'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.27842999999999996, "gpt-4-0613": {"cost": 0.27842999999999996, "prompt_tokens": 8583, "completion_tokens": 349, "total_tokens": 8932}}, "usage_excluding_cached_inference": {"total_cost": 0.27842999999999996, "gpt-4-0613": {"cost": 0.27842999999999996, "prompt_tokens": 8583, "completion_tokens": 349, "total_tokens": 8932}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("Let's find you some food. Can you let me know your preference?")
preferred_food = ask("Do you prefer fruits or fast food?")

if 'fruit' in preferred_food.lower():
    say("I am searching for fruits.")
    result = detect('banana,apple,orange')
elif 'fast' in preferred_food.lower():
    say("I am searching for fast food.")
    result = detect('sandwich,hot dog,pizza,donut,cake')

if result is not None and not result.empty:
    first_result = result.iloc[0]
    x, y = first_result['x'], first_result['y']
    say(f"I have found {first_result['label']} for you. Now, I will take you there.")
    trajectory_result = move_to(x, y)
    if trajectory_result.is_done:
        say("We have arrived. You can grab your food now.")
    else:
        say("I'm sorry, I couldn't take you there due to an issue. Let's try again.")
else:
    say("Unfortunately, I couldn't find any food. Let's try another place.")