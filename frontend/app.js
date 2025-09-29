// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import CalculatorForm from 'C:\Users\Yeshwant\OneDrive\Desktop\diabetes\Lifecycle-assesment-tool\frontend\components\calculatorform.js';
// 1. UNCOMMENT the line below to import your new component
import ResultsDashboard from './components/ResultsDashboard';
import './App.css';

function App() {
  // ... (all the state and handleCalculate function remains the same)
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleCalculate = async (formData) => {
    setLoading(true);
    setError('');
    setResults(null);
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/calculate', formData);
      setResults(response.data);
    } catch (err) {
      setError('Failed to connect to the server. Please ensure the backend is running.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>CircularityAI ♻️</h1>
        <p>An AI-Powered Sustainability Calculator</p>
      </header>
      <main>
        <CalculatorForm onCalculate={handleCalculate} loading={loading} />
        
        {error && <p className="error">{error}</p>}
        
        {/* 2. UNCOMMENT this line to display the dashboard when you have results */}
        {results && <ResultsDashboard results={results} />}
      </main>
    </div>
  );
}

export default App;