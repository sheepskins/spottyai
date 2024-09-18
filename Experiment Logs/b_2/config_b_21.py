'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.26876999999999995, "gpt-4-0613": {"cost": 0.26876999999999995, "prompt_tokens": 8457, "completion_tokens": 251, "total_tokens": 8708}}, "usage_excluding_cached_inference": {"total_cost": 0.26876999999999995, "gpt-4-0613": {"cost": 0.26876999999999995, "prompt_tokens": 8457, "completion_tokens": 251, "total_tokens": 8708}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("I understand you're tired, let's find a place for you to rest.")
detection = detect('bench')
if detection is not None and not detection.empty:
    nearest_bench = detection.iloc[0] # the nearest bench
    say("A bench has been found")
    move_to(nearest_bench['x'], nearest_bench['y'])
    say("You're at the bench now. You can rest.")
else:
    say("I'm sorry, but I don't see any benches nearby.")