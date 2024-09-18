'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 0.05271, "gpt-4-0613": {"cost": 0.05271, "prompt_tokens": 1395, "completion_tokens": 181, "total_tokens": 1576}}, "usage_excluding_cached_inference": {"total_cost": 0.05271, "gpt-4-0613": {"cost": 0.05271, "prompt_tokens": 1395, "completion_tokens": 181, "total_tokens": 1576}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# First, we need to ensure the surroundings are safe
say("Looking for threats in the surrounding")

detections = detect('snake')
if detections:
    # snake detected avoid it
    for idx, detection in detections.iterrows():
        say("Snake detected at coordinates {},{}. Taking evasive actions.".format(detection['x'], detection['y']))
        safe_x = detection['x'] + 1  # add 1 meter to the current location
        safe_y = detection['y'] + 1  # add 1 meter to the current location
        move_to(safe_x, safe_y)

# Now Call for help
say("Calling for help, please hold on")

# Here goes your code to call help
