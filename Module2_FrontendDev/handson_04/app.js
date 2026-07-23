/**
 * HANDS-ON 04: Async JavaScript, Fetch API & Axios Integration
 * 
 * ===================================================================================
 * COMPARISON: FETCH API vs AXIOS (Task 59)
 * ===================================================================================
 * 1. Automatic JSON Parsing:
 *    - Fetch: Requires manual call to response.json() to parse the JSON response body.
 *    - Axios: Automatically parses JSON data and places it under response.data.
 * 
 * 2. HTTP Error Handling (Non-2xx Statuses like 404 or 500):
 *    - Fetch: Resolves successfully on 404/500 errors. You MUST manually check response.ok.
 *    - Axios: Automatically rejects the Promise for HTTP errors (outside 2xx range), triggering catch().
 * 
 * 3. Built-in Interceptors & Request Configuration:
 *    - Fetch: Does not have built-in request/response interceptors or automatic query param formatting.
 *    - Axios: Provides native interceptors (axios.interceptors) and query param formatting ({ params: {} }).
 * ===================================================================================
 */

// ===================================================================================
// Task 1: Promises and Async/Await Demonstrations
// ===================================================================================

// Task 45: Fetch user using Promise chaining (.then)
function fetchUserPromise(id) {
    console.log(`[Task 45] Fetching user ${id} using Promise .then()...`);
    return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return response.json();
        })
        .then(userData => {
            console.log(`[Task 45 Result] Promise .then() user name: ${userData.name}`);
            return userData;
        })
        .catch(error => console.error('[Task 45 Error]:', error));
}

// Task 46: Rewrite fetchUser using async/await and try/catch
async function fetchUserAsync(id) {
    console.log(`[Task 46] Fetching user ${id} using async/await...`);
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const userData = await response.json();
        console.log(`[Task 46 Result] Async/await user name: ${userData.name}`);
        return userData;
    } catch (error) {
        console.error('[Task 46 Error]:', error);
    }
}

// Task 47: Simulate 1-second network delay using new Promise
function fetchAllCourses() {
    console.log('[Task 47] Simulating 1-second network delay for course data...');
    return new Promise((resolve) => {
        setTimeout(() => {
            const localCourses = [
                { id: 1, title: "CS101 - Algorithms", credits: 4 },
                { id: 2, title: "CS202 - Web Engineering", credits: 4 },
                { id: 3, title: "CS303 - Database Design", credits: 3 }
            ];
            resolve(localCourses);
        }, 1000);
    });
}

// Task 48: Render courses after promise resolves with loading indicator
async function loadCoursesWithDelay() {
    const loader = document.getElementById('courses-loader');
    const grid = document.getElementById('course-grid');

    loader.style.display = 'flex';
    grid.style.display = 'none';

    const courses = await fetchAllCourses();

    loader.style.display = 'none';
    grid.style.display = 'grid';

    grid.innerHTML = courses.map(course => `
        <article class="course-card">
            <h3>${course.title}</h3>
            <p><strong>Credits:</strong> ${course.credits}</p>
        </article>
    `).join('');
}

// Task 49: Promise.all() fetching User 1 and User 2 simultaneously
async function fetchMultipleUsersSimultaneously() {
    console.log('[Task 49] Executing Promise.all() for User 1 and User 2...');
    try {
        const [user1Response, user2Response] = await Promise.all([
            fetch('https://jsonplaceholder.typicode.com/users/1').then(r => r.json()),
            fetch('https://jsonplaceholder.typicode.com/users/2').then(r => r.json())
        ]);
        console.log(`[Task 49 Result] Promise.all Completed: User 1 = "${user1Response.name}", User 2 = "${user2Response.name}"`);
    } catch (error) {
        console.error('[Task 49 Error]:', error);
    }
}

// ===================================================================================
// Task 2 & 3: Axios Integration, Interceptors & Error Handling
// ===================================================================================

// Task 58: Axios Request Interceptor
axios.interceptors.request.use(
    config => {
        console.log(`[Axios Interceptor] API call started: ${config.url}`, config);
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

// Task 50 & 56: Fetch notifications using Axios (replaces manual response.ok check)
async function fetchNotificationsFromAPI(targetUrl) {
    const apiLoader = document.getElementById('api-loader');
    const errorContainer = document.getElementById('error-container');
    const errorMessage = document.getElementById('error-message');
    const notificationsGrid = document.getElementById('notifications-grid');

    // UI Loading State
    apiLoader.style.display = 'flex';
    errorContainer.style.display = 'none';
    notificationsGrid.innerHTML = '';

    try {
        // Task 57: Use axios.get with params object (userId: 1)
        const response = await axios.get(targetUrl, {
            params: { _limit: 6 }
        });

        // Axios automatically parses JSON into response.data
        const posts = response.data;

        apiLoader.style.display = 'none';

        if (posts.length === 0) {
            notificationsGrid.innerHTML = '<p>No notifications available.</p>';
            return;
        }

        notificationsGrid.innerHTML = posts.map(post => `
            <article class="notification-card">
                <h3 class="notification-title">${post.title}</h3>
                <p class="notification-body">${post.body}</p>
            </article>
        `).join('');

    } catch (error) {
        // Task 53: Friendly UI Error Handling
        apiLoader.style.display = 'none';
        errorContainer.style.display = 'flex';
        
        if (error.response) {
            errorMessage.textContent = `Server Error (${error.response.status}): Failed to load notifications from "${targetUrl}".`;
        } else if (error.request) {
            errorMessage.textContent = `Network Error: Unable to reach the server. Please check your internet connection.`;
        } else {
            errorMessage.textContent = `Error: ${error.message}`;
        }
        console.error('[API Fetch Error]:', error);
    }
}

// Event Listeners for Interactivity
document.addEventListener('DOMContentLoaded', () => {
    // Run Tasks 45, 46, 49 in background logs
    fetchUserPromise(1);
    fetchUserAsync(2);
    fetchMultipleUsersSimultaneously();

    // Render Delayed Courses (Tasks 47, 48)
    loadCoursesWithDelay();

    // Initial API Fetch for Notifications (Tasks 51, 57)
    const validUrl = 'https://jsonplaceholder.typicode.com/posts';
    const invalidUrl = 'https://jsonplaceholder.typicode.com/nonexistent_endpoint';

    fetchNotificationsFromAPI(validUrl);

    // Fetch Valid Posts Button
    document.getElementById('fetch-valid-btn').addEventListener('click', () => {
        fetchNotificationsFromAPI(validUrl);
    });

    // Simulate 404 Error Button (Task 53)
    document.getElementById('fetch-error-btn').addEventListener('click', () => {
        fetchNotificationsFromAPI(invalidUrl);
    });

    // Retry Button (Task 54)
    document.getElementById('retry-btn').addEventListener('click', () => {
        fetchNotificationsFromAPI(validUrl);
    });
});
