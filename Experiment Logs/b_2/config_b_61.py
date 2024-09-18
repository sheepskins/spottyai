'''Go nudge the nearest person to get their attention''''''{"usage_including_cached_inference": {"total_cost": 0.28847999999999996, "gpt-4-0613": {"cost": 0.28847999999999996, "prompt_tokens": 8514, "completion_tokens": 551, "total_tokens": 9065}}, "usage_excluding_cached_inference": {"total_cost": 0.28847999999999996, "gpt-4-0613": {"cost": 0.28847999999999996, "prompt_tokens": 8514, "completion_tokens": 551, "total_tokens": 9065}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detect the nearest person
detected_obj = detect('person')

if detected_obj is not None and len(detected_obj) > 0:
    # Choose the nearest detected person
    nearest_person = detected_obj.loc[detected_obj['distance'].idxmin()].values.tolist()

    # Approach movement
    approach_distance = 1.0  # meters, distance to stop from the person

    if nearest_person[0] > approach_distance:
        say('Moving towards the nearest person.')
        move_result = move_to(nearest_person[0] - approach_distance, nearest_person[1])

        if move_result.succeed:
            say('Now close to the person. I will give them a gentle nudge.')
            move_to(approach_distance - 0.5, 0)  # nudge with half meter
        else:
            say('Failed to move to person.')
    else:
        say("I'm already close to the person. I will give them a gentle nudge.")
        move_to(approach_distance - 0.5, 0) # nudge with half meter
else:
    say('No people detected.')
