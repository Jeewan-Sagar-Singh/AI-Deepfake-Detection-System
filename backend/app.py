from fastapi import FastAPI, UploadFile, File
import shutil
import os
import cv2
from services.deepfake_service import analyze_image
from fastapi.middleware.cors import CORSMiddleware
from services.video_service import analyze_video

app = FastAPI(title="DeepFake Detection API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {
        "message": "DeepFake Detection API Running"
    }

@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_image(file_path)

    return {
        "filename": file.filename,
        **result
    }
@app.post("/predict-video")
async def predict_video(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_video(file_path)

    return {
        "filename": file.filename,
        **result
    }