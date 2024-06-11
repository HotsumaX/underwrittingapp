import React from 'react';
import { useSelector } from 'react-redux';

const Logs = () => {
    const logs = useSelector((state) => state.logs);

    return (
        <div>
            <h2>Logs</h2>
            <ul>
                {logs.map((log, index) => (
                    <li key={index}>{log}</li>
                ))}
            </ul>
        </div>
    );
};

export default Logs;
