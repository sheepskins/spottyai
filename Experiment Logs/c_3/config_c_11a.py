'''take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.50826, "gpt-4-0613": {"cost": 0.50826, "prompt_tokens": 16326, "completion_tokens": 308, "total_tokens": 16634}}, "usage_excluding_cached_inference": {"total_cost": 0.50826, "gpt-4-0613": {"cost": 0.50826, "prompt_tokens": 16326, "completion_tokens": 308, "total_tokens": 16634}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# Detect the nearest chair
detected_chairs = detect('chair')
if detected_chairs is not None:
    nearest_chair = detected_chairs.iloc[0]

    # Inform the user
    say("I have found a chair. Now guiding you towards it.")
    
    # Navigate to the nearest chair
    move_to(nearest_chair['x'], nearest_chair['y'])
else:
    say("I'm sorry, I couldn't find a chair.")