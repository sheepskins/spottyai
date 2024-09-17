'''I'm tired of all this walking around''''''{"usage_including_cached_inference": {"total_cost": 0.05097, "gpt-4-0613": {"cost": 0.05097, "prompt_tokens": 1391, "completion_tokens": 154, "total_tokens": 1545}}, "usage_excluding_cached_inference": {"total_cost": 0.05097, "gpt-4-0613": {"cost": 0.05097, "prompt_tokens": 1391, "completion_tokens": 154, "total_tokens": 1545}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("Would you like to sit down?")
answer = ask("Do you want me to find a chair for you? Yes or No?").lower()

if 'yes' in answer:
    chairs = detect("chair")
    if chairs is not False and chairs is not None:
        x, y = chairs.iloc[0]['x'], chairs.iloc[0]['y']
        move_to(x, y)
        say("We have arrived at the chair.")
    else:
        say("Sorry, I was unable to locate a chair.")
else:
    say("Okay, let me know whenever you need assistance.")
