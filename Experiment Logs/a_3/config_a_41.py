'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.055979999999999995, "gpt-4-0613": {"cost": 0.055979999999999995, "prompt_tokens": 1402, "completion_tokens": 232, "total_tokens": 1634}}, "usage_excluding_cached_inference": {"total_cost": 0.055979999999999995, "gpt-4-0613": {"cost": 0.055979999999999995, "prompt_tokens": 1402, "completion_tokens": 232, "total_tokens": 1634}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Locate the refrigerator
fridge_location = detect('refrigerator')
if fridge_location is not None:
    # Move to the refrigerator
    move_to(fridge_location['x'], fridge_location['y'])
    say('We are at the fridge.')
else:
    say('I could not locate the fridge.')

# Wait until user is ready
while True:
    user_ready = ask('Are you ready to move to the microwave?')
    if user_ready.lower() in ['yes', 'y', 'ready', 'ok', 'okay']:
        break
    else:
        say('Okay, take your time. Let me know when you are ready to move.')

# Locate the microwave
microwave_location = detect('microwave')
if microwave_location is not None:
    # Move to the microwave
    move_to(microwave_location['x'], microwave_location['y'])
    say('We are at the microwave.')
else:
    say('I could not locate the microwave.')
