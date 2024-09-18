'''Take me to the fridge, wait until i'm ready adn then take me to the microwave''''''{"usage_including_cached_inference": {"total_cost": 0.54648, "gpt-4-0613": {"cost": 0.54648, "prompt_tokens": 16816, "completion_tokens": 700, "total_tokens": 17516}}, "usage_excluding_cached_inference": {"total_cost": 0.54648, "gpt-4-0613": {"cost": 0.54648, "prompt_tokens": 16816, "completion_tokens": 700, "total_tokens": 17516}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Find the location of the refrigerator
refrigerator_location = detect('refrigerator')

# If the refrigerator is found, move to it
if refrigerator_location is not None:
    move_to(refrigerator_location['x'], refrigerator_location['y'])
    # Wait for user to confirm they are ready to move
    ready = ask('Are you ready to move to the microwave?')
    while ready.lower() != 'yes':
        ready = ask('Are you ready to move to the microwave?')
    # Find the location of the microwave
    microwave_location = detect('microwave')
    # If the microwave is found, move to it
    if microwave_location is not None:
        move_to(microwave_location['x'], microwave_location['y'])
    else:
        say("I'm sorry, I can't find the microwave.")
else:
    say("I'm sorry, I can't find the refrigerator.")