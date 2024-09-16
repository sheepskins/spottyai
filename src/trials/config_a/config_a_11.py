'''Take me to the nearest chair''''''{"usage_including_cached_inference": {"total_cost": 0.05337000000000001, "gpt-4-0613": {"cost": 0.05337000000000001, "prompt_tokens": 1389, "completion_tokens": 195, "total_tokens": 1584}}, "usage_excluding_cached_inference": {"total_cost": 0.05337000000000001, "gpt-4-0613": {"cost": 0.05337000000000001, "prompt_tokens": 1389, "completion_tokens": 195, "total_tokens": 1584}}}'''python
from ai import detect, move_to, say
import rospy
import pandas as pd

rospy.init_node('SPOTTYAI')

# First, the AI detects the chair.
detected_chairs = detect('chair')

if isinstance(detected_chairs, pd.DataFrame) and not detected_chairs.empty:
    # Sorting the chairs by their distance from the robot (the square root of the sum of their x and y squared)
    detected_chairs['distance'] = detected_chairs['x']**2 + detected_chairs['y']**2
    detected_chairs = detected_chairs.sort_values('distance')

    # Move to the nearest chair
    nearest_chair = detected_chairs.iloc[0]
    say("Moving to the nearest chair now.")
    move_to(nearest_chair['x'], nearest_chair['y'])
    
else:
    say("I'm sorry, I couldn't detect any chairs nearby.")
