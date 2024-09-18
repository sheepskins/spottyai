'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.55335, "gpt-4-0613": {"cost": 0.55335, "prompt_tokens": 16691, "completion_tokens": 877, "total_tokens": 17568}}, "usage_excluding_cached_inference": {"total_cost": 0.55335, "gpt-4-0613": {"cost": 0.55335, "prompt_tokens": 16691, "completion_tokens": 877, "total_tokens": 17568}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Initial detection of people and the oven
detections = detect('person, oven')

# Verifying that the detection was successful
if detections is not None and detections is not False:
    # Fetch the coordinates of people and ovens detected
    people_coordinates = detections[detections['label'] == 'person'][['x', 'y']]
    oven_coordinates = detections[detections['label'] == 'oven'][['x', 'y']]
    
    # Check if any person is close to the oven
    for i, oven_coordinate in oven_coordinates.iterrows():
        for j, person_coordinate in people_coordinates.iterrows():
            distance = ((oven_coordinate['x'] - person_coordinate['x'])**2 + (oven_coordinate['y'] - person_coordinate['y'])**2) ** 0.5
            if distance < 1:  # if a person is within 1 metre of the oven
                say('There is a person near the oven.')
                # Find a microwave 
                microwave_df = detect('microwave')
                if microwave_df is not None and microwave_df is not False:
                    # Move to the microwave
                    move_to(microwave_df.iloc[0]['x'], microwave_df.iloc[0]['y'])
                else:
                    say('I can not find any microwave.')
                break
        else:
            continue
        break
    else:
        # If no person is near any oven, move to the first oven
        move_to(oven_coordinates.iloc[0]['x'], oven_coordinates.iloc[0]['y'])
else:
    say('I was unable to detect any people or ovens.')
