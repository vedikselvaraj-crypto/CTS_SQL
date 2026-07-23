import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './store/store';
import { EnrollmentProvider } from './context/EnrollmentContext';
import App from './App';
import './styles/index.css';

/**
 * Entrypoint wrapping App with BrowserRouter, Redux Provider, and Context Provider (Tasks 76, 82, 88)
 */
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <EnrollmentProvider>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </EnrollmentProvider>
    </Provider>
  </React.StrictMode>
);
