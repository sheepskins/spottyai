'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead''''''{"usage_including_cached_inference": {"total_cost": 0.06597, "gpt-4-0613": {"cost": 0.06597, "prompt_tokens": 1405, "completion_tokens": 397, "total_tokens": 1802}}, "usage_excluding_cached_inference": {"total_cost": 0.06597, "gpt-4-0613": {"cost": 0.06597, "prompt_tokens": 1405, "completion_tokens": 397, "total_tokens": 1802}}}'''
from ai import detect, move_to, say
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Detect people and oven
people = detect('person')
oven = detect('oven')
microwave = detect('microwave')

# Check if people are detected and there are people near the oven
if isinstance(people, pd.DataFrame) and not oven.empty:
    for _, person in people.iterrows():
        if abs(person.x - oven.iloc[0].x) < 2 and abs(person.y - oven.iloc[0].y) < 2:
            # If there are people near the oven, guide the user to the microwave
            if isinstance(microwave, pd.DataFrame):
                say('Someone is near the oven. I will take you to the microwave instead.')
                move_to(microwave.iloc[0].x, microwave.iloc[0].y)
            else:
                say('Someone is near the oven, and there is no microwave detected.')
            break
    else:
        # If there is no one near the oven, guide the user to the oven
        say('Taking you to the oven.')
        move_to(oven.iloc[0].x, oven.iloc[0].y)
elif isinstance(microwave, pd.DataFrame):
    # There is no people detected but there is a microwave, guide the user to the microwave
    say('I will take you to the microwave.')
    move_to(microwave.iloc[0].x, microwave.iloc[0].y)
elif not oven.empty:
    # Neither people nor microwave is detected but there is an oven, guide the user to the oven
    say('Taking you to the oven.')
    move_to(oven.iloc[0].x, oven.iloc[0].y)
else:
    # Neither people, oven nor microwave is detected
    say('There is no one, oven or microwave detected.')
