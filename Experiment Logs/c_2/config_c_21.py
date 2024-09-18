'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.50427, "gpt-4-0613": {"cost": 0.50427, "prompt_tokens": 16285, "completion_tokens": 262, "total_tokens": 16547}}, "usage_excluding_cached_inference": {"total_cost": 0.50427, "gpt-4-0613": {"cost": 0.50427, "prompt_tokens": 16285, "completion_tokens": 262, "total_tokens": 16547}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detect bench
detected_objects = detect('bench')

# If a bench is detected
if detected_objects is not None and not detected_objects.empty:
    # Get the nearest bench
    nearest_bench = detected_objects.loc[detected_objects['distance'].idxmin()]

    # Say the bench location
    say("Bench found at {} meters".format(nearest_bench['distance']))

    # Move to the bench
    move_to(nearest_bench['x'], nearest_bench['y'])

else:
    say("No bench was detected. Please try another area or wait for a while.")