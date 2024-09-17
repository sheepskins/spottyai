'''Take me to the fridge, wait until I'm ready, and then take me to the microwave''''''{"usage_including_cached_inference": {"total_cost": 0.052559999999999996, "gpt-4-0613": {"cost": 0.052559999999999996, "prompt_tokens": 1402, "completion_tokens": 175, "total_tokens": 1577}}, "usage_excluding_cached_inference": {"total_cost": 0.052559999999999996, "gpt-4-0613": {"cost": 0.052559999999999996, "prompt_tokens": 1402, "completion_tokens": 175, "total_tokens": 1577}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

def take_to_destination(destination):
    while True:
        detect_result = detect(destination)
        if isinstance(detect_result, pd.DataFrame):
            x = detect_result['x'].values[0]
            y = detect_result['y'].values[0]
            move_result = move_to(x, y)
            if move_result.success:
                break

def wait_until_ready():
    while True:
        ready = ask("Are you ready to proceed?")
        if ready.lower() == 'yes':
            break

take_to_destination('refrigerator')
say("We've arrived at the refrigerator.")
wait_until_ready()
take_to_destination('microwave')
say("We've arrived at the microwave.")
