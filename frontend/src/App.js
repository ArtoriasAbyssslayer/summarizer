import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [summary, setSummary] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileUpload = (e) => {
    setFile(e.target.files[0]);
    setInput(""); // Clear text input when file is uploaded
  };

  const handleTextChange = (e) => {
    setInput(e.target.value);
    setFile(null); // Clear file when typing in text
  };

  const handleSummarize = async () => {
    if (!input && !file) return;

    setLoading(true);
    setSummary("");

    try {
      const formData = new FormData();
      if (file) {
        formData.append("userfile", file);
      } else {
        formData.append("chat", input);
      }

      const res = await axios.post("http://localhost:5000/summarize", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setSummary(res.data.summary);
    } catch (err) {
      console.error(err);
      const errorType = err?.response?.data?.error || err?.message || "Unknown Error";
      setSummary(`Error summarizing: ${errorType}.`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-title">Summarizer</h1>

      {/* Input Area */}
      <div className="input-box">
        <textarea
          value={input}
          onChange={handleTextChange}
          placeholder="Paste your text here..."
          className="input-field"
          rows="6"
        />
        <input
          type="file"
          accept=".pdf"
          onChange={handleFileUpload}
          className="file-upload-input"
        />
      </div>

      {/* Button */}
      <button
        onClick={handleSummarize}
        className="summarize-button"
        disabled={!input && !file || loading}
      >
        {loading ? "Summarizing..." : "Summarize"}
      </button>

      {/* Summary Output */}
      {summary && (
        <div className="summary-box">
          <h2 className="summary-title">Summary:</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
