'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.5242499999999999, "gpt-4-0613": {"cost": 0.5242499999999999, "prompt_tokens": 16571, "completion_tokens": 452, "total_tokens": 17023}}, "usage_excluding_cached_inference": {"total_cost": 0.5242499999999999, "gpt-4-0613": {"cost": 0.5242499999999999, "prompt_tokens": 16571, "completion_tokens": 452, "total_tokens": 17023}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Inform user about our actions
say("I am checking for available food near you.")

# Check for nearby food
food_categories = "banana,apple,sandwich,orange,broccoli,carrot,hot dog,pizza,donut,cake"
detected_food = detect(food_categories)

if detected_food is not None and not detected_food.empty:
    # Move to closest detected food
    closest_food = detected_food.iloc[0]  # Assume the DataFrame is sorted by distance
    say("I found some food. I will guide you there.")
    move_to(closest_food['x'], closest_food['y'])
else:
    # Ask user for preferred food
    preferred_food = ask("I couldn't find any food nearby. What food would you like to eat?")
    say(f"Let's go to the usual place where you keep {preferred_food}. Please guide me to the direction.")
    # Code execution would run here to navigate to the food as guided by the user
    # Implementation depends on additional capabilities of the robot such as
    # following directional voice commands from the user