'''Take me to the fridge, wait until I'm ready and then take me to the microwave''''''{"usage_including_cached_inference": {"total_cost": 0.9082799999999999, "gpt-4-0613": {"cost": 0.9082799999999999, "prompt_tokens": 28642, "completion_tokens": 817, "total_tokens": 29459}}, "usage_excluding_cached_inference": {"total_cost": 0.9082799999999999, "gpt-4-0613": {"cost": 0.9082799999999999, "prompt_tokens": 28642, "completion_tokens": 817, "total_tokens": 29459}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detect location of fridge
fridge_location = detect('refrigerator')

# If fridge is detected
if fridge_location is not None:

    # Move to the fridge
    move_to_result = move_to(fridge_location['x'], fridge_location['y'])

    # Wait for the user to finish with the fridge
    ready = ask('Are you ready to move to the microwave?')

    # wait for user response
    while ready.lower() != 'yes' and ready.lower() != 'emergency':
        ready = ask('Are you ready to move to the microwave?')
    
    # if user says it's an emergency, stop the operation
    if ready.lower() == 'emergency':
        say('Emergency acknowledged. Operation halted.')
    
    else:
        # Detect location of microwave
        microwave_location = detect('microwave')

        # If microwave is detected
        if microwave_location is not None:
            # Move to the microwave
            move_to_result = move_to(microwave_location['x'], microwave_location['y'])
            
        else:
            say('Unable to detect microwave')
else:
    say('Unable to detect refrigerator')