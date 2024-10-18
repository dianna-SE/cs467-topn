import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export const GenrePredictionChart = ({ predictions }) => (
  <div className="mt-4">
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={predictions}>
        <XAxis dataKey="genre" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="confidence" fill="#8884d8" />
      </BarChart>
    </ResponsiveContainer>
    <ul className="mt-4">
      {predictions.map((pred, index) => (
        <li key={index} className="flex justify-between items-center mb-2">
          <span>{pred.genre}</span>
          <span className="font-semibold">{(pred.confidence * 100).toFixed(1)}%</span>
        </li>
      ))}
    </ul>
  </div>
);
