'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.056339999999999994, "gpt-4-0613": {"cost": 0.056339999999999994, "prompt_tokens": 1392, "completion_tokens": 243, "total_tokens": 1635}}, "usage_excluding_cached_inference": {"total_cost": 0.056339999999999994, "gpt-4-0613": {"cost": 0.056339999999999994, "prompt_tokens": 1392, "completion_tokens": 243, "total_tokens": 1635}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# First, try to detect refrigerator and return the location of the refrigerator.
refrigerator_info = detect('refrigerator')

# If the refrigerator is detected and it is safe to move to the refrigerator
if refrigerator_info is not None and not refrigerator_info.empty:
    refrigerator_x = refrigerator_info['x'].values[0]
    refrigerator_y = refrigerator_info['y'].values[0]
    
    # Announce to user that refrigerator is detected and we are moving towards it.
    say("Refrigerator detected. Going to fetch food for you.")

    # Move to the refrigerator
    move_result = move_to(refrigerator_x, refrigerator_y)

    # Check if the robot has reached the refrigerator successfully.
    if move_result is not None and move_result.success:
        say("We have reached the refrigerator.")
    else:
        say("Oops, some error occurred. Please try again later.")

# If the refrigerator is not detected
else:
    say("Sorry, refrigerator not detected. You may need to manually guide me.")
