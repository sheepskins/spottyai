import rospy
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
from std_msgs.msg import Header
import cv2

bridge = CvBridge()
img = cv2.imread("bus.jpg")
im = bridge.cv2_to_imgmsg(img)
info_msg = CameraInfo()
info_msg.header = Header()

info_msg.height = 720
info_msg.width = 1280
info_msg.distortion_model = "plumb_bob"
info_msg.K = [10, 0, 0, 0, 10, 0, 0, 0, 1]

pubs = []
pubs.append(rospy.Publisher("camera/back/image", Image, queue_size=10))
pubs.append(rospy.Publisher("camera/frontleft/image", Image, queue_size=10))
pubs.append(rospy.Publisher("camera/frontright/image", Image, queue_size=10))
pubs.append(rospy.Publisher("camera/right/image", Image, queue_size=10))
pubs.append(rospy.Publisher("camera/left/image", Image, queue_size=10))

in_pub = []
in_pub.append(rospy.Publisher("camera/back/camera_info", CameraInfo, queue_size=10))
in_pub.append(rospy.Publisher("camera/frontleft/camera_info", CameraInfo, queue_size=10))
in_pub.append(rospy.Publisher("camera/frontright/camera_info", CameraInfo, queue_size=10))
in_pub.append(rospy.Publisher("camera/right/camera_info", CameraInfo, queue_size=10))
in_pub.append(rospy.Publisher("camera/left/camera_info", CameraInfo, queue_size=10))

if __name__ == "__main__":
    rospy.init_node('im')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        im.header.stamp = rospy.Time.now()
        info_msg.header.stamp = rospy.Time.now()
        for i, pub in enumerate(pubs):
            pub.publish(im)
            info_msg.header.frame_id = str(i)
            in_pub[i].publish(info_msg)
        rate.sleep()


