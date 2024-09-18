'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.51333, "gpt-4-0613": {"cost": 0.51333, "prompt_tokens": 16405, "completion_tokens": 353, "total_tokens": 16758}}, "usage_excluding_cached_inference": {"total_cost": 0.51333, "gpt-4-0613": {"cost": 0.51333, "prompt_tokens": 16405, "completion_tokens": 353, "total_tokens": 16758}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

chair_location = detect('chair')

if chair_location is not None:
    x, y = chair_location['x'], chair_location['y']
    say('I have found a chair. I will guide you to it.')
    move_result = move_to(x, y)

    if move_result:
        say('We have arrived at the chair.')
        user_confirm = ask('Please confirm if we are at the chair.')
        if user_confirm.lower() in ['yes', 'we are at the chair']:
            say('Thank you for confirming. Let me know if you need anything else.')
        else:
            say('I apologize for the confusion. Let\'s try again.')
    else:
        say('I was unable to move to the chair. Let\'s try again.')
else:
    say('I am unable to locate a chair at the moment.')