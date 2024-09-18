'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 0.04917, "gpt-4-0613": {"cost": 0.04917, "prompt_tokens": 1395, "completion_tokens": 122, "total_tokens": 1517}}, "usage_excluding_cached_inference": {"total_cost": 0.04917, "gpt-4-0613": {"cost": 0.04917, "prompt_tokens": 1395, "completion_tokens": 122, "total_tokens": 1517}}}'''
from ai import detect, move_to, say, ask
import rospy

rospy.init_node('SPOTTYAI')

say("I am finding a hospital nearby.")
detect('hospital')

observations = detect('hospital')
if observations is not None:
    hospital_location = observations[0] # use the location of the first observed hospital
    say("I found a hospital. Let's go there.")
    move_to(hospital_location['x'], hospital_location['y'])
else:
    say("I did not find a hospital nearby. It may be safer to call for emergency medical assistance.")
