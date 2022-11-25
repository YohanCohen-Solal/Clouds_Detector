//import logo from './logo.svg';
import './App.css';
import React from 'react';
import Dropzone from './Dropzone';

const pythonExec=()=>{
  const python_code=`
  print("hello world")
  `;
  
}
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 id="typo_ombre">Cloud Detector</h1>
        <p id="typo_ombre">Principle : Insert an image of cloud and we will tell you which type it is</p>
        <Dropzone />
        <h3>The type of cloud is : </h3>
        <h1>Run python from react</h1>
        <button onClick={pythonExec} >Click me to console</button>
      </header>
    </div>
  );
}

export default App;
