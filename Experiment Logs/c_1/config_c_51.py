'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 0.8979900000000001, "gpt-4-0613": {"cost": 0.8979900000000001, "prompt_tokens": 28425, "completion_tokens": 754, "total_tokens": 29179}}, "usage_excluding_cached_inference": {"total_cost": 0.8979900000000001, "gpt-4-0613": {"cost": 0.8979900000000001, "prompt_tokens": 28425, "completion_tokens": 754, "total_tokens": 29179}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("I understand the gravity of the situation! We must not panic!")
safe_to_proceed = ask("Is it safe to take a picture of the snake?")
if safe_to_proceed.lower() == 'yes':
    detection_result = detect('snake')
    if detection_result is not None:
        say(f"I have detected a {detection_result.label} at location {detection_result.x}, {detection_result.y}")
        # Dial emergency services immediately as a snake bite is potentially life threatening
        dial_emergency_services()
    else:
        say("I'm unable to detect the snake. But as you've been bitten, I'll dial the emergency services.")
        dial_emergency_services()
else:
    say("I understand. Your safety is paramount. I'm contacting the emergency services immediately. Please stay calm while help arrives.")
    dial_emergency_services()