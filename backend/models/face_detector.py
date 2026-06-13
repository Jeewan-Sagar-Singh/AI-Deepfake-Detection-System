from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_faces(image_path):
    results = model(image_path)

    return len(results[0].boxes)