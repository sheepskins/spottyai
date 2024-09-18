'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.5621700000000001, "gpt-4-0613": {"cost": 0.5621700000000001, "prompt_tokens": 16825, "completion_tokens": 957, "total_tokens": 17782}}, "usage_excluding_cached_inference": {"total_cost": 0.5621700000000001, "gpt-4-0613": {"cost": 0.5621700000000001, "prompt_tokens": 16825, "completion_tokens": 957, "total_tokens": 17782}}}'''
from ai import detect, move_to, say
import rospy
import numpy as np

rospy.init_node('SPOTTYAI')

# Step 1: Detect a person
people_detected = detect('person')

# Check if people have been detected
if people_detected is not None and not people_detected.empty:
    # Get the location of the nearest person
    nearest_person = people_detected.iloc[0]
    x_person, y_person = nearest_person['x'], nearest_person['y']

    # Maintain a safe distance and calculate target position
    safe_distance = 0.3  # You can adjust this value as needed
    distance_to_person = np.hypot(x_person, y_person)
    safe_x = x_person * (distance_to_person - safe_distance) / distance_to_person
    safe_y = y_person * (distance_to_person - safe_distance) / distance_to_person
    
    # Alert the person of the robot's intentions
    say("Dear person, I am coming towards you to get your attention.")
 
    # Step 2: Move towards the detected person
    move_result = move_to(safe_x, safe_y)
    if move_result.success:
        say("Hello, I have a message for you.")
    else:
        say("I am sorry, I couldn't reach you.")

else:
    # In case no people are detected
    say('I am sorry, but I could not detect any people near me.')
