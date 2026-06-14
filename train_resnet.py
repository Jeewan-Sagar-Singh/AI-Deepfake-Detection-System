import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms
from torchvision.models import resnet18

from torch.utils.data import DataLoader, random_split

# ----------------------------
# Config
# ----------------------------

BATCH_SIZE = 16
EPOCHS = 5
LEARNING_RATE = 0.001

# ----------------------------
# Dataset
# ----------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

dataset = datasets.ImageFolder(
    "datasets",
    transform=transform
)

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size

train_dataset, val_dataset = random_split(
    dataset,
    [train_size, val_size]
)

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("Train Images:", len(train_dataset))
print("Validation Images:", len(val_dataset))

# ----------------------------
# Model
# ----------------------------

model = resnet18(weights="DEFAULT")

model.fc = nn.Linear(
    model.fc.in_features,
    2
)

device = torch.device("cpu")

model = model.to(device)

# ----------------------------
# Loss + Optimizer
# ----------------------------

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)

best_accuracy = 0

# ----------------------------
# Training Loop
# ----------------------------

for epoch in range(EPOCHS):

    model.train()

    running_loss = 0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    # ------------------------
    # Validation
    # ------------------------

    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in val_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)

            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total

    print(
        f"Epoch {epoch+1}/{EPOCHS} | "
        f"Loss: {running_loss:.4f} | "
        f"Val Accuracy: {accuracy:.2f}%"
    )

    if accuracy > best_accuracy:

        best_accuracy = accuracy

        torch.save(
            model.state_dict(),
            "best_model.pth"
        )

        print("Model Saved")

print("\nTraining Complete")
print("Best Accuracy:", best_accuracy)