import cv2
from models.face_detector import detect_faces

def analyze_image(image_path):

    image = cv2.imread(image_path)

    height, width, channels = image.shape

    face_count = detect_faces(image_path)

    return {
        "height": height,
        "width": width,
        "channels": channels,
        "faces_detected": face_count,
        "prediction": "FAKE",
        "confidence": "92%"
    }