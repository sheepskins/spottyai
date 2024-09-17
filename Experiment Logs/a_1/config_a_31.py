'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.053579999999999996, "gpt-4-0613": {"cost": 0.053579999999999996, "prompt_tokens": 1392, "completion_tokens": 197, "total_tokens": 1589}}, "usage_excluding_cached_inference": {"total_cost": 0.053579999999999996, "gpt-4-0613": {"cost": 0.053579999999999996, "prompt_tokens": 1392, "completion_tokens": 197, "total_tokens": 1589}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Ask the user for their food preference
food_preference = ask("What type of food are you in the mood for?")

# Detect the requested food
food_detected = detect(food_preference)

if food_detected is not False and food_detected is not None:
    # Get the coordinates of the detected food
    x, y = food_detected[['x', 'y']].values[0]
    
    # Inform the user that the requested food has been detected and the robot is moving towards it
    say(f"I have detected {food_preference}, moving towards it now.")
  
    # Move the robot towards the detected food
    move_to(x, y)
else:
    # Inform the user that the requested food could not be detected
    say(f"I'm sorry, I couldn't find any {food_preference}.")
