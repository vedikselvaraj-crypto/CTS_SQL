/**
 * HANDS-ON 09: Accessibility & Keyboard Navigation Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // Task 137: Initialize css-vars-ponyfill for older browser support
    if (window.cssVars) {
        window.cssVars({
            watch: true
        });
        console.log('[a11y Polyfill] css-vars-ponyfill initialized successfully.');
    }

    // Task 131: Toggle mobile menu aria-expanded state
    const menuToggleBtn = document.getElementById('menu-toggle');
    const primaryNav = document.getElementById('primary-nav');

    if (menuToggleBtn && primaryNav) {
        menuToggleBtn.addEventListener('click', () => {
            const isExpanded = menuToggleBtn.getAttribute('aria-expanded') === 'true';
            menuToggleBtn.setAttribute('aria-expanded', !isExpanded);
            primaryNav.classList.toggle('nav-open');
        });
    }

    // Task 129: Make course cards keyboard operable via Enter / Space key press
    const courseCards = document.querySelectorAll('.course-card');
    const statusAnnouncer = document.getElementById('search-count');

    courseCards.forEach(card => {
        // Click Handler
        card.addEventListener('click', () => {
            handleCardInteraction(card);
        });

        // Keydown Handler for Enter / Space (Task 129)
        card.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault(); // Prevent page scroll on Space
                handleCardInteraction(card);
            }
        });
    });

    function handleCardInteraction(card) {
        const title = card.querySelector('.course-title')?.textContent || 'Course';
        alert(`Navigating to accessible course view: ${title}`);
    }

    // Task 130: Live Screen Reader Announcer on Search Filter
    const searchInput = document.getElementById('search-courses');

    if (searchInput && statusAnnouncer) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            let count = 0;

            courseCards.forEach(card => {
                const text = card.textContent.toLowerCase();
                if (text.includes(query)) {
                    card.style.display = 'block';
                    count++;
                } else {
                    card.style.display = 'none';
                }
            });

            // Update text inside role="status" aria-live="polite" element (Task 130)
            statusAnnouncer.textContent = `${count} ${count === 1 ? 'course' : 'courses'} found.`;
        });
    }
});
