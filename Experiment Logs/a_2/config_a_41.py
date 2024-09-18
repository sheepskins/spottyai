'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.057839999999999996, "gpt-4-0613": {"cost": 0.057839999999999996, "prompt_tokens": 1402, "completion_tokens": 263, "total_tokens": 1665}}, "usage_excluding_cached_inference": {"total_cost": 0.057839999999999996, "gpt-4-0613": {"cost": 0.057839999999999996, "prompt_tokens": 1402, "completion_tokens": 263, "total_tokens": 1665}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Locate the fridge
fridge_location = detect('refrigerator')
if isinstance(fridge_location, pd.DataFrame):
    fridge_x = fridge_location['x'].iloc[0]
    fridge_y = fridge_location['y'].iloc[0]

    # Move to the fridge
    move_to(fridge_x, fridge_y)
    say("We have arrived at the fridge.")

    # Wait for user to finish
    while True:
        ready = ask("Are you ready to move to the microwave?")
        if ready.lower() == "yes":
            break

    # Locate the microwave
    microwave_location = detect('microwave')
    if isinstance(microwave_location, pd.DataFrame):
        microwave_x = microwave_location['x'].iloc[0]
        microwave_y = microwave_location['y'].iloc[0]

        # Move to the microwave
        move_to(microwave_x, microwave_y)
        say("We have now arrived at the microwave.")

    else:
        say("I could not detect the microwave. Please direct me.")

else:
    say("I cannot locate the fridge. Please direct me.")
