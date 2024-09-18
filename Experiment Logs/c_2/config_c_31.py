'''I'm hungry, help me get some food''''''{"usage_including_cached_inference": {"total_cost": 0.8553, "gpt-4-0613": {"cost": 0.8553, "prompt_tokens": 27560, "completion_tokens": 475, "total_tokens": 28035}}, "usage_excluding_cached_inference": {"total_cost": 0.8553, "gpt-4-0613": {"cost": 0.8553, "prompt_tokens": 27560, "completion_tokens": 475, "total_tokens": 28035}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# define categories of obstacles to be detected
obstacles = 'person,bicycle,car,bus,motorcycle'

# use detect function to look for obstacles
obstacle_detection = detect(obstacles)

# if obstacles are detected, inform the user and adjust the route
if obstacle_detection is not None:
    say('Obstacle detected. Adjusting route.')
    
# inform the user that we're about to start moving
say('We are about to start moving towards the restaurant. Please make sure you are ready.')

# ask if the user is ready to start moving
ready = ask('Are you ready to start moving towards the restaurant?')
if ready.lower() == 'yes':
    # move towards the restaurant
    move_to_result = move_to(0, 10)  # update the coordinates as required

    # if moving to the restaurant was successful, inform the user
    if move_to_result:
        say('We have arrived at the restaurant.')
    else:
        # if there was a problem moving to the restaurant, inform the user
        say('Something went wrong while attempting to move. Please try again.')
else:
    say('Ok, we will wait until you are ready.')