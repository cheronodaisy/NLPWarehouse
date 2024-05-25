import axios from 'axios';

const BASE_URL = 'http://localhost:5000'; // Update with your Flask server URL

export const fetchAllTexts = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/texts`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const fetchTextById = async (id) => {
  try {
    const response = await axios.get(`${BASE_URL}/texts/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const fetchData = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/data`);
    return response.data;
  } catch (error) {
    throw error;
  }
};
