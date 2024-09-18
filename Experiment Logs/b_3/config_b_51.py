'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 0.28637999999999997, "gpt-4-0613": {"cost": 0.28637999999999997, "prompt_tokens": 8580, "completion_tokens": 483, "total_tokens": 9063}}, "usage_excluding_cached_inference": {"total_cost": 0.28637999999999997, "gpt-4-0613": {"cost": 0.28637999999999997, "prompt_tokens": 8580, "completion_tokens": 483, "total_tokens": 9063}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

say("Are you certain it was a snake?")
snake_bite_confirm = ask("Please confirm if you were bitten by a snake")
if 'yes' in snake_bite_confirm.lower():
    say("Okay, stay calm. I'm going to get help. Can you tell me any landmarks or places nearby?")
    location_hint = ask("Do you know any landmark or place nearby?")
    say("I am going to find help. Please stay still and try not to panic")
    # Detect persons around to ask for help
    detected_persons = detect('person')
    if detected_persons is not None:
        for index, row in detected_persons.iterrows():
            move_to(row['x'], row['y'])
            say("Hello, my owner needs help. He got bitten by a snake near " + location_hint)
    else:
        say("There is no one around. I am going to search for a closer populated area")
        move_to(50, 50)
else:
    say("Alright, just stay calm and let me know if you need anything else.")