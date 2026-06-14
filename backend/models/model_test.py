import torch
import torch.nn as nn
import timm


class DeepfakeModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.backbone = timm.create_model(
            "tf_efficientnetv2_s",
            pretrained=False,
            num_classes=0
        )

        self.classifier = nn.Sequential(
            nn.Linear(1280, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(256, 1)
        )

    def forward(self, x):
        x = self.backbone(x)
        x = self.classifier(x)
        return x


model = DeepfakeModel()

checkpoint = torch.load(
    "model/pytorch_model.bin",
    map_location="cpu"
)

model.load_state_dict(checkpoint)

print("MODEL LOADED SUCCESSFULLY")