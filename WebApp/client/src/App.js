import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState(0);

  useEffect(() => {
    fetch('/')
    .then(res => res.json())
    .then(data => {
      setData(data);
      console.log(data)
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p>The current time is {data}.</p>
      </header>
    </div>
  );
}

export default App;

// fetch(url).then((response) => {
//   // La req
// }).catch((error) => {
//   console.log(error)
// });