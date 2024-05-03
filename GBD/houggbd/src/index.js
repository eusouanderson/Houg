import React from 'react';
import { createRoot } from 'react-dom'; 
import './index.css';
import reportWebVitals from './reportWebVitals';
import GerenciamentoCamisetas from './components/GerenciamentoCamisetas';

const root = document.getElementById('root');
const rootElement = createRoot(root); 

rootElement.render(
  <React.StrictMode>
    <GerenciamentoCamisetas />
  </React.StrictMode>
);

reportWebVitals();
