'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.58464, "gpt-4-0613": {"cost": 0.58464, "prompt_tokens": 17900, "completion_tokens": 794, "total_tokens": 18694}}, "usage_excluding_cached_inference": {"total_cost": 0.58464, "gpt-4-0613": {"cost": 0.58464, "prompt_tokens": 17900, "completion_tokens": 794, "total_tokens": 18694}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detect the nearby chairs
detected_objects = detect('chair')

# Check if a chair was detected
if detected_objects is not None:
    # Inform the user about the detected chair
    say('Chair detected.')
    
    # Assume the first chair in our dataframe is the closest for this example
    chair = detected_objects.iloc[0]
    
    # Inform the user that the robot is moving towards the chair
    say("Moving towards the chair.")
    
    # Navigate towards the chair
    move_to_result = move_to(chair.x, chair.y)
    
    # Check if the movement was a success
    if move_to_result.success:
        say("Successfully moved towards the chair.")
    else:
        say("Something went wrong while moving towards the chair. I'll try again.")

else:
    # If no chair was detected, inform the user
    say('No chair detected nearby.')
