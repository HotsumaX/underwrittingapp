// src/components/ServerStatus.js
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setBackendStatus, setError, logMessage } from '../store';

const ServerStatus = () => {
    const dispatch = useDispatch();
    const backendStatus = useSelector((state) => state.backendStatus);

    const handleResetConnection = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/reset_connection', { method: 'POST' });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            dispatch(logMessage(data.status));
        } catch (error) {
            dispatch(setError('Error resetting connection: ' + error.message));
            dispatch(logMessage('Error resetting connection: ' + error.message));
        }
    };

    return (
        <div>
            <h2>Server Connection Status: {backendStatus}</h2>
            <button onClick={handleResetConnection}>Reset Connection</button>
        </div>
    );
};

export default ServerStatus;
