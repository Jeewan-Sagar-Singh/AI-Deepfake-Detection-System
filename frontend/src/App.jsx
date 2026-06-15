import { useState } from "react";
import axios from "axios";
import "./App.css";
import { useNavigate } from "react-router-dom";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const navigate = useNavigate();
  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "https://ai-deepfake-detection-system-1nnx.onrender.com/predict-image",
        formData
      );

      navigate("/result", {
        state: {
          result: response.data,
          imageUrl: URL.createObjectURL(file)
        }
      });
    } catch (error) {
      console.error(error);
      alert("Upload Failed");
    }
  };

  return (
    <div className="container">

      <h1 className="title">
        Welcome to Jeewan Sagar Singh
        <br />
        Deep Fake Detection Model
      </h1>

      <p className="subtitle">
        AI Powered Image & Video DeepFake Detection System
      </p>

      <div className="upload-section">

  <label className="upload-box">

    <h2>📷 IMAGE</h2>

    <p>Click To Upload Image</p>

    <input
      type="file"
      accept="image/*"
      style={{ display: "none" }}
      onChange={(e) => setFile(e.target.files[0])}
    />

  </label>

  <label className="upload-box">

    <h2>🎥 VIDEO</h2>

    <p>Click To Upload Video</p>

    <input
      type="file"
      accept="video/*"
      style={{ display: "none" }}
    />

  </label>

</div>

      <br />

      <button onClick={handleUpload}>
        Detect DeepFake
      </button>

      {result && (
  <div className="result-card">

    <h2>🔍 Detection Result</h2>

    <p><strong>Filename:</strong> {result.filename}</p>

    <p><strong>Height:</strong> {result.height}</p>

    <p><strong>Width:</strong> {result.width}</p>

    <p><strong>Faces Detected:</strong> {result.faces_detected}</p>

    <p><strong>Prediction:</strong> {result.prediction}</p>

    <p><strong>Confidence:</strong> {result.confidence}</p>

  </div>
)}

    </div>
  );
}

export default App;