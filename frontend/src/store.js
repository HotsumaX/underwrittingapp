// src/store.js
import { createSlice, configureStore } from '@reduxjs/toolkit';

const initialState = {
    backendStatus: 'unknown',
    error: null,
    logs: [],
};

const slice = createSlice({
    name: 'app',
    initialState,
    reducers: {
        setBackendStatus: (state, action) => {
            state.backendStatus = action.payload;
        },
        setError: (state, action) => {
            state.error = action.payload;
        },
        logMessage: (state, action) => {
            state.logs.push(action.payload);
        },
    },
});

export const { setBackendStatus, setError, logMessage } = slice.actions;

const store = configureStore({
    reducer: slice.reducer,
});

export default store;
