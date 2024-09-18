'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.52752, "gpt-4-0613": {"cost": 0.52752, "prompt_tokens": 16646, "completion_tokens": 469, "total_tokens": 17115}}, "usage_excluding_cached_inference": {"total_cost": 0.52752, "gpt-4-0613": {"cost": 0.52752, "prompt_tokens": 16646, "completion_tokens": 469, "total_tokens": 17115}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detecting the refrigerator
fridge_location = detect('refrigerator')
if not fridge_location.empty:
    say("Moving towards the refrigerator.")
    move_to(fridge_location.iloc[0]['x'], fridge_location.iloc[0]['y'])
    say("We have arrived at the refrigerator. Please take your time.")
    while True:
        ready_to_move = ask("Are you ready to move to the microwave?")
        if ready_to_move.lower() == 'yes':
            break
    
    # Detecting the microwave
    microwave_location = detect('microwave')
    if not microwave_location.empty:
        say("Moving towards the microwave.")
        move_to(microwave_location.iloc[0]['x'], microwave_location.iloc[0]['y'])
        say("We have arrived at the microwave. You can use it now.")
    else:
        say("Unable to locate the microwave.")
else:
    say("Unable to locate the refrigerator.")