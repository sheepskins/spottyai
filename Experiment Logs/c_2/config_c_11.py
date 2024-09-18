'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.9832799999999999, "gpt-4-0613": {"cost": 0.9832799999999999, "prompt_tokens": 29982, "completion_tokens": 1397, "total_tokens": 31379}}, "usage_excluding_cached_inference": {"total_cost": 0.9832799999999999, "gpt-4-0613": {"cost": 0.9832799999999999, "prompt_tokens": 29982, "completion_tokens": 1397, "total_tokens": 31379}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import time

rospy.init_node('SPOTTYAI')

# Detect nearest chair
detection = detect('chair')

# Make sure chair is detected and no errors
if detection is not None and detection is not False:

    # Notify user that a chair is spotted
    say("Spotted a chair. Moving towards it.")

    # Extract the coordinates of the chair
    x_chair = detection['x'].values[0]
    y_chair = detection['y'].values[0]

    # Initialize time
    start_time = rospy.Time.now().to_sec()

    # Try to move towards the chair
    while True:
        # Continually update detection and position information while moving towards the chair
        detection = detect('chair')

        # If chair is not detected, stop navigation
        if detection is None or detection is False:
            say("Chair not detected anymore, stopping navigation.")
            break

        # Check if the robot has taken too much time to reach the chair - might indicate a problem
        if (rospy.Time.now().to_sec() - start_time) > 60:
            say("Took too long to reach the chair, something might be wrong. Stopping navigation.")
            break
            
        # Update the coordinates of the chair
        x_chair = detection['x'].values[0]
        y_chair = detection['y'].values[0]

        # Command the robot to move towards the chair
        result = move_to(x_chair, y_chair)
        
        # Check success of robot's movement
        if result.success:
            break
        else:
            say("Unable to move to the chair. Retrying...")

    # Notify the user that they have been relocated to the chair
    say("You have been relocated to the chair.")
else:
    # Notify the user that no chair is detected
    say("No chair detected.")