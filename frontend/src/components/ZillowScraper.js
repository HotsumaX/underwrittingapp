import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { logMessage } from '../store';

const ZillowScraper = ({ setScrapedData }) => {
    const dispatch = useDispatch();
    const [url, setUrl] = useState('');
    const [scrapedDataLocal, setScrapedDataLocal] = useState(null);
    const [loading, setLoading] = useState(false);
    const [copyMessage, setCopyMessage] = useState('');

    const handleScrape = async () => {
        setLoading(true);
        try {
            const response = await fetch(`http://localhost:5000/api/sample_zillow?url=${encodeURIComponent(url)}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            setScrapedData(data);
            setScrapedDataLocal(data);
            dispatch(logMessage('Scraped Zillow data successfully'));
        } catch (error) {
            console.error('Scrape error:', error);
            dispatch(logMessage('Error scraping Zillow data: ' + error.message));
        } finally {
            setLoading(false);
        }
    };

    const handleTestScrape = async () => {
        const testUrl = 'https://www.zillow.com/homedetails/404-Cardinal-Dr-Clayton-NC-27520/69130415_zpid/';
        setLoading(true);
        try {
            const response = await fetch(`http://localhost:5000/api/sample_zillow?url=${encodeURIComponent(testUrl)}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            setScrapedData(data);
            setScrapedDataLocal(data);
            dispatch(logMessage('Test scraped Zillow data successfully'));
        } catch (error) {
            console.error('Test scrape error:', error);
            dispatch(logMessage('Error scraping Zillow data: ' + error.message));
        } finally {
            setLoading(false);
        }
    };

    const syntaxHighlight = (json) => {
        if (typeof json !== 'string') {
            json = JSON.stringify(json, undefined, 2);
        }
        json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|\b\d+\b)/g, (match) => {
            let cls = 'number';
            if (/^"/.test(match)) {
                cls = /:$/.test(match) ? 'key' : 'string';
            } else if (/true|false/.test(match)) {
                cls = 'boolean';
            } else if (/null/.test(match)) {
                cls = 'null';
            }
            return `<span class="${cls}">${match}</span>`;
        });
    };

    const handleCopy = () => {
        const textToCopy = JSON.stringify(scrapedDataLocal, null, 2);
        navigator.clipboard.writeText(textToCopy).then(() => {
            setCopyMessage('Data copied to clipboard!');
            setTimeout(() => setCopyMessage(''), 3000);
        }, (err) => {
            console.error('Could not copy text: ', err);
        });
    };

    const renderTroubleshooting = () => {
        if (scrapedDataLocal?.html_content.includes('px-captcha')) {
            return 'It looks like a CAPTCHA page was returned. Possible issues: blocked by Zillow, need to use a different IP or add a CAPTCHA solver.';
        }
        return 'No obvious issues detected in the HTML content.';
    };

    return (
        <div>
            <h2>Scrape Zillow</h2>
            <input
                type="text"
                placeholder="Enter Zillow URL"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                style={styles.input}
            />
            <button onClick={handleScrape} disabled={loading} style={styles.button}>Fetch Zillow Data</button>
            <button onClick={handleTestScrape} disabled={loading} style={styles.button}>Test Zillow</button>
            {loading && <p style={styles.loading}>Loading...</p>}
            {scrapedDataLocal && (
                <div style={styles.scrapedDataContainer}>
                    <div style={styles.header}>
                        <h3>Processed Data</h3>
                        <button onClick={handleCopy} style={styles.copyButton}>Copy Data</button>
                    </div>
                    {copyMessage && <p style={styles.copyMessage}>{copyMessage}</p>}
                    <p style={styles.troubleshooting}>{renderTroubleshooting()}</p>
                    <pre style={styles.scrapedData} dangerouslySetInnerHTML={{ __html: syntaxHighlight(scrapedDataLocal.html_content) }}></pre>
                </div>
            )}
            <style jsx>{`
                .string { color: green; }
                .number { color: darkorange; }
                .boolean { color: blue; }
                .null { color: magenta; }
                .key { color: red; }
            `}</style>
        </div>
    );
};

const styles = {
    input: {
        padding: '10px',
        margin: '10px 0',
        width: '100%',
        maxWidth: '400px',
        boxSizing: 'border-box',
    },
    button: {
        padding: '10px 20px',
        margin: '10px 5px',
        cursor: 'pointer',
        backgroundColor: '#007BFF',
        color: '#FFF',
        border: 'none',
        borderRadius: '5px',
    },
    loading: {
        fontStyle: 'italic',
    },
    scrapedDataContainer: {
        marginTop: '20px',
        maxWidth: '600px',
        overflowX: 'auto',
        wordWrap: 'break-word',
        backgroundColor: '#F9F9F9',
        padding: '10px',
        borderRadius: '5px',
    },
    scrapedData: {
        whiteSpace: 'pre-wrap',
        fontFamily: 'monospace',
        fontSize: '14px',
        lineHeight: '1.5',
    },
    copyButton: {
        padding: '10px 20px',
        marginLeft: '10px',
        cursor: 'pointer',
        backgroundColor: '#28A745',
        color: '#FFF',
        border: 'none',
        borderRadius: '5px',
    },
    troubleshooting: {
        fontStyle: 'italic',
        color: 'red',
    },
    header: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
    },
    copyMessage: {
        color: 'green',
        fontStyle: 'italic',
    }
};

export default ZillowScraper;