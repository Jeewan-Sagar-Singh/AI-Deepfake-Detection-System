import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import "./ResultPage.css";

function ResultPage() {
  const { state } = useLocation();

  const [showResult, setShowResult] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowResult(true);
    }, 3000);

    return () => clearTimeout(timer);
  }, []);

  if (!state) {
    return <h1>No Result Found</h1>;
  }

  const { result, imageUrl } = state;

  return (
    <div
      style={{
        minHeight: "100vh",
        color: "white",
        textAlign: "center",
        paddingTop: "40px"
      }}
    >
      <h1>🔍 DeepFake Analysis Report</h1>

      <div
        style={{
          width: "400px",
          margin: "30px auto",
          border: "2px solid cyan",
          borderRadius: "20px",
          overflow: "hidden",
          position: "relative"
        }}
      >
        <img
          src={imageUrl}
          alt="uploaded"
          style={{
            width: "100%"
          }}
        />

        {!showResult && (
          <div
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              height: "100%",
              background:
                "linear-gradient(to bottom, transparent, rgba(0,255,255,0.5), transparent)",
              animation: "scan 1.5s linear infinite"
            }}
          />
        )}
      </div>

      {!showResult ? (
        <h2>🤖 Scanning Image...</h2>
      ) : (
        <div className="result-card">

  <h2 className="result-title">
    🤖 AI Analysis Complete
  </h2>

  <div className="fake-badge">
    {result.prediction}
  </div>

  <div className="info-box">
    <strong>Confidence</strong>
    <br />
    {result.confidence}
  </div>

  <div className="info-box">
    <strong>Faces Detected</strong>
    <br />
    {result.faces_detected}
  </div>

</div>
      )}
    </div>
  );
}

export default ResultPage;