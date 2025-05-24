## 🗓️ Curso: React Developer Pro – De Cero a Producción

---

### 🔹 Semana 9: Introducción a React 🚀🧠💡💻

**Tema principal:** React como ecosistema declarativo moderno

#### 🧩 Temas:

* ❓ ¿Qué es React? ¿Por qué es declarativo?
* ⚙️ Setup del proyecto con **Vite + JSX**
* 🗂️ Configuración inicial del `index.html`: `<title>`, favicon, estructura mínima
* ✨ JSX básico: interpolaciones, atributos, expresiones
* 🧱 Functional components simples
* 📦 Props básicas

#### 🌐 Temas transversales:

* 🛡️ **Seguridad:** Sanitización de datos con `{safeString}`
* ♿ **Accesibilidad inicial:** etiquetas HTML5 mínimas (`<main>`, `<header>`)
* 🎯 **Buenas prácticas:** estructura limpia desde el inicio
* 🧠 **Arquitectura:** estructura base del proyecto por convenciones
* 📐 **Design Patterns:** enfoque declarativo desde el comienzo

#### 🔧 Reto:

* Crear `Header`, `HeroBanner` y `MovieTeaser` con datos hardcodeados

---

### 🔹 Semana 10: Componentes, Props, Hooks y Eventos 🧩⚡📦🔁

**Tema principal:** Interactividad, composición y lógica interna

#### 🧩 Temas:

* 🧱 Componentes reutilizables con props dinámicas
* 📦 Props anidadas, destructuring y defaults
* ⚡ `useState` y `useEffect` como hooks esenciales
* 🔁 Renderizado condicional (`&&`, ternarios, fallback)
* 🗃️ Renderizado de listas (`.map`, keys, index)

#### 🌐 Temas transversales:

* ♿ **Accesibilidad:** navegación por teclado, uso correcto de roles y focus
* 🎯 **Buenas prácticas:** separación UI/lógica, función pura y simple
* 🛡️ **Seguridad:** validación manual y control de eventos inseguros
* 📐 **Design Patterns:** presentación vs contenedor, separación por responsabilidad

#### 🔧 Reto:

* Galería de películas con favoritos (toggle visual)
* Formulario de búsqueda funcional con validación y feedback visual accesible

---

### 🔹 Semana 11: Custom Hooks, Librerías Esenciales y UI 🪝📚🎨🧠

**Tema principal:** Modularidad, lógica compartida y sistema visual escalable

#### 🧩 Temas:

* 🪝 `useEffect` en lógica compartida (loading, timeout, scroll)
* 🧠 Creación de custom hooks reutilizables (`useTheme`, `useDebounce`, `useLocalStorage`)
* 🎨 Estilos con Tailwind CSS y CSS Modules
* 📚 Librerías esenciales para UI y productividad:

  * 📡 Axios (API client)
  * 📋 React Hook Form (manejo y validación de formularios)
  * 🎛️ classnames (utilidad condicional de clases)
  * 🖼️ react-icons (íconos populares)
  * 🎠 keen-slider (sliders responsivos)
  * 💬 react-toastify (notificaciones)
  * 🧩 react-loading-skeleton (placeholders visuales)

#### 🌐 Temas transversales:

* 📐 **Design Patterns:** separación de lógica en hooks para mayor escalabilidad
* ♿ **Accesibilidad:** formularios accesibles y retroalimentación clara
* 🎯 **Buenas prácticas:** creación de hooks genéricos y desacoplados
* 🛡️ **Seguridad:** validación de datos, control de inputs, prevención de mal uso de efectos
* 🧠 **Arquitectura:** archivos organizados por propósito (hooks, styles, lib)

#### 🔧 Reto:

* Desarrollar una sección de “Estrenos” con:

  * Custom hook `usePremieres` con fetch y control de loading
  * Slider visual accesible con foco por teclado
  * Estilo adaptable con Tailwind + módulos
  * Toast al seleccionar favorito + validación en formulario simple

---

### 🔹 Semana 12: Routing, Estado Global, Fetching y Frameworks UI 🔄🧭📡📁

**Tema principal:** Navegación, datos en tiempo real y frameworks escalables

#### 🧩 Temas:

* 🧭 React Router: rutas públicas, privadas y dinámicas (`/movies/:slug`)
* 🌍 Zustand: creación de múltiples stores (usuario, carrito, tema)
* 📡 TanStack Query: caching, retries, invalidaciones, paginación
* 🧩 UI Framework: integración con Shadcn UI y Tailwind
* 🦴 Skeletons loaders + fallback visuales con Suspense

#### 🌐 Temas transversales:

* 📐 **Arquitectura:** organización modular por features
* 🛡️ **Seguridad:** protección de rutas, API keys en `.env`
* ♿ **Accesibilidad:** estructura semántica, navegación y roles claros
* 🎯 **Buenas prácticas:** separación visual/lógica y carga eficiente
* 📐 **Design Patterns:** manejo por layout + store encapsulado

#### 🔧 Reto:

* Página `/movies` con loading inteligente (skeletons), cards desde API TMDB y detalle con routing dinámico

---

### 🔹 Semana 13: Autenticación, Seguridad y Testing 🔐🧪🧠🌍

**Tema principal:** Protección de rutas, gestión de usuarios y pruebas de confianza

#### 🧩 Temas:

* 🔐 Login/Register con React Hook Form + validación + toast
* 🔑 Rutas privadas con Zustand + persistencia de sesión
* 🔏 Encriptación de información sensible en localStorage
* 🧪 Testing con React Testing Library y Playwright (UI, flows, accesibilidad)
* 🛡️ Prevención de XSS, validación agresiva y headers seguros

#### 🌐 Temas transversales:

* ♿ **Accesibilidad:** flujos accesibles con inputs y navegación por teclado
* 📐 **Design Patterns:** validadores externos, encapsulación de sesión
* 🧠 **Arquitectura:** sesión centralizada y reusable por contexto/store
* 🎯 **Buenas prácticas:** testing modular desde hooks hasta vistas
* 🛡️ **Seguridad:** enfoque full-stack en validación, control y persistencia

#### 🔧 Reto:

* Autenticación completa con feedback visual + test e2e de login/logout + encriptación simulada en datos del usuario

---

### 🔹 Semana 14: Integración de APIs de Inteligencia Artificial 🤖🧠✨🔮

**Tema principal:** Contenido dinámico y enriquecido con generación automática

#### 🧩 Temas:

* 🔮 OpenAI API: reseñas sin spoilers con `useAIGeneratedReview`
* 🧠 Hooks con lógica asíncrona avanzada y manejo de errores
* ✨ Render dinámico con `dangerouslySetInnerHTML` seguro
* 📣 `aria-live`, animaciones y UX generativo accesible

#### 🌐 Temas transversales:

* 🛡️ **Seguridad:** sanitizar resultados, controlar HTML remoto
* 📐 **Arquitectura:** integración externa desacoplada en servicios
* 🎯 **Buenas prácticas:** patrón efecto-control-render
* ♿ **Accesibilidad:** lectura dinámica de contenido generado
* 📐 **Design Patterns:** custom hook como fachada para AI

#### 🔧 Reto:

* Reseña generada por IA en detalle de película con render semántico, respuesta accesible y fallback visual

### 🔹 Semana 15: Pasarela de Pagos, SEO y Deploy 💳🌐🚀⚙️

**Tema principal:** Aplicación lista para producción con visibilidad y protección real

#### 🧩 Temas:

* 💳 Stripe/MercadoPago: integración test mode, validación y tokens
* 🌐 SEO para SPA: metadata dinámica con Helmet, Open Graph, estructura semántica
* 🚀 Deploy en Vercel/Render: variables `.env`, build optimizado y rutas limpias
* ⚙️ Seguridad avanzada en producción: headers (CSP, X-Frame-Options, STS)
* 🔀 Versionado y despliegue continuo básico (preview envs en Vercel)

#### 🌐 Temas transversales:

* 🛡️ **Seguridad:** en headers, en la pasarela, en persistencia y almacenamiento
* 📐 **Arquitectura:** entorno de producción, estructura lista para CI/CD
* ♿ **Accesibilidad:** contenido correctamente etiquetado para SEO semántico
* 🎯 **Buenas prácticas:** separación de claves, carga optimizada, logs controlados
* 📐 **Design Patterns:** `envAdapter`, layout SEO reusable, wrappers de configuración

#### 🔧 Reto:

* Implementar pasarela de pagos simulada + deploy en Vercel + validación con helmet y headers custom

---

### 🔹 Semana 16: Siguientes Pasos Profesionales 🧠⚙️🧪📈

**Tema principal:** Convertirte en un Frontend Architect moderno y competitivo

#### 🧩 Temas:

* 🏗️ Arquitectura avanzada:

  * Mono-repo, estructura atómica por dominio, microfrontends (introductorio)
* 🎭 Rendering & performance:

  * `React.memo`, `useMemo`, `useCallback`, Suspense avanzado, carga progresiva
* 🧪 Testing de alto nivel:

  * Snapshot testing, mocks avanzados, integración en CI/CD
* ✍️ Extensiones y herramientas:

  * TypeScript básico (tipado de props, interfaces simples)
  * Animaciones con Framer Motion
  * Introducción real a React Native (arquitectura común, diferencias clave)

#### 🌐 Temas transversales:

* 📐 **Design Patterns:** Observer, Facade, Strategy, Adapter, Command, Decorator, Factory, Reducer (repaso aplicado)
* 🧠 **Arquitectura:** modelos escalables para apps de equipos grandes
* ♿ **Accesibilidad:** testing automatizado + axe-core
* 🛡️ **Seguridad:** revisiones automáticas, manejo de errores y límites
* 🎯 **Buenas prácticas:** DevX, monitoreo, clean code + CLI linting

#### 🔧 Reto:

* Migrar una sección del proyecto a TypeScript + snapshot test + animación con Framer Motion + mini presentación final del proyecto
