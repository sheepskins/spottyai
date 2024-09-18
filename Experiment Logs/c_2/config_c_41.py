'''Take me to the fridge, wait until I'm ready and then take me to the microwave.''''''{"usage_including_cached_inference": {"total_cost": 0.52515, "gpt-4-0613": {"cost": 0.52515, "prompt_tokens": 16651, "completion_tokens": 427, "total_tokens": 17078}}, "usage_excluding_cached_inference": {"total_cost": 0.52515, "gpt-4-0613": {"cost": 0.52515, "prompt_tokens": 16651, "completion_tokens": 427, "total_tokens": 17078}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Step 1: Detect the fridge
fridge_location = detect('refrigerator')

# Step 2: Navigate to the fridge
if isinstance(fridge_location, pd.DataFrame):
    fridge_x = fridge_location['x'][0]
    fridge_y = fridge_location['y'][0]
    move_to(fridge_x, fridge_y)

# Step 3: Wait for the user's ready signal
ask('Please tell me when you are ready to move to the microwave.')

# Step 4: Detect the microwave
microwave_location = detect('microwave')

# Step 5: Navigate to the microwave
if isinstance(microwave_location, pd.DataFrame):
    microwave_x = microwave_location['x'][0]
    microwave_y = microwave_location['y'][0]
    say('Moving to the microwave...')
    move_to(microwave_x, microwave_y)