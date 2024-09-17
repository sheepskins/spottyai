'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.05067, "gpt-4-0613": {"cost": 0.05067, "prompt_tokens": 1389, "completion_tokens": 150, "total_tokens": 1539}}, "usage_excluding_cached_inference": {"total_cost": 0.05067, "gpt-4-0613": {"cost": 0.05067, "prompt_tokens": 1389, "completion_tokens": 150, "total_tokens": 1539}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# First, we'll check for any chairs in the vicinity
detected_objects = detect('chair')

# Check if a chair was detected
if not detected_objects.empty:
    # Fetch the nearest chair's coordinates
    nearest_chair = detected_objects.iloc[0]
    x = nearest_chair['x']
    y = nearest_chair['y']
    
    # Inform user that we're heading towards the nearest chair
    say("Heading towards the nearest chair.")
    # Move to the nearest chair
    move_to(x, y)
else:
    say("No chair detected in the vicinity.")
