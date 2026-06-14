import cv2
import os

FACE_CROP_DIR = "face_crops"

os.makedirs(FACE_CROP_DIR, exist_ok=True)

cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

def detect_faces(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return 0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for i, (x, y, w, h) in enumerate(faces):

        face_crop = image[y:y+h, x:x+w]

        crop_path = os.path.join(
            FACE_CROP_DIR,
            f"face_{i}.jpg"
        )

        cv2.imwrite(crop_path, face_crop)

    return len(faces)