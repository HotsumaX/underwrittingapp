import React, { useState } from 'react';
import axios from 'axios';
import DataDisplay from './components/DataDisplay';

function App() {
  const [zillowData, setZillowData] = useState([]);
  const [crexiData, setCrexiData] = useState([]);
  const [codeReview, setCodeReview] = useState('');
  const [code, setCode] = useState('');

  const fetchZillowData = async () => {
    const response = await axios.get('/api/scrape_zillow');
    setZillowData(response.data);
  };

  const fetchCrexiData = async () => {
    const response = await axios.get('/api/scrape_crexi');
    setCrexiData(response.data);
  };

  const reviewCode = async () => {
    const response = await axios.post('/api/review_code', { code });
    setCodeReview(response.data);
  };

  return (
    <div>
      <h1>Real Estate Scraper</h1>
      <button onClick={fetchZillowData}>Scrape Zillow</button>
      <button onClick={fetchCrexiData}>Scrape CREXi</button>
      <div>
        <h2>Zillow Data</h2>
        <DataDisplay data={zillowData} />
      </div>
      <div>
        <h2>CREXi Data</h2>
        <DataDisplay data={crexiData} />
      </div>
      <div>
        <h2>Code Review</h2>
        <textarea value={code} onChange={(e) => setCode(e.target.value)} />
        <button onClick={reviewCode}>Review Code</button>
        <pre>{codeReview}</pre>
      </div>
    </div>
  );
}

export default App;
