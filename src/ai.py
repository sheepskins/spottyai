import detection.detector as detector
import rospy
import pandas as pd
from spottyai.srv import detection, detectionResponse

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

def say(string):
    print(string)

def ask(string):
    string = string + ": "
    return input(string)