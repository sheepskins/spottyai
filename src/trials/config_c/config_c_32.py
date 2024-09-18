'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.5413199999999999, "gpt-4-0613": {"cost": 0.5413199999999999, "prompt_tokens": 16800, "completion_tokens": 622, "total_tokens": 17422}}, "usage_excluding_cached_inference": {"total_cost": 0.5413199999999999, "gpt-4-0613": {"cost": 0.5413199999999999, "prompt_tokens": 16800, "completion_tokens": 622, "total_tokens": 17422}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# 1. Detect persons
results = detect('person')

# 2. Check if a person was detected
if not results.empty:
    # Get the nearest person coordinates
    x_nearest_person, y_nearest_person = results.iloc[0][['x', 'y']]
    
    # Safe distance definition
    safe_distance = 1.5
    closer_distance = 1.0

    # 3. Move to the nearest person with a safe distance
    move_to(x_nearest_person, y_nearest_person - safe_distance)
    
    # 4. Ask for attention
    say("Excuse me")

    # 5. Nudge the person by moving closer
    move_to(x_nearest_person, y_nearest_person - closer_distance)
    
    # 6. Convey purpose
    say("Your attention is needed.")
else:
    # If no persons were detected
    say("I can't detect anyone nearby.")