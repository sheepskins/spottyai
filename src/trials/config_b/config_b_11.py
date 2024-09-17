'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.27117, "gpt-4-0613": {"cost": 0.27117, "prompt_tokens": 8521, "completion_tokens": 259, "total_tokens": 8780}}, "usage_excluding_cached_inference": {"total_cost": 0.27117, "gpt-4-0613": {"cost": 0.27117, "prompt_tokens": 8521, "completion_tokens": 259, "total_tokens": 8780}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# Our main goal is to detect a chair and move towards it.
# First, we will call the detect function to detect the chair
# If chair is detected, it will return a dataframe containing the chair's location. Otherwise, it will return None.

chair_position = detect('chair')

if isinstance(chair_position, pd.DataFrame):
  x = chair_position['x'][0]
  y = chair_position['y'][0]
  
  say("A chair has been detected. Now moving towards the chair.") 

  result = move_to(x, y)

  if result:
     say("You have reached to the chair.")
  else:
    say("Sorry, I was unable to reach the chair. Let's try detecting again.")

else:
  say("No chair detected. Please ensure that there is a chair detected in the surroundings.")