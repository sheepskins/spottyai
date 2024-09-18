'''Help! i think I've been bitten by a snake''''''{"usage_including_cached_inference": {"total_cost": 0.89838, "gpt-4-0613": {"cost": 0.89838, "prompt_tokens": 28268, "completion_tokens": 839, "total_tokens": 29107}}, "usage_excluding_cached_inference": {"total_cost": 0.89838, "gpt-4-0613": {"cost": 0.89838, "prompt_tokens": 28268, "completion_tokens": 839, "total_tokens": 29107}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')


def seek_help():
    # Check for nearby people who might be able to help
    people = detect('person')
    # If people detected, move towards them and inform user
    if people is not None and len(people) > 0:
        x = people.iloc[0]['x']
        y = people.iloc[0]['y']
        move_to(x, y)
        say("A person is nearby. I am guiding you towards them.")
    else:
        # If no people detected, check if user has a phone to call for help
        reply = ask("Do you have a phone with you?")
        if reply.lower() == 'yes':
            say("Please call emergency services immediately.")
        else:
            say("Searching for audible signs of people or traffic.")
            # As we don't have a function for crowd noise, guide robot in arbitrary direction 
            move_to(10, 0)  # This should be replaced with more advanced search if possible

while True:
    seek_help()