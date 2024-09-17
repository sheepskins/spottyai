'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.05772, "gpt-4-0613": {"cost": 0.05772, "prompt_tokens": 1402, "completion_tokens": 261, "total_tokens": 1663}}, "usage_excluding_cached_inference": {"total_cost": 0.05772, "gpt-4-0613": {"cost": 0.05772, "prompt_tokens": 1402, "completion_tokens": 261, "total_tokens": 1663}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detect the fridge
fridge = detect('refrigerator')
if fridge is not None and fridge is not False:
    # Move to the fridge
    move_x, move_y = fridge[0]['x'], fridge[0]['y']
    move_to(move_x, move_y)
    say('We have arrived at the fridge. Let me know when you are ready to move to the microwave.')

    ready_to_move = 'No'
    while ready_to_move.lower() != 'yes':
        # Ask the user if they are ready to move
        ready_to_move = ask('Are you ready to move to the microwave?')

    # Detect the microwave
    microwave = detect('microwave')
    if microwave is not None and microwave is not False:
        # Move to the microwave
        move_x, move_y = microwave[0]['x'], microwave[0]['y']
        move_to(move_x, move_y)
        say('We have arrived at the microwave.')
    else:
        say('I am unable to locate the microwave.')
else:
    say('I am unable to locate the fridge.')
