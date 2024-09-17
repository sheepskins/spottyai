'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 0.05547, "gpt-4-0613": {"cost": 0.05547, "prompt_tokens": 1395, "completion_tokens": 227, "total_tokens": 1622}}, "usage_excluding_cached_inference": {"total_cost": 0.05547, "gpt-4-0613": {"cost": 0.05547, "prompt_tokens": 1395, "completion_tokens": 227, "total_tokens": 1622}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# First, alert the user to perform basic first aid steps from a bite
say("Remain calm, try to remember the color and shape of the snake, stay still to keep the venom from spreading, and keep the bitten area below heart level.")

# Look around for potential help from people
people = detect('person')
if people:
    # If there are people in proximity, move towards the closest person
    closest_person = people.loc[people['distance'].idxmin()]
    x, y = closest_person['x'], closest_person['y']
    move_to(x, y)
    say("I am moving towards a person to seek immediate help.")
else:
    # If no one is around, seek immediate professional help
    say("There is no one in the immediate vicinity. I am activating the distress signal to summon professional help immediately.")
    # Replace FunctionNeededToActivateDistressSignal with actual function
    FunctionNeededToActivateDistressSignal()
