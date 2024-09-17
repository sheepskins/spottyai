'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.50286, "gpt-4-0613": {"cost": 0.50286, "prompt_tokens": 16278, "completion_tokens": 242, "total_tokens": 16520}}, "usage_excluding_cached_inference": {"total_cost": 0.50286, "gpt-4-0613": {"cost": 0.50286, "prompt_tokens": 16278, "completion_tokens": 242, "total_tokens": 16520}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# First, let's look for a bench
detected_items = detect('bench')

# If a bench is detected
if detected_items is not None and not detected_items.empty:
    x, y = detected_items.iloc[0][['x', 'y']]  # grab the first bench coordinates

    # Inform the user that we found a bench and are moving towards it
    say("Bench detected. Moving towards it.")

    # Move towards the bench
    move_to(x, y)
    
# If no bench is detected, inform the user
else: 
    say("No bench detected nearby. Let's keep looking.")