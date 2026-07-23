# Module 2: Frontend Development - Student Portal (Hands-On 01 - 10)

This repository contains the complete, production-quality implementation of the **Student Portal** web application for the **Digital Nurture 5.0 - Python Full Stack Engineer Track (Module 2: Frontend Development)**.

All 10 hands-on exercises are implemented as independent, self-contained applications spanning standalone HTML5/CSS3/JavaScript, React (Vite), Angular, and Vue.js 3 frameworks, along with web accessibility auditing and advanced state management patterns.

---

## 📁 Repository Folder Structure

```
Module2_FrontendDev/
├── README.md
├── handson_01/                 # HTML5 Semantic Structure & CSS3 Foundations
│   ├── index.html
│   └── styles.css
├── handson_02/                 # CSS Flexbox, Grid & Responsive Design
│   ├── index.html
│   └── styles.css
├── handson_03/                 # JavaScript ES6+ & DOM Manipulation
│   ├── index.html
│   ├── styles.css
│   ├── data.js
│   └── app.js
├── handson_04/                 # Async JavaScript, Fetch API & Axios Integration
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── handson_05/                 # React Fundamentals (Vite + React)
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── data/courses.js
│       ├── components/
│       │   ├── Header.jsx
│       │   ├── Footer.jsx
│       │   ├── CourseCard.jsx
│       │   └── StudentProfile.jsx
│       └── styles/index.css
├── handson_06/                 # React Routing & State Management (React Router + Redux Toolkit)
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── context/EnrollmentContext.jsx
│       ├── store/
│       │   ├── store.js
│       │   └── enrollmentSlice.js
│       ├── components/
│       │   ├── Header.jsx
│       │   └── CourseCard.jsx
│       ├── pages/
│       │   ├── HomePage.jsx
│       │   ├── CoursesPage.jsx
│       │   ├── CourseDetailPage.jsx
│       │   └── ProfilePage.jsx
│       └── styles/index.css
├── handson_07/                 # Angular Application (Components, Services, DI, Routing & Reactive Forms)
│   ├── package.json
│   ├── angular.json
│   ├── tsconfig.json
│   ├── tsconfig.app.json
│   └── src/
│       ├── index.html
│       ├── main.ts
│       ├── styles.css
│       └── app/
│           ├── app.module.ts
│           ├── app.component.ts
│           ├── app.component.html
│           ├── app-routing.module.ts
│           ├── services/course.service.ts
│           └── components/
│               ├── header/
│               ├── course-list/
│               ├── course-card/
│               └── student-profile/
├── handson_08/                 # Vue 3 Application (Composition API, Vue Router & Pinia)
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── main.js
│       ├── App.vue
│       ├── router/index.js
│       ├── stores/enrollment.js
│       ├── components/
│       │   ├── Header.vue
│       │   └── CourseCard.vue
│       ├── views/
│       │   ├── HomeView.vue
│       │   ├── CoursesView.vue
│       │   ├── CourseDetailView.vue
│       │   └── ProfileView.vue
│       └── style.css
├── handson_09/                 # Web Accessibility (a11y) & Cross-Browser Compatibility
│   ├── index.html
│   ├── styles.css
│   └── app.js
└── handson_10/                 # Centralized API Service Layer & Advanced Redux Toolkit
    ├── package.json
    ├── vite.config.js
    ├── index.html
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── api/
        │   ├── apiClient.js
        │   └── courseApi.js
        ├── store/
        │   ├── store.js
        │   └── coursesSlice.js
        ├── components/
        │   ├── ErrorBoundary.jsx
        │   ├── Header.jsx
        │   └── CourseCard.jsx
        ├── pages/
        │   ├── CoursesPage.jsx
        │   └── ProfilePage.jsx
        └── styles/index.css
```

---

## 🛠️ Software & System Requirements

- **Node.js**: v18.x or v20.x (LTS recommended)
- **npm**: v9.x or higher
- **Modern Browser**: Google Chrome, Mozilla Firefox, Microsoft Edge, or Apple Safari

---

## 🚀 How to Run Each Hands-On Exercise

### Hands-On 01 to 04 & 09 (Vanilla HTML/CSS/JS)
These exercises require no node module installation.
1. Open the respective directory (e.g. `handson_01`).
2. Open `index.html` directly in your browser or launch it using VS Code Live Server.

### Hands-On 05 (React Fundamentals - Vite)
```bash
cd handson_05
npm install
npm run dev
```

### Hands-On 06 (React Router & Redux Toolkit)
```bash
cd handson_06
npm install
npm run dev
```

### Hands-On 07 (Angular Application)
```bash
cd handson_07
npm install
npm run build
```

### Hands-On 08 (Vue 3 + Pinia + Vue Router)
```bash
cd handson_08
npm install
npm run dev
```

### Hands-On 10 (Advanced State Management & Centralized API)
```bash
cd handson_10
npm install
npm run dev
```

---

## 🎨 Unified Design System & Color Palette

All exercises strictly adhere to the following design system:

| Element | Color Code | Description |
| :--- | :--- | :--- |
| **Primary** | `#2563eb` | Royal Blue (Buttons, Brand Highlights, Focus states) |
| **Secondary** | `#0f172a` | Deep Slate / Dark Navy (Header, Footer, Dark Headings) |
| **Accent** | `#38bdf8` | Sky Blue (Hover effects, Active Indicators, Badges) |
| **Background** | `#f8fafc` | Cool Off-White (Body Background) |
| **Cards** | `#ffffff` | Pure White with subtle shadow (`0 4px 6px -1px rgba(0,0,0,0.1)`) |

---

## ♿ Web Accessibility (WCAG 2.1 Compliance in Hands-On 09)

- **Semantic Elements**: Native `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<button>`, and `<label>`.
- **Keyboard Navigability**: Full tab order support, `tabindex="0"`, and custom `Enter`/`Space` keydown listener handlers for interactive cards.
- **ARIA Attributes**: `aria-label="Main navigation"`, `aria-current="page"`, `role="status"`, `aria-live="polite"`, `aria-expanded`.
- **Contrast Ratios**: Minimum 4.5:1 ratio for standard text against backgrounds across all light/dark themes.

---

## 📊 State Management Comparison (React + Redux vs. Angular + NgRx vs. Vue + Pinia)

| Feature | React + Redux Toolkit | Angular + NgRx | Vue 3 + Pinia |
| :--- | :--- | :--- | :--- |
| **Boilerplate** | Moderate (Slice + Store + Thunks) | High (Actions, Reducers, Effects, Selectors) | Low (Setup store function with refs & actions) |
| **Learning Curve** | Moderate | Steep (Requires RxJS knowledge) | Gentle (Uses standard Vue Composition API) |
| **Reactivity** | Immutable updates via Immer | Immutable Observables | Direct reactive refs (`ref()`, `computed()`) |
| **Async Flow** | `createAsyncThunk` | NgRx Effects (`Actions.pipe(...)`) | Async action functions directly in store |
| **Built-in Tooling** | Redux DevTools extension | Redux DevTools / Angular DevTools | Vue DevTools (native integration) |

---

## 📝 License & Attribution
Designed for **Digital Nurture 5.0 Deep Skilling Program - Python Full Stack Engineer Track**.
