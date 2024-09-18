'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.04887, "gpt-4-0613": {"cost": 0.04887, "prompt_tokens": 1391, "completion_tokens": 119, "total_tokens": 1510}}, "usage_excluding_cached_inference": {"total_cost": 0.04887, "gpt-4-0613": {"cost": 0.04887, "prompt_tokens": 1391, "completion_tokens": 119, "total_tokens": 1510}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("I understand you are tired. Let's find a place for you to rest.")
bench_location = detect('bench')
if bench_location is not None:
    x = bench_location['x'].values[0]
    y = bench_location['y'].values[0]
    move_to(x, y)
else:
    say("I'm sorry, I couldn't find a bench around. Please, take a rest where we are.")
