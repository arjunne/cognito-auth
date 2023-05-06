import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Replace with your FastAPI backend URL

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
});

export default api;
