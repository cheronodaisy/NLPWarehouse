import React, { useEffect, useState } from 'react';

import DataList from '../components/DataTable';
import FilterPanel from '../components/FilterPanel';
import SearchBar from '../components/SearchBar';
import { fetchData } from '../services/api'; // Import the fetchData function from the API service

const Homepage = () => {
  const [data, setData] = useState([]); // State to store fetched data
  const [filteredData, setFilteredData] = useState([]); // State to store filtered data

  useEffect(() => {
    // Fetch data from API when component mounts
    fetchData()
      .then(response => {
        setData(response.data);
        setFilteredData(response.data); // Initially, set filtered data to all data
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  const handleSearch = (searchTerm) => {
    // Filter data based on search term
    const filtered = data.filter(item =>
      item.title.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredData(filtered);
  };

  const handleFilter = (filterOption) => {
    // Filter data based on selected filter option
    // Implement filter logic based on your specific requirements
    // Example: const filtered = data.filter(item => item.category === filterOption);
    // Replace 'category' with the actual property you want to filter by
    // Update the filter logic as needed
    // setFilteredData(filtered);
  };

  return (
    <div>
      <h1>Homepage</h1>
      <SearchBar onSearch={handleSearch} />
      <FilterPanel onFilterChange={handleFilter} /> {/* Changed prop name from 'onFilter' to 'onFilterChange' */}
      <DataList data={filteredData} />
    </div>
  );
};

export default Homepage;
