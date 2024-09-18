'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.58197, "gpt-4-0613": {"cost": 0.58197, "prompt_tokens": 17271, "completion_tokens": 1064, "total_tokens": 18335}}, "usage_excluding_cached_inference": {"total_cost": 0.58197, "gpt-4-0613": {"cost": 0.58197, "prompt_tokens": 17271, "completion_tokens": 1064, "total_tokens": 18335}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Step 1: Detect the nearest person
detection_results = detect('person')
if detection_results is not None and not isinstance(detection_results, bool):
    nearest_person = detection_results.loc[detection_results['id'] == 'person'].iloc[0]
    x, y = nearest_person['x'], nearest_person['y']
    
    # Step 2: Inform the user we've detected someone and are moving towards them
    say('Person detected, moving towards them now')
    
    # Step 3: Move towards the detected person
    move_result = move_to(x, y)
    if move_result.success:
        
        # Step 4: Let the user know we're about to nudge
        say('About to nudge the person to get their attention')
        
        # Step 5 & 6: Adjust pose to nudge the person, then reset pose
        pose(0, 5, 0, 0.1)  # Slight lean forward to simulate nudge
        pose(0, 0, 0, 0)  # Reset body pose
    else:
        say('Could not move to person safely')
else:
    say('No one detected')