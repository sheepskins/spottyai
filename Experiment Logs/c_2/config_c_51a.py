'''help! I think I've been bitten by a snake''''''{"usage_including_cached_inference": {"total_cost": 1.7914199999999998, "gpt-4-0613": {"cost": 1.7914199999999998, "prompt_tokens": 55924, "completion_tokens": 1895, "total_tokens": 57819}}, "usage_excluding_cached_inference": {"total_cost": 1.7914199999999998, "gpt-4-0613": {"cost": 1.7914199999999998, "prompt_tokens": 55924, "completion_tokens": 1895, "total_tokens": 57819}}}'''

from ai import detect, move_to, say, ask, pose
import rospy

# Start the robot system
rospy.init_node('SPOTTYAI')

# Ask the user to describe the snake
snake_description = ask("Can you describe the snake that bit you?")

# Check for nearby humans who could assist
nearby_humans = detect('person')
direction_co_ordinates = {'North': (0.0, 10.0), 'South': (0.0, -10.0), 'East': (10.0, 0.0), 'West': (-10.0, 0.0)} # Map of directions to coordinates

# If no humans are close, ask the user for a known open spot and move there
if not nearby_humans:
    direction = ask("Do you know any open spots near you where we can move? Please answer in North, South, East, or West.")
    say("No one is near us right now. I am guiding you to the open spot you described.")
    # The direction needs to be processed and converted into coordinates in an actual implementation
    x, y = direction_co_ordinates.get(direction, (0.0, 0.0))  # Gets the coordinates for the direction, defaults to (0, 0) if direction isn't in the map
    move_to(x, y)
    
# Keep detecting for any approaching humans and inform them about the situation
while True:
    nearby_humans = detect('person')
    if nearby_humans:
        say("Human detected nearby. Help is on the way.")
        break    # Stop moving once a human is detected
        
rospy.sleep(1)