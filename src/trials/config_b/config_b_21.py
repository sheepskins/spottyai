'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.26169, "gpt-4-0613": {"cost": 0.26169, "prompt_tokens": 8341, "completion_tokens": 191, "total_tokens": 8532}}, "usage_excluding_cached_inference": {"total_cost": 0.26169, "gpt-4-0613": {"cost": 0.26169, "prompt_tokens": 8341, "completion_tokens": 191, "total_tokens": 8532}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Let the user know the robot is searching for a bench
say('Searching for a nearby bench.')

# Call the detect function to search for a bench
bench_location = detect('bench')

if bench_location is not None:
    # If a bench is found, move to the bench
    say('Bench found, moving towards it.')
    move_to(bench_location.x, bench_location.y)
else:
    # If a bench isn't found, notify the user
    say('Bench could not be found.')
