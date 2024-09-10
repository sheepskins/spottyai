from sensor_msgs.msg import CameraInfo
import rospy

from aruco_opencv_msgs.msg import ArucoDetection

from spot_msgs.msg import TrajectoryAction, TrajectoryResult, TrajectoryFeedback, TrajectoryGoal
from std_msgs.msg import Duration
import actionlib
from geometry_msgs.msg import PointStamped
from image_geometry import PinholeCameraModel
import tf2_ros
import tf2_geometry_msgs
from spot_msgs.srv import PosedStand

import sys
import os
sys.path.append(os.path.dirname(__file__))

import pandas as pd

def detect(keys):
    return_df = pd.DataFrame(columns=('x', 'y', 'id', 'label'))
    spot_cams = ["back", "frontleft", "frontright", "right", "left"]
    keys = [category.strip().lower() for category in keys.split(',')]
    categories = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),'mscoco.csv'), header=None, names=['id', 'label'])
    for cam in spot_cams:
        topic = cam+"/aruco_detections"
        camera_info = get_camera_info_once(cam)
        frame_id = camera_info.header.frame_id

        detections = rospy.wait_for_message(topic, ArucoDetection, rospy.Duration(1))
        data = []
        for marker in detections.markers:
            pose = marker.pose
            body_point = reproject(pose.position.x, pose.position.y, pose.position.z, frame_id)

            data.append({
                'x': body_point.point.x,
                'y': body_point.point.y,
                'id': marker.marker_id
            })

        # Create DataFrame from the processed data
        detections_df = pd.DataFrame(data, columns=['x', 'y', 'id'])
        detections_w_cat = detections_df.merge(categories, on = 'id')
        # filtered_detections = detections_w_cat[detections_w_cat["label"].isin(keys)]
        return_df = pd.concat([return_df, detections_w_cat], ignore_index=True)
    return return_df

def move_to(x,y):
    client = actionlib.SimpleActionClient('/spot/trajectory', TrajectoryAction)
    
    goal = TrajectoryGoal()

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.header.frame_id = 'body'
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    duration = Duration()
    duration.data.secs = 120
    duration.data.nsecs = 0
    goal.duration = duration

    goal.precise_positioning = 0
    
    client.wait_for_server()

    client.send_goal(goal)

    client.wait_for_result()

    return client.get_result()

def reproject(x,y,z, frame_id):   

    # Create a PointStamped message for the 3D point
    point_camera = PointStamped()
    point_camera.header.frame_id = frame_id
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
    topic = 'spot/camera/' + cam + "/camera_info"
    # Wait for a single message from the /camera_info topic
    camera_info_msg = rospy.wait_for_message(topic, CameraInfo)

    # Process the message
    # rospy.loginfo(f"Received Camera Info: {camera_info_msg}")
    return camera_info_msg

def say(string):
    print(string)

def ask(string):
    string = string + ": "
    return input(string)
    
def pose(roll, pitch, yaw, body_height): 
    rospy.wait_for_service('spot/posed_stand')

    pose_client = rospy.ServiceProxy('spot/posed_stand', PosedStand)

    return(pose_client(max(min(body_height, 0.1), -0.1),
                       max(min(yaw, 30), -30), 
                       max(min(pitch, 30), -30), 
                       max(min(roll, 20), -20)))
