import yolov5
import rospy
import pandas as pd
import json
import os
import actionlib
from cv_bridge import CvBridge
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
                im_topic = "camera/" + cam + "/image"
                depth_topic = "depth/" + cam + "/image"
                im = rospy.wait_for_message(im_topic, Image)
                depth_im = rospy.wait_for_message(depth_topic, CameraInfo)
                cv_im = self.bridge.imgmsg_to_cv2(im)
                depth_cv_im = self.bridge.imgmsg_to_cv2(depth_im)
                df = self.ros_detector.detect(cv_im, category)
                
                if df is not False:        
                    simple_df = pd.DataFrame()
                    for index, row in df.iterrows(): 
                        x = (row['x2'] - row['x1'])/2
                        y = (row['y2'] - row['y1'])/2 
                        simple_df.at[index, 'u'] = x
                        simple_df.at[index, 'v'] = y
                        simple_df.at[index, 'depth'] = depth_cv_im[x,y]
                        simple_df.at[index, 'category'] = row['category']
                    simple_df['camera'] = cam
                    detections_df = pd.concat([simple_df, df], ignore_index=True)
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
    


        

    