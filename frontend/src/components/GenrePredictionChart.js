import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export const GenrePredictionChart = ({ predictions, file}) => (
  <>
  {/* Display using file name props */}
    <div className="top-10 right-4 p-5 mb-6 bg-gray-100 shadow-md">
      <h1><strong>File name:</strong></h1>
      <p>{file.name.slice(0,-4)}</p> {/* Remove '.wav' from file name */}
    </div>

    <div className="mt-4 w-full flex h-[400px]">
      {/* Left Side: List of Genres and Confidence */}
      <div className="w-1/3 p-4 flex flex-col justify-center">
        <ul>
          {predictions.map((pred, index) => (
            <li key={index} className="flex justify-between items-center mb-4 text-lg font-bold">
              <span className="text-xl">{pred[0]}:</span>
              <span className="ml-4 pr-7">{(pred[1] * 100).toFixed(1)}%</span>
            </li>
          ))}
        </ul>
      </div>

      {/* Right Side: Vertical Bar Chart */}
      <div className="w-2/3 p-4 flex justify-center items-center">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={predictions.map(pred => ({ genre: pred[0], confidence: pred[1] }))}
            margin={{ bottom: 40 }} // Increase bottom margin to make space for angled labels
          >
            <XAxis dataKey="genre" interval={0} angle={-45} dy={10} /> {/* Angle and adjust position */}
            <YAxis />
            <Tooltip />
            <Bar dataKey="confidence" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  </>
);
