//import logo from './logo.svg';
import './App.css';
import React from 'react';
import Dropzone from './Dropzone';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Cloud Detector</h1>
        <p id="try">Principle : Insert an image of cloud and we will tell you which type it is</p>
        <Dropzone />
        <h3>The type of cloud is : </h3>
      </header>
    </div>
  );
}

export default App;
