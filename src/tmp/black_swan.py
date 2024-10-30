from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Identifying the space as the stage
say("Setting the stage for the performance of the Black Swan.")
# Starting Pose - Opening Scene
pose(0, 20, 0, 0.1)  # Head up looking at the audience

# Scene 1 - Black Swan's entrance
say("The Black Swan makes a dramatic entrance.")
move_to(0.3, 0, 60)

# Scene 2 - Black Swan dances across the stage
say("The Black Swan dances gracefully across the stage.")
pose(0, -20, 30, 0)  # Movement like a swan paddling
move_to(0.6, 0.2, -30)

# Scene 3 - Black Swan makes a dramatic twist
say("A dramatic twist ensues...")
pose(0, 20, -30, 0)
move_to(0, 0, -90)  # 90 degree turn

# Scene 4 - Black Swan finale
say("The performance reaches its heartfelt finale.")
pose(0, 0, 0, -0.1)  # Bow to the audience

# Closing
say("End of the Black Swan performance. Thank you.")