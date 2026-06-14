import cv2
import os
from models.face_detector import detect_faces

FRAMES_DIR = "frames"

os.makedirs(FRAMES_DIR, exist_ok=True)

def analyze_video(video_path):

    cap = cv2.VideoCapture(video_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_index = 0
    saved_frames = 0
    total_faces = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        if frame_index % 20 == 0:

            frame_path = os.path.join(
                FRAMES_DIR,
                f"frame_{saved_frames}.jpg"
            )

            cv2.imwrite(frame_path, frame)

            faces = detect_faces(frame_path)

            total_faces += faces

            saved_frames += 1

        frame_index += 1

    cap.release()

    return {
        "total_frames": total_frames,
        "fps": fps,
        "frames_extracted": saved_frames,
        "faces_detected": total_faces
    }