# **🟨 Examen de Fundamentos de JavaScript - Variables, Estructuras de Control y Funciones 💻✨**

Este examen está diseñado para evaluar tus conocimientos esenciales en programación con JavaScript. A través de cuatro secciones temáticas, practicarás variables y tipos de datos, estructuras condicionales, bucles y funciones básicas. Cada reto te ayudará a aplicar conceptos fundamentales mediante ejercicios prácticos y situaciones cotidianas. Los casos de prueba automatizados te permitirán verificar que tu código funciona correctamente al instante ✅. ¡Demuestra tu dominio de JavaScript paso a paso! 🎯⚡✨

---

## 🎯 o1 Variables, Tipos de Datos y Estructuras Básicas - Fundamentos de JavaScript 📦🔤

⚙️ En esta sección aprenderás a trabajar con variables, diferentes tipos de datos (números, strings, booleans, arrays) y operaciones básicas en JavaScript. Usarás `let`, `const` y `var` para declarar variables, y aprenderás a manipular datos básicos que son la base de cualquier programa 🧩🔍.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `console.log(true)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### Reto o1.1: Calculadora de Información Personal 👤🧮

**Problema**: Crea variables para almacenar información personal y realiza cálculos básicos con ellas 🎯📊

**Descripción**: JavaScript usa diferentes tipos de datos para almacenar información. En este ejercicio trabajarás con strings (texto), numbers (números) y booleans (verdadero/falso), y aprenderás a combinarlos para crear información útil.

🏷️ **Tipos de datos básicos**:

```javascript
let nombre = "Juan";        // String
let edad = 25;              // Number
let estudiante = true;      // Boolean
```

Tu programa debe:

* 📝 Crear variables para nombre, edad y si es estudiante
* 🎂 Calcular el año de nacimiento
* 💬 Crear un mensaje de presentación
* ✅ Determinar si es mayor de edad

**Casos de prueba**:

1. Entrada ➡️ nombre="Ana", edad=20, estudiante=true → nacimiento=2005, mayorEdad=true
2. Entrada ➡️ nombre="Carlos", edad=17, estudiante=false → nacimiento=2008, mayorEdad=false
3. Entrada ➡️ nombre="María", edad=25, estudiante=true → nacimiento=2000, mayorEdad=true
4. Entrada ➡️ nombre="Luis", edad=16, estudiante=true → nacimiento=2009, mayorEdad=false
5. Entrada ➡️ nombre="Elena", edad=30, estudiante=false → nacimiento=1995, mayorEdad=true

**Código base**:

```javascript
// Reto 1: Calculadora de Información Personal 👤🧮
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function personalInfo(name, age, isStudent) {
    // Tu solución aquí 🛠️
    let birthYear = 0;          // Esta variable debe calcularse
    let isAdult = false;        // Esta variable debe calcularse
    let message = "";           // Esta variable debe calcularse
    
    return { birthYear, isAdult, message };
}

function test_o1_1() {
    // o1.1.1: Ana, 20, estudiante
    let result1 = personalInfo("Ana", 20, true);
    recordTest("o1.1.1 Ana data", result1.birthYear === 2005 && result1.isAdult === true);
    
    // o1.1.2: Carlos, 17, no estudiante
    let result2 = personalInfo("Carlos", 17, false);
    recordTest("o1.1.2 Carlos data", result2.birthYear === 2008 && result2.isAdult === false);
    
    // o1.1.3: María, 25, estudiante
    let result3 = personalInfo("María", 25, true);
    recordTest("o1.1.3 María data", result3.birthYear === 2000 && result3.isAdult === true);
    
    // o1.1.4: Luis, 16, estudiante
    let result4 = personalInfo("Luis", 16, true);
    recordTest("o1.1.4 Luis data", result4.birthYear === 2009 && result4.isAdult === false);
    
    // o1.1.5: Elena, 30, no estudiante
    let result5 = personalInfo("Elena", 30, false);
    recordTest("o1.1.5 Elena data", result5.birthYear === 1995 && result5.isAdult === true);
}

// 🚀 Run tests
test_o1_1();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🎂 Calcula el año de nacimiento: `2025 - edad`
* ✅ Determina si es mayor de edad: `edad >= 18`
* 💬 Crea mensaje combinando strings: `"Hola, soy " + nombre`
* 📊 Usa operadores de comparación y aritméticos

👤 ¡Crea perfiles de usuarios con datos! 📋✨

---

### Reto o1.2: Manipulador de Arrays Básico 📚🔢

**Problema**: Trabaja con arrays (listas) para almacenar y manipular colecciones de datos usando métodos básicos 🎯📊

**Descripción**: Los arrays son estructuras de datos que permiten almacenar múltiples valores en una sola variable. En JavaScript, los arrays tienen métodos útiles como `push()`, `length`, y puedes acceder a elementos usando índices.

📚 **Operaciones básicas con arrays**:

```javascript
let numeros = [1, 2, 3];
numeros.push(4);              // Agregar elemento
let longitud = numeros.length; // Obtener longitud
let primero = numeros[0];     // Acceder por índice
```

Tu programa debe:

* 📚 Crear un array con números iniciales
* ➕ Agregar nuevos números al array
* 📏 Calcular la longitud del array
* 🔍 Encontrar el primer y último elemento

**Casos de prueba**:

1. Entrada ➡️ inicial=[1,2,3], agregar=[4,5] → longitud=5, primero=1, ultimo=5
2. Entrada ➡️ inicial=[10,20], agregar=[30,40,50] → longitud=5, primero=10, ultimo=50
3. Entrada ➡️ inicial=[7], agregar=[8,9,10] → longitud=4, primero=7, ultimo=10
4. Entrada ➡️ inicial=[100,200,300], agregar=[400] → longitud=4, primero=100, ultimo=400
5. Entrada ➡️ inicial=[5,15,25], agregar=[35,45] → longitud=5, primero=5, ultimo=45

**Código base**:

```javascript
// Reto 2: Manipulador de Arrays Básico 📚🔢
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function arrayManipulator(initialArray, numbersToAdd) {
    // Tu solución aquí 🛠️
    let resultArray = [];       // Esta variable debe calcularse
    let arrayLength = 0;        // Esta variable debe calcularse
    let firstElement = 0;       // Esta variable debe calcularse
    let lastElement = 0;        // Esta variable debe calcularse
    
    return { resultArray, arrayLength, firstElement, lastElement };
}

function test_o1_2() {
    // o1.2.1: [1,2,3] + [4,5]
    let result1 = arrayManipulator([1,2,3], [4,5]);
    recordTest("o1.2.1 array ops", result1.arrayLength === 5 && result1.firstElement === 1 && result1.lastElement === 5);
    
    // o1.2.2: [10,20] + [30,40,50]
    let result2 = arrayManipulator([10,20], [30,40,50]);
    recordTest("o1.2.2 array ops", result2.arrayLength === 5 && result2.firstElement === 10 && result2.lastElement === 50);
    
    // o1.2.3: [7] + [8,9,10]
    let result3 = arrayManipulator([7], [8,9,10]);
    recordTest("o1.2.3 array ops", result3.arrayLength === 4 && result3.firstElement === 7 && result3.lastElement === 10);
    
    // o1.2.4: [100,200,300] + [400]
    let result4 = arrayManipulator([100,200,300], [400]);
    recordTest("o1.2.4 array ops", result4.arrayLength === 4 && result4.firstElement === 100 && result4.lastElement === 400);
    
    // o1.2.5: [5,15,25] + [35,45]
    let result5 = arrayManipulator([5,15,25], [35,45]);
    recordTest("o1.2.5 array ops", result5.arrayLength === 5 && result5.firstElement === 5 && result5.lastElement === 45);
}

// 🚀 Run tests
test_o1_2();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 📚 Usa `[...array1, ...array2]` o `concat()` para combinar arrays
* ➕ Usa `push()` para agregar elementos uno por uno
* 📏 Usa `.length` para obtener la longitud
* 🔍 Accede con `array[0]` y `array[array.length - 1]`

📚 ¡Organiza datos como un bibliotecario! 📖✨

---

### Reto o1.3: Calculadora de Strings 📝🔤

**Problema**: Manipula strings (cadenas de texto) usando métodos básicos como longitud, mayúsculas, minúsculas y concatenación 🎯✂️

**Descripción**: Los strings en JavaScript tienen muchos métodos útiles para manipular texto. Puedes cambiar el caso, obtener la longitud, extraer partes del texto y combinar múltiples strings.

📝 **Métodos básicos de strings**:

```javascript
let texto = "Hola Mundo";
texto.length;              // Longitud
texto.toUpperCase();       // Mayúsculas
texto.toLowerCase();       // Minúsculas
texto.slice(0, 4);         // Extraer parte
```

Tu programa debe:

* 📏 Calcular la longitud de un string
* 🔤 Convertir a mayúsculas y minúsculas
* ✂️ Extraer las primeras 3 letras
* 🔗 Concatenar con otro string

**Casos de prueba**:

1. Entrada ➡️ texto="JavaScript", sufijo=" es genial" → longitud=10, mayus="JAVASCRIPT", primeras3="JAV"
2. Entrada ➡️ texto="Programar", sufijo=" es divertido" → longitud=9, mayus="PROGRAMAR", primeras3="PRO"
3. Entrada ➡️ texto="Codigo", sufijo=" limpio" → longitud=6, mayus="CODIGO", primeras3="COD"
4. Entrada ➡️ texto="Datos", sufijo=" importantes" → longitud=5, mayus="DATOS", primeras3="DAT"
5. Entrada ➡️ texto="Web", sufijo=" desarrollo" → longitud=3, mayus="WEB", primeras3="WEB"

**Código base**:

```javascript
// Reto 3: Calculadora de Strings 📝🔤
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function stringCalculator(text, suffix) {
    // Tu solución aquí 🛠️
    let textLength = 0;         // Esta variable debe calcularse
    let upperText = "";         // Esta variable debe calcularse
    let lowerText = "";         // Esta variable debe calcularse
    let firstThree = "";        // Esta variable debe calcularse
    let concatenated = "";      // Esta variable debe calcularse
    
    return { textLength, upperText, lowerText, firstThree, concatenated };
}

function test_o1_3() {
    // o1.3.1: "JavaScript" + " es genial"
    let result1 = stringCalculator("JavaScript", " es genial");
    recordTest("o1.3.1 string ops", result1.textLength === 10 && result1.upperText === "JAVASCRIPT" && result1.firstThree === "Jav");
    
    // o1.3.2: "Programar" + " es divertido"
    let result2 = stringCalculator("Programar", " es divertido");
    recordTest("o1.3.2 string ops", result2.textLength === 9 && result2.upperText === "PROGRAMAR" && result2.firstThree === "Pro");
    
    // o1.3.3: "Codigo" + " limpio"
    let result3 = stringCalculator("Codigo", " limpio");
    recordTest("o1.3.3 string ops", result3.textLength === 6 && result3.upperText === "CODIGO" && result3.firstThree === "Cod");
    
    // o1.3.4: "Datos" + " importantes"
    let result4 = stringCalculator("Datos", " importantes");
    recordTest("o1.3.4 string ops", result4.textLength === 5 && result4.upperText === "DATOS" && result4.firstThree === "Dat");
    
    // o1.3.5: "Web" + " desarrollo"
    let result5 = stringCalculator("Web", " desarrollo");
    recordTest("o1.3.5 string ops", result5.textLength === 3 && result5.upperText === "WEB" && result5.firstThree === "Web");
}

// 🚀 Run tests
test_o1_3();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 📏 Usa `.length` para obtener la longitud
* 🔤 Usa `.toUpperCase()` y `.toLowerCase()`
* ✂️ Usa `.slice(0, 3)` para las primeras 3 letras
* 🔗 Usa el operador `+` para concatenar

📝 ¡Manipula texto como un editor profesional! ✏️✨

---

### Reto o1.4: Comparador de Números 🔢⚖️

**Problema**: Usa operadores de comparación para analizar relaciones entre números y crear reportes booleanos 🎯📊

**Descripción**: Los operadores de comparación (`>`, `<`, `>=`, `<=`, `===`, `!==`) son fundamentales para tomar decisiones en programación. Te permiten comparar valores y obtener resultados verdaderos o falsos.

⚖️ **Operadores de comparación**:

```javascript
let a = 10, b = 5;
a > b;      // true
a === b;    // false
a >= 10;    // true
a !== b;    // true
```

Tu programa debe:

* 🔢 Comparar dos números con diferentes operadores
* ✅ Determinar si son iguales, diferentes, mayor, menor
* 📊 Crear un reporte completo de comparaciones
* 🎯 Retornar múltiples resultados booleanos

**Casos de prueba**:

1. Entrada ➡️ num1=10, num2=5 → mayor=true, menor=false, igual=false, diferente=true
2. Entrada ➡️ num1=7, num2=7 → mayor=false, menor=false, igual=true, diferente=false
3. Entrada ➡️ num1=3, num2=8 → mayor=false, menor=true, igual=false, diferente=true
4. Entrada ➡️ num1=15, num2=12 → mayor=true, menor=false, igual=false, diferente=true
5. Entrada ➡️ num1=20, num2=20 → mayor=false, menor=false, igual=true, diferente=false

**Código base**:

```javascript
// Reto 4: Comparador de Números 🔢⚖️
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function numberComparator(num1, num2) {
    // Tu solución aquí 🛠️
    let isGreater = false;      // Esta variable debe calcularse
    let isLess = false;         // Esta variable debe calcularse
    let isEqual = false;        // Esta variable debe calcularse
    let isDifferent = false;    // Esta variable debe calcularse
    
    return { isGreater, isLess, isEqual, isDifferent };
}

function test_o1_4() {
    // o1.4.1: 10 vs 5
    let result1 = numberComparator(10, 5);
    recordTest("o1.4.1 comparisons", result1.isGreater === true && result1.isLess === false && result1.isEqual === false && result1.isDifferent === true);
    
    // o1.4.2: 7 vs 7
    let result2 = numberComparator(7, 7);
    recordTest("o1.4.2 comparisons", result2.isGreater === false && result2.isLess === false && result2.isEqual === true && result2.isDifferent === false);
    
    // o1.4.3: 3 vs 8
    let result3 = numberComparator(3, 8);
    recordTest("o1.4.3 comparisons", result3.isGreater === false && result3.isLess === true && result3.isEqual === false && result3.isDifferent === true);
    
    // o1.4.4: 15 vs 12
    let result4 = numberComparator(15, 12);
    recordTest("o1.4.4 comparisons", result4.isGreater === true && result4.isLess === false && result4.isEqual === false && result4.isDifferent === true);
    
    // o1.4.5: 20 vs 20
    let result5 = numberComparator(20, 20);
    recordTest("o1.4.5 comparisons", result5.isGreater === false && result5.isLess === false && result5.isEqual === true && result5.isDifferent === false);
}

// 🚀 Run tests
test_o1_4();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🔢 Usa `num1 > num2` para mayor
* 📊 Usa `num1 < num2` para menor
* ✅ Usa `num1 === num2` para igualdad exacta
* ❌ Usa `num1 !== num2` para diferencia

⚖️ ¡Compara como un juez matemático! 🏛️✨

---

### Reto o1.5: Analizador de Objetos Básico 📦🔍

**Problema**: Crea y manipula objetos JavaScript básicos para almacenar información estructurada usando propiedades 🎯📋

**Descripción**: Los objetos en JavaScript permiten agrupar datos relacionados usando propiedades. Puedes acceder a las propiedades usando notación de punto o corchetes, y agregar nuevas propiedades dinámicamente.

📦 **Sintaxis básica de objetos**:

```javascript
let persona = {
    nombre: "Juan",
    edad: 25,
    activo: true
};
persona.nombre;           // Acceso con punto
persona["edad"];          // Acceso con corchetes
persona.ciudad = "Madrid"; // Agregar propiedad
```

Tu programa debe:

* 📦 Crear un objeto con información de producto
* 🔍 Acceder a propiedades específicas
* ➕ Agregar nuevas propiedades
* 📊 Contar el número total de propiedades

**Casos de prueba**:

1. Entrada ➡️ producto={nombre:"Laptop", precio:1000, stock:5} → nombre="Laptop", numPropiedades=4
2. Entrada ➡️ producto={nombre:"Mouse", precio:25, stock:50} → nombre="Mouse", numPropiedades=4
3. Entrada ➡️ producto={nombre:"Teclado", precio:75, stock:20} → nombre="Teclado", numPropiedades=4
4. Entrada ➡️ producto={nombre:"Monitor", precio:300, stock:8} → nombre="Monitor", numPropiedades=4
5. Entrada ➡️ producto={nombre:"Webcam", precio:80, stock:15} → nombre="Webcam", numPropiedades=4

**Código base**:

```javascript
// Reto 5: Analizador de Objetos Básico 📦🔍
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function objectAnalyzer(productData) {
    // Tu solución aquí 🛠️
    let productObject = {};     // Esta variable debe calcularse
    let productName = "";       // Esta variable debe calcularse
    let totalPrice = 0;         // Esta variable debe calcularse
    let propertyCount = 0;      // Esta variable debe calcularse
    
    return { productObject, productName, totalPrice, propertyCount };
}

function test_o1_5() {
    // o1.5.1: Laptop data
    let result1 = objectAnalyzer({nombre: "Laptop", precio: 1000, stock: 5});
    recordTest("o1.5.1 object ops", result1.productName === "Laptop" && result1.propertyCount === 4);
    
    // o1.5.2: Mouse data
    let result2 = objectAnalyzer({nombre: "Mouse", precio: 25, stock: 50});
    recordTest("o1.5.2 object ops", result2.productName === "Mouse" && result2.propertyCount === 4);
    
    // o1.5.3: Teclado data
    let result3 = objectAnalyzer({nombre: "Teclado", precio: 75, stock: 20});
    recordTest("o1.5.3 object ops", result3.productName === "Teclado" && result3.propertyCount === 4);
    
    // o1.5.4: Monitor data
    let result4 = objectAnalyzer({nombre: "Monitor", precio: 300, stock: 8});
    recordTest("o1.5.4 object ops", result4.productName === "Monitor" && result4.propertyCount === 4);
    
    // o1.5.5: Webcam data
    let result5 = objectAnalyzer({nombre: "Webcam", precio: 80, stock: 15});
    recordTest("o1.5.5 object ops", result5.productName === "Webcam" && result5.propertyCount === 4);
}

// 🚀 Run tests
test_o1_5();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 📦 Crea objetos con `{propiedad: valor}`
* 🔍 Accede con `objeto.propiedad` o `objeto["propiedad"]`
* ➕ Agrega propiedades con `objeto.nuevaPropiedad = valor`
* 📊 Cuenta propiedades con `Object.keys(objeto).length`

📦 ¡Organiza datos como un archivista digital! 🗃️✨

---

## 🚦 o2 Estructuras Condicionales - Tomando Decisiones con If/Else 🤔💡

🎯 En esta sección aprenderás a usar estructuras condicionales en JavaScript para que tu programa tome decisiones según diferentes situaciones. Usarás `if`, `else if` y `else` para ejecutar código diferente dependiendo de las condiciones que evalúes. Este tipo de lógica es esencial para crear programas que respondan de manera diferente según los datos que reciban 🧩🔍.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada resultado `true` en las pruebas equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### Reto o2.1: Sistema de Calificaciones Académicas 📚🎓

**Problema**: Convierte calificaciones numéricas a letras usando condicionales múltiples y determina el estado académico 🎯📊

**Descripción**: Los sistemas académicos usan diferentes escalas para evaluar el rendimiento. Tu función debe convertir una calificación numérica (0-100) a su equivalente en letras y determinar si el estudiante aprueba o reprueba.

🎓 **Escala de calificaciones**:

```javascript
90-100: "A" (Excelente)
80-89:  "B" (Bueno)
70-79:  "C" (Regular)
60-69:  "D" (Deficiente)
0-59:   "F" (Reprobado)
```

Tu programa debe:

* 📊 Recibir una calificación numérica
* 🔍 Determinar la letra correspondiente
* ✅ Calcular si aprueba (>= 60) o reprueba
* 📋 Retornar tanto la letra como el estado

**Casos de prueba**:

1. Entrada ➡️ calificación=95 → letra="A", aprueba=true, descripción="Excelente"
2. Entrada ➡️ calificación=82 → letra="B", aprueba=true, descripción="Bueno"
3. Entrada ➡️ calificación=75 → letra="C", aprueba=true, descripción="Regular"
4. Entrada ➡️ calificación=65 → letra="D", aprueba=true, descripción="Deficiente"
5. Entrada ➡️ calificación=45 → letra="F", aprueba=false, descripción="Reprobado"

**Código base**:

```javascript
// Reto 1: Sistema de Calificaciones Académicas 📚🎓
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function gradeSystem(score) {
    // Tu solución aquí 🛠️
    let letterGrade = "";       // Esta variable debe calcularse
    let passes = false;         // Esta variable debe calcularse
    let description = "";       // Esta variable debe calcularse
    
    return { letterGrade, passes, description };
}

function test_o2_1() {
    // o2.1.1: score = 95
    let result1 = gradeSystem(95);
    recordTest("o2.1.1 grade A", result1.letterGrade === "A" && result1.passes === true && result1.description === "Excelente");
    
    // o2.1.2: score = 82
    let result2 = gradeSystem(82);
    recordTest("o2.1.2 grade B", result2.letterGrade === "B" && result2.passes === true && result2.description === "Bueno");
    
    // o2.1.3: score = 75
    let result3 = gradeSystem(75);
    recordTest("o2.1.3 grade C", result3.letterGrade === "C" && result3.passes === true && result3.description === "Regular");
    
    // o2.1.4: score = 65
    let result4 = gradeSystem(65);
    recordTest("o2.1.4 grade D", result4.letterGrade === "D" && result4.passes === true && result4.description === "Deficiente");
    
    // o2.1.5: score = 45
    let result5 = gradeSystem(45);
    recordTest("o2.1.5 grade F", result5.letterGrade === "F" && result5.passes === false && result5.description === "Reprobado");
}

// 🚀 Run tests
test_o2_1();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 📊 Usa `if (score >= 90)` para empezar desde la calificación más alta
* 🔍 Continúa con `else if (score >= 80)`, `else if (score >= 70)`, etc.
* ✅ Determina aprobación con `score >= 60`
* 📋 Asigna descripción correspondiente en cada caso

🎓 ¡Evalúa el conocimiento como un profesor! 📚⭐

---

### Reto o2.2: Verificador de Edad y Permisos 🆔🔒

**Problema**: Determina los permisos y privilegios de una persona según su edad usando condicionales anidados 🎯👤

**Descripción**: Diferentes actividades requieren diferentes edades mínimas. Tu función debe evaluar qué puede hacer una persona según su edad: votar, conducir, beber alcohol, o si aún es menor de edad.

🆔 **Categorías por edad**:

```javascript
0-15:   "Menor" (sin permisos especiales)
16-17:  "Adolescente" (puede conducir con supervisión)
18-20:  "Joven adulto" (puede votar y conducir)
21+:    "Adulto" (todos los permisos)
```

Tu programa debe:

* 🎂 Recibir la edad de una persona
* 🔍 Determinar su categoría
* 🚗 Evaluar si puede conducir
* 🗳️ Evaluar si puede votar
* 🍺 Evaluar si puede beber alcohol

**Casos de prueba**:

1. Entrada ➡️ edad=14 → categoría="Menor", votar=false, conducir=false, alcohol=false
2. Entrada ➡️ edad=17 → categoría="Adolescente", votar=false, conducir=true, alcohol=false
3. Entrada ➡️ edad=19 → categoría="Joven adulto", votar=true, conducir=true, alcohol=false
4. Entrada ➡️ edad=25 → categoría="Adulto", votar=true, conducir=true, alcohol=true
5. Entrada ➡️ edad=16 → categoría="Adolescente", votar=false, conducir=true, alcohol=false

**Código base**:

```javascript
// Reto 2: Verificador de Edad y Permisos 🆔🔒
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function ageVerifier(age) {
    // Tu solución aquí 🛠️
    let category = "";          // Esta variable debe calcularse
    let canVote = false;        // Esta variable debe calcularse
    let canDrive = false;       // Esta variable debe calcularse
    let canDrinkAlcohol = false; // Esta variable debe calcularse
    
    return { category, canVote, canDrive, canDrinkAlcohol };
}

function test_o2_2() {
    // o2.2.1: age = 14
    let result1 = ageVerifier(14);
    recordTest("o2.2.1 minor", result1.category === "Menor" && result1.canVote === false && result1.canDrive === false && result1.canDrinkAlcohol === false);
    
    // o2.2.2: age = 17
    let result2 = ageVerifier(17);
    recordTest("o2.2.2 teen", result2.category === "Adolescente" && result2.canVote === false && result2.canDrive === true && result2.canDrinkAlcohol === false);
    
    // o2.2.3: age = 19
    let result3 = ageVerifier(19);
    recordTest("o2.2.3 young adult", result3.category === "Joven adulto" && result3.canVote === true && result3.canDrive === true && result3.canDrinkAlcohol === false);
    
    // o2.2.4: age = 25
    let result4 = ageVerifier(25);
    recordTest("o2.2.4 adult", result4.category === "Adulto" && result4.canVote === true && result4.canDrive === true && result4.canDrinkAlcohol === true);
    
    // o2.2.5: age = 16
    let result5 = ageVerifier(16);
    recordTest("o2.2.5 teen 16", result5.category === "Adolescente" && result5.canVote === false && result5.canDrive === true && result5.canDrinkAlcohol === false);
}

// 🚀 Run tests
test_o2_2();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🎂 Usa rangos de edad con `if (age <= 15)`, `else if (age <= 17)`, etc.
* 🔍 Asigna permisos según la categoría de edad
* 🚗 Conducir permitido desde los 16 años
* 🗳️ Votar permitido desde los 18 años
* 🍺 Alcohol permitido desde los 21 años

🆔 ¡Verifica permisos como un oficial! 👮‍♂️✨

---

### Reto o2.3: Calculadora de Descuentos por Volumen 💰🛒

**Problema**: Calcula descuentos progresivos según el monto de compra usando condicionales escalonados 🎯💸

**Descripción**: Las tiendas ofrecen descuentos por volumen para incentivar compras grandes. Tu función debe aplicar diferentes porcentajes de descuento según el monto total y calcular el precio final.

💰 **Escala de descuentos**:

```javascript
$0-$49:     0% descuento
$50-$99:    5% descuento
$100-$199:  10% descuento
$200-$499:  15% descuento
$500+:      20% descuento
```

Tu programa debe:

* 💵 Recibir el monto original de compra
* 🔍 Determinar qué descuento aplicar
* 🧮 Calcular el monto de descuento
* 💸 Calcular el precio final

**Casos de prueba**:

1. Entrada ➡️ monto=$30 → descuento=0%, ahorrado=$0, final=$30
2. Entrada ➡️ monto=$75 → descuento=5%, ahorrado=$3.75, final=$71.25
3. Entrada ➡️ monto=$150 → descuento=10%, ahorrado=$15, final=$135
4. Entrada ➡️ monto=$300 → descuento=15%, ahorrado=$45, final=$255
5. Entrada ➡️ monto=$600 → descuento=20%, ahorrado=$120, final=$480

**Código base**:

```javascript
// Reto 3: Calculadora de Descuentos por Volumen 💰🛒
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function discountCalculator(amount) {
    // Tu solución aquí 🛠️
    let discountPercentage = 0;     // Esta variable debe calcularse
    let discountAmount = 0;         // Esta variable debe calcularse
    let finalPrice = 0;             // Esta variable debe calcularse
    
    return { discountPercentage, discountAmount, finalPrice };
}

function test_o2_3() {
    // o2.3.1: amount = $30
    let result1 = discountCalculator(30);
    recordTest("o2.3.1 no discount", result1.discountPercentage === 0 && result1.discountAmount === 0 && result1.finalPrice === 30);
    
    // o2.3.2: amount = $75
    let result2 = discountCalculator(75);
    recordTest("o2.3.2 5% discount", result2.discountPercentage === 5 && result2.discountAmount === 3.75 && result2.finalPrice === 71.25);
    
    // o2.3.3: amount = $150
    let result3 = discountCalculator(150);
    recordTest("o2.3.3 10% discount", result3.discountPercentage === 10 && result3.discountAmount === 15 && result3.finalPrice === 135);
    
    // o2.3.4: amount = $300
    let result4 = discountCalculator(300);
    recordTest("o2.3.4 15% discount", result4.discountPercentage === 15 && result4.discountAmount === 45 && result4.finalPrice === 255);
    
    // o2.3.5: amount = $600
    let result5 = discountCalculator(600);
    recordTest("o2.3.5 20% discount", result5.discountPercentage === 20 && result5.discountAmount === 120 && result5.finalPrice === 480);
}

// 🚀 Run tests
test_o2_3();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 💰 Usa `if (amount < 50)` para el primer rango
* 🔍 Continúa con `else if (amount < 100)`, `else if (amount < 200)`, etc.
* 🧮 Calcula descuento: `amount * (percentage / 100)`
* 💸 Calcula precio final: `amount - discountAmount`

💰 ¡Crea ofertas irresistibles con lógica! 🛍️✨

---

### Reto o2.4: Clasificador de Temperatura 🌡️❄️

**Problema**: Clasifica temperaturas en diferentes categorías y da recomendaciones de vestimenta usando condicionales 🎯👕

**Descripción**: Según la temperatura, las personas necesitan vestirse de manera diferente. Tu función debe clasificar la temperatura y sugerir qué tipo de ropa usar para estar cómodo.

🌡️ **Categorías de temperatura (Celsius)**:

```javascript
< 0°C:      "Congelante" → "Abrigo grueso y guantes"
0-10°C:     "Frío" → "Abrigo y bufanda"
11-20°C:    "Fresco" → "Chaqueta ligera"
21-30°C:    "Cálido" → "Ropa ligera"
> 30°C:     "Caluroso" → "Ropa muy ligera"
```

Tu programa debe:

* 🌡️ Recibir una temperatura en Celsius
* 🔍 Clasificar la temperatura
* 👕 Sugerir vestimenta apropiada
* ❄️ Determinar si necesita calefacción/aire acondicionado

**Casos de prueba**:

1. Entrada ➡️ temp=-5 → categoría="Congelante", ropa="Abrigo grueso y guantes", clima="calefacción"
2. Entrada ➡️ temp=8 → categoría="Frío", ropa="Abrigo y bufanda", clima="calefacción"
3. Entrada ➡️ temp=18 → categoría="Fresco", ropa="Chaqueta ligera", clima="neutro"
4. Entrada ➡️ temp=25 → categoría="Cálido", ropa="Ropa ligera", clima="neutro"
5. Entrada ➡️ temp=35 → categoría="Caluroso", ropa="Ropa muy ligera", clima="aire acondicionado"

**Código base**:

```javascript
// Reto 4: Clasificador de Temperatura 🌡️❄️
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function temperatureClassifier(temp) {
    // Tu solución aquí 🛠️
    let category = "";              // Esta variable debe calcularse
    let clothingAdvice = "";        // Esta variable debe calcularse
    let climateControl = "";        // Esta variable debe calcularse
    
    return { category, clothingAdvice, climateControl };
}

function test_o2_4() {
    // o2.4.1: temp = -5
    let result1 = temperatureClassifier(-5);
    recordTest("o2.4.1 freezing", result1.category === "Congelante" && result1.clothingAdvice === "Abrigo grueso y guantes" && result1.climateControl === "calefacción");
    
    // o2.4.2: temp = 8
    let result2 = temperatureClassifier(8);
    recordTest("o2.4.2 cold", result2.category === "Frío" && result2.clothingAdvice === "Abrigo y bufanda" && result2.climateControl === "calefacción");
    
    // o2.4.3: temp = 18
    let result3 = temperatureClassifier(18);
    recordTest("o2.4.3 cool", result3.category === "Fresco" && result3.clothingAdvice === "Chaqueta ligera" && result3.climateControl === "neutro");
    
    // o2.4.4: temp = 25
    let result4 = temperatureClassifier(25);
    recordTest("o2.4.4 warm", result4.category === "Cálido" && result4.clothingAdvice === "Ropa ligera" && result4.climateControl === "neutro");
    
    // o2.4.5: temp = 35
    let result5 = temperatureClassifier(35);
    recordTest("o2.4.5 hot", result5.category === "Caluroso" && result5.clothingAdvice === "Ropa muy ligera" && result5.climateControl === "aire acondicionado");
}

// 🚀 Run tests
test_o2_4();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🌡️ Usa `if (temp < 0)` para temperaturas bajo cero
* 🔍 Continúa con rangos: `else if (temp <= 10)`, `else if (temp <= 20)`, etc.
* 👕 Asigna recomendaciones de ropa para cada rango
* ❄️ Considera calefacción para <11°C, aire acondicionado para >30°C

🌡️ ¡Predice el clima como un meteorólogo! ☀️❄️

---

### Reto o2.5: Validador de Contraseñas Seguras 🔒🛡️

**Problema**: Evalúa la fortaleza de contraseñas usando múltiples criterios de seguridad con condicionales complejos 🎯🔐

**Descripción**: Las contraseñas seguras deben cumplir varios requisitos. Tu función debe evaluar una contraseña y determinar su nivel de seguridad basándose en longitud, contenido y complejidad.

🔒 **Criterios de seguridad**:

```javascript
Longitud mínima: 8 caracteres
Debe contener: mayúsculas, minúsculas, números
Niveles: "Débil", "Media", "Fuerte", "Muy fuerte"
```

Tu programa debe:

* 🔤 Verificar longitud mínima
* 🔍 Verificar presencia de mayúsculas, minúsculas y números
* 📊 Calcular nivel de seguridad
* ✅ Determinar si es aceptable para uso

**Casos de prueba**:

1. Entrada ➡️ password="abc123" → nivel="Débil", aceptable=false, longitud=6
2. Entrada ➡️ password="Password1" → nivel="Fuerte", aceptable=true, longitud=9
3. Entrada ➡️ password="password" → nivel="Débil", aceptable=false, longitud=8
4. Entrada ➡️ password="PASS123" → nivel="Media", aceptable=false, longitud=7
5. Entrada ➡️ password="MySecure123" → nivel="Muy fuerte", aceptable=true, longitud=11

**Código base**:

```javascript
// Reto 5: Validador de Contraseñas Seguras 🔒🛡️
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function passwordValidator(password) {
    // Tu solución aquí 🛠️
    let securityLevel = "";         // Esta variable debe calcularse
    let isAcceptable = false;       // Esta variable debe calcularse
    let passwordLength = 0;         // Esta variable debe calcularse
    
    return { securityLevel, isAcceptable, passwordLength };
}

function test_o2_5() {
    // o2.5.1: password = "abc123"
    let result1 = passwordValidator("abc123");
    recordTest("o2.5.1 weak short", result1.securityLevel === "Débil" && result1.isAcceptable === false && result1.passwordLength === 6);
    
    // o2.5.2: password = "Password1"
    let result2 = passwordValidator("Password1");
    recordTest("o2.5.2 strong", result2.securityLevel === "Fuerte" && result2.isAcceptable === true && result2.passwordLength === 9);
    
    // o2.5.3: password = "password"
    let result3 = passwordValidator("password");
    recordTest("o2.5.3 weak long", result3.securityLevel === "Débil" && result3.isAcceptable === false && result3.passwordLength === 8);
    
    // o2.5.4: password = "PASS123"
    let result4 = passwordValidator("PASS123");
    recordTest("o2.5.4 medium short", result4.securityLevel === "Media" && result4.isAcceptable === false && result4.passwordLength === 7);
    
    // o2.5.5: password = "MySecure123"
    let result5 = passwordValidator("MySecure123");
    recordTest("o2.5.5 very strong", result5.securityLevel === "Muy fuerte" && result5.isAcceptable === true && result5.passwordLength === 11);
}

// 🚀 Run tests
test_o2_5();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🔤 Usa `.length` para verificar longitud
* 🔍 Usa regex o métodos como `/[A-Z]/.test(password)` para mayúsculas
* 📊 Combina criterios para determinar nivel de seguridad
* ✅ Considera aceptable si tiene >=8 caracteres y cumple criterios básicos

🔒 ¡Protege datos como un especialista en seguridad! 🛡️💻

---

## 🔄 o3 Estructuras de Repetición - Bucles For y While 🌀💪

🎯 En esta sección aprenderás a usar bucles `for` y `while` para repetir código de manera eficiente. Los bucles son fundamentales para procesar arrays, generar secuencias, realizar cálculos repetitivos y automatizar tareas. Dominarás tanto bucles simples como anidados para resolver problemas complejos 📈🔍.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada resultado `true` en las pruebas equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### Reto o3.1: Procesador de Arrays con For 📊🔢

**Problema**: Usa bucles `for` para procesar arrays de números y calcular estadísticas básicas como suma, promedio y valores extremos 🎯📈

**Descripción**: Los bucles `for` son perfectos para recorrer arrays y realizar cálculos. En este ejercicio procesarás arrays de números para obtener información estadística útil usando acumuladores y comparaciones.

🔢 **Operaciones a realizar**:

```javascript
- Sumar todos los números
- Calcular el promedio
- Encontrar el mayor y menor
- Contar números pares
```

Tu programa debe:

* 📊 Recorrer el array con un bucle `for`
* ➕ Usar acumuladores para suma y conteo
* 🔍 Comparar valores para encontrar extremos
* 🧮 Calcular promedio y estadísticas finales

**Casos de prueba**:

1. Entrada ➡️ números=[1,2,3,4,5] → suma=15, promedio=3, mayor=5, menor=1, pares=2
2. Entrada ➡️ números=[10,20,30,40] → suma=100, promedio=25, mayor=40, menor=10, pares=4
3. Entrada ➡️ números=[7,3,9,1,5] → suma=25, promedio=5, mayor=9, menor=1, pares=0
4. Entrada ➡️ números=[2,4,6,8] → suma=20, promedio=5, mayor=8, menor=2, pares=4
5. Entrada ➡️ números=[15,25,35] → suma=75, promedio=25, mayor=35, menor=15, pares=0

**Código base**:

```javascript
// Reto 1: Procesador de Arrays con For 📊🔢
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function arrayProcessor(numbers) {
    // Tu solución aquí 🛠️
    let sum = 0;                    // Esta variable debe calcularse
    let average = 0;                // Esta variable debe calcularse
    let max = 0;                    // Esta variable debe calcularse
    let min = 0;                    // Esta variable debe calcularse
    let evenCount = 0;              // Esta variable debe calcularse
    
    return { sum, average, max, min, evenCount };
}

function test_o3_1() {
    // o3.1.1: [1,2,3,4,5]
    let result1 = arrayProcessor([1,2,3,4,5]);
    recordTest("o3.1.1 basic array", result1.sum === 15 && result1.average === 3 && result1.max === 5 && result1.min === 1 && result1.evenCount === 2);
    
    // o3.1.2: [10,20,30,40]
    let result2 = arrayProcessor([10,20,30,40]);
    recordTest("o3.1.2 tens array", result2.sum === 100 && result2.average === 25 && result2.max === 40 && result2.min === 10 && result2.evenCount === 4);
    
    // o3.1.3: [7,3,9,1,5]
    let result3 = arrayProcessor([7,3,9,1,5]);
    recordTest("o3.1.3 odds array", result3.sum === 25 && result3.average === 5 && result3.max === 9 && result3.min === 1 && result3.evenCount === 0);
    
    // o3.1.4: [2,4,6,8]
    let result4 = arrayProcessor([2,4,6,8]);
    recordTest("o3.1.4 evens array", result4.sum === 20 && result4.average === 5 && result4.max === 8 && result4.min === 2 && result4.evenCount === 4);
    
    // o3.1.5: [15,25,35]
    let result5 = arrayProcessor([15,25,35]);
    recordTest("o3.1.5 big odds", result5.sum === 75 && result5.average === 25 && result5.max === 35 && result5.min === 15 && result5.evenCount === 0);
}

// 🚀 Run tests
test_o3_1();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 📊 Usa `for (let i = 0; i < numbers.length; i++)` para recorrer
* ➕ Acumula suma con `sum += numbers[i]`
* 🔍 Inicializa max y min con `numbers[0]`
* 🧮 Calcula promedio al final: `sum / numbers.length`

📊 ¡Analiza datos como un estadístico! 📈✨

---

### Reto o3.2: Generador de Patrones con Bucles Anidados ⭐🔺

**Problema**: Usa bucles anidados (`for` dentro de `for`) para generar patrones geométricos de caracteres 🎯🎨

**Descripción**: Los bucles anidados permiten crear estructuras bidimensionales como patrones y figuras. El bucle exterior controla las filas y el bucle interior controla las columnas o elementos por fila.

⭐ **Patrón a generar**:

```javascript
Para n=3:
*
**
***

Para n=4:
*
**
***
****
```

Tu programa debe:

* 🔄 Usar bucle exterior para controlar filas
* ⭐ Usar bucle interior para generar estrellas en cada fila
* 📝 Construir cada línea del patrón
* 📊 Contar total de caracteres generados

**Casos de prueba**:

1. Entrada ➡️ filas=3 → patrón=["*","**","***"], totalEstrellas=6
2. Entrada ➡️ filas=4 → patrón=["*","**","***","****"], totalEstrellas=10
3. Entrada ➡️ filas=5 → patrón=["*","**","***","****","*****"], totalEstrellas=15
4. Entrada ➡️ filas=2 → patrón=["*","**"], totalEstrellas=3
5. Entrada ➡️ filas=1 → patrón=["*"], totalEstrellas=1

**Código base**:

```javascript
// Reto 2: Generador de Patrones con Bucles Anidados ⭐🔺
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function patternGenerator(rows) {
    // Tu solución aquí 🛠️
    let pattern = [];               // Esta variable debe calcularse
    let totalStars = 0;             // Esta variable debe calcularse
    
    return { pattern, totalStars };
}

function test_o3_2() {
    // o3.2.1: rows = 3
    let result1 = patternGenerator(3);
    recordTest("o3.2.1 triangle 3", JSON.stringify(result1.pattern) === JSON.stringify(["*","**","***"]) && result1.totalStars === 6);
    
    // o3.2.2: rows = 4
    let result2 = patternGenerator(4);
    recordTest("o3.2.2 triangle 4", JSON.stringify(result2.pattern) === JSON.stringify(["*","**","***","****"]) && result2.totalStars === 10);
    
    // o3.2.3: rows = 5
    let result3 = patternGenerator(5);
    recordTest("o3.2.3 triangle 5", JSON.stringify(result3.pattern) === JSON.stringify(["*","**","***","****","*****"]) && result3.totalStars === 15);
    
    // o3.2.4: rows = 2
    let result4 = patternGenerator(2);
    recordTest("o3.2.4 triangle 2", JSON.stringify(result4.pattern) === JSON.stringify(["*","**"]) && result4.totalStars === 3);
    
    // o3.2.5: rows = 1
    let result5 = patternGenerator(1);
    recordTest("o3.2.5 triangle 1", JSON.stringify(result5.pattern) === JSON.stringify(["*"]) && result5.totalStars === 1);
}

// 🚀 Run tests
test_o3_2();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🔄 Usa `for (let i = 1; i <= rows; i++)` para las filas
* ⭐ Usa `for (let j = 0; j < i; j++)` para las estrellas
* 📝 Construye cada línea concatenando: `line += "*"`
* 📊 Cuenta estrellas totales sumando `i` en cada fila

⭐ ¡Dibuja patrones como un artista digital! 🎨🌟

---

### Reto o3.3: Contador Dinámico con While 🔢⚡

**Problema**: Usa bucles `while` para contar números que cumplan condiciones específicas hasta alcanzar una meta 🎯🎲

**Descripción**: Los bucles `while` son útiles cuando no sabes exactamente cuántas iteraciones necesitas. En este ejercicio contarás números que cumplan criterios hasta alcanzar una cantidad objetivo.

🔢 **Lógica del contador**:

```javascript
1. Empezar desde un número inicial
2. Mientras no hayas encontrado suficientes números:
   - Verificar si el número actual cumple la condición
   - Si cumple, incrementar contador
   - Avanzar al siguiente número
3. Retornar información del proceso
```

Tu programa debe:

* 🔢 Usar `while` para buscar números que sean múltiplos de 3
* 📊 Contar cuántos múltiplos encuentras
* 🎯 Parar cuando encuentres la cantidad objetivo
* 📈 Retornar el último número revisado

**Casos de prueba**:

1. Entrada ➡️ objetivo=3, inicio=1 → encontrados=3, ultimoNumero=9, numerosRevisados=9
2. Entrada ➡️ objetivo=5, inicio=1 → encontrados=5, ultimoNumero=15, numerosRevisados=15
3. Entrada ➡️ objetivo=2, inicio=10 → encontrados=2, ultimoNumero=15, numerosRevisados=6
4. Entrada ➡️ objetivo=4, inicio=5 → encontrados=4, ultimoNumero=18, numerosRevisados=14
5. Entrada ➡️ objetivo=1, inicio=1 → encontrados=1, ultimoNumero=3, numerosRevisados=3

**Código base**:

```javascript
// Reto 3: Contador Dinámico con While 🔢⚡
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function dynamicCounter(target, start) {
    // Tu solución aquí 🛠️
    let found = 0;                  // Esta variable debe calcularse
    let lastNumber = 0;             // Esta variable debe calcularse
    let numbersChecked = 0;         // Esta variable debe calcularse
    
    return { found, lastNumber, numbersChecked };
}

function test_o3_3() {
    // o3.3.1: target=3, start=1
    let result1 = dynamicCounter(3, 1);
    recordTest("o3.3.1 find 3 from 1", result1.found === 3 && result1.lastNumber === 9 && result1.numbersChecked === 9);
    
    // o3.3.2: target=5, start=1
    let result2 = dynamicCounter(5, 1);
    recordTest("o3.3.2 find 5 from 1", result2.found === 5 && result2.lastNumber === 15 && result2.numbersChecked === 15);
    
    // o3.3.3: target=2, start=10
    let result3 = dynamicCounter(2, 10);
    recordTest("o3.3.3 find 2 from 10", result3.found === 2 && result3.lastNumber === 15 && result3.numbersChecked === 6);
    
    // o3.3.4: target=4, start=5
    let result4 = dynamicCounter(4, 5);
    recordTest("o3.3.4 find 4 from 5", result4.found === 4 && result4.lastNumber === 18 && result4.numbersChecked === 14);
    
    // o3.3.5: target=1, start=1
    let result5 = dynamicCounter(1, 1);
    recordTest("o3.3.5 find 1 from 1", result5.found === 1 && result5.lastNumber === 3 && result5.numbersChecked === 3);
}

// 🚀 Run tests
test_o3_3();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🔢 Inicializa contadores y variables antes del bucle
* 🔄 Usa `while (found < target)` como condición
* 🎯 Verifica múltiplos de 3 con `numero % 3 === 0`
* 📊 Incrementa contadores y avanza el número en cada iteración

🔢 ¡Cuenta dinámicamente como un algoritmo inteligente! ⚡✨

---

### Reto o3.4: Tabla de Multiplicar Interactiva 📊✖️

**Problema**: Genera tablas de multiplicar personalizadas usando bucles `for` y calcula totales por fila y columna 🎯📈

**Descripción**: Las tablas de multiplicar son perfectas para practicar bucles anidados. En este ejercicio crearás una tabla personalizable y calcularás estadísticas útiles como sumas de filas y columnas.

✖️ **Estructura de la tabla**:

```javascript
Para tabla del 2, hasta 4:
2x1=2  2x2=4  2x3=6  2x4=8

Calcular:
- Suma de cada fila
- Total general
- Número de operaciones
```

Tu programa debe:

* ✖️ Generar tabla de multiplicar para un número dado
* 📊 Calcular hasta un multiplicador máximo
* ➕ Sumar todos los resultados de la tabla
* 🔢 Contar el total de operaciones realizadas

**Casos de prueba**:

1. Entrada ➡️ tabla=2, hasta=3 → resultados=[2,4,6], suma=12, operaciones=3
2. Entrada ➡️ tabla=5, hasta=4 → resultados=[5,10,15,20], suma=50, operaciones=4
3. Entrada ➡️ tabla=3, hasta=5 → resultados=[3,6,9,12,15], suma=45, operaciones=5
4. Entrada ➡️ tabla=7, hasta=2 → resultados=[7,14], suma=21, operaciones=2
5. Entrada ➡️ tabla=4, hasta=6 → resultados=[4,8,12,16,20,24], suma=84, operaciones=6

**Código base**:

```javascript
// Reto 4: Tabla de Multiplicar Interactiva 📊✖️
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function multiplicationTable(table, upTo) {
    // Tu solución aquí 🛠️
    let results = [];               // Esta variable debe calcularse
    let totalSum = 0;               // Esta variable debe calcularse
    let operations = 0;             // Esta variable debe calcularse
    
    return { results, totalSum, operations };
}

function test_o3_4() {
    // o3.4.1: table=2, upTo=3
    let result1 = multiplicationTable(2, 3);
    recordTest("o3.4.1 table 2x3", JSON.stringify(result1.results) === JSON.stringify([2,4,6]) && result1.totalSum === 12 && result1.operations === 3);
    
    // o3.4.2: table=5, upTo=4
    let result2 = multiplicationTable(5, 4);
    recordTest("o3.4.2 table 5x4", JSON.stringify(result2.results) === JSON.stringify([5,10,15,20]) && result2.totalSum === 50 && result2.operations === 4);
    
    // o3.4.3: table=3, upTo=5
    let result3 = multiplicationTable(3, 5);
    recordTest("o3.4.3 table 3x5", JSON.stringify(result3.results) === JSON.stringify([3,6,9,12,15]) && result3.totalSum === 45 && result3.operations === 5);
    
    // o3.4.4: table=7, upTo=2
    let result4 = multiplicationTable(7, 2);
    recordTest("o3.4.4 table 7x2", JSON.stringify(result4.results) === JSON.stringify([7,14]) && result4.totalSum === 21 && result4.operations === 2);
    
    // o3.4.5: table=4, upTo=6
    let result5 = multiplicationTable(4, 6);
    recordTest("o3.4.5 table 4x6", JSON.stringify(result5.results) === JSON.stringify([4,8,12,16,20,24]) && result5.totalSum === 84 && result5.operations === 6);
}

// 🚀 Run tests
test_o3_4();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* ✖️ Usa `for (let i = 1; i <= upTo; i++)` para multiplicadores
* 📊 Calcula `resultado = table * i` en cada iteración
* ➕ Agrega resultados al array y suma al total
* 🔢 Cuenta operaciones incrementando contador

✖️ ¡Multiplica conocimiento con precisión! 📊🚀

---

### Reto o3.5: Buscador de Números Primos con While 🔍🎯

**Problema**: Encuentra números primos usando bucles `while` anidados para verificar divisibilidad y construir una lista de primos 🎯🔢

**Descripción**: Un número primo solo es divisible por 1 y por sí mismo. Este ejercicio combina bucles `while` para buscar primos y verificar su condición usando divisiones sucesivas.

🔍 **Algoritmo de búsqueda**:

```javascript
1. Para cada número desde 2:
   2. Verificar si es primo (solo divisible por 1 y él mismo)
   3. Si es primo, agregarlo a la lista
   4. Continuar hasta encontrar la cantidad deseada
```

Tu programa debe:

* 🔍 Buscar números primos empezando desde 2
* 🎯 Parar cuando encuentres la cantidad solicitada
* 📊 Verificar si cada número es primo usando divisiones
* 📋 Retornar la lista de primos encontrados

**Casos de prueba**:

1. Entrada ➡️ cantidad=3 → primos=[2,3,5], mayorPrimo=5, numerosVerificados=6
2. Entrada ➡️ cantidad=5 → primos=[2,3,5,7,11], mayorPrimo=11, numerosVerificados=12
3. Entrada ➡️ cantidad=2 → primos=[2,3], mayorPrimo=3, numerosVerificados=4
4. Entrada ➡️ cantidad=4 → primos=[2,3,5,7], mayorPrimo=7, numerosVerificados=8
5. Entrada ➡️ cantidad=1 → primos=[2], mayorPrimo=2, numerosVerificados=2

**Código base**:

```javascript
// Reto 5: Buscador de Números Primos con While 🔍🎯
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

function primeFinder(count) {
    // Tu solución aquí 🛠️
    let primes = [];                // Esta variable debe calcularse
    let largestPrime = 0;           // Esta variable debe calcularse
    let numbersChecked = 0;         // Esta variable debe calcularse
    
    return { primes, largestPrime, numbersChecked };
}

function test_o3_5() {
    // o3.5.1: count=3
    let result1 = primeFinder(3);
    recordTest("o3.5.1 first 3 primes", JSON.stringify(result1.primes) === JSON.stringify([2,3,5]) && result1.largestPrime === 5 && result1.numbersChecked === 6);
    
    // o3.5.2: count=5
    let result2 = primeFinder(5);
    recordTest("o3.5.2 first 5 primes", JSON.stringify(result2.primes) === JSON.stringify([2,3,5,7,11]) && result2.largestPrime === 11 && result2.numbersChecked === 12);
    
    // o3.5.3: count=2
    let result3 = primeFinder(2);
    recordTest("o3.5.3 first 2 primes", JSON.stringify(result3.primes) === JSON.stringify([2,3]) && result3.largestPrime === 3 && result3.numbersChecked === 4);
    
    // o3.5.4: count=4
    let result4 = primeFinder(4);
    recordTest("o3.5.4 first 4 primes", JSON.stringify(result4.primes) === JSON.stringify([2,3,5,7]) && result4.largestPrime === 7 && result4.numbersChecked === 8);
    
    // o3.5.5: count=1
    let result5 = primeFinder(1);
    recordTest("o3.5.5 first 1 prime", JSON.stringify(result5.primes) === JSON.stringify([2]) && result5.largestPrime === 2 && result5.numbersChecked === 2);
}

// 🚀 Run tests
test_o3_5();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🔍 Empieza verificando desde el número 2
* 🎯 Para verificar si es primo, divide entre todos los números menores
* 📊 Si no es divisible por ninguno (excepto 1 y él mismo), es primo
* 📋 Usa `while` externo para buscar y `while` interno para verificar

🔍 ¡Descubre números primos como un matemático! 🎯✨

---

## ⚙️ o4 Funciones en JavaScript - Reutilización y Modularidad 🔧✨

🎯 En esta sección aprenderás a crear y usar funciones para organizar tu código de manera eficiente. Las funciones te permiten reutilizar código, recibir parámetros, retornar valores y crear programas más modulares y fáciles de mantener. Dominarás tanto funciones simples como funciones con múltiples parámetros y lógica compleja 🧩🚀.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada resultado `true` en las pruebas equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### Reto o4.1: Calculadora de Operaciones Básicas ➕➖

**Problema**: Crea funciones para realizar operaciones matemáticas básicas y una función principal que las utilice según el operador especificado 🎯🧮

**Descripción**: Las funciones permiten organizar código en bloques reutilizables. En este ejercicio crearás funciones separadas para suma, resta, multiplicación y división, y una función coordinadora que llame a la función correcta.

🧮 **Funciones a implementar**:

```javascript
function sumar(a, b) { return a + b; }
function restar(a, b) { return a - b; }
function multiplicar(a, b) { return a * b; }
function dividir(a, b) { return a / b; }
function calcular(num1, num2, operador) { ... }
```

Tu programa debe:

* ➕ Crear funciones para cada operación matemática
* 🔧 Crear función principal que reciba operador como string
* 🎯 Llamar a la función correcta según el operador
* ⚠️ Manejar división por cero retornando "Error"

**Casos de prueba**:

1. Entrada ➡️ calcular(10, 5, "+") → resultado=15, operacion="suma"
2. Entrada ➡️ calcular(10, 3, "-") → resultado=7, operacion="resta"
3. Entrada ➡️ calcular(4, 6, "*") → resultado=24, operacion="multiplicacion"
4. Entrada ➡️ calcular(15, 3, "/") → resultado=5, operacion="division"
5. Entrada ➡️ calcular(10, 0, "/") → resultado="Error", operacion="division"

**Código base**:

```javascript
// Reto 1: Calculadora de Operaciones Básicas ➕➖
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

// Tu solución aquí 🛠️
function add(a, b) {
    // Implementar suma
}

function subtract(a, b) {
    // Implementar resta
}

function multiply(a, b) {
    // Implementar multiplicación
}

function divide(a, b) {
    // Implementar división (manejar división por cero)
}

function calculator(num1, num2, operator) {
    // Tu función coordinadora aquí
    let result = 0;             // Esta variable debe calcularse
    let operation = "";         // Esta variable debe calcularse
    
    return { result, operation };
}

function test_o4_1() {
    // o4.1.1: 10 + 5
    let result1 = calculator(10, 5, "+");
    recordTest("o4.1.1 addition", result1.result === 15 && result1.operation === "suma");
    
    // o4.1.2: 10 - 3
    let result2 = calculator(10, 3, "-");
    recordTest("o4.1.2 subtraction", result2.result === 7 && result2.operation === "resta");
    
    // o4.1.3: 4 * 6
    let result3 = calculator(4, 6, "*");
    recordTest("o4.1.3 multiplication", result3.result === 24 && result3.operation === "multiplicacion");
    
    // o4.1.4: 15 / 3
    let result4 = calculator(15, 3, "/");
    recordTest("o4.1.4 division", result4.result === 5 && result4.operation === "division");
    
    // o4.1.5: 10 / 0
    let result5 = calculator(10, 0, "/");
    recordTest("o4.1.5 division by zero", result5.result === "Error" && result5.operation === "division");
}

// 🚀 Run tests
test_o4_1();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* ➕ Implementa cada operación en su propia función
* 🔧 Usa `if/else if` en la función calculadora para elegir operación
* 🎯 Retorna objeto con resultado y nombre de operación
* ⚠️ Verifica `b === 0` antes de dividir

🧮 ¡Calcula como una computadora profesional! 💻✨

---

### Reto o4.2: Analizador de Strings con Funciones 📝🔍

**Problema**: Crea funciones especializadas para analizar diferentes aspectos de strings y una función principal que combine todos los análisis 🎯📊

**Descripción**: Al dividir tareas complejas en funciones pequeñas, el código se vuelve más fácil de entender y mantener. Crearás funciones para contar caracteres, palabras, vocales y una función que coordine todos los análisis.

📝 **Funciones a implementar**:

```javascript
function contarCaracteres(texto)
function contarPalabras(texto)  
function contarVocales(texto)
function esPalindromo(texto)
function analizarTexto(texto)
```

Tu programa debe:

* 📏 Contar caracteres totales (sin espacios)
* 📝 Contar palabras separadas por espacios
* 🔤 Contar vocales (a, e, i, o, u)
* 🔄 Verificar si es palíndromo (se lee igual al revés)

**Casos de prueba**:

1. Entrada ➡️ "Hola mundo" → caracteres=9, palabras=2, vocales=4, palindromo=false
2. Entrada ➡️ "oso" → caracteres=3, palabras=1, vocales=2, palindromo=true
3. Entrada ➡️ "JavaScript es genial" → caracteres=16, palabras=3, vocales=7, palindromo=false
4. Entrada ➡️ "anana" → caracteres=5, palabras=1, vocales=4, palindromo=true
5. Entrada ➡️ "Programar es divertido" → caracteres=18, palabras=3, vocales=8, palindromo=false

**Código base**:

```javascript
// Reto 2: Analizador de Strings con Funciones 📝🔍
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

// Tu solución aquí 🛠️
function countCharacters(text) {
    // Contar caracteres sin espacios
}

function countWords(text) {
    // Contar palabras
}

function countVowels(text) {
    // Contar vocales
}

function isPalindrome(text) {
    // Verificar si es palíndromo
}

function textAnalyzer(text) {
    // Tu función coordinadora aquí
    let characters = 0;         // Esta variable debe calcularse
    let words = 0;              // Esta variable debe calcularse
    let vowels = 0;             // Esta variable debe calcularse
    let palindrome = false;     // Esta variable debe calcularse
    
    return { characters, words, vowels, palindrome };
}

function test_o4_2() {
    // o4.2.1: "Hola mundo"
    let result1 = textAnalyzer("Hola mundo");
    recordTest("o4.2.1 hello world", result1.characters === 9 && result1.words === 2 && result1.vowels === 4 && result1.palindrome === false);
    
    // o4.2.2: "oso"
    let result2 = textAnalyzer("oso");
    recordTest("o4.2.2 bear", result2.characters === 3 && result2.words === 1 && result2.vowels === 2 && result2.palindrome === true);
    
    // o4.2.3: "JavaScript es genial"
    let result3 = textAnalyzer("JavaScript es genial");
    recordTest("o4.2.3 js cool", result3.characters === 16 && result3.words === 3 && result3.vowels === 7 && result3.palindrome === false);
    
    // o4.2.4: "anana"
    let result4 = textAnalyzer("anana");
    recordTest("o4.2.4 pineapple", result4.characters === 5 && result4.words === 1 && result4.vowels === 4 && result4.palindrome === true);
    
    // o4.2.5: "Programar es divertido"
    let result5 = textAnalyzer("Programar es divertido");
    recordTest("o4.2.5 coding fun", result5.characters === 18 && result5.words === 3 && result5.vowels === 8 && result5.palindrome === false);
}

// 🚀 Run tests
test_o4_2();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 📏 Usa `text.replace(/ /g, "").length` para contar sin espacios
* 📝 Usa `text.split(" ").length` para contar palabras
* 🔤 Verifica cada carácter con `"aeiou".includes(char.toLowerCase())`
* 🔄 Para palíndromo, compara texto con `texto.split("").reverse().join("")`

📝 ¡Analiza texto como un lingüista computacional! 🔍✨

---

### Reto o4.3: Sistema de Gestión de Arrays 📚⚙️

**Problema**: Crea funciones para manipular arrays de diferentes maneras y una función principal que aplique múltiples operaciones en secuencia 🎯📊

**Descripción**: Los arrays necesitan diferentes tipos de manipulaciones. Crearás funciones especializadas para filtrar, transformar y analizar arrays, y una función coordinadora que aplique varias operaciones.

📚 **Funciones a implementar**:

```javascript
function filtrarPares(array)
function duplicarValores(array) 
function encontrarMaximo(array)
function calcularPromedio(array)
function procesarArray(array)
```

Tu programa debe:

* 🔢 Filtrar solo números pares del array
* ✖️ Duplicar todos los valores (multiplicar por 2)
* 🔍 Encontrar el valor máximo
* 📊 Calcular el promedio de todos los números

**Casos de prueba**:

1. Entrada ➡️ [1,2,3,4,5] → pares=[2,4], duplicados=[2,4,6,8,10], maximo=10, promedio=6
2. Entrada ➡️ [10,15,20,25] → pares=[10,20], duplicados=[20,30,40,50], maximo=50, promedio=35
3. Entrada ➡️ [2,4,6] → pares=[2,4,6], duplicados=[4,8,12], maximo=12, promedio=8
4. Entrada ➡️ [1,3,5,7] → pares=[], duplicados=[2,6,10,14], maximo=14, promedio=8
5. Entrada ➡️ [8,12,16] → pares=[8,12,16], duplicados=[16,24,32], maximo=32, promedio=24

**Código base**:

```javascript
// Reto 3: Sistema de Gestión de Arrays 📚⚙️
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

// Tu solución aquí 🛠️
function filterEvens(array) {
    // Filtrar números pares
}

function doubleValues(array) {
    // Duplicar todos los valores
}

function findMaximum(array) {
    // Encontrar el máximo
}

function calculateAverage(array) {
    // Calcular promedio
}

function arrayProcessor(array) {
    // Tu función coordinadora aquí
    let evens = [];             // Esta variable debe calcularse
    let doubled = [];           // Esta variable debe calcularse
    let maximum = 0;            // Esta variable debe calcularse
    let average = 0;            // Esta variable debe calcularse
    
    return { evens, doubled, maximum, average };
}

function test_o4_3() {
    // o4.3.1: [1,2,3,4,5]
    let result1 = arrayProcessor([1,2,3,4,5]);
    recordTest("o4.3.1 mixed array", JSON.stringify(result1.evens) === JSON.stringify([2,4]) && JSON.stringify(result1.doubled) === JSON.stringify([2,4,6,8,10]) && result1.maximum === 10 && result1.average === 6);
    
    // o4.3.2: [10,15,20,25]
    let result2 = arrayProcessor([10,15,20,25]);
    recordTest("o4.3.2 big numbers", JSON.stringify(result2.evens) === JSON.stringify([10,20]) && JSON.stringify(result2.doubled) === JSON.stringify([20,30,40,50]) && result2.maximum === 50 && result2.average === 35);
    
    // o4.3.3: [2,4,6]
    let result3 = arrayProcessor([2,4,6]);
    recordTest("o4.3.3 all evens", JSON.stringify(result3.evens) === JSON.stringify([2,4,6]) && JSON.stringify(result3.doubled) === JSON.stringify([4,8,12]) && result3.maximum === 12 && result3.average === 8);
    
    // o4.3.4: [1,3,5,7]
    let result4 = arrayProcessor([1,3,5,7]);
    recordTest("o4.3.4 all odds", JSON.stringify(result4.evens) === JSON.stringify([]) && JSON.stringify(result4.doubled) === JSON.stringify([2,6,10,14]) && result4.maximum === 14 && result4.average === 8);
    
    // o4.3.5: [8,12,16]
    let result5 = arrayProcessor([8,12,16]);
    recordTest("o4.3.5 big evens", JSON.stringify(result5.evens) === JSON.stringify([8,12,16]) && JSON.stringify(result5.doubled) === JSON.stringify([16,24,32]) && result5.maximum === 32 && result5.average === 24);
}

// 🚀 Run tests
test_o4_3();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🔢 Usa `array.filter(num => num % 2 === 0)` para filtrar pares
* ✖️ Usa `array.map(num => num * 2)` para duplicar valores
* 🔍 Usa `Math.max(...array)` para encontrar el máximo
* 📊 Suma todos y divide por longitud para el promedio

📚 ¡Manipula arrays como un científico de datos! 📊✨

---

### Reto o4.4: Conversor de Temperaturas con Validación 🌡️🔄

**Problema**: Crea funciones para convertir entre diferentes escalas de temperatura y valida que las entradas sean correctas 🎯❄️

**Descripción**: Las conversiones de temperatura requieren fórmulas específicas y validación de datos. Crearás funciones para convertir entre Celsius, Fahrenheit y Kelvin, y validarás que las temperaturas sean físicamente posibles.

🌡️ **Fórmulas de conversión**:

```javascript
Celsius a Fahrenheit: (C × 9/5) + 32
Fahrenheit a Celsius: (F - 32) × 5/9
Celsius a Kelvin: C + 273.15
Kelvin a Celsius: K - 273.15
```

Tu programa debe:

* 🔄 Convertir entre las tres escalas de temperatura
* ✅ Validar que las temperaturas sean físicamente posibles
* 🌡️ Retornar error si la temperatura es menor al cero absoluto
* 📊 Redondear resultados a 2 decimales

**Casos de prueba**:

1. Entrada ➡️ convertir(0, "C", "F") → resultado=32, valida=true, escala="Fahrenheit"
2. Entrada ➡️ convertir(100, "C", "K") → resultado=373.15, valida=true, escala="Kelvin"
3. Entrada ➡️ convertir(32, "F", "C") → resultado=0, valida=true, escala="Celsius"
4. Entrada ➡️ convertir(-300, "C", "F") → resultado="Error", valida=false, escala="Invalid"
5. Entrada ➡️ convertir(273.15, "K", "C") → resultado=0, valida=true, escala="Celsius"

**Código base**:

```javascript
// Reto 4: Conversor de Temperaturas con Validación 🌡️🔄
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

// Tu solución aquí 🛠️
function celsiusToFahrenheit(celsius) {
    // Convertir Celsius a Fahrenheit
}

function fahrenheitToCelsius(fahrenheit) {
    // Convertir Fahrenheit a Celsius
}

function celsiusToKelvin(celsius) {
    // Convertir Celsius a Kelvin
}

function kelvinToCelsius(kelvin) {
    // Convertir Kelvin a Celsius
}

function isValidTemperature(temp, scale) {
    // Validar si la temperatura es físicamente posible
}

function temperatureConverter(temp, fromScale, toScale) {
    // Tu función coordinadora aquí
    let result = 0;             // Esta variable debe calcularse
    let isValid = false;        // Esta variable debe calcularse
    let targetScale = "";       // Esta variable debe calcularse
    
    return { result, isValid, targetScale };
}

function test_o4_4() {
    // o4.4.1: 0°C to °F
    let result1 = temperatureConverter(0, "C", "F");
    recordTest("o4.4.1 freezing point", result1.result === 32 && result1.isValid === true && result1.targetScale === "Fahrenheit");
    
    // o4.4.2: 100°C to K
    let result2 = temperatureConverter(100, "C", "K");
    recordTest("o4.4.2 boiling point", result2.result === 373.15 && result2.isValid === true && result2.targetScale === "Kelvin");
    
    // o4.4.3: 32°F to °C
    let result3 = temperatureConverter(32, "F", "C");
    recordTest("o4.4.3 fahrenheit freeze", result3.result === 0 && result3.isValid === true && result3.targetScale === "Celsius");
    
    // o4.4.4: -300°C to °F (invalid)
    let result4 = temperatureConverter(-300, "C", "F");
    recordTest("o4.4.4 invalid temp", result4.result === "Error" && result4.isValid === false && result4.targetScale === "Invalid");
    
    // o4.4.5: 273.15K to °C
    let result5 = temperatureConverter(273.15, "K", "C");
    recordTest("o4.4.5 absolute zero", result5.result === 0 && result5.isValid === true && result5.targetScale === "Celsius");
}

// 🚀 Run tests
test_o4_4();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 🌡️ El cero absoluto es -273.15°C, -459.67°F, 0K
* 🔄 Usa las fórmulas exactas para conversiones
* ✅ Valida antes de convertir para evitar resultados imposibles
* 📊 Usa `Math.round(numero * 100) / 100` para redondear a 2 decimales

🌡️ ¡Convierte temperaturas como un físico! ❄️🔥

---

### Reto o4.5: Generador de Reportes de Estudiantes 📊🎓

**Problema**: Crea un sistema completo de funciones para procesar calificaciones de estudiantes y generar reportes estadísticos detallados 🎯📋

**Descripción**: Los sistemas académicos requieren análisis completos de datos. Crearás funciones para calcular promedios, determinar estados académicos, encontrar extremos y generar reportes completos de rendimiento estudiantil.

📊 **Sistema de funciones**:

```javascript
function calcularPromedio(calificaciones)
function determinarEstado(promedio)
function encontrarExtremos(calificaciones) 
function contarAprobados(estudiantes)
function generarReporte(estudiantes)
```

Tu programa debe:

* 📊 Calcular promedio de calificaciones por estudiante
* 🎓 Determinar estado: "Excelente" (>=90), "Bueno" (>=80), "Regular" (>=70), "Reprobado" (<70)
* 🔍 Encontrar calificación más alta y más baja
* ✅ Contar estudiantes aprobados (promedio >= 70)

**Casos de prueba**:

1. Entrada ➡️ estudiantes=[{nombre:"Ana", calificaciones:[90,85,95]}] → promedio=90, estado="Excelente", aprobados=1
2. Entrada ➡️ estudiantes=[{nombre:"Luis", calificaciones:[75,80,70]}] → promedio=75, estado="Regular", aprobados=1
3. Entrada ➡️ estudiantes=[{nombre:"María", calificaciones:[60,65,55]}] → promedio=60, estado="Reprobado", aprobados=0
4. Entrada ➡️ estudiantes=[{nombre:"Carlos", calificaciones:[88,92,85]}] → promedio=88.33, estado="Bueno", aprobados=1
5. Entrada ➡️ estudiantes=[{nombre:"Elena", calificaciones:[95,98,100]}] → promedio=97.67, estado="Excelente", aprobados=1

**Código base**:

```javascript
// Reto 5: Generador de Reportes de Estudiantes 📊🎓
// 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

let testResults = [];
function recordTest(testName, condition) {
    const emoji = condition ? "✅" : "❌";
    testResults.push(`${emoji} ${testName}`);
}

// Tu solución aquí 🛠️
function calculateAverage(grades) {
    // Calcular promedio de calificaciones
}

function determineStatus(average) {
    // Determinar estado académico
}

function findExtremes(grades) {
    // Encontrar calificación más alta y más baja
}

function countPassed(students) {
    // Contar estudiantes aprobados
}

function generateReport(students) {
    // Tu función coordinadora aquí
    let studentData = {};       // Esta variable debe calcularse
    let totalPassed = 0;        // Esta variable debe calcularse
    
    // Para un solo estudiante en las pruebas
    if (students.length > 0) {
        let student = students[0];
        let avg = calculateAverage(student.calificaciones);
        let status = determineStatus(avg);
        studentData = {
            average: Math.round(avg * 100) / 100,
            status: status
        };
        totalPassed = countPassed(students);
    }
    
    return { studentData, totalPassed };
}

function test_o4_5() {
    // o4.5.1: Ana - Excelente
    let result1 = generateReport([{nombre:"Ana", calificaciones:[90,85,95]}]);
    recordTest("o4.5.1 excellent student", result1.studentData.average === 90 && result1.studentData.status === "Excelente" && result1.totalPassed === 1);
    
    // o4.5.2: Luis - Regular
    let result2 = generateReport([{nombre:"Luis", calificaciones:[75,80,70]}]);
    recordTest("o4.5.2 regular student", result2.studentData.average === 75 && result2.studentData.status === "Regular" && result2.totalPassed === 1);
    
    // o4.5.3: María - Reprobado
    let result3 = generateReport([{nombre:"María", calificaciones:[60,65,55]}]);
    recordTest("o4.5.3 failed student", result3.studentData.average === 60 && result3.studentData.status === "Reprobado" && result3.totalPassed === 0);
    
    // o4.5.4: Carlos - Bueno
    let result4 = generateReport([{nombre:"Carlos", calificaciones:[88,92,85]}]);
    recordTest("o4.5.4 good student", result4.studentData.average === 88.33 && result4.studentData.status === "Bueno" && result4.totalPassed === 1);
    
    // o4.5.5: Elena - Excelente
    let result5 = generateReport([{nombre:"Elena", calificaciones:[95,98,100]}]);
    recordTest("o4.5.5 top student", result5.studentData.average === 97.67 && result5.studentData.status === "Excelente" && result5.totalPassed === 1);
}

// 🚀 Run tests
test_o4_5();

// 📋 Summary
testResults.forEach(result => console.log(result));
```

🧠 **Tips útiles**:

* 📊 Suma todas las calificaciones y divide por la cantidad
* 🎓 Usa rangos de promedio para determinar estado académico
* 🔍 Usa `Math.max(...grades)` y `Math.min(...grades)` para extremos
* ✅ Recorre estudiantes y cuenta los que tienen promedio >= 70

📊 ¡Analiza rendimiento académico como un director! 🎓📈

---

## 🎉 ¡Felicitaciones! Has Completado el Examen de Fundamentos de JavaScript! 🚀✨

### 📋 Resumen del Examen 📊

Has trabajado con:

🎯 **o1 Variables y Tipos de Datos**: Strings, numbers, booleans, arrays, objetos y comparaciones básicas

🚦 **o2 Estructuras Condicionales**: If/else, else if, y lógica de decisiones complejas

🔄 **o3 Bucles y Repetición**: For loops, while loops, bucles anidados y procesamiento de datos

⚙️ **o4 Funciones**: Creación, parámetros, valores de retorno y modularización de código

### 🏆 Criterios de Evaluación 📈

- **Excelente (90-100%)**: Dominio completo de conceptos fundamentales ⭐⭐⭐⭐⭐
- **Bueno (80-89%)**: Sólido entendimiento con pequeños detalles por pulir ⭐⭐⭐⭐
- **Regular (70-79%)**: Conceptos básicos comprendidos, necesita práctica ⭐⭐⭐
- **Necesita Mejora (<70%)**: Requiere estudio adicional de fundamentos ⭐⭐

### 🚀 Próximos Pasos en tu Aprendizaje 🌟

1. **DOM Manipulation**: Interactuar con páginas web 🌐
2. **Eventos**: Manejar clicks, inputs y interacciones 👆
3. **Asincronía**: Promises, async/await y APIs 🔄
4. **Frameworks**: React, Vue o Angular 📚
5. **Backend**: Node.js y Express 🖥️

### 💡 Consejos para Seguir Mejorando 🎯

- **Practica diariamente**: La consistencia es clave 📅
- **Construye proyectos**: Aplica lo aprendido en proyectos reales 🛠️
- **Lee código de otros**: Aprende diferentes enfoques 👥
- **Documenta tu código**: Buenas prácticas desde el inicio 📝
- **Resuelve problemas**: Algoritmos y lógica de programación 🧩

¡Continúa programando y nunca dejes de aprender! 💻🚀✨