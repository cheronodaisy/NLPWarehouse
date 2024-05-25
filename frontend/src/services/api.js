import axios from 'axios';

const BASE_URL = 'http://localhost:5000'; 

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

export const searchData = async (query) => {
  try {
    const response = await axios.get(`${BASE_URL}/search?query=${query}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const filterData = async (filter) => {
  try {
    const response = await axios.get(`${BASE_URL}/filter?filter=${filter}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};
