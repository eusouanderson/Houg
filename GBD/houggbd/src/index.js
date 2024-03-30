import React from 'react';
import ReactDOM from 'react-dom'; // Importe ReactDOM corretamente
import './index.css';
import reportWebVitals from './reportWebVitals';
import GerenciamentoCamisetas from './components/GerenciamentoCamisetas';

ReactDOM.render(
  <React.StrictMode>
    <GerenciamentoCamisetas />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
