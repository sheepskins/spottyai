from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Using the say function to express the robot's excitement
say("Goal! What an amazing match! I'm moving to celebrate.")

# Move to celebrate the goal
move_to(1, 0)  # Move forward by 1 meter
pose(0, 0, 0, 0.1)  # Jump by increasing body height by 0.1 meters
move_to(-1, 0)  # Move backward to original position
pose(0, 0, 0, -0.1)  # Come back to the original position

# Using the say function to conclude the celebration
say("That was a fantastic celebration! Now, back to the game.")
