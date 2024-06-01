import './style.css';

import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';

import Homepage from './pages/HomePage';
import React from 'react';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Homepage />} />
      </Routes>
    </Router>
  );
};

export default App;
