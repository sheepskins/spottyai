from ai import detect, move_to, say, ask, pose
import rospy
import time

rospy.init_node('SPOTTYAI')

# Making an announcemet
say('Starting a ballet twirl and jump.')

# Start ballet twirl, rotate 180 degree in spot. To perform a full spin, we do this twice.
move_to(0, 0, 180)

# Brief pause to make sure the turn above is completed
time.sleep(1)

# Rotate another 180 degrees to complete full spin
move_to(0, 0, 180)

# Pause again before the next movement
time.sleep(1)

# Lift the body height represents a jump movement
say('Performing a jump.')
pose(0, 0, 0, 0.1)

# Brief pause before going back down
time.sleep(0.5)

# Lower the body to complete the jump
pose(0, 0, 0, 0)

# Completion message
say('Finished the ballet twirl and jump.')