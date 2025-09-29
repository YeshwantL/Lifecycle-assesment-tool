// src/components/CalculatorForm.js
import React, { useState } from 'react';

function CalculatorForm({ onCalculate, loading }) {
  // State to manage the form inputs
  const [tons, setTons] = useState(100);
  const [recycledPercent, setRecycledPercent] = useState(50);

  // This function is called when the user clicks the submit button
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevents the browser from reloading the page
    // Call the onCalculate function passed down from App.js
    onCalculate({ tons: parseFloat(tons), recycled_percent: parseFloat(recycledPercent) });
  };

  return (
    <div className="form-container">
      <h2>Enter Production Details</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="tons">Production Volume (in tons)</label>
          <input
            type="number"
            id="tons"
            value={tons}
            onChange={(e) => setTons(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="recycledPercent">Recycled Content ({recycledPercent}%)</label>
          <input
            type="range"
            id="recycledPercent"
            min="0"
            max="100"
            value={recycledPercent}
            onChange={(e) => setRecycledPercent(e.target.value)}
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Calculating...' : 'Calculate Impact'}
        </button>
      </form>
    </div>
  );
}

export default CalculatorForm;