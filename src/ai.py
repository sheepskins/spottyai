from sensor_msgs.msg import CameraInfo
import detection.detector as detector
import rospy
import pandas as pd
from spottyai.srv import detection, detectionResponse
from spot_msgs.msg import TrajectoryAction, TrajectoryResult, TrajectoryFeedback, TrajectoryGoal
from std_msgs.msg import Duration
import actionlib
from geometry_msgs.msg import PointStamped
from image_geometry import PinholeCameraModel
import tf2_ros
import tf2_geometry_msgs
from spot_msgs.msg import PoseBodyAction, PoseBodyResult, PoseBodyFeedback, PoseBodyGoal

def detect(category):
    rospy.wait_for_service('detection_service')
    try:
        detect = rospy.ServiceProxy('detection_service', detection)
        response = detect(category)
        if response.status == 2:
            df = pd.read_json(response.detection_results, orient='split')
            return df
        else: 
            return False
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return None

def move_to(x,y):
    client = actionlib.SimpleActionClient('trajectory', TrajectoryAction)
    
    goal = TrajectoryGoal()

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.header.frame_id = 'body'
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.duration = rospy.Duration(120)

    goal.precise_positioning = 0
    
    client.wait_for_server()

    client.send_goal(goal)

    client.wait_for_result()

    return client.get_result()

def reproject(u, v, depth, cam):
    camera_info = get_camera_info_once(cam)

    # Extract camera intrinsics
    fx = camera_info.K[0]
    fy = camera_info.K[4]
    cx = camera_info.K[2]
    cy = camera_info.K[5]

    # Compute the 3D point in the camera frame
    x = (u - cx) * depth / fx
    y = (v - cy) * depth / fy
    z = depth

    # Create a PointStamped message for the 3D point
    point_camera = PointStamped()
    point_camera.header.frame_id = camera_info.header.frame_id
    point_camera.point.x = x
    point_camera.point.y = y
    point_camera.point.z = z

    # Transform the point to the body frame
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)

    try:
        # Wait for the transform to become available
        transform = tf_buffer.lookup_transform('body', point_camera.header.frame_id, rospy.Time(0), rospy.Duration(1.0))
        point_body = tf2_geometry_msgs.do_transform_point(point_camera, transform)

        rospy.loginfo(f"3D Point in Body Frame: x={point_body.point.x}, y={point_body.point.y}, z={point_body.point.z}")
        return point_body
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
        rospy.logwarn("Transform to body frame failed.")
        return None


def get_camera_info_once(cam):
    topic = 'camera/' + cam + "/camera_info"
    # Wait for a single message from the /camera_info topic
    camera_info_msg = rospy.wait_for_message(topic, CameraInfo)

    # Process the message
    rospy.loginfo(f"Received Camera Info: {camera_info_msg}")
    return camera_info_msg

def say(string):
    print(string)

def ask(string):
    string = string + ": "
    return input(string)
    
def pose(roll, pitch, yaw, body_height): 
    client = actionlib.SimpleActionClient('pose', PoseBodyAction)
    pose = PoseBodyGoal()
    pose.roll = max(min(roll, 20), -20)
    pose.pitch = max(min(pitch, 30), -30)
    pose.yaw = max(min(yaw, 30), -30)
    pose.body_height = max(min(body_height, 0.1), -0.1)

    client.wait_for_server()

    client.send_goal_and_wait(pose)

    return(client.get_result())
