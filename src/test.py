from ai import detect, reproject, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# while True:
#     pose(20, -10, 0, 0)
#     rospy.sleep(rospy.Duration(1))
#     pose(-20, -10, 0, 0)
#     rospy.sleep(rospy.Duration(1))
#     pose(0, -10, 0, 0.1)
#     rospy.sleep(rospy.Duration(1))
#     pose(0, -10, 0, 0)
#     rospy.sleep(rospy.Duration(1))


chair = detect('chair, dog').iloc[0]
reproject(chair['u'], chair['v'], chair['depth'], chair['camera'])