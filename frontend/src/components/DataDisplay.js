import React from 'react';

const DataDisplay = ({ data }) => {
  return (
    <div>
      <h3>Scraped Data:</h3>
      {Object.keys(data).length === 0 ? (
        <p>No data available</p>
      ) : (
        <ul>
          {Object.keys(data).map((key, index) => (
            <li key={index}>
              <strong>{key}:</strong> {data[key]}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default DataDisplay;
