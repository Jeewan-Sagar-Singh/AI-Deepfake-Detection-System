from PIL import Image
import torchvision.transforms as transforms

def predict_deepfake(face_path):

    image = Image.open(face_path).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    tensor = transform(image)

    return {
        "prediction": "FAKE",
        "confidence": str(tensor.shape)
    }