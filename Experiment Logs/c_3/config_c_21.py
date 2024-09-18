'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.86229, "gpt-4-0613": {"cost": 0.86229, "prompt_tokens": 27757, "completion_tokens": 493, "total_tokens": 28250}}, "usage_excluding_cached_inference": {"total_cost": 0.86229, "gpt-4-0613": {"cost": 0.86229, "prompt_tokens": 27757, "completion_tokens": 493, "total_tokens": 28250}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Looking for a place to sit
detected_items = detect('chair,bench')

if detected_items is not None and not detected_items.empty:
    # Choose the first available option
    item = detected_items.iloc[0]

    say("I found a " + item['label'] + ", and now we are moving towards it.")
    
    # Move towards the found sitting spot
    move_result = move_to(item['x'], item['y'])
    if move_result:
        say("We have arrived at the "+ item['label'] + ". You can sit down now.")
    else:
        say("Sorry, we could not move to the desired location. We will try again.")

elif detected_items is False:
    say("Apologies, we encountered an issue while searching for a place to sit.")

else:
    say("Sorry, I couldn't find a bench or a chair nearby.")