'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.049890000000000004, "gpt-4-0613": {"cost": 0.049890000000000004, "prompt_tokens": 1389, "completion_tokens": 137, "total_tokens": 1526}}, "usage_excluding_cached_inference": {"total_cost": 0.049890000000000004, "gpt-4-0613": {"cost": 0.049890000000000004, "prompt_tokens": 1389, "completion_tokens": 137, "total_tokens": 1526}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

def move_to_object(object_name):
    say(f"Searching for the nearest {object_name}")
    df = detect(object_name)
    
    if df is not None and not df.empty:
        closest_object = df.loc[df['y'].idxmin()]
        x_coord = closest_object['x']
        
        say(f"Moving towards the nearest {object_name}")
        move_to(x_coord, 0)
    else:
        say(f"No {object_name} found nearby")

move_to_object('chair')
