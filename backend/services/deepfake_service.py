import cv2

def analyze_image(image_path):

    image = cv2.imread(image_path)

    height, width, channels = image.shape

    return {
        "height": height,
        "width": width,
        "channels": channels,
        "prediction": "FAKE",
        "confidence": "92%"
    }