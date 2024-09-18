'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.5185500000000001, "gpt-4-0613": {"cost": 0.5185500000000001, "prompt_tokens": 16461, "completion_tokens": 412, "total_tokens": 16873}}, "usage_excluding_cached_inference": {"total_cost": 0.5185500000000001, "gpt-4-0613": {"cost": 0.5185500000000001, "prompt_tokens": 16461, "completion_tokens": 412, "total_tokens": 16873}}}'''
from ai import detect, move_to, say
import rospy

rospy.init_node('SPOTTYAI')

# Detect the chair
chair = detect('chair')

# Check if chair is detected
if chair is not None:
    # Chair detected, retrieve its coordinates
    x = chair['x']
    y = chair['y']

    # Inform the user
    say("Chair detected, moving towards it.")

    # Move to the chair
    move_to(x, y)

else:
    # Chair not detected
    say("Sorry, no chair detected in the vicinity.")