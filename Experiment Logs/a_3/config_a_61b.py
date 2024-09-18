'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.04898999999999999, "gpt-4-0613": {"cost": 0.04898999999999999, "prompt_tokens": 1393, "completion_tokens": 120, "total_tokens": 1513}}, "usage_excluding_cached_inference": {"total_cost": 0.04898999999999999, "gpt-4-0613": {"cost": 0.04898999999999999, "prompt_tokens": 1393, "completion_tokens": 120, "total_tokens": 1513}}}'''
from ai import detect, move_to, say
import rospy
import pandas as pd 

rospy.init_node('SPOTTYAI')

people = detect('person')
if isinstance(people, pd.DataFrame):
    nearest_person = people.loc[people['x'].idxmin()]
    say('Approaching to nearest person.')
    result = move_to(nearest_person['x'], nearest_person['y'])

    if result.success:
        say('I have reached the person.')
    else:
        say('Unable to reach the person')
else:
    say('No person detected.')
