# Sin E Spoiler: Your First React Cinema App 🎬✨

_A professional guide to building a modern cinema web application using React 19, modular CSS architecture, and accessible HTML semantics._

🎥 Welcome to **Sin E Spoiler**, an AI-enhanced movie listing platform built with cutting-edge frontend technologies. This guide will walk you through your first steps using **React**, **Vite**, and a custom CSS system — preparing you to design robust, scalable interfaces with components, props, JSX, and secure data rendering. 🚀

---

## 📚 Table of Contents

- [Sin E Spoiler: Your First React Cinema App 🎬✨](#sin-e-spoiler-your-first-react-cinema-app-)
  - [📚 Table of Contents](#-table-of-contents)
  - [1. Understanding the Concept](#1-understanding-the-concept)
    - [What is React?](#what-is-react)
    - [Why Declarative?](#why-declarative)
    - [Core React Concepts](#core-react-concepts)
    - [Component Structure](#component-structure)
    - [JSX Syntax](#jsx-syntax)
  - [2. Environment Setup](#2-environment-setup)
    - [Project Structure](#project-structure)
    - [Creating the React App](#creating-the-react-app)
    - [HTML Entry Point Setup](#html-entry-point-setup)
    - [CSS Modular Architecture](#css-modular-architecture)
    - [Safe Rendering with `safeString`](#safe-rendering-with-safestring)
  - [3. Implementation](#3-implementation)
    - [Step 0: HTML Entry Setup I Base Structure 🧱](#step-0-html-entry-setup-i-base-structure-)
    - [Step 1: Base CSS Architecture I Complete System for “Sin E Spoiler”](#step-1-base-css-architecture-i-complete-system-for-sin-e-spoiler)
    - [Step 2: Movie Data Structure I Realistic TMDB-based Records](#step-2-movie-data-structure-i-realistic-tmdb-based-records)
    - [Step 3: Header Component I Sin E Spoiler](#step-3-header-component-i-sin-e-spoiler)
    - [Step 4: Footer Component I Contact \& Info](#step-4-footer-component-i-contact--info)
    - [Step 5: Hero Component I Highlight Banner](#step-5-hero-component-i-highlight-banner)
    - [Step 6: Rating Component I Score](#step-6-rating-component-i-score)
    - [Step 7: MovieCard Component I Card Display](#step-7-moviecard-component-i-card-display)
    - [Step 8: MovieList Component I Grid Section](#step-8-movielist-component-i-grid-section)
    - [Step 9: App Component I App Orchestrator](#step-9-app-component-i-app-orchestrator)
    - [Step 10: Entry Point I App Bootstrap](#step-10-entry-point-i-app-bootstrap)
  - [4. Running the Application](#4-running-the-application)
  - [5. Next Steps](#5-next-steps)
    - [Best Practices](#best-practices)
    - [Resources](#resources)
    - [Congratulations!](#congratulations)
    - [Week 10 Preview](#week-10-preview)

---

## 1. Understanding the Concept

### What is React?

🧠 **React** is a modern JavaScript library for building user interfaces declaratively using a component-based architecture. It allows you to create modular UI structures that update automatically with changes in state or props.

- 🧩 Component-Based UI
- 🔁 One-way data flow
- ⚡ Virtual DOM efficiency
- ✨ JSX (HTML + JS fusion)
- 🔒 Secure rendering with sanitization

---

### Why Declarative?

🪄 With React, you don't describe step-by-step how to change the UI — you **declare** the expected output, and React handles the rest. This leads to more predictable and maintainable code.

```jsx
// Declarative
const WelcomeMessage = ({ name }) => (
  <h1>Hello, {safeString(name)}! 🎉</h1>
);
```

---

### Core React Concepts

```
   Components          Props           JSX              Result
       │                │              │                 │
       ▼                ▼              ▼                 ▼
   ┌─────────┐     ┌─────────┐    ┌─────────┐     ┌──────────┐
   │ <Movie  │ ──> │ title=  │ ──>│ <div>   │ ──> │ Rendered │
   │   />    │     │ "Avatar"│    │  Movie  │     │   Card   │
   └─────────┘     └─────────┘    └─────────┘     └──────────┘
```

🧭 React apps are made of composable **functions** that return JSX. Each function accepts **props** (inputs), uses state/hooks internally (if needed), and returns a tree of **JSX elements**.

---

### Component Structure

```jsx
// Functional Component – no React import required in React 19
const MovieTeaser = ({ title }) => (
  <div className="card">
    <h2 className="title">{safeString(title)}</h2>
  </div>
);
```

📦 Features:
- Only **functional components**
- Stateless by default
- Named with **PascalCase**
- Always return a **single JSX tree**

---

### JSX Syntax

🔤 JSX is not a string, not HTML — it’s a syntactic sugar for JavaScript objects:

```jsx
const element = <h1 className="headline">Now Showing</h1>;

// Equivalent to:
const element = React.createElement("h1", { className: "headline" }, "Now Showing");
```

💡 JSX allows:
- Using `{}` to embed JS expressions
- Binding data inside markup
- Adding dynamic attributes and conditions

---

## 2. Environment Setup

### Project Structure

📁 Recommended architecture:

```
sin-e-spoiler/
├── public/
│   └── index.html               # 📄 HTML entry point
├── src/
│   ├── components/
│   │   ├── layouts/             # 🧭 Header, Footer
│   │   ├── modules/             # 🧠 Hero, Teasers
│   │   ├── widgets/             # 🧱 OverlayCardList
│   │   └── components/          # 🎴 Buttons, Cards, Rating
│   ├── css/
│   │   ├── index.css            # 🎨 CSS entry
│   │   └── modules/
│   │       ├── properties.css
│   │       ├── variables.css
│   │       ├── keyframes.css
│   │       ├── globals.css
│   │       ├── layout.css
│   │       ├── components.css
│   │       ├── elements.css
│   │       └── utils.css
│   ├── data/                    # 📊 Movie data
│   ├── App.jsx                  # 🚀 Root component
│   └── main.jsx                 # 📍 Entry point
├── vite.config.js
├── package.json                # 📦 Project config
└── README.md                   # 📖 Documentation
```

---

### Creating the React App

⚡ Create the project with Vite:

```bash
npm create vite@latest sin-e-spoiler -- --template react
cd sin-e-spoiler

# Clean defaults 🧹
rm src/App.css src/logo.svg src/index.css

npm install
```

---

### HTML Entry Point Setup

✏️ Edit `public/index.html`:

```html
<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <link rel="icon" type="image/svg+xml" href="/vite.svg" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>🎬 Sin E Spoiler</title>
</head>

<body class="body">
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>

</html>
```

🎯 Tip: Use classes to give styles and semantic tags inside div#root like `<main class="main">`, `<header class="header">` and `<footer class="footer">`.

---

### CSS Modular Architecture

🎨 In `src/css/index.css`, import your modular system:

```css
@import url("./modules/properties.css");
@import url("./modules/variables.css");
@import url("./modules/keyframes.css");
@import url("./modules/globals.css");
@import url("./modules/layout.css");
@import url("./modules/components.css");
@import url("./modules/elements.css");
@import url("./modules/utils.css");
```

💼 Your utility-first system supports:
- BEM-like partial naming
- Responsive and semantic CSS
- Animations via `@property` and scroll-based transitions

---

### Safe Rendering with `safeString`

🛡️ Prevent XSS and malformed content by sanitizing text:

```ts
export const safeString = (str = "") =>
  String(str).replace(/[<>]/g, "");

<p>{safeString(movie.description)}</p>
```

🧼 Always sanitize movie descriptions, user content or API-driven strings.

## 3. Implementation

### Step 0: HTML Entry Setup I Base Structure 🧱

This step prepares your Vite + React project with the essential HTML metadata and assets for a professional cinema experience. 🎬✨

---

**📁 File Path**

```
index.html
```

---

**✅ Features**

- Title and favicon customization
- Viewport and charset meta tags
- Mount point for React app (`#root`)
- Clean semantic base for SEO & accessibility

---

**🧩 Code**

```html
<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sin E Spoiler 🎥 | AI-Powered Movie Reviews</title>
  <meta name="description" content="Spoiler-free cinema experience. AI reviews, AR posters, and premiere giveaways." />
  <meta name="theme-color" content="#23B5E8" />
  <link rel="icon" type="image/svg+xml" href="/logo.svg" />
  <!-- <link rel="apple-touch-icon" href="/apple-touch-icon.png" /> -->
</head>

<body class="body">
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>

</html>
```

---

**🧠 UX Guidelines**

- Use meaningful metadata for SEO and share previews (e.g., Open Graph later)
- Replace `/vite.svg` with `/logo.svg` for branding
- Add `apple-touch-icon` for mobile bookmarks (coming soon)
- Theme color sets browser UI color on mobile devices

---

### Step 1: Base CSS Architecture I Complete System for “Sin E Spoiler”

This section contains the **entire CSS system** needed to support the "Sin E Spoiler" React cinema app. It follows your modular, responsive, and animation-rich style methodology with `@property`, keyframes, and scroll-driven interactions. Layered CSS system designed to be:
- ✅ **Semantic** (HTML5)
- ✅ **Scalable** (utility-first + BEM partial)
- ✅ **Customizable** (CSS variables)
- ✅ **Responsive** (media queries, clamp units)
- ✅ **Animated** (using `@property` and keyframes)

---


**📁 Folder Structure**

```
src/css/ 📂
├── index.css 🎨
└── modules/ 📂
    ├── properties.css 🛠️
    ├── variables.css 🌈
    ├── keyframes.css 🌀
    ├── globals.css 🌐
    ├── layout.css 📐
    ├── components.css 📌
    ├── elements.css 🧱
    └── utils.css 🧰
```

---

**✨ `src/css/modules/properties.css`**

Enable smooth animations by registering animatable custom properties:

```css
@property --length {
  syntax: "<length>";
  inherits: true;
  initial-value: 0;
}

@property --color {
  syntax: "<color>";
  inherits: true;
  initial-value: transparent;
}
```

---

**🌈 `src/css/modules/variables.css`**

Centralized design tokens for consistent theming and spacing:

```css
:root {
  color-scheme: dark;
  scroll-behavior: smooth;

  --primary-color: #23B5E8;
  --secondary-color: #234B96;
  --black-color: #010508;
  --white-color: #FEFEFE;

  --neutral-950: #191B1C;
  --shadow: #fefefe80;
  --light-shadow: #01050880;

  --size: 0.21875rem;
  --max-width: 1280px;
  --transition-duration: 0.25s;

  --primary-font: "Open Sans", sans-serif;

  --primary-background: var(--black-color);
  --secondary-background: var(--neutral-950);

  --primary-text: var(--white-color);
  --light-primary-text: var(--black-color);

  --border-radius: calc(var(--size) * 2);

  @media (width >=768px) {
    --size: 0.25rem;
  }
}
```

---

**🎞️ `src/css/modules/keyframes.css`**

Animation for scroll-based length and color transitions:

```css
@keyframes change-length {
  from {
    --length: var(--initial-length);
  }
  to {
    --length: var(--final-length);
  }
}

@keyframes change-color {
  from {
    --color: var(--initial-color);
  }
  to {
    --color: var(--final-color);
  }
}
```

---

**🌐 `src/css/modules/globals.css`**

Global document-level rules:

```css
.body {
  margin: 0;
  font-family: var(--primary-font);
  background-color: var(--primary-background);
  color: var(--primary-text);
}

#root {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main *[id] {
  scroll-margin-top: calc(var(--size) * 32);
}
```

---

**📐 `src/css/modules/layout.css`**

Utility classes for flexible layout systems:

```css
.container {
  max-width: var(--max-width);
  padding-inline: calc(var(--size) * 4);
  margin-inline: auto;
}

.flexbox {
  display: flex;
}

.flexbox--center {
  place-items: center;
  place-content: center;
}

.flexbox--centered-spacing {
  align-items: center;
  justify-content: space-between;
}

.flexbox--responsive {
  flex-direction: column;

  @media (width >=768px) {
    flex-direction: row;
  }
}

.g-layout {
  display: grid;
}

.g-layout--center {
  place-items: center;
  place-content: center;
}

.g-layout--auto-fit-columns {
  grid-template-columns: repeat(auto-fit, minmax(calc(var(--size) * 60), 1fr));
}

.g-layout--auto-fit-columns-lg {
  grid-template-columns: repeat(auto-fit, minmax(calc(var(--size) * 80), 1fr));
}
```

---

**🧩 `src/css/modules/components.css`**

```css
.header {
  --initial-length: 0;
  --final-length: var(--size);
  --length: var(--initial-length);
  --initial-color: transparent;
  --final-color: var(--light-shadow);
  --color: var(--initial-color);
  position: fixed;
  z-index: 5;
  top: 0;
  width: 100%;
  box-shadow: 0 0 calc(var(--length) * 0.5) calc(var(--length) * 0.125) var(--shadow);
  background-color: var(--color);
  backdrop-filter: blur(calc(var(--length) * 2));
  animation: change-length linear forwards, change-color linear forwards;
  animation-timeline: scroll();
  animation-range: 0 calc(var(--size) * 64);
}

.main {
  --grad-primary: color-mix(in srgb, var(--primary-color) 18%, transparent);
  --grad-secondary: color-mix(in srgb, var(--secondary-color) 15%, transparent);
}

.main > :nth-child(odd) {
  background-image:
    radial-gradient(circle at 20% 30%, var(--grad-primary) 0%, transparent 40%),
    radial-gradient(circle at 80% 70%, var(--grad-secondary) 0%, transparent 40%),
    linear-gradient(135deg, var(--primary-background) 0%, var(--secondary-background) 100%);
}

.main > :nth-child(even) {
  background-image:
    radial-gradient(circle at 80% 30%, var(--grad-secondary) 0%, transparent 40%),
    radial-gradient(circle at 20% 70%, var(--grad-primary) 0%, transparent 40%),
    linear-gradient(135deg, var(--secondary-background) 0%, var(--primary-background) 100%);
}

.nav {
  padding-block: calc(var(--size) * 4);
}

.nav--scroll {
  --initial-length: calc(var(--size) * 6);
  --final-length: calc(var(--size) * 4);
  --length: var(--initial-length);
  padding-block: var(--length);
  animation: change-length linear forwards;
  animation-timeline: scroll();
  animation-range: 0 calc(var(--size) * 64);
}

.off-canvas {
  --t-translate: -100%;
  position: fixed;
  inset: 0;
  display: flex;
  background-color: var(--light-shadow);
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-duration);
}

.off-canvas:target {
  --t-translate: 0;
  opacity: initial;
  pointer-events: initial;
}

.off-canvas--right {
  --t-translate: 100%;
  justify-content: flex-end;
}

.off-canvas--right .off-canvas__child {
  width: min(calc(var(--size) * 80), 50%);
  transform: translate(var(--t-translate), 0);
}

.off-canvas--mobile {
  @media (width >= 768px) {
    all: unset;
  }

  .off-canvas__child {
    all: unset;
  }

  .off-canvas__backdrop {
    display: none;
  }
}

.off-canvas__backdrop {
  position: fixed;
  inset: 0;
}

.off-canvas__child {
  cursor: initial;
  width: 100%;
  height: 100dvh;
  padding: calc(var(--size) * 4);
  box-sizing: border-box;
  background-color: var(--light-shadow);
  transform: translate(0, var(--t-translate));
  transition: transform var(--transition-duration);
}

.hero {
  padding-block: calc(var(--size) * 32);
}

.hero__title {
  margin: 0;
  font-size: clamp(2rem, 5vw, 4rem);
}

.hero__paragraph {
  margin: 0;
  font-size: clamp(1.125rem, 2.5vw, 1.5rem);
}

.section {
  padding-block: calc(var(--size) * 16);
}

.list {
  padding: 0;
  margin: 0;
  list-style: none;
}

.card {
  --primary-card-color: var(--shadow);
  border-radius: calc(var(--border-radius) * 2);
  box-shadow: calc(var(--size) * 0.0625) calc(var(--size) * 0.125) var(--size) calc(var(--size) * 0.0625) var(--primary-card-color);
  overflow: hidden;
  transition: box-shadow var(--transition-duration), transform var(--transition-duration);
}

.card:hover {
  --primary-card-color: var(--primary-color);
  transform: scale(1.0625);
}

.card--overlay {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: flex-end;
  max-width: calc(var(--size) * 106.5);
  height: calc(var(--size) * 60);
  background-color: var(--primary-background);
  text-decoration: none;
}

.card__body {
  display: flex;
  flex-direction: column;
  gap: var(--size);
  padding: calc(var(--size) * 4);
}

.footer {
  position: relative;
  box-shadow: 0 0 calc(var(--size) * 0.5) calc(var(--size) * 0.125) var(--shadow);
}

.footer > .nav:nth-child(odd) {
  background-color: var(--secondary-background);
}

.footer > .nav:nth-child(even) {
  background-color: var(--primary-background);
}
```

---

**📄 `src/css/modules/elements.css`**

```css
.title {
  margin: 0;
  font-size: calc(var(--size) * 8);
  font-weight: 800;
}

.title--sm {
  font-size: calc(var(--size) * 7);
}

.title--xs {
  font-size: calc(var(--size) * 6);
  font-weight: 700;
}

.text {
  margin: 0;
  font-size: calc(var(--size) * 4);
}

.text--sm {
  font-size: calc(var(--size) * 3.5);
}

.text--xs {
  font-size: calc(var(--size) * 3);
}

.interactive {
  margin: 0;
  font-size: calc(var(--size) * 3.5);
  font-weight: 600;
}

.interactive--xl {
  font-size: calc(var(--size) * 4.5);
}

.interactive--lg {
  font-size: calc(var(--size) * 4);
}

.interactive--sm {
  font-size: calc(var(--size) * 3);
}

.interactive--xs {
  font-size: calc(var(--size) * 2.5);
}

.img {
  display: block;
  object-fit: cover;
}

.img--logo {
  height: calc(var(--size) * 9);
  width: auto;
}

.img--background {
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  inset: 0;
  opacity: 0.5;
}

.link {
  position: relative;
  color: var(--primary-text);
  text-decoration: none;
  transition: color var(--transition-duration);
}

.link::before {
  content: "";
  position: absolute;
  bottom: -0.125em;
  width: 100%;
  height: 0.0625em;
  background-color: var(--primary-color);
  transform: scale(0);
  transition: transform var(--transition-duration);
}

.link:hover {
  color: var(--primary-color);
}

.link:hover::before {
  transform: scale(1);
}

.button {
  --primary-button-color: var(--primary-background);
  --primary-button-text: var(--primary-text);
  padding: 0.5em 1em;
  border: calc(var(--size) * 0.125) solid var(--primary-button-color);
  border-radius: calc(var(--size) * 2);
  background-color: var(--primary-button-color);
  color: var(--primary-button-text);
  cursor: pointer;
  text-decoration: none;
  font-family: var(--primary-font);
  transition: box-shadow var(--transition-duration), filter var(--transition-duration);
}

.button:hover {
  box-shadow: 0 0 calc(var(--size) * 2) var(--primary-button-color);
  filter: opacity(0.875);
}

.button--primary {
  --primary-button-color: var(--primary-color);
  --primary-button-text: var(--light-primary-text);
}

.badge {
  --primary-badge-color: var(--primary-background);
  --primary-badge-text: var(--primary-text);
  padding: 0.25em 0.5em;
  border-radius: calc(var(--size) * 2);
  background-color: var(--primary-badge-color);
  color: var(--primary-badge-text);
}

.badge--primary {
  --primary-badge-color: var(--primary-color);
  --primary-badge-text: var(--light-primary-text);
}
```

---

**🛠️ `src/css/modules/utils.css`**

```css
.d-flex {
  display: flex;
}

.f-direction-column {
  flex-direction: column;
}

.a-items-center {
  align-items: center;
}

.j-content-end {
  justify-content: flex-end;
}

.j-content-center {
  justify-content: center;
}

.j-content-between {
  justify-content: space-between;
}

.f-wrap {
  flex-wrap: wrap;
}

.g-1 {
  gap: var(--size);
}

.g-2 {
  gap: calc(var(--size) * 2);
}

.g-4 {
  gap: calc(var(--size) * 4);
}

.g-5 {
  gap: calc(var(--size) * 5);
}

.g-8 {
  gap: calc(var(--size) * 8);
}

.g-10 {
  gap: calc(var(--size) * 10);
}

.f-1 {
  flex: 1;
}

.f-2 {
  flex: 2;
}

.c-primary {
  color: var(--primary-color);
}

.c-secondary {
  color: var(--secondary-color);
}

.c-white {
  color: var(--white-color);
}

.c-warning {
  color: var(--warning-color);
}

.t-align-center {
  text-align: center;
}

@media (width >= 768px) {
  .md\:d-none {
    display: none;
  }
}
```


---

**🔧 `src/css/index.css`**

This is the entry point for all your CSS modules. Import your styles in order:

```css
@import url("./modules/properties.css");
@import url("./modules/variables.css");
@import url("./modules/keyframes.css");
@import url("./modules/globals.css");
@import url("./modules/layout.css");
@import url("./modules/components.css");
@import url("./modules/elements.css");
@import url("./modules/utils.css");
```

✅ With this structure, your CSS is now **powerful, scalable, and ready** to deliver a professional UI experience. 🎬

---

### Step 2: Movie Data Structure I Realistic TMDB-based Records

This step defines how to structure and use movie data in our app. We use real TMDB data, map it to our app format with a custom mapper, and expose utility functions for components to consume. 📊✨

---


**📁 Folder Structure**

```
src/ 📂
├── data/
│   └── movies.data.js 🎞️  # Raw TMDB movie data
└── utils/
    └── movie.utils.js 🧠  # Mapping and image utilities
```
---

**🎞️ `src/data/movies.data.js`**
```js
export const tmdbNowPlayingMock = {
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/qdKGpTHVaaKaFTnRynQDg4qHdEv.jpg",
      "genre_ids": [
        10751,
        35,
        12,
        14
      ],
      "id": 950387,
      "original_language": "en",
      "original_title": "A Minecraft Movie",
      "overview": "Four misfits find themselves struggling with ordinary problems when they are suddenly pulled through a mysterious portal into the Overworld: a bizarre, cubic wonderland that thrives on imagination. To get back home, they'll have to master this world while embarking on a magical quest with an unexpected, expert crafter, Steve.",
      "popularity": 767.9151,
      "poster_path": "/yFHHfHcUgGAxziP1C3lLt0q2T4s.jpg",
      "release_date": "2025-03-31",
      "title": "A Minecraft Movie",
      "video": false,
      "vote_average": 6.487,
      "vote_count": 1137
    },
    {
      "adult": false,
      "backdrop_path": "/cJvUJEEQ86LSjl4gFLkYpdCJC96.jpg",
      "genre_ids": [
        10752,
        28
      ],
      "id": 1241436,
      "original_language": "en",
      "original_title": "Warfare",
      "overview": "A platoon of Navy SEALs embarks on a dangerous mission in Ramadi, Iraq, with the chaos and brotherhood of war retold through their memories of the event.",
      "popularity": 384.6248,
      "poster_path": "/srj9rYrjefyWqkLc6l2xjTGeBGO.jpg",
      "release_date": "2025-04-09",
      "title": "Warfare",
      "video": false,
      "vote_average": 7.1,
      "vote_count": 313
    },
    {
      "adult": false,
      "backdrop_path": "/tyfO9jHgkhypUFizRVYD0bytPjP.jpg",
      "genre_ids": [
        10751,
        14
      ],
      "id": 447273,
      "original_language": "en",
      "original_title": "Snow White",
      "overview": "Following the benevolent King's disappearance, the Evil Queen dominated the once fair land with a cruel streak. Princess Snow White flees the castle when the Queen, in her jealousy over Snow White's inner beauty, tries to kill her. Deep into the dark woods, she stumbles upon seven magical dwarves and a young bandit named Jonathan. Together, they strive to survive the Queen's relentless pursuit and aspire to take back the kingdom.",
      "popularity": 358.0439,
      "poster_path": "/oLxWocqheC8XbXbxqJ3x422j9PW.jpg",
      "release_date": "2025-03-12",
      "title": "Snow White",
      "video": false,
      "vote_average": 4.323,
      "vote_count": 789
    },
    {
      "adult": false,
      "backdrop_path": "/jRvhP4AfFnJ03lCQhp1fie7XPSd.jpg",
      "genre_ids": [
        28,
        53
      ],
      "id": 977294,
      "original_language": "en",
      "original_title": "Tin Soldier",
      "overview": "An ex-special forces operative seeks revenge against a cult leader who has corrupted his former comrades, the Shinjas. This leader, known as The Bokushi, promises veterans a purpose and protection, but is revealed to be a destructive influence. The ex-soldier, Nash Cavanaugh, joins forces with military operative Emmanuel Ashburn to infiltrate the Bokushi's fortress and expose his reign of terror",
      "popularity": 341.4585,
      "poster_path": "/lFFDrFLXywFhy6khHes1LCFVMsL.jpg",
      "release_date": "2025-05-22",
      "title": "Tin Soldier",
      "video": false,
      "vote_average": 5.469,
      "vote_count": 16
    },
    {
      "adult": false,
      "backdrop_path": "/fTrQsdMS2MUw00RnzH0r3JWHhts.jpg",
      "genre_ids": [
        28,
        80,
        53
      ],
      "id": 1197306,
      "original_language": "en",
      "original_title": "A Working Man",
      "overview": "Levon Cade left behind a decorated military career in the black ops to live a simple life working construction. But when his boss's daughter, who is like family to him, is taken by human traffickers, his search to bring her home uncovers a world of corruption far greater than he ever could have imagined.",
      "popularity": 335.4882,
      "poster_path": "/6FRFIogh3zFnVWn7Z6zcYnIbRcX.jpg",
      "release_date": "2025-03-26",
      "title": "A Working Man",
      "video": false,
      "vote_average": 6.5,
      "vote_count": 719
    },
    {
      "adult": false,
      "backdrop_path": "/j0NUh5irX7q2jIRtbLo8TZyRn6y.jpg",
      "genre_ids": [
        27,
        9648
      ],
      "id": 574475,
      "original_language": "en",
      "original_title": "Final Destination Bloodlines",
      "overview": "Plagued by a violent recurring nightmare, college student Stefanie heads home to track down the one person who might be able to break the cycle and save her family from the grisly demise that inevitably awaits them all.",
      "popularity": 305.7915,
      "poster_path": "/6WxhEvFsauuACfv8HyoVX6mZKFj.jpg",
      "release_date": "2025-05-09",
      "title": "Final Destination Bloodlines",
      "video": false,
      "vote_average": 7.276,
      "vote_count": 127
    },
    {
      "adult": false,
      "backdrop_path": "/rthMuZfFv4fqEU4JVbgSW9wQ8rs.jpg",
      "genre_ids": [
        28,
        878,
        12
      ],
      "id": 986056,
      "original_language": "en",
      "original_title": "Thunderbolts*",
      "overview": "After finding themselves ensnared in a death trap, seven disillusioned castoffs must embark on a dangerous mission that will force them to confront the darkest corners of their pasts.",
      "popularity": 239.5162,
      "poster_path": "/m9EtP1Yrzv6v7dMaC9mRaGhd1um.jpg",
      "release_date": "2025-04-30",
      "title": "Thunderbolts*",
      "video": false,
      "vote_average": 7.484,
      "vote_count": 863
    },
    {
      "adult": false,
      "backdrop_path": "/4A5HH9HkCPqAwyYL6CnA0mxbYjn.jpg",
      "genre_ids": [
        28,
        80,
        53,
        18
      ],
      "id": 1144430,
      "original_language": "fr",
      "original_title": "Balle perdue 3",
      "overview": "Car genius Lino returns to conclude his vendetta against Areski and the corrupt commander who ruined their lives in this turbo-charged trilogy finale.",
      "popularity": 232.3141,
      "poster_path": "/qycPITRqXgPai7zj1gKffjCdSB5.jpg",
      "release_date": "2025-05-06",
      "title": "Last Bullet",
      "video": false,
      "vote_average": 6.777,
      "vote_count": 110
    },
    {
      "adult": false,
      "backdrop_path": "/jmLfuMFn6o4Rkp7dzT57Vp2GpoQ.jpg",
      "genre_ids": [
        28,
        18,
        35
      ],
      "id": 897160,
      "original_language": "ko",
      "original_title": "용감한 시민",
      "overview": "An expelled boxing champion, who now is a high-school teacher, witnesses intolerable violence and throws her first punch to build justice against it, while putting on a mask.",
      "popularity": 211.1394,
      "poster_path": "/6Ea5i6APeTfm4hHh6dg5Z733JVS.jpg",
      "release_date": "2023-10-25",
      "title": "Brave Citizen",
      "video": false,
      "vote_average": 7.1,
      "vote_count": 37
    },
    {
      "adult": false,
      "backdrop_path": "/mrmaTVp7PTBkjj5G62cE9pjrENg.jpg",
      "genre_ids": [
        27,
        18
      ],
      "id": 1359977,
      "original_language": "en",
      "original_title": "Conjuring the Cult",
      "overview": "After discovering his blood-soaked daughter dead in the bathtub, David Bryson attends a self-help group to help save him from his ghostly nightmares. But when a group of mysterious cult-like women offer to help him resurrect his daughter. David's choices will not just decide his fate... but the fate of his dead daughter's SOUL.",
      "popularity": 205.5955,
      "poster_path": "/t4MiAeYpjL7saYvqvcn9xtOfA4K.jpg",
      "release_date": "2024-10-01",
      "title": "Conjuring the Cult",
      "video": false,
      "vote_average": 5.263,
      "vote_count": 19
    },
    {
      "adult": false,
      "backdrop_path": "/bIh56F8e5EaZ3r2nD1hXAOisItZ.jpg",
      "genre_ids": [
        12,
        10751
      ],
      "id": 1094473,
      "original_language": "fr",
      "original_title": "Bambi, l'histoire d'une vie dans les bois",
      "overview": "The life of Bambi, a male roe deer, from his birth through childhood, the loss of his mother, the finding of a mate, the lessons he learns from his father, and the experience he gains about the dangers posed by human hunters in the forest.",
      "popularity": 204.0274,
      "poster_path": "/vWNVHtwOhcoOEUSrY1iHRGbgH8O.jpg",
      "release_date": "2024-10-16",
      "title": "Bambi: A Life in the Woods",
      "video": false,
      "vote_average": 6.133,
      "vote_count": 15
    },
    {
      "adult": false,
      "backdrop_path": "/bVm6udIB6iKsRqgMdQh6HywuEBj.jpg",
      "genre_ids": [
        53,
        28
      ],
      "id": 1233069,
      "original_language": "de",
      "original_title": "Exterritorial",
      "overview": "When her son vanishes inside a US consulate, ex-special forces soldier Sara does everything in her power to find him — and uncovers a dark conspiracy.",
      "popularity": 198.7709,
      "poster_path": "/jM2uqCZNKbiyStyzXOERpMqAbdx.jpg",
      "release_date": "2025-04-29",
      "title": "Exterritorial",
      "video": false,
      "vote_average": 6.627,
      "vote_count": 335
    },
    {
      "adult": false,
      "backdrop_path": "/8eifdha9GQeZAkexgtD45546XKx.jpg",
      "genre_ids": [
        28,
        53,
        878
      ],
      "id": 822119,
      "original_language": "en",
      "original_title": "Captain America: Brave New World",
      "overview": "After meeting with newly elected U.S. President Thaddeus Ross, Sam finds himself in the middle of an international incident. He must discover the reason behind a nefarious global plot before the true mastermind has the entire world seeing red.",
      "popularity": 157.431,
      "poster_path": "/pzIddUEMWhWzfvLI3TwxUG2wGoi.jpg",
      "release_date": "2025-02-12",
      "title": "Captain America: Brave New World",
      "video": false,
      "vote_average": 6.118,
      "vote_count": 1847
    },
    {
      "adult": false,
      "backdrop_path": "/op3qmNhvwEvyT7UFyPbIfQmKriB.jpg",
      "genre_ids": [
        28,
        14,
        12
      ],
      "id": 324544,
      "original_language": "en",
      "original_title": "In the Lost Lands",
      "overview": "A queen sends the powerful and feared sorceress Gray Alys to the ghostly wilderness of the Lost Lands in search of a magical power, where she and her guide, the drifter Boyce, must outwit and outfight both man and demon.",
      "popularity": 145.1824,
      "poster_path": "/dDlfjR7gllmr8HTeN6rfrYhTdwX.jpg",
      "release_date": "2025-02-27",
      "title": "In the Lost Lands",
      "video": false,
      "vote_average": 6.351,
      "vote_count": 368
    },
    {
      "adult": false,
      "backdrop_path": "/zXUxcXnBPHF1cD0IHi4KUpsNvF4.jpg",
      "genre_ids": [
        53,
        18,
        10749
      ],
      "id": 1323784,
      "original_language": "es",
      "original_title": "Mala influencia",
      "overview": "An ex-con gets a fresh start when hired to protect a wealthy heiress from a stalker — but their chemistry is hard to resist as they grow closer.",
      "popularity": 144.358,
      "poster_path": "/ghhooCOqQDqC6vhS1SVN2tCE0k8.jpg",
      "release_date": "2025-01-24",
      "title": "Bad Influence",
      "video": false,
      "vote_average": 5.621,
      "vote_count": 103
    },
    {
      "adult": false,
      "backdrop_path": "/12tEzU0bNYKIjXXEwI5abuOotHF.jpg",
      "genre_ids": [
        37
      ],
      "id": 710258,
      "original_language": "en",
      "original_title": "Rust",
      "overview": "Infamous outlaw Harland Rust breaks his estranged grandson Lucas out of prison, after Lucas is convicted to hang for an accidental murder. The two must outrun legendary U.S Marshal Wood Helm and bounty hunter Fenton \"Preacher\" Lang who are hot on their tails. Deeply buried secrets rise from the ashes and an unexpected familial bond begins to form as the mismatched duo tries to survive the merciless American Frontier.",
      "popularity": 139.922,
      "poster_path": "/tbJ3RkA2s6X5qrBzrYHYTxvDBui.jpg",
      "release_date": "2025-05-01",
      "title": "Rust",
      "video": false,
      "vote_average": 6.388,
      "vote_count": 49
    },
    {
      "adult": false,
      "backdrop_path": "/jI8j3vy1fFZpjaGA6ALuyQuadfm.jpg",
      "genre_ids": [
        27
      ],
      "id": 1260820,
      "original_language": "es",
      "original_title": "Stream",
      "overview": "Craven, a streamer with thousands of followers on a live streaming platform, has prepared a very special stream for Halloween. What no one expects when reacting to a video of Pentagram, a group of young paranormal investigators, is that the live experience will turn into the worst night of their lives. And maybe... the last.",
      "popularity": 133.3677,
      "poster_path": "/nnyjtBfUYA8ASHA9OhADrX0sMNQ.jpg",
      "release_date": "2024-02-06",
      "title": "Stream",
      "video": false,
      "vote_average": 6.5,
      "vote_count": 14
    },
    {
      "adult": false,
      "backdrop_path": "/65MVgDa6YjSdqzh7YOA04mYkioo.jpg",
      "genre_ids": [
        28,
        80,
        53
      ],
      "id": 668489,
      "original_language": "en",
      "original_title": "Havoc",
      "overview": "When a drug heist swerves lethally out of control, a jaded cop fights his way through a corrupt city's criminal underworld to save a politician's son.",
      "popularity": 118.2762,
      "poster_path": "/r46leE6PSzLR3pnVzaxx5Q30yUF.jpg",
      "release_date": "2025-04-25",
      "title": "Havoc",
      "video": false,
      "vote_average": 6.5,
      "vote_count": 627
    },
    {
      "adult": false,
      "backdrop_path": "/7ONMDhnErvpkKvkZqM82ud7bzcT.jpg",
      "genre_ids": [
        28,
        12,
        53
      ],
      "id": 575265,
      "original_language": "en",
      "original_title": "Mission: Impossible - The Final Reckoning",
      "overview": "Ethan Hunt and the IMF team continue their search for the terrifying AI known as the Entity — which has infiltrated intelligence networks all over the globe — with the world's governments and a mysterious ghost from Ethan's past on their trail. Joined by new allies and armed with the means to shut the Entity down for good, Hunt is in a race against time to prevent the world as we know it from changing forever.",
      "popularity": 117.4008,
      "poster_path": "/z53D72EAOxGRqdr7KXXWp9dJiDe.jpg",
      "release_date": "2025-05-17",
      "title": "Mission: Impossible - The Final Reckoning",
      "video": false,
      "vote_average": 7.786,
      "vote_count": 14
    },
    {
      "adult": false,
      "backdrop_path": "/aX5xxdrmf56jaD5VWs9HCWmrPc2.jpg",
      "genre_ids": [
        27,
        53
      ],
      "id": 1092073,
      "original_language": "en",
      "original_title": "The Haunting at Saint Joseph's",
      "overview": "An engaged Muslim doctor, her fiancé, and their friends go on a holiday at St. Joseph’s Guesthouse, unaware that it was the site of a sacrifice of an innocent centuries before. They soon come to believe that it's haunted and causing them to go crazy, as their emotions spiral out of control.",
      "popularity": 115.0108,
      "poster_path": "/eDzQFxs0KTzHUPkIR0c44TSGJUR.jpg",
      "release_date": "2023-02-26",
      "title": "The Haunting at Saint Joseph's",
      "video": false,
      "vote_average": 3.8,
      "vote_count": 8
    }
  ],
  "total_pages": 50373,
  "total_results": 1007451
};
```

---

**🧠 `src/utils/movie.utils.js`**

```javascript
export const getImageUrl = (size = "w342", path) => {
  if (!path) return "https://picsum.photos/342/513?random";
  return `https://image.tmdb.org/t/p/${size}/${path}`; 
};

export const genres = {
  12: "Adventure",
  14: "Fantasy",
  28: "Action",
  35: "Comedy",
  53: "Thriller",
  80: "Crime",
  878: "Sci-Fi",
  10751: "Family",
  10752: "War",
  18: "Drama",
  9648: "Mystery",
  27: "Horror",
  10749: "Romance",
  37: "Western"
};

export const mapTmdbToMovie = (tmdbMovie) => {
  return {
    id: tmdbMovie.id,
    title: tmdbMovie.title,
    rating: Math.round(tmdbMovie.vote_average) / 2,
    genre: tmdbMovie.genre_ids.map(id => genres[id] || "Drama")[0],
    duration: "120 min",
    image: getImageUrl("w342", tmdbMovie.poster_path),
    description: tmdbMovie.overview,
    showTimes: ["2:30 PM", "5:45 PM", "9:00 PM", "11:30 PM"],
    releaseDate: tmdbMovie.release_date
  };
};

export const getMovies = (tmdbResponse) => tmdbResponse.results.map(mapTmdbToMovie);
```

✅ With this setup, your app is now equipped with realistic data and utility helpers to simulate a real-world movie listing platform. 🧠📊

---

### Step 3: Header Component I Sin E Spoiler

Build a responsive, stylish movie-themed header 🎥. Includes smooth navigation to Movies, Cinemas, AR Posters, and more! 🎞️🍿 Great for first impressions! 🚀

---

**📁 File Path**

```
src/components/layouts/Header.jsx
```

---

**✅ Features**

- Responsive container with flexbox utilities
- SVG logo for branding 🎞️
- Main navigation: Movies, Cinemas, Promotions, My Tickets, AR Posters
- Highlighted sign-in button with icon
- Semantic and accessible HTML

---

**🧩 Code**

```jsx
const Header = () => {
  return (
    <header className="header">
      <nav className="nav nav--scroll">
        <div className="container d-flex a-items-center j-content-between g-4">
          <a href="#" className="d-flex a-items-center g-2">
            <img src="/logo.svg" alt="Sin E Spoiler" width="32" height="32" />
            <strong className="c-primary">Sin E Spoiler</strong>
          </a>
          <ul className="list d-flex g-5 f-2 j-content-center">
            <li><a href="#movies" className="link interactive">Movies</a></li>
            <li><a href="#cinemas" className="link interactive">Cinemas</a></li>
            <li><a href="#promotions" className="link interactive">Promotions</a></li>
            <li><a href="#tickets" className="link interactive">My Tickets</a></li>
            <li><a href="#ar" className="link interactive">AR Posters</a></li>
          </ul>
          <div className="d-flex g-3">
            <a href="#signin" className="button button--primary interactive">🎟️ Sign In</a>
          </div>
        </div>
      </nav>
    </header>
  );
};
export default Header;
```

---

**🧠 UX Guidelines**

- Clear, visible navigation
- Prioritize booking and AR features
- Use film-inspired icons for ambiance

---

### Step 4: Footer Component I Contact & Info

Wrap up your app with a clean, informative footer ✨. Includes branding, quick links, contact info, and social media icons! 📬📍 A perfect ending! 👣

---

**📁 File Path**

```
src/components/layouts/Footer.jsx
```

---

**✅ Features**

- Responsive columns for branding, links, and social media
- Clear visual separation
- Contact and informational content

---

**🧩 Code**

```jsx
const Footer = () => {
  const currentYear = new Date().getFullYear();
  return (
    <footer className="footer">
      <div className="container g-layout g-layout--auto-fit-columns g-5">
        <div className="d-flex f-direction-column g-2">
          <a href="#"><img src="/logo.svg" alt="Sin E Spoiler Logo" className="img img--logo" /></a>
          <h2 className="interactive interactive--lg">Sin E Spoiler</h2>
          <p className="text text--xs">Enjoy spoiler-free cinema, smart reviews, and exclusive experiences.</p>
        </div>
        <div className="d-flex f-direction-column g-2">
          <h3 className="interactive interactive--lg">Showtimes</h3>
          <ul className="list d-flex f-direction-column g-1">
            <li><a href="#now-showing" className="link interactive interactive--sm">Now Showing</a></li>
            <li><a href="#coming-soon" className="link interactive interactive--sm">Coming Soon</a></li>
            <li><a href="#premieres" className="link interactive interactive--sm">Premiere Giveaways</a></li>
          </ul>
        </div>
        <div className="d-flex f-direction-column g-2">
          <h3 className="interactive interactive--lg">Explore</h3>
          <ul className="list d-flex f-direction-column g-1">
            <li><a href="#faq" className="link interactive interactive--sm">FAQs</a></li>
            <li><a href="#about" className="link interactive interactive--sm">About Us</a></li>
            <li><a href="#blog" className="link interactive interactive--sm">Cinema Blog</a></li>
          </ul>
        </div>
        <div className="d-flex f-direction-column g-2">
          <h3 className="interactive interactive--lg">Social Media</h3>
          <ul className="list d-flex f-direction-column g-1">
            <li><a href="#" className="link interactive interactive--sm">Instagram</a></li>
            <li><a href="#" className="link interactive interactive--sm">YouTube</a></li>
            <li><a href="#" className="link interactive interactive--sm">TikTok</a></li>
          </ul>
        </div>
      </div>
      <nav className="nav">
        <div className="container flexbox flexbox--centered-spacing flexbox--responsive g-2">
          <p className="interactive interactive--xs">&copy; {currentYear} Sin E Spoiler. All rights reserved.</p>
          <p className="interactive interactive--xs">Developed by <a href="https://www.instagram.com/elliotgaramendi/" className="link interactive interactive--xs">Elliot Garamendi</a></p>
        </div>
      </nav>
    </footer>
  );
};
export default Footer;
```

---

### Step 5: Hero Component I Highlight Banner

Make a cinematic entrance! 🌟 Display a bold title, a compelling description, and powerful CTAs to guide users into the experience 🎬🚪💡

---

**📁 File Path**

```
src/components/modules/Hero.jsx
```

---

**✅ Features**

- Visually impactful title
- Descriptive paragraph with CTA
- Mobile-first design

---

**🧩 Code**

```jsx
const Hero = () => {
  return (
    <article className="hero">
      <div className="container d-flex f-direction-column g-10">
        <div className="d-flex f-direction-column a-items-center g-4">
          <h1 className="hero__title t-align-center">
            Explore spoiler-free cinema with <span className="c-primary">AI reviews</span>
          </h1>
          <p className="hero__paragraph t-align-center">
            Your movie app with advanced features, premieres, and interactive AR experiences.
          </p>
          <a href="#now-showing" className="button button--primary interactive interactive--xl">
            🎬 Browse Movies
          </a>
        </div>
      </div>
    </article>
  );
};
export default Hero;
```

---

### Step 6: Rating Component I Score

Visualize AI-powered ratings with beautiful stars 🌠 – full, half, and empty. Show clean decimal values for sharp movie impressions! 📈🔍

---

**📁 File Path**

```
src/components/widgets/Rating.jsx
```

---

**✅ Features**

- Full, half, and empty star rendering
- Formatted decimal score display
- Ideal for AI-generated reviews

---

**🧩 Code**

```jsx
const Rating = ({ value, maxValue = 5 }) => {
  const fullStars = Math.floor(value);
  const hasHalfStar = value % 1 !== 0;
  const emptyStars = maxValue - Math.ceil(value);

  return (
    <div className="rating d-flex a-items-center g-1">
      {[...Array(fullStars)].map((_, i) => (
        <span key={`full-${i}`} className="rating__star">★</span>
      ))}
      {hasHalfStar && <span className="rating__star rating__star--half">★</span>}
      {[...Array(emptyStars)].map((_, i) => (
        <span key={`empty-${i}`} className="rating__star rating__star--empty">☆</span>
      ))}
      <span className="rating__value">{value.toFixed(1)}</span>
    </div>
  );
};
export default Rating;
```

---

**🧠 UX Guidelines**

- Place ratings near titles or cards
- Use subtle animation or color highlight
- Always show decimal value for clarity

---

### Step 7: MovieCard Component I Card Display

Every movie deserves a spotlight 🎞️. This card shows title, poster, genre badge, rating, short description, and showtimes – all in one elegant frame 🍿🕓

---

**📁 File Path**

```
src/components/widgets/MovieCard.jsx
```

---

**✅ Features**

- Displays movie poster, genre badge, and metadata
- Uses reusable `<Rating />` component
- Showtimes with accessible buttons
- Optimized image with lazy loading

---

**🧩 Code**

```jsx
import Rating from './Rating';

const MovieCard = ({ movie }) => {
  const { title, rating, genre, duration, image, description, showTimes } = movie;
  
  return (
    <article className="card card--movie">
      <div className="card__header">
        <img 
          src={image} 
          alt={`${title} poster`}
          className="card__image"
          loading="lazy"
        />
        <div className="card__overlay">
          <span className="badge badge--primary">{genre}</span>
        </div>
      </div>
      
      <div className="card__body">
        <h3 className="card__title">{title}</h3>
        <div className="card__meta d-flex g-2">
          <Rating value={rating} />
          <span className="card__duration">{duration}</span>
        </div>
        
        <p className="card__description">{description}</p>
        
        <div className="card__showtimes">
          <h4 className="card__subtitle">Today's Showtimes</h4>
          <div className="d-flex f-wrap g-2">
            {showTimes.map((time, index) => (
              <button 
                key={index}
                className="button button--time"
                aria-label={`Show time ${time} for ${title}`}
              >
                {time}
              </button>
            ))}
          </div>
        </div>
      </div>
    </article>
  );
};

export default MovieCard;
```

---

**🧠 UX Guidelines**

- Show key movie data at a glance
- Limit description to ~2 lines for visual balance
- Ensure touch targets are accessible

---

### Step 8: MovieList Component I Grid Section

Display your movie collection in a responsive grid layout 🧩📽️. Dynamically renders each <MovieCard /> and keeps everything well-aligned 🎯🎞️

---

**📁 File Path**

```
src/components/modules/MovieList.jsx
```

---

**✅ Features**

- Responsive section with title
- Renders a grid of `<MovieCard />` components
- Movie list dynamically populated

---

**🧩 Code**

```jsx
import MovieCard from '../widgets/MovieCard';

const MovieList = ({ movies }) => {
  return (
    <section id="movies" className="section section--movies">
      <div className="container">
        <h2 className="section__title">Now Showing</h2>
        
        <div className="g-layout g-layout--auto-fit-columns">
          {movies.map(movie => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default MovieList;
```

---

**🧠 UX Guidelines**

- Maintain uniform spacing in grid
- Prioritize top-rated or newest movies
- Anchor ID `#movies` for navigation

---

### Step 9: App Component I App Orchestrator

The brain of your application 🧠. Composes the full layout with <Header />, <Hero />, <MovieList />, and <Footer /> in perfect order 🎬🛠️

---

**📁 File Path**

```
src/App.jsx
```

---

**✅ Features**

- Imports layout and modules
- Loads movies from data utils
- Central point for rendering the app

---

**🧩 Code**

```jsx
import Header from './components/layouts/Header';
import Hero from './components/modules/Hero';
import MovieList from './components/modules/MovieList';
import Footer from './components/layouts/Footer';
import { getMovies } from './data/movie.utils';

const App = () => {
  const movies = getMovies();

  return (
    <>
      <Header />
      <main className="main">
        <Hero />
        <MovieList movies={movies} />
      </main>
      <Footer />
    </>
  );
};

export default App;
```

---

**🧠 UX Guidelines**

- Place `<main>` between `<Header />` and `<Footer />`
- Load realistic data via `getMovies()`
- Wrap components in React Fragment

---

### Step 10: Entry Point I App Bootstrap

The launchpad for your React app! 🎯 Uses createRoot with StrictMode, loads global styles, and mounts the app into #root. Ready for takeoff! 🛸💻

---

**📁 File Path**

```
src/main.jsx
```

---

**✅ Features**

- Entry point with React 19 `createRoot`
- Uses `StrictMode` for dev best practices
- Imports global styles

---

**🧩 Code**

```jsx
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';
import './css/index.css';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
```

---

**🧠 UX Guidelines**

- Use `StrictMode` to catch issues early
- Keep this file minimal and clean
- Ensure `index.html` has a `#root` div

---

## 4. Running the Application

---

**📁 File Path**

```
/
```

---

**✅ Features**

* Launch app using Vite development server
* Verify all components render correctly
* Inspect with React DevTools

---

**🥉 Commands**

```bash
# Start the development server
npm run dev

# Open browser at:
http://localhost:5173
```

---

**📊 Checklist**

* [x] Header navigation is visible and fixed
* [x] Hero section displays with gradient background
* [x] Movie cards render with data (e.g. 8 cards)
* [x] Star ratings show correctly
* [x] Footer content and links present
* [x] Fully responsive design

---

**🔍 React DevTools**

1. Install the React Developer Tools browser extension
2. Open browser DevTools (`F12`)
3. Use the "Components" tab to explore structure

```
┌──────────────────────────────────────┐
│  React DevTools - Components         │
├──────────────────────────────────────┤
│  ▼ App                               │
│    ▼ Header                          │
│    ▼ Hero                            │
│    ▼ MovieList                       │
│      ▼ MovieCard                     │
│        ▼ Rating                      │
│    ▼ Footer                          │
└──────────────────────────────────────┘
```

---

## 5. Next Steps

---

**✨ 5 Challenges to Level Up**

**1. Genre Filter Component** 🎭

```jsx
const GenreFilter = ({ genres, activeGenre, onGenreChange }) => (
  <div className="genre-filter d-flex g-2">
    <button className={`button ${!activeGenre ? 'button--primary' : ''}`} onClick={() => onGenreChange(null)}>
      All
    </button>
    {genres.map(genre => (
      <button
        key={genre}
        className={`button ${activeGenre === genre ? 'button--primary' : ''}`}
        onClick={() => onGenreChange(genre)}>
        {genre}
      </button>
    ))}
  </div>
);
```

**2. Featured Movie Component** 🌟

```jsx
const FeaturedMovie = ({ movie }) => (
  <div className="featured-movie">
    <div className="featured-movie__backdrop">
      <img src={getImageUrl(movie.backdrop_path, 'w1280')} alt={movie.title} className="img img--background" />
    </div>
    <div className="featured-movie__content container">
      <h2 className="title">{movie.title}</h2>
      <p className="text">{movie.overview}</p>
      <button className="button button--primary">Book Now</button>
    </div>
  </div>
);
```

**3. Movie Search Component** 🔍

```jsx
const MovieSearch = ({ onSearch }) => (
  <div className="movie-search">
    <input
      type="text"
      placeholder="Search movies..."
      className="form__input"
      onChange={(e) => onSearch(e.target.value)}
    />
    <button className="button button--primary">Search</button>
  </div>
);
```

**4. Promo Banner Component** 🎫

```jsx
const PromoBanner = ({ promo }) => (
  <div className="promo-banner">
    <div className="promo-banner__content">
      <h3 className="title--xs">{promo.title}</h3>
      <p className="text--sm">{promo.description}</p>
      <span className="badge badge--primary">{promo.code}</span>
    </div>
    <img src={promo.image} alt={promo.title} className="promo-banner__image" />
  </div>
);
```

**5. Coming Soon Section** 🎬

```jsx
const ComingSoon = ({ upcomingMovies }) => (
  <section className="section">
    <div className="container">
      <h2 className="section__title">Coming Soon</h2>
      <div className="g-layout g-layout--auto-fit-columns">
        {upcomingMovies.map(movie => (
          <div key={movie.id} className="coming-soon__item">
            <img src={movie.image} alt={movie.title} className="coming-soon__image" />
            <h3 className="title--xs">{movie.title}</h3>
            <p className="text--sm">Release: {new Date(movie.releaseDate).toLocaleDateString()}</p>
          </div>
        ))}
      </div>
    </div>
  </section>
);
```

---

### Best Practices

**Component Organization**

```jsx
// ✅ Good
const MovieTitle = ({ title }) => <h3 className="card__title">{title}</h3>;

// ❌ Avoid combining too much logic
const MovieEverything = ({ movie }) => { /* too much responsibility */ };
```

**Data Management**

```jsx
import { getMovies } from '../data/movies';

const formatted = movies.map(movie => ({
  ...movie,
  formattedDate: new Date(movie.releaseDate).toLocaleDateString()
}));
```

**CSS Structure**

* Follow BEM naming convention
* Use modular styles
* Rely on CSS variables for theming
* Prioritize mobile-first responsive design

---

### Resources

**React Docs**:

* [https://react.dev/](https://react.dev/)
* [https://react.dev/blog](https://react.dev/blog)
* [https://react.dev/learn/writing-markup-with-jsx](https://react.dev/learn/writing-markup-with-jsx)

**TMDB Docs**:

* [https://developers.themoviedb.org/3](https://developers.themoviedb.org/3)
* [https://developers.themoviedb.org/3/configuration](https://developers.themoviedb.org/3/configuration)

**CSS References**:

* [https://getbem.com/](https://getbem.com/)
* [https://developer.mozilla.org/en-US/docs/Web/CSS/Using\_CSS\_custom\_properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

---

### Congratulations!

You've completed your first full-stack-ready **React Cinema App** with:

* ✅ Modern React 19 syntax
* ✅ JSX and component composition
* ✅ TMDB movie data
* ✅ Modular CSS with BEM
* ✅ Reusable, scalable components

---

### Week 10 Preview

> Learn about React **state management**, **event handling**, and dynamic UI updates!
> Build forms, filters, and interactive features to power up your app even more!

🚀 Keep building. You're on fire! 🔥
