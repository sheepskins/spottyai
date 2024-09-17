'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.04869, "gpt-4-0613": {"cost": 0.04869, "prompt_tokens": 1393, "completion_tokens": 115, "total_tokens": 1508}}, "usage_excluding_cached_inference": {"total_cost": 0.04869, "gpt-4-0613": {"cost": 0.04869, "prompt_tokens": 1393, "completion_tokens": 115, "total_tokens": 1508}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# Detect nearest person
person_df = detect('person')

if person_df is not None:
    # Get the nearest person
    nearest_person = person_df.loc[person_df['distance'].idxmin()]
    
    say("Approaching a person nearby to get their attention")
    
    # Nudge the person
    move_to(nearest_person['x'], nearest_person['y'])
   
else:
    say("No person detected nearby.")
