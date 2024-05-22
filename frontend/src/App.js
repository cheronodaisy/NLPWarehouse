// src/App.js

import './App.css';

import Footer from './components/Footer';
import Header from './components/Header';
import Main from './components/Main';
import React from 'react';

function App() {
  return (
    <div className="App">
      <Header />
      <Main />
      <Footer />
    </div>
  );
}

export default App;
