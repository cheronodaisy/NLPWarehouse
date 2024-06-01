import './FilterPanel.css';

import React from 'react';

const FilterPanel = ({ filters, onFilterChange }) => {
    return (
        <div>
            <h3>Filters</h3>
            <label>
                Source:
                <select onChange={(e) => onFilterChange('source', e.target.value)}>
                    <option value="">All</option>
                    <option value="news">News</option>
                    <option value="blog">Blog</option>
                    <option value="social">Social Media</option>
                </select>
            </label>
            <label>
                Date:
                <input
                    type="date"
                    onChange={(e) => onFilterChange('date', e.target.value)}
                />
            </label>
        </div>
    );
};

export default FilterPanel;
