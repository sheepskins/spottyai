'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.276, "gpt-4-0613": {"cost": 0.276, "prompt_tokens": 8576, "completion_tokens": 312, "total_tokens": 8888}}, "usage_excluding_cached_inference": {"total_cost": 0.276, "gpt-4-0613": {"cost": 0.276, "prompt_tokens": 8576, "completion_tokens": 312, "total_tokens": 8888}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

def navigate_to_object(object_name):
    object_detected = detect(object_name)
    if not isinstance(object_detected, pd.DataFrame) or object_detected.empty:
        say(f'I cannot find {object_name}. Please make sure it is within my sight.')
        return False
    # Assuming here only one instance of the object is found, simply taking the first row in dataframe. Ideally, we should handle multiple object instances.    
    target = object_detected.iloc[0]  

    say(f'Moving towards the {object_name}.')
    move_to(target.x, target.y)
    say(f'We have reached the {object_name}.')
    return True

navigate_to_object('refrigerator')

ready_to_move = ask('Are you ready to go to the microwave? Answer with yes or no.')
while ready_to_move.lower() != 'yes':
    ready_to_move = ask('Are you ready to go to the microwave? Answer with yes or no.')
    
navigate_to_object('microwave')