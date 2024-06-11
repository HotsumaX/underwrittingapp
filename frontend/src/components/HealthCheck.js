// src/components/HealthCheck.js
import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { setBackendStatus, setError, logMessage } from '../store';

const HealthCheck = () => {
    const dispatch = useDispatch();

    useEffect(() => {
        const checkBackendHealth = async () => {
            try {
                const response = await fetch('http://localhost:5000/api/health');
                console.log('Health check response:', response); // Log the raw response
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                console.log('Health check data:', data); // Log the parsed data
                dispatch(setBackendStatus(data.status));
                dispatch(logMessage('Backend health check passed'));
            } catch (error) {
                console.error('Health check error:', error); // Log the error
                dispatch(setBackendStatus('error'));
                dispatch(setError('Error connecting to backend: ' + error.message));
                dispatch(logMessage('Backend health check failed: ' + error.message));
            }
        };

        checkBackendHealth();
        const interval = setInterval(checkBackendHealth, 5000);
        return () => clearInterval(interval);
    }, [dispatch]);

    return null;
};

export default HealthCheck;
