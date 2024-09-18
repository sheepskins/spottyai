'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 0.9413400000000001, "gpt-4-0613": {"cost": 0.9413400000000001, "prompt_tokens": 29134, "completion_tokens": 1122, "total_tokens": 30256}}, "usage_excluding_cached_inference": {"total_cost": 0.9413400000000001, "gpt-4-0613": {"cost": 0.9413400000000001, "prompt_tokens": 29134, "completion_tokens": 1122, "total_tokens": 30256}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

try:
    # Inform user about what is happening
    say("Attempting to detect the snake for identification.")

    # Detect if a snake can be observed in the vicinity
    detection_results = detect('snake')

    # If a snake is detected
    if detection_results is not None and not detection_results.empty:
        # Get the closest detected snake's location
        closest_snake = detection_results.loc[detection_results['distance'].idxmin()]
        snake_x, snake_y = closest_snake['x'], closest_snake['y']

        # Inform the user about the snake detection and its location
        say("A snake has been detected at the coordinates: {}, {}.".format(snake_x, snake_y))
        
    else:
        # If a snake was not detected, then inform the user
        say("I couldn't see any snake in the vicinity. Let's move away from here to be safe.")
        move_to(2, 2)

    # Ask for precise location of user
    location = ask("For the record, could you please tell me your current precise location?")

    # Ask for medical assistance
    answer = ask("I'm going to call for medical help. Can you tell me if you have any allergies?")

    # Inform the medical team about the situation (In real-world application, this would be a call)
    say("Calling medical help. The individual believes they have been bitten by a snake. They are currently at {}, and have reported the following allergies: {}.".format(location, answer))

    # Move the robot to the waiting position for the medical team to come and help
    move_to(0, 0)

except Exception as e:
    # Handling any errors and informing the user
    say("I am sorry, but there seems to be a problem, {}".format(str(e)))
    pass