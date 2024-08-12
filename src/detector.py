import yolov5


img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

model = yolov5.load('yolov5s.pt', device='0')

# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

results = model(img)
print (results.pred[0][:,:4])

results.show()
