'''Help! I think i've been bitten by a snake''''''{"usage_including_cached_inference": {"total_cost": 0.27266999999999997, "gpt-4-0613": {"cost": 0.27266999999999997, "prompt_tokens": 8511, "completion_tokens": 289, "total_tokens": 8800}}, "usage_excluding_cached_inference": {"total_cost": 0.27266999999999997, "gpt-4-0613": {"cost": 0.27266999999999997, "prompt_tokens": 8511, "completion_tokens": 289, "total_tokens": 8800}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("Don't panic, I'm here to help you.")
say("I'm going to look for some people around to assist you.")

# Detect for people
results = detect('person')

# If there is a person nearby
if results is not None and not results.empty:
    # Retrieve the nearest person's location
    nearest_person = results.loc[results['distance'].idxmin()]
    x, y = nearest_person['x'], nearest_person['y']
    
    # Inform the user
    say("I found someone nearby. I will take you there.")
    
    # Move to the detected person's location
    move_to(x, y)
else:
    say("I'm unable to find anyone nearby. I suggest you call the local emergency number.")