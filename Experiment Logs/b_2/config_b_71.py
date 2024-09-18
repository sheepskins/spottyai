'''Take me to the oven, but, if there is someone near it, then take me to a microwave instead.''''''{"usage_including_cached_inference": {"total_cost": 0.32118, "gpt-4-0613": {"cost": 0.32118, "prompt_tokens": 8778, "completion_tokens": 964, "total_tokens": 9742}}, "usage_excluding_cached_inference": {"total_cost": 0.32118, "gpt-4-0613": {"cost": 0.32118, "prompt_tokens": 8778, "completion_tokens": 964, "total_tokens": 9742}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# Detect objects in the surroundings
objects = detect('person,oven,microwave')

# Check if person is detected near oven
if objects is not None and 'person' in objects['label'].values and 'oven' in objects['label'].values:
    person_index = objects[objects['label'] == 'person'].index[0]
    oven_index = objects[objects['label'] == 'oven'].index[0]
    if abs(objects.loc[oven_index, 'x'] - objects.loc[person_index, 'x']) <= 1 and abs(objects.loc[oven_index, 'y'] - objects.loc[person_index, 'y']) <= 1:
        if 'microwave' in objects['label'].values:
            microwave_index = objects[objects['label'] == 'microwave'].index[0]
            say('Taking you to the microwave.')
            move_to(objects.loc[microwave_index, 'x'], objects.loc[microwave_index, 'y'])
        else:
            say('Person detected near the oven, but no microwave detected.')
            
    else:
        say('Taking you to the oven.')
        move_to(objects.loc[oven_index, 'x'], objects.loc[oven_index, 'y'])
elif objects is not None and 'oven' in objects['label'].values:
    oven_index = objects[objects['label'] == 'oven'].index[0]
    say('Taking you to the oven.')
    move_to(objects.loc[oven_index, 'x'], objects.loc[oven_index, 'y'])
else:
    say('No oven detected.')
