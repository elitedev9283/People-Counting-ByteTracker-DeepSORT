from ultralytics import YOLO
# from supervision.video.dataclasses import VideoInfo
# from supervision.video.sink import VideoSink
# from supervision.video.source import get_video_frames_generator
# from supervision.tools.line_counter import LineCounter
# from supervision.geometry.dataclasses import Point
# Configure the tracking parameters and run the tracker
model = YOLO('yolov8n.pt')
results = model.track(source="SnapSave.io-background video _ people _ walking _.mp4", save_txt=True,save=True,show=True,tracker="bytetrack.yaml") 
print(len(results[0]))

# results = model.track(source="https://youtu.be/LNwODJXcvt4", conf=0.3, iou=0.5, show=True)

# boxes = results[0].boxes.xywh.cpu()
# # class_ids = [results[0].boxes.class[i].item() for i in range(len(boxes))]
# track_ids = [results[0].boxes.id[i].item() for i in range(len(boxes))]