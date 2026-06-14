from PIL import Image

import torch
import torch.nn as nn

from torchvision import transforms
from torchvision.models import resnet18


# -------------------------
# Model
# -------------------------

model = resnet18(weights=None)

model.fc = nn.Linear(
    model.fc.in_features,
    2
)

model.load_state_dict(
    torch.load(
        "../best_model.pth",
        map_location="cpu"
    )
)

model.eval()


# -------------------------
# Prediction
# -------------------------

def predict_deepfake(face_path):

    image = Image.open(
        face_path
    ).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(
            output,
            dim=1
        )

        confidence, predicted = torch.max(
            probabilities,
            1
        )

    classes = [
        "DEEPFAKE",
        "REAL"
    ]

    return {
        "prediction": classes[predicted.item()],
        "confidence": f"{round(confidence.item()*100,2)}%"
    }