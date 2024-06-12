import React, { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import HealthCheck from './components/HealthCheck';
import ZillowScraper from './components/ZillowScraper';
import CrexiScraper from './components/CrexiScraper';
import Logs from './components/Logs';
import ServerStatus from './components/ServerStatus';
import { setBackendStatus, setError, logMessage } from './store';

const App = () => {
    const dispatch = useDispatch();
    const [scrapedData, setScrapedData] = useState({ html_content: 'No data fetched yet.' });
    const [consoleLog, setConsoleLog] = useState('');

    useEffect(() => {
        const checkBackendHealth = async () => {
            try {
                const response = await fetch('http://localhost:5000/api/health');
                const data = await response.json();
                console.log('Health check response:', response);
                console.log('Health check data:', data);
                setConsoleLog((prevLog) => `${prevLog}\nHealth check response: ${JSON.stringify(response)}\nHealth check data: ${JSON.stringify(data)}`);
                dispatch(setBackendStatus(data.status));
                dispatch(logMessage('Backend health check passed'));
            } catch (error) {
                console.error('Health check error:', error);
                setConsoleLog((prevLog) => `${prevLog}\nHealth check error: ${error.message}`);
                dispatch(setBackendStatus('error'));
                dispatch(setError(`Error connecting to backend: ${error.message}`));
                dispatch(logMessage(`Backend health check failed: ${error.message}`));
            }
        };

        checkBackendHealth();
        const interval = setInterval(checkBackendHealth, 5000);
        return () => clearInterval(interval);
    }, [dispatch]);

    const handleCopyData = () => {
        navigator.clipboard.writeText(scrapedData.html_content)
            .then(() => {
                const copyDataButton = document.getElementById('copy-data-button');
                const originalText = copyDataButton.innerText;
                copyDataButton.innerText = 'Data Copied!';
                setTimeout(() => {
                    copyDataButton.innerText = originalText;
                }, 2000);
            })
            .catch((err) => console.error('Failed to copy text: ', err));
    };

    const handleCopyLog = () => {
        navigator.clipboard.writeText(consoleLog)
            .then(() => {
                const copyLogButton = document.getElementById('copy-log-button');
                const originalText = copyLogButton.innerText;
                copyLogButton.innerText = 'Log Copied!';
                setTimeout(() => {
                    copyLogButton.innerText = originalText;
                }, 2000);
            })
            .catch((err) => console.error('Failed to copy text: ', err));
    };

    return (
        <div>
            <h1>Real Estate Scraper</h1>
            <ServerStatus />
            <ZillowScraper setScrapedData={setScrapedData} />
            <CrexiScraper />
            <div>
                <h2>Processed Data</h2>
                <button id="copy-data-button" onClick={handleCopyData}>Copy Data</button>
                <button id="copy-log-button" onClick={handleCopyLog}>Copy Console Log</button>
                <pre id="scraped-data">{scrapedData.html_content}</pre>
            </div>
            <Logs />
            <HealthCheck />
        </div>
    );
};

export default App;