'''Take me to the fridge, wait until I'm ready and then take me to the microwave''''''{"usage_including_cached_inference": {"total_cost": 0.89535, "gpt-4-0613": {"cost": 0.89535, "prompt_tokens": 28427, "completion_tokens": 709, "total_tokens": 29136}}, "usage_excluding_cached_inference": {"total_cost": 0.89535, "gpt-4-0613": {"cost": 0.89535, "prompt_tokens": 28427, "completion_tokens": 709, "total_tokens": 29136}}}'''
from ai import detect, move_to, say, ask
import rospy

rospy.init_node('SPOTTYAI')

# Step 1 and 2: Detect the fridge and move to its position
fridge = detect('refrigerator')
if fridge is not None and fridge is not False:
    fridge_x = fridge.iloc[0]['x']
    fridge_y = fridge.iloc[0]['y']
    result = move_to(fridge_x, fridge_y)

    if result.is_successful:
        # Step 3: Inform the user that they've arrived at the fridge
        say('We have arrived at the fridge. I will wait until you are ready to proceed.')
        
        # Step 4: Wait till user is ready to proceed
        response = ''
        while response.lower() not in ['yes', 'yeah', 'yea', 'yup', 'y']:
            response = ask('Are you ready to proceed to the microwave? Please respond with yes or no.')
            
        # Step 5: Detect the microwave and move to its position
        microwave = detect('microwave')
        if microwave is not None and microwave is not False:
            microwave_x = microwave.iloc[0]['x']
            microwave_y = microwave.iloc[0]['y']
            result = move_to(microwave_x, microwave_y)
            
            if result.is_successful:
                # Step 6: Inform the user that they've arrived at the microwave
                say('We have arrived at the microwave.')
            else:
                say('Sorry, there was an error in the movement to the microwave, please try again.')
        else:
            say('Sorry, the microwave was not found in the area.')
    else:
        say('Sorry, there was an error in the movement to the fridge, please try again.')
else:
    say('Sorry, the fridge was not detected in the area.')