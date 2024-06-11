import React, { useState } from 'react';
import axios from 'axios';

const CrexiScraper = () => {
    const [url, setUrl] = useState('');
    const [result, setResult] = useState(null);

    const fetchCrexiData = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/api/scrape_crexi?url=${url}`);
            setResult(response.data);
        } catch (error) {
            setResult({ error: error.message });
        }
    };

    return (
        <div>
            <h2>Scrape CREXi</h2>
            <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} placeholder="Enter CREXi URL" />
            <button onClick={fetchCrexiData}>Fetch CREXi Data</button>
            {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
        </div>
    );
};

export default CrexiScraper;
