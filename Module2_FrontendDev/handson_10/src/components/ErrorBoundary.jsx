import React, { Component } from 'react';

/**
 * Global React Error Boundary Component (Task 150)
 * Catches JavaScript errors anywhere in child component tree and displays fallback UI.
 */
class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('[Global ErrorBoundary Caught Error]:', error, errorInfo);
    this.setState({ errorInfo });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '3rem', textAlign: 'center', backgroundColor: '#fef2f2', minHeight: '100vh' }}>
          <h1 style={{ color: '#991b1b', marginBottom: '1rem' }}>Something went wrong!</h1>
          <p style={{ color: '#7f1d1d', marginBottom: '1.5rem' }}>
            {this.state.error?.toString() || 'An unexpected application error occurred.'}
          </p>
          <button 
            className="btn-primary" 
            onClick={() => window.location.reload()}
          >
            Reload Application
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
