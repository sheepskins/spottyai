'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.91035, "gpt-4-0613": {"cost": 0.91035, "prompt_tokens": 28689, "completion_tokens": 828, "total_tokens": 29517}}, "usage_excluding_cached_inference": {"total_cost": 0.91035, "gpt-4-0613": {"cost": 0.91035, "prompt_tokens": 28689, "completion_tokens": 828, "total_tokens": 29517}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detection of Oven and Person
detected_items = detect('oven, person')

# Threshold for 'near'
threshold = 5

# Check whether a person is near the oven
if detected_items is not None and 'oven' in detected_items['label'].values:
    oven_location = detected_items[detected_items['label'] == 'oven'][['x', 'y']].values[0]
    persons_within_threshold = detected_items[(detected_items['label'] == 'person') & 
                                              ((abs(detected_items['x'] - oven_location[0]) < threshold) &
                                               (abs(detected_items['y'] - oven_location[1]) < threshold))]
                               
# If person is detected near the oven, go to microwave else go to oven
if not persons_within_threshold.empty:
    detected_microwave = detect('microwave')
    
    if detected_microwave is not None and 'microwave' in detected_microwave['label'].values:
        move_to(detected_microwave[detected_microwave['label'] == 'microwave'][['x', 'y']].values[0])
    else:
        say("Sorry, there is no microwave detected.")
else:
    move_to(oven_location)