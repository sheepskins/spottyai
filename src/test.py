from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Tell the user that we are looking for a place to rest
say('Alright, lets find a place for you to rest. Let me look around.')

# Detect chairs or benches
rest_locations = detect('chair,bench,couch')

# If rest_places exists
if isinstance(rest_locations, pd.DataFrame):
    # Choose the first location
    resting_spot = rest_locations.iloc[0]

    # Tell the user that we found a place to rest
    say('I have found a place for you to rest. Let me guide you there.')

    # Move to the resting spot
    move_to(resting_spot['x'], resting_spot['y'])

    # Say that we have reached the destination
    say('We have reached the resting place.')
else:
    # If no rest_places is found
    say('I am sorry, I could not find any place for you to rest nearby.')