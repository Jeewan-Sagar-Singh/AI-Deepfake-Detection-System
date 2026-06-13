import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/predict-image",
        formData
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Upload Failed");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>DeepFake Detection System</h1>

      <input
        type="file"
        accept="image/*"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>
        Detect DeepFake
      </button>

      {result && (
        <div>
          <h2>Result</h2>

          <p>Filename: {result.filename}</p>
          <p>Height: {result.height}</p>
          <p>Width: {result.width}</p>
          <p>Faces Detected: {result.faces_detected}</p>
          <p>Prediction: {result.prediction}</p>
          <p>Confidence: {result.confidence}</p>
        </div>
      )}
    </div>
  );
}

export default App;