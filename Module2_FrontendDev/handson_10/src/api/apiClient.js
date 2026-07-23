import axios from 'axios';

/**
 * Centralized Axios API Client Instance (Tasks 138, 140, 141)
 */
const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

// Task 141: Request Interceptor attaching mock Authorization header
apiClient.interceptors.request.use(
  (config) => {
    const mockAuthToken = 'Bearer mock-jwt-token-xyz-12345';
    config.headers['Authorization'] = mockAuthToken;
    console.log(`[Central API Request] ${config.method.toUpperCase()} -> ${config.url}`, config);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Task 140: Response Interceptor unwrapping response.data & standardizing errors
apiClient.interceptors.response.use(
  (response) => {
    // Unwraps response.data directly so callers don't need response.data wrapper
    return response.data;
  },
  (error) => {
    // Catches and formats standardized error object
    const customError = {
      message: error.response?.data?.message || error.message || 'An unexpected API error occurred',
      statusCode: error.response?.status || 500,
      url: error.config?.url
    };
    console.error('[Central API Response Error]:', customError);
    return Promise.reject(customError);
  }
);

export default apiClient;
