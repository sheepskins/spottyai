import yolov5
import rospy
import pandas as pd
import json
import os
import actionlib
from cv_bridge import CvBridge
from image_geometry import PinholeCameraModel
import tf2_ros
from sensor_msgs.msg import Image, CameraInfo
import tf2_geometry_msgs
from spottyai.srv import detection, detectionRequest, detectionResponse

class Detector:
    """docstring for detector."""
    def __init__(self, config):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, config)

        with open(config_path, 'r') as f:
            self.config = json.load(f)

        self.model = yolov5.load(os.path.join(base_dir,self.config.get('weights')))
        # set model parameters
        self.model.conf = 0.25  # NMS confidence threshold
        self.model.iou = 0.45  # NMS IoU threshold
        self.model.agnostic = False  # NMS class-agnostic
        self.model.multi_label = False  # NMS multiple labels per box
        self.model.max_det = 1000  # maximum number of detections per image
        self.categories = pd.read_csv(os.path.join(base_dir,self.config.get('categories')), header=None, names=['category', 'labels'])
    
    def detect(self, img, category):
        results = self.model(img)
        categories = ['x1', 'y1', 'x2', 'y2', 'score', 'category']
        predictions = pd.DataFrame(results.pred[0].cpu(), columns=categories)
        detections = predictions.merge(self.categories, on = 'category')
        filtered_detections = detections.loc[detections['labels'].str.lower() == str(category).lower()]
        if filtered_detections.empty:
            return False
        return filtered_detections.iloc[:,:4]
    
# class Reproject:
#     """docstring for Reproject."""
#     def __init__(self, arg):
#         self.camera_model  = PinholeCameraModel()
#         self.tf_buffer = tf2_ros.Buffer()
#         self.tf_listenener = tf2_ros.TransformListener(self.tf_buffer)
        
#     def reproject(self, im, centre_x, centre_y, info):
#         self.camera_model.fromCameraInfo(info)
        

class RosBridge:
    def __init__(self):
        self.ros_detector = Detector('config/config.json')
        self.spot_cams = self.ros_detector.config.get('spot_cams')
        service = rospy.Service('detection_service', detection, self.service_handle)

        self.bridge = CvBridge()

    def callback(self, category):
        detections_df = pd.DataFrame()
        string = ""
        success = 1
        try:
            for cam in self.spot_cams: 
                im_topic = cam + "/image"
                info_topic = cam + "/camera_info"
                im = rospy.wait_for_message(im_topic, Image)
                info = rospy.wait_for_message(info_topic, CameraInfo)
                cv_im = self.bridge.imgmsg_to_cv2(im)
                df = self.ros_detector.detect(cv_im, category)
                if df is not False:        
                    df['camera'] = info_topic
                    detections_df = pd.concat([detections_df, df], ignore_index=True)
            if ~detections_df.empty:
                success = 1
                string =  detections_df.to_json(orient='split')
        except:
            success = 0  

        return success, string
        
    def service_handle(self, req):
        category = req.category
        success, dataframe_json  = self.callback(category)
        return detectionResponse(success, dataframe_json)


if __name__ == "__main__":
    rospy.init_node('Detection_Server')
    mybridge = RosBridge()
    rospy.loginfo("Detection service is ready.")
    
    rospy.spin()
    


        

    