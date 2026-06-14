import torch
import torch.nn as nn

from PIL import Image
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
        "best_model.pth",
        map_location="cpu"
    )
)

model.eval()

# -------------------------
# Image Path
# -------------------------

IMAGE_PATH = input("Enter image path: ")

# -------------------------
# Transform
# -------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

image = Image.open(
    IMAGE_PATH
).convert("RGB")

image = transform(image)

image = image.unsqueeze(0)

# -------------------------
# Prediction
# -------------------------

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
    "FAKE",
    "REAL"
]

print(
    "\nPrediction:",
    classes[predicted.item()]
)
print("Predicted Class Index:", predicted.item())
print("All Probabilities:", probabilities)
print(
    "Confidence:",
    round(
        confidence.item() * 100,
        2
    ),
    "%"
)