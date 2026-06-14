import os
import random
import torch
import torch.nn as nn

from PIL import Image
from torchvision import transforms
from torchvision.models import resnet18

# -----------------------------
# Load Model
# -----------------------------

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

# -----------------------------
# Transform
# -----------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# -----------------------------
# Dataset Paths
# -----------------------------

REAL_PATH = "datasets/real"
FAKE_PATH = "datasets/fake"

# -----------------------------
# Sample Images
# -----------------------------

real_images = random.sample(
    os.listdir(REAL_PATH),
    min(100, len(os.listdir(REAL_PATH)))
)

fake_images = random.sample(
    os.listdir(FAKE_PATH),
    min(100, len(os.listdir(FAKE_PATH)))
)

# -----------------------------
# Evaluation Function
# -----------------------------

def predict(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        output = model(image)

        prediction = torch.argmax(
            output,
            dim=1
        ).item()

    return prediction

# -----------------------------
# Real Accuracy
# -----------------------------

real_correct = 0

for file in real_images:

    pred = predict(
        os.path.join(
            REAL_PATH,
            file
        )
    )

    if pred == 1:
        real_correct += 1

# -----------------------------
# Fake Accuracy
# -----------------------------

fake_correct = 0

for file in fake_images:

    pred = predict(
        os.path.join(
            FAKE_PATH,
            file
        )
    )

    if pred == 0:
        fake_correct += 1

# -----------------------------
# Results
# -----------------------------

real_acc = real_correct
fake_acc = fake_correct

overall = (
    real_correct +
    fake_correct
) / 200 * 100

print("\n===== RESULTS =====")
print(f"Real Accuracy : {real_acc}%")
print(f"Fake Accuracy : {fake_acc}%")
print(f"Overall Accuracy : {overall:.2f}%")