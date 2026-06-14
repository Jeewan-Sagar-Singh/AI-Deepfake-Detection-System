import cv2
import os

from models.face_detector import detect_faces
from models.deepfake_classifier import predict_deepfake

def analyze_image(image_path):

    image = cv2.imread(image_path)

    height, width, channels = image.shape

    face_count = detect_faces(image_path)

    prediction = {
        "prediction": "NO_FACE",
        "confidence": "0%"
    }

    if face_count > 0:

        first_face = os.path.join(
            "face_crops",
            "face_0.jpg"
        )

        prediction = predict_deepfake(first_face)

    return {
        "height": height,
        "width": width,
        "channels": channels,
        "faces_detected": face_count,
        **prediction
    }