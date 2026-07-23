/**
 * HANDS-ON 03: JavaScript ES6+ & DOM Manipulation Application Logic
 */

// Import dataset from data.js module
import { coursesData } from './data.js';

// Local mutable copy of courses for filtering and sorting
let currentCourses = [...coursesData];

// =================================================================
// Task 1: ES6+ Syntax & Array Methods Practice
// =================================================================

// 1. Destructuring demonstration in array iteration
console.log("--- Task 1: ES6+ Destructuring Demo ---");
coursesData.forEach(course => {
    const { code, name, credits } = course;
    console.log(`[Extracted]: ${code} - ${name} (${credits} Credits)`);
});

// 2. Array.map(): Create formatted string array
const formattedCourses = coursesData.map(course => 
    `${course.code} — ${course.name} (${course.credits} credits)`
);
console.log("--- Formatted Courses (Array.map) ---", formattedCourses);

// 3. Array.filter(): Filter courses with credits >= 4
const highCreditCourses = coursesData.filter(course => course.credits >= 4);
console.log(`--- High Credit Courses Count (>= 4 Credits): ${highCreditCourses.length} ---`, highCreditCourses);

// 4. Array.reduce(): Calculate total sum of credits
const calculateTotalCredits = (coursesList) => {
    return coursesList.reduce((acc, course) => acc + course.credits, 0);
};
console.log("--- Total Credits (Array.reduce) ---", calculateTotalCredits(coursesData));

// =================================================================
// Task 2: Dynamic DOM Selection & Rendering
// =================================================================

const courseGridElement = document.querySelector('.course-grid');
const totalCreditsElement = document.querySelector('#total-credits');
const searchInputElement = document.querySelector('#search-courses');
const sortButtonElement = document.querySelector('#sort-btn');
const resetButtonElement = document.querySelector('#reset-btn');
const selectedCourseBanner = document.querySelector('#selected-course');
const selectedCourseText = document.querySelector('#selected-course-text');

/**
 * Arrow function to dynamically render course cards into the DOM
 * @param {Array} coursesList - Array of course objects to render
 */
const renderCourses = (coursesList) => {
    // Clear existing container content to prevent duplication
    courseGridElement.innerHTML = '';

    if (coursesList.length === 0) {
        courseGridElement.innerHTML = `
            <p style="grid-column: 1/-1; text-align: center; color: #64748b; padding: 2rem;">
                No matching courses found. Try a different search term.
            </p>
        `;
        totalCreditsElement.textContent = 'Total Credits Enrolled: 0';
        return;
    }

    // Use DocumentFragment for performance batch DOM update
    const fragment = document.createDocumentFragment();

    coursesList.forEach(course => {
        const { id, code, name, credits, grade, description } = course;

        // Create article element
        const article = document.createElement('article');
        article.className = 'course-card';
        article.setAttribute('data-id', id);

        // Build inner content using Template Literal
        article.innerHTML = `
            <div class="card-header">
                <span class="course-code">${code}</span>
                <span class="course-credits">${credits} Credits</span>
            </div>
            <h3 class="course-name">${name}</h3>
            <p class="course-desc">${description}</p>
            <div class="card-footer">
                <span class="grade-tag">Grade: ${grade}</span>
                <span class="click-hint">Click to inspect</span>
            </div>
        `;

        fragment.appendChild(article);
    });

    // Batch append to grid container
    courseGridElement.appendChild(fragment);

    // Update total credits display dynamically
    const totalCredits = calculateTotalCredits(coursesList);
    totalCreditsElement.textContent = `Total Credits Enrolled: ${totalCredits}`;
};

// =================================================================
// Task 3: Event Listeners & Event Delegation Interactivity
// =================================================================

// Real-time search filter on input keystrokes
searchInputElement.addEventListener('input', (event) => {
    const searchTerm = event.target.value.toLowerCase().trim();
    currentCourses = coursesData.filter(course => 
        course.name.toLowerCase().includes(searchTerm) || 
        course.code.toLowerCase().includes(searchTerm)
    );
    renderCourses(currentCourses);
});

// Sort by Credits Descending
sortButtonElement.addEventListener('click', () => {
    currentCourses.sort((a, b) => b.credits - a.credits);
    renderCourses(currentCourses);
});

// Reset Filters
resetButtonElement.addEventListener('click', () => {
    searchInputElement.value = '';
    currentCourses = [...coursesData];
    renderCourses(currentCourses);
    selectedCourseBanner.style.display = 'none';
});

// Event Delegation: Attach single listener to course-grid container
courseGridElement.addEventListener('click', (event) => {
    // Detect closest course-card relative to click target
    const cardElement = event.target.closest('.course-card');
    
    if (!cardElement) return; // Clicked outside a card

    const courseId = parseInt(cardElement.getAttribute('data-id'), 10);
    const selectedCourse = coursesData.find(c => c.id === courseId);

    if (selectedCourse) {
        selectedCourseBanner.style.display = 'block';
        selectedCourseText.innerHTML = `
            <strong>Selected Course:</strong> ${selectedCourse.code} — ${selectedCourse.name} 
            | <strong>Credits:</strong> ${selectedCourse.credits} 
            | <strong>Current Grade:</strong> ${selectedCourse.grade}
        `;
    }
});

// Initial DOM Render on Page Load
document.addEventListener('DOMContentLoaded', () => {
    renderCourses(currentCourses);
});
