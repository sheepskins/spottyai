'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.90009, "gpt-4-0613": {"cost": 0.90009, "prompt_tokens": 28351, "completion_tokens": 826, "total_tokens": 29177}}, "usage_excluding_cached_inference": {"total_cost": 0.90009, "gpt-4-0613": {"cost": 0.90009, "prompt_tokens": 28351, "completion_tokens": 826, "total_tokens": 29177}}}'''
from ai import detect, move_to, say, ask
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

def find_nearest_person(df):
    df['distance'] = df.apply(lambda row: (row["x"] ** 2 + row["y"] ** 2) ** 0.5, axis=1)
    nearest_person = df[df['distance'] == df['distance'].min()]
    return nearest_person

def nudge_person(near_person):
    for i, person in near_person.iterrows():
        target_x = person['x']
        target_y = person['y']
        if abs(target_x) > 0.5 or abs(target_y) > 0.5:
            move_to(target_x, target_y)

say("Looking for the nearest person.")
detected_people = detect('person')

if isinstance(detected_people, pd.DataFrame):
    nearest_person = find_nearest_person(detected_people)
    response = ask("I have detected someone nearby, should I proceed to nudge them?")
    if response.lower() == "yes":
        say("Moving towards the person to nudge.")
        nudge_person(nearest_person)
        say("Nudged the person.")
    else:
        say("Okay, I will not nudge them.")
else:
    say("Could not find any people around.")
