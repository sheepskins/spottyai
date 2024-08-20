import detection.detector as detector
import rospy
import pandas as pd
from spottyai.srv import detection, detectionResponse
from spot_msgs.msg import TrajectoryAction, TrajectoryResult, TrajectoryFeedback, TrajectoryGoal
from std_msgs.msg import Duration
import actionlib

def detection_client(category):
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
    
    client.wait_for_server()

    goal = TrajectoryGoal()

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.header.frame_id = 'body'
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.duration = rospy.Duration(120)

    goal.precise_positioning = 0

    client.send_goal(goal)

    client.wait_for_result()

    return client.get_result()


def say(string):
    print(string)

def ask(string):
    string = string + ": "
    return input(string)