'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.26802000000000004, "gpt-4-0613": {"cost": 0.26802000000000004, "prompt_tokens": 8472, "completion_tokens": 231, "total_tokens": 8703}}, "usage_excluding_cached_inference": {"total_cost": 0.26802000000000004, "gpt-4-0613": {"cost": 0.26802000000000004, "prompt_tokens": 8472, "completion_tokens": 231, "total_tokens": 8703}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')
# inform the user of the action
say("Sure, let's find a place to sit.")
# detect nearby benches
benches = detect('bench')
# Check if we detected a bench
if benches is not None and not benches.empty:
    # We'll move to the first bench detected
    x, y = benches.iloc[0]['x'], benches.iloc[0]['y']
    # move to the bench 
    move_to(x, y)
    say("Here is a bench you can sit on.")
else: 
    say("Sorry, I couldn't find any benches nearby.")