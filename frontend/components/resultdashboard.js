// src/components/ResultsDashboard.js
import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

// This registers the necessary components for Chart.js
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function ResultsDashboard({ results }) {
  // Prepare the data for the bar chart
  const chartData = {
    labels: ['Carbon Emissions (kg CO₂e)', 'Energy Consumption (kWh)', 'Water Usage (m³)'],
    datasets: [
      {
        label: 'Linear Path (0% Recycling)',
        data: [
          results.linearScenario.carbonEmissions,
          results.linearScenario.energyConsumption,
          results.linearScenario.waterUsage,
        ],
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
      {
        label: 'Your Circular Path',
        data: [
          results.circularScenario.carbonEmissions,
          results.circularScenario.energyConsumption,
          results.circularScenario.waterUsage,
        ],
        backgroundColor: 'rgba(75, 192, 192, 0.5)',
      },
    ],
  };

  // Configure the chart's options
  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Environmental Impact Comparison',
      },
    },
  };

  return (
    <div className="results-container">
      <h2>Impact Analysis</h2>
      
      {/* Display the "Savings" metrics */}
      <div className="savings-metrics">
        <div className="metric">
          <h3>Carbon Saved</h3>
          <p>{results.savings.carbonSaved.toLocaleString()} kg CO₂e</p>
        </div>
        <div className="metric">
          <h3>Energy Saved</h3>
          <p>{results.savings.energySaved.toLocaleString()} kWh</p>
        </div>
        <div className="metric">
          <h3>Water Saved</h3>
          <p>{results.savings.waterSaved.toLocaleString()} m³</p>
        </div>
      </div>
      
      {/* Display the Bar Chart */}
      <div className="chart-container">
        <Bar options={chartOptions} data={chartData} />
      </div>
    </div>
  );
}

export default ResultsDashboard;