import yolov5
import rospy
import pandas as pd
import json
import os
import actionlib
from cv_bridge import CvBridge
from image_geometry import PinholeCameraModel
import tf2_ros, tf2_geometry_msgs

# ADD Depth and Images
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
        self.categories = pd.read_csv(os.path.join(base_dir,self.config.get('categories')), header=None, names=['categories', 'labels'])
    
    def detect(self, img, category):
        results = self.model(img).pandas()
        predictions = results.pred[0]
        detections = predictions.merge(self.categories, on = 'categories')
        filtered_detections = detections[detections['labels'] == category]
        return filtered_detections[:,:4]
    
class Reproject:
    """docstring for Reproject."""
    def __init__(self, arg):
        self.camera_model  = PinholeCameraModel()
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listenener = tf2_ros.TransformListener(self.tf_buffer)
        
    def reproject(self, im, centre_x, centre_y, info):
        self.camera_model.fromCameraInfo(info)
        

class RosBridge:
    """docstring for RosBridge."""
    def __init__(self, arg):
        self.ros_detector = Detector('config/config.json')
        self.spot_cams = self.ros_detector.config.get('spot_cams')
        self._as = actionlib.SimpleActionServer('object_detect', object_action, execute_cb = self.callback, auto_start = False)
        self._as.start()
        self.bridge = CvBridge()
        self.projector = Reproject()

    def callback(self, category):
        detections_df = pd.DataFrame()
        for cam in self.spot_cams: 
            im_topic = cam + "/depth_in_visual"
            info_topic = cam + "/depth_in_visual/camera_info"
            im = rospy.wait_for_message(im_topic, Image)
            info = rospy.wait_for_message(info_topic, CameraInfo)
            cv_im = self.bridge.imgmsg_to_cv2(im, desired_encoding='bgr8')
            df = self.ros_detector.detect(cv_im, category)
            for detection in df: 
                centre_x = (detection[0] + detection[2])/2
                centre_y = (detection[1] + detection[3])/2
                self.projector.reproject(im, centre_x, centre_y, info)


            df['camera'] = info_topic
            detections_df = pd.concat([detections_df, df], ignore_index=True)
        
        

        

        

            



        

    