import cv2

def analyze_video(video_path):

    cap = cv2.VideoCapture(video_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    sampled_frames = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        sampled_frames += 1

        if sampled_frames >= 10:
            break

    cap.release()

    return {
        "total_frames": total_frames,
        "fps": fps,
        "sampled_frames": sampled_frames
    }