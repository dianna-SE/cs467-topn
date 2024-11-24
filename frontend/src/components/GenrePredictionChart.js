import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';
import LoadingSpinner from './LoadingSpinner';

export const GenrePredictionChart = ({ predictions, loading}) => (
  <>

    <div className="mt-5 w-full flex h-[400px] items-center justify-center dark:text-gray-200">
    {loading ? (
      <LoadingSpinner />
    ) : (
      <div className="flex w-full">
          {/* Left Side: List of Genres and Confidence */}
          <div className="w-1/3 p-7 flex flex-col justify-center">
            <ul>
              {predictions.map((pred, index) => (
                <li key={index} className="flex justify-between items-center mb-2.5 text-lg">
                <span className="flex items-center">
                  <span className="text-gray-500 font-semibold pr-4" style={{ width: '30px' }}>{index + 1}.</span>
                    <span className="text-xl font-bold capitalize">{pred[0]}</span>
                  </span>
                <span className="ml-4 pr-12">{(pred[1] * 100).toFixed(1)}%</span>
                </li>
              ))}
            </ul>
          </div>

        {/* Right Side: Vertical Bar Chart */}
        <div className="w-2/3 flex justify-center items-center bg-white dark:bg-gray-900 text-white rounded-lg shadow-md">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={predictions.map(pred => ({ genre: pred[0], confidence: pred[1] }))}
              margin={{ top: 20, bottom: 60, right: 20 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="genre"
                interval={0}
                angle={-45}
                dy={10}
                tick={{ fill: document.documentElement.classList.contains('dark') ? '#D1D5DB' : '#374151' }} // gray-200 for dark, gray-800 for light
              />
              <YAxis tick={{ fill: document.documentElement.classList.contains('dark') ? '#D1D5DB' : '#374151' }} />

              <Tooltip
                formatter={(value) => `${(value * 100).toFixed(1)}%`}
                contentStyle={{
                  backgroundColor: document.documentElement.classList.contains('dark') ? '#1F2937' : '#FFFFFF', // gray-800 for dark, white for light
                  borderColor: document.documentElement.classList.contains('dark') ? '#4B5563' : '#E5E7EB', // gray-600 for dark, gray-200 for light
                }}
                itemStyle={{
                  color: document.documentElement.classList.contains('dark') ? '#D1D5DB' : '#374151' // gray-200 for dark, gray-800 for light
                }}
                labelStyle={{
                  color: document.documentElement.classList.contains('dark') ? '#D1D5DB' : '#374151' // gray-200 for dark, gray-800 for light
                }}
              />              
              <Bar dataKey="confidence" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    )}
  </div>
  </>
);

