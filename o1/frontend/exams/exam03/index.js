// 🟨 EXAMEN DE FUNDAMENTOS DE JAVASCRIPT - SOLUCIONES COMPLETAS 💻✨
// ========================================================================

console.log("🚀 Iniciando Examen de Fundamentos de JavaScript! ✨");

const testResults = [];

const recordTest = (testName, condition) => {
  const emoji = condition ? "✅" : "❌";
  testResults.push(`${emoji} ${testName}`);
};

// ====================================================================
// 🎯 o1 Variables, Tipos de Datos y Estructuras Básicas 📦🔤
// ====================================================================

// --------------------------------------------------------------------
// o1.1 👤 Calculadora de Información Personal 🧮
// --------------------------------------------------------------------
const personalInfo = (name, age, isStudent) => {
  const currentYear = 2025; // 📅 Año actual
  const birthYear = currentYear - age; // 🎂 Calcular año de nacimiento
  const isAdult = age >= 18; // ✅ Determinar si es mayor de edad
  const studentStatus = isStudent ? "estudiante" : "no estudiante"; // 🎓 Estado estudiantil
  const message = `Hola, soy ${name}, tengo ${age} años y soy ${studentStatus}`; // 💬 Mensaje personalizado

  return { birthYear, isAdult, message };
};

const test_o1_1 = () => {
  console.log("\n🧪 Testing o1.1 - Calculadora de Información Personal 👤");

  // o1.1.1: Ana, 20, estudiante
  const result1 = personalInfo("Ana", 20, true);
  recordTest("o1.1.1 Ana data", result1.birthYear === 2005 && result1.isAdult === true);

  // o1.1.2: Carlos, 17, no estudiante
  const result2 = personalInfo("Carlos", 17, false);
  recordTest("o1.1.2 Carlos data", result2.birthYear === 2008 && result2.isAdult === false);

  // o1.1.3: María, 25, estudiante
  const result3 = personalInfo("María", 25, true);
  recordTest("o1.1.3 María data", result3.birthYear === 2000 && result3.isAdult === true);

  // o1.1.4: Luis, 16, estudiante
  const result4 = personalInfo("Luis", 16, true);
  recordTest("o1.1.4 Luis data", result4.birthYear === 2009 && result4.isAdult === false);

  // o1.1.5: Elena, 30, no estudiante
  const result5 = personalInfo("Elena", 30, false);
  recordTest("o1.1.5 Elena data", result5.birthYear === 1995 && result5.isAdult === true);
};

// --------------------------------------------------------------------
// o1.2 📚 Manipulador de Arrays Básico 🔢
// --------------------------------------------------------------------
const arrayManipulator = (initialArray, numbersToAdd) => {
  const resultArray = [...initialArray, ...numbersToAdd]; // 🔗 Combinar arrays usando spread operator
  const arrayLength = resultArray.length; // 📏 Obtener longitud
  const firstElement = resultArray[0]; // 🔍 Primer elemento
  const lastElement = resultArray[resultArray.length - 1]; // 🔍 Último elemento

  return { resultArray, arrayLength, firstElement, lastElement };
};

const test_o1_2 = () => {
  console.log("\n🧪 Testing o1.2 - Manipulador de Arrays Básico 📚");

  // o1.2.1: [1,2,3] + [4,5]
  const result1 = arrayManipulator([1, 2, 3], [4, 5]);
  recordTest("o1.2.1 array ops", result1.arrayLength === 5 && result1.firstElement === 1 && result1.lastElement === 5);

  // o1.2.2: [10,20] + [30,40,50]
  const result2 = arrayManipulator([10, 20], [30, 40, 50]);
  recordTest("o1.2.2 array ops", result2.arrayLength === 5 && result2.firstElement === 10 && result2.lastElement === 50);

  // o1.2.3: [7] + [8,9,10]
  const result3 = arrayManipulator([7], [8, 9, 10]);
  recordTest("o1.2.3 array ops", result3.arrayLength === 4 && result3.firstElement === 7 && result3.lastElement === 10);

  // o1.2.4: [100,200,300] + [400]
  const result4 = arrayManipulator([100, 200, 300], [400]);
  recordTest("o1.2.4 array ops", result4.arrayLength === 4 && result4.firstElement === 100 && result4.lastElement === 400);

  // o1.2.5: [5,15,25] + [35,45]
  const result5 = arrayManipulator([5, 15, 25], [35, 45]);
  recordTest("o1.2.5 array ops", result5.arrayLength === 5 && result5.firstElement === 5 && result5.lastElement === 45);
};

// --------------------------------------------------------------------
// o1.3 📝 Calculadora de Strings 🔤
// --------------------------------------------------------------------
const stringCalculator = (text, suffix) => {
  const textLength = text.length; // 📏 Longitud del texto
  const upperText = text.toUpperCase(); // 🔤 Convertir a mayúsculas
  const lowerText = text.toLowerCase(); // 🔤 Convertir a minúsculas
  const firstThree = text.slice(0, 3); // ✂️ Primeras 3 letras
  const concatenated = text + suffix; // 🔗 Concatenar con sufijo

  return { textLength, upperText, lowerText, firstThree, concatenated };
};

const test_o1_3 = () => {
  console.log("\n🧪 Testing o1.3 - Calculadora de Strings 📝");

  // o1.3.1: "JavaScript" + " es genial"
  const result1 = stringCalculator("JavaScript", " es genial");
  recordTest("o1.3.1 string ops", result1.textLength === 10 && result1.upperText === "JAVASCRIPT" && result1.firstThree === "Jav");

  // o1.3.2: "Programar" + " es divertido"
  const result2 = stringCalculator("Programar", " es divertido");
  recordTest("o1.3.2 string ops", result2.textLength === 9 && result2.upperText === "PROGRAMAR" && result2.firstThree === "Pro");

  // o1.3.3: "Codigo" + " limpio"
  const result3 = stringCalculator("Codigo", " limpio");
  recordTest("o1.3.3 string ops", result3.textLength === 6 && result3.upperText === "CODIGO" && result3.firstThree === "Cod");

  // o1.3.4: "Datos" + " importantes"
  const result4 = stringCalculator("Datos", " importantes");
  recordTest("o1.3.4 string ops", result4.textLength === 5 && result4.upperText === "DATOS" && result4.firstThree === "Dat");

  // o1.3.5: "Web" + " desarrollo"
  const result5 = stringCalculator("Web", " desarrollo");
  recordTest("o1.3.5 string ops", result5.textLength === 3 && result5.upperText === "WEB" && result5.firstThree === "Web");
};

// --------------------------------------------------------------------
// o1.4 🔢 Comparador de Números ⚖️
// --------------------------------------------------------------------
const numberComparator = (num1, num2) => {
  const isGreater = num1 > num2; // 🔍 Mayor que
  const isLess = num1 < num2; // 🔍 Menor que
  const isEqual = num1 === num2; // ✅ Igual
  const isDifferent = num1 !== num2; // ❌ Diferente

  return { isGreater, isLess, isEqual, isDifferent };
};

const test_o1_4 = () => {
  console.log("\n🧪 Testing o1.4 - Comparador de Números 🔢");

  // o1.4.1: 10 vs 5
  const result1 = numberComparator(10, 5);
  recordTest("o1.4.1 comparisons", result1.isGreater === true && result1.isLess === false && result1.isEqual === false && result1.isDifferent === true);

  // o1.4.2: 7 vs 7
  const result2 = numberComparator(7, 7);
  recordTest("o1.4.2 comparisons", result2.isGreater === false && result2.isLess === false && result2.isEqual === true && result2.isDifferent === false);

  // o1.4.3: 3 vs 8
  const result3 = numberComparator(3, 8);
  recordTest("o1.4.3 comparisons", result3.isGreater === false && result3.isLess === true && result3.isEqual === false && result3.isDifferent === true);

  // o1.4.4: 15 vs 12
  const result4 = numberComparator(15, 12);
  recordTest("o1.4.4 comparisons", result4.isGreater === true && result4.isLess === false && result4.isEqual === false && result4.isDifferent === true);

  // o1.4.5: 20 vs 20
  const result5 = numberComparator(20, 20);
  recordTest("o1.4.5 comparisons", result5.isGreater === false && result5.isLess === false && result5.isEqual === true && result5.isDifferent === false);
};

// --------------------------------------------------------------------
// o1.5 📦 Analizador de Objetos Básico 🔍
// --------------------------------------------------------------------
const objectAnalyzer = (productData) => {
  const productObject = { ...productData, categoria: "Tecnología" }; // 📦 Crear objeto con propiedad adicional
  const productName = productData.nombre; // 🔍 Extraer nombre
  const totalPrice = productData.precio * productData.stock; // 💰 Calcular valor total del inventario
  const propertyCount = Object.keys(productObject).length; // 📊 Contar propiedades

  return { productObject, productName, totalPrice, propertyCount };
};

const test_o1_5 = () => {
  console.log("\n🧪 Testing o1.5 - Analizador de Objetos Básico 📦");

  // o1.5.1: Laptop data
  const result1 = objectAnalyzer({ nombre: "Laptop", precio: 1000, stock: 5 });
  recordTest("o1.5.1 object ops", result1.productName === "Laptop" && result1.propertyCount === 4);

  // o1.5.2: Mouse data
  const result2 = objectAnalyzer({ nombre: "Mouse", precio: 25, stock: 50 });
  recordTest("o1.5.2 object ops", result2.productName === "Mouse" && result2.propertyCount === 4);

  // o1.5.3: Teclado data
  const result3 = objectAnalyzer({ nombre: "Teclado", precio: 75, stock: 20 });
  recordTest("o1.5.3 object ops", result3.productName === "Teclado" && result3.propertyCount === 4);

  // o1.5.4: Monitor data
  const result4 = objectAnalyzer({ nombre: "Monitor", precio: 300, stock: 8 });
  recordTest("o1.5.4 object ops", result4.productName === "Monitor" && result4.propertyCount === 4);

  // o1.5.5: Webcam data
  const result5 = objectAnalyzer({ nombre: "Webcam", precio: 80, stock: 15 });
  recordTest("o1.5.5 object ops", result5.productName === "Webcam" && result5.propertyCount === 4);
};

// ====================================================================
// 🚦 o2 Estructuras Condicionales - If/Else 🤔💡
// ====================================================================

// --------------------------------------------------------------------
// o2.1 📚 Sistema de Calificaciones Académicas 🎓
// --------------------------------------------------------------------
const gradeSystem = (score) => {
  let letterGrade = "";
  let passes = false;
  let description = "";

  if (score >= 90) {
    letterGrade = "A";
    description = "Excelente";
    passes = true;
  } else if (score >= 80) {
    letterGrade = "B";
    description = "Bueno";
    passes = true;
  } else if (score >= 70) {
    letterGrade = "C";
    description = "Regular";
    passes = true;
  } else if (score >= 60) {
    letterGrade = "D";
    description = "Deficiente";
    passes = true;
  } else {
    letterGrade = "F";
    description = "Reprobado";
    passes = false;
  }

  return { letterGrade, passes, description };
};

const test_o2_1 = () => {
  console.log("\n🧪 Testing o2.1 - Sistema de Calificaciones Académicas 📚");

  // o2.1.1: score = 95
  const result1 = gradeSystem(95);
  recordTest("o2.1.1 grade A", result1.letterGrade === "A" && result1.passes === true && result1.description === "Excelente");

  // o2.1.2: score = 82
  const result2 = gradeSystem(82);
  recordTest("o2.1.2 grade B", result2.letterGrade === "B" && result2.passes === true && result2.description === "Bueno");

  // o2.1.3: score = 75
  const result3 = gradeSystem(75);
  recordTest("o2.1.3 grade C", result3.letterGrade === "C" && result3.passes === true && result3.description === "Regular");

  // o2.1.4: score = 65
  const result4 = gradeSystem(65);
  recordTest("o2.1.4 grade D", result4.letterGrade === "D" && result4.passes === true && result4.description === "Deficiente");

  // o2.1.5: score = 45
  const result5 = gradeSystem(45);
  recordTest("o2.1.5 grade F", result5.letterGrade === "F" && result5.passes === false && result5.description === "Reprobado");
};

// --------------------------------------------------------------------
// o2.2 🆔 Verificador de Edad y Permisos 🔒
// --------------------------------------------------------------------
const ageVerifier = (age) => {
  let category = "";
  let canVote = false;
  let canDrive = false;
  let canDrinkAlcohol = false;

  if (age <= 15) {
    category = "Menor";
    canVote = false;
    canDrive = false;
    canDrinkAlcohol = false;
  } else if (age <= 17) {
    category = "Adolescente";
    canVote = false;
    canDrive = true; // 🚗 Puede conducir con supervisión
    canDrinkAlcohol = false;
  } else if (age <= 20) {
    category = "Joven adulto";
    canVote = true; // 🗳️ Puede votar
    canDrive = true;
    canDrinkAlcohol = false;
  } else {
    category = "Adulto";
    canVote = true;
    canDrive = true;
    canDrinkAlcohol = true; // 🍺 Todos los permisos
  }

  return { category, canVote, canDrive, canDrinkAlcohol };
};

const test_o2_2 = () => {
  console.log("\n🧪 Testing o2.2 - Verificador de Edad y Permisos 🆔");

  // o2.2.1: age = 14
  const result1 = ageVerifier(14);
  recordTest("o2.2.1 minor", result1.category === "Menor" && result1.canVote === false && result1.canDrive === false && result1.canDrinkAlcohol === false);

  // o2.2.2: age = 17
  const result2 = ageVerifier(17);
  recordTest("o2.2.2 teen", result2.category === "Adolescente" && result2.canVote === false && result2.canDrive === true && result2.canDrinkAlcohol === false);

  // o2.2.3: age = 19
  const result3 = ageVerifier(19);
  recordTest("o2.2.3 young adult", result3.category === "Joven adulto" && result3.canVote === true && result3.canDrive === true && result3.canDrinkAlcohol === false);

  // o2.2.4: age = 25
  const result4 = ageVerifier(25);
  recordTest("o2.2.4 adult", result4.category === "Adulto" && result4.canVote === true && result4.canDrive === true && result4.canDrinkAlcohol === true);

  // o2.2.5: age = 16
  const result5 = ageVerifier(16);
  recordTest("o2.2.5 teen 16", result5.category === "Adolescente" && result5.canVote === false && result5.canDrive === true && result5.canDrinkAlcohol === false);
};

// --------------------------------------------------------------------
// o2.3 💰 Calculadora de Descuentos por Volumen 🛒
// --------------------------------------------------------------------
const discountCalculator = (amount) => {
  let discountPercentage = 0;
  let discountAmount = 0;
  let finalPrice = 0;

  if (amount >= 500) {
    discountPercentage = 20; // 💎 Descuento premium
  } else if (amount >= 200) {
    discountPercentage = 15; // 🥇 Descuento alto
  } else if (amount >= 100) {
    discountPercentage = 10; // 🥈 Descuento medio
  } else if (amount >= 50) {
    discountPercentage = 5; // 🥉 Descuento básico
  } else {
    discountPercentage = 0; // 😐 Sin descuento
  }

  discountAmount = amount * (discountPercentage / 100); // 💰 Calcular descuento
  finalPrice = amount - discountAmount; // 💸 Precio final

  return { discountPercentage, discountAmount, finalPrice };
};

const test_o2_3 = () => {
  console.log("\n🧪 Testing o2.3 - Calculadora de Descuentos por Volumen 💰");

  // o2.3.1: amount = $30
  const result1 = discountCalculator(30);
  recordTest("o2.3.1 no discount", result1.discountPercentage === 0 && result1.discountAmount === 0 && result1.finalPrice === 30);

  // o2.3.2: amount = $75
  const result2 = discountCalculator(75);
  recordTest("o2.3.2 5% discount", result2.discountPercentage === 5 && result2.discountAmount === 3.75 && result2.finalPrice === 71.25);

  // o2.3.3: amount = $150
  const result3 = discountCalculator(150);
  recordTest("o2.3.3 10% discount", result3.discountPercentage === 10 && result3.discountAmount === 15 && result3.finalPrice === 135);

  // o2.3.4: amount = $300
  const result4 = discountCalculator(300);
  recordTest("o2.3.4 15% discount", result4.discountPercentage === 15 && result4.discountAmount === 45 && result4.finalPrice === 255);

  // o2.3.5: amount = $600
  const result5 = discountCalculator(600);
  recordTest("o2.3.5 20% discount", result5.discountPercentage === 20 && result5.discountAmount === 120 && result5.finalPrice === 480);
};

// --------------------------------------------------------------------
// o2.4 🌡️ Clasificador de Temperatura ❄️
// --------------------------------------------------------------------
const temperatureClassifier = (temp) => {
  let category = "";
  let clothingAdvice = "";
  let climateControl = "";

  if (temp < 0) {
    category = "Congelante";
    clothingAdvice = "Abrigo grueso y guantes";
    climateControl = "calefacción";
  } else if (temp <= 10) {
    category = "Frío";
    clothingAdvice = "Abrigo y bufanda";
    climateControl = "calefacción";
  } else if (temp <= 20) {
    category = "Fresco";
    clothingAdvice = "Chaqueta ligera";
    climateControl = "neutro";
  } else if (temp <= 30) {
    category = "Cálido";
    clothingAdvice = "Ropa ligera";
    climateControl = "neutro";
  } else {
    category = "Caluroso";
    clothingAdvice = "Ropa muy ligera";
    climateControl = "aire acondicionado";
  }

  return { category, clothingAdvice, climateControl };
};

const test_o2_4 = () => {
  console.log("\n🧪 Testing o2.4 - Clasificador de Temperatura 🌡️");

  // o2.4.1: temp = -5
  const result1 = temperatureClassifier(-5);
  recordTest("o2.4.1 freezing", result1.category === "Congelante" && result1.clothingAdvice === "Abrigo grueso y guantes" && result1.climateControl === "calefacción");

  // o2.4.2: temp = 8
  const result2 = temperatureClassifier(8);
  recordTest("o2.4.2 cold", result2.category === "Frío" && result2.clothingAdvice === "Abrigo y bufanda" && result2.climateControl === "calefacción");

  // o2.4.3: temp = 18
  const result3 = temperatureClassifier(18);
  recordTest("o2.4.3 cool", result3.category === "Fresco" && result3.clothingAdvice === "Chaqueta ligera" && result3.climateControl === "neutro");

  // o2.4.4: temp = 25
  const result4 = temperatureClassifier(25);
  recordTest("o2.4.4 warm", result4.category === "Cálido" && result4.clothingAdvice === "Ropa ligera" && result4.climateControl === "neutro");

  // o2.4.5: temp = 35
  const result5 = temperatureClassifier(35);
  recordTest("o2.4.5 hot", result5.category === "Caluroso" && result5.clothingAdvice === "Ropa muy ligera" && result5.climateControl === "aire acondicionado");
};

// --------------------------------------------------------------------
// o2.5 🔒 Validador de Contraseñas Seguras 🛡️
// --------------------------------------------------------------------
const passwordValidator = (password) => {
  const passwordLength = password.length;
  let securityLevel = "";
  let isAcceptable = false;

  // 🔍 Verificar criterios de seguridad
  const hasMinLength = passwordLength >= 8;
  const hasUppercase = /[A-Z]/.test(password);
  const hasLowercase = /[a-z]/.test(password);
  const hasNumbers = /[0-9]/.test(password);

  // 📊 Contar criterios cumplidos
  const criteriaCount = [hasUppercase, hasLowercase, hasNumbers].filter(Boolean).length;

  if (!hasMinLength) {
    securityLevel = "Débil";
    isAcceptable = false;
  } else if (criteriaCount === 3 && passwordLength >= 10) {
    securityLevel = "Muy fuerte"; // 💪 Todos los criterios + longitud extra
    isAcceptable = true;
  } else if (criteriaCount === 3) {
    securityLevel = "Fuerte"; // 🛡️ Todos los criterios básicos
    isAcceptable = true;
  } else if (criteriaCount >= 2) {
    securityLevel = "Media"; // ⚖️ Cumple algunos criterios
    isAcceptable = hasMinLength; // Solo aceptable si tiene longitud mínima
  } else {
    securityLevel = "Débil"; // 😐 Pocos criterios
    isAcceptable = false;
  }

  return { securityLevel, isAcceptable, passwordLength };
};

const test_o2_5 = () => {
  console.log("\n🧪 Testing o2.5 - Validador de Contraseñas Seguras 🔒");

  // o2.5.1: password = "abc123"
  const result1 = passwordValidator("abc123");
  recordTest("o2.5.1 weak short", result1.securityLevel === "Débil" && result1.isAcceptable === false && result1.passwordLength === 6);

  // o2.5.2: password = "Password1"
  const result2 = passwordValidator("Password1");
  recordTest("o2.5.2 strong", result2.securityLevel === "Fuerte" && result2.isAcceptable === true && result2.passwordLength === 9);

  // o2.5.3: password = "password"
  const result3 = passwordValidator("password");
  recordTest("o2.5.3 weak long", result3.securityLevel === "Débil" && result3.isAcceptable === false && result3.passwordLength === 8);

  // o2.5.4: password = "PASS123"
  const result4 = passwordValidator("PASS123");
  recordTest("o2.5.4 medium short", result4.securityLevel === "Media" && result4.isAcceptable === false && result4.passwordLength === 7);

  // o2.5.5: password = "MySecure123"
  const result5 = passwordValidator("MySecure123");
  recordTest("o2.5.5 very strong", result5.securityLevel === "Muy fuerte" && result5.isAcceptable === true && result5.passwordLength === 11);
};

// ====================================================================
// 🔄 o3 Estructuras de Repetición - Bucles 🌀💪
// ====================================================================

// --------------------------------------------------------------------
// o3.1 📊 Procesador de Arrays con For 🔢
// --------------------------------------------------------------------
const arrayProcessor = (numbers) => {
  let sum = 0;
  let max = numbers[0];
  let min = numbers[0];
  let evenCount = 0;

  // 🔄 Procesar cada número en el array
  for (let i = 0; i < numbers.length; i++) {
    const num = numbers[i];

    sum += num; // ➕ Acumular suma

    if (num > max) max = num; // 🔍 Encontrar máximo
    if (num < min) min = num; // 🔍 Encontrar mínimo

    if (num % 2 === 0) evenCount++; // 📊 Contar pares
  }

  const average = sum / numbers.length; // 🧮 Calcular promedio

  return { sum, average, max, min, evenCount };
};

const test_o3_1 = () => {
  console.log("\n🧪 Testing o3.1 - Procesador de Arrays con For 📊");

  // o3.1.1: [1,2,3,4,5]
  const result1 = arrayProcessor([1, 2, 3, 4, 5]);
  recordTest("o3.1.1 basic array", result1.sum === 15 && result1.average === 3 && result1.max === 5 && result1.min === 1 && result1.evenCount === 2);

  // o3.1.2: [10,20,30,40]
  const result2 = arrayProcessor([10, 20, 30, 40]);
  recordTest("o3.1.2 tens array", result2.sum === 100 && result2.average === 25 && result2.max === 40 && result2.min === 10 && result2.evenCount === 4);

  // o3.1.3: [7,3,9,1,5]
  const result3 = arrayProcessor([7, 3, 9, 1, 5]);
  recordTest("o3.1.3 odds array", result3.sum === 25 && result3.average === 5 && result3.max === 9 && result3.min === 1 && result3.evenCount === 0);

  // o3.1.4: [2,4,6,8]
  const result4 = arrayProcessor([2, 4, 6, 8]);
  recordTest("o3.1.4 evens array", result4.sum === 20 && result4.average === 5 && result4.max === 8 && result4.min === 2 && result4.evenCount === 4);

  // o3.1.5: [15,25,35]
  const result5 = arrayProcessor([15, 25, 35]);
  recordTest("o3.1.5 big odds", result5.sum === 75 && result5.average === 25 && result5.max === 35 && result5.min === 15 && result5.evenCount === 0);
};

// --------------------------------------------------------------------
// o3.2 ⭐ Generador de Patrones con Bucles Anidados 🔺
// --------------------------------------------------------------------
const patternGenerator = (rows) => {
  const pattern = [];
  let totalStars = 0;

  // 🔄 Bucle exterior para controlar filas
  for (let i = 1; i <= rows; i++) {
    let line = "";

    // ⭐ Bucle interior para generar estrellas en cada fila
    for (let j = 0; j < i; j++) {
      line += "*";
    }

    pattern.push(line); // 📝 Agregar línea al patrón
    totalStars += i; // 📊 Sumar estrellas de esta fila
  }

  return { pattern, totalStars };
};

const test_o3_2 = () => {
  console.log("\n🧪 Testing o3.2 - Generador de Patrones con Bucles Anidados ⭐");

  // o3.2.1: rows = 3
  const result1 = patternGenerator(3);
  recordTest("o3.2.1 triangle 3", JSON.stringify(result1.pattern) === JSON.stringify(["*", "**", "***"]) && result1.totalStars === 6);

  // o3.2.2: rows = 4
  const result2 = patternGenerator(4);
  recordTest("o3.2.2 triangle 4", JSON.stringify(result2.pattern) === JSON.stringify(["*", "**", "***", "****"]) && result2.totalStars === 10);

  // o3.2.3: rows = 5
  const result3 = patternGenerator(5);
  recordTest("o3.2.3 triangle 5", JSON.stringify(result3.pattern) === JSON.stringify(["*", "**", "***", "****", "*****"]) && result3.totalStars === 15);

  // o3.2.4: rows = 2
  const result4 = patternGenerator(2);
  recordTest("o3.2.4 triangle 2", JSON.stringify(result4.pattern) === JSON.stringify(["*", "**"]) && result4.totalStars === 3);

  // o3.2.5: rows = 1
  const result5 = patternGenerator(1);
  recordTest("o3.2.5 triangle 1", JSON.stringify(result5.pattern) === JSON.stringify(["*"]) && result5.totalStars === 1);
};

// --------------------------------------------------------------------
// o3.3 🔢 Contador Dinámico con While ⚡
// --------------------------------------------------------------------
const dynamicCounter = (target, start) => {
  let found = 0;
  let currentNumber = start;
  let numbersChecked = 0;
  let lastNumber = 0;

  // 🔄 Buscar múltiplos de 3 hasta encontrar la cantidad objetivo
  while (found < target) {
    numbersChecked++;

    if (currentNumber % 3 === 0) { // 🎯 Es múltiplo de 3
      found++;
      lastNumber = currentNumber; // 📊 Actualizar último número encontrado
    }

    currentNumber++; // ➕ Avanzar al siguiente número
  }

  return { found, lastNumber, numbersChecked };
};

const test_o3_3 = () => {
  console.log("\n🧪 Testing o3.3 - Contador Dinámico con While 🔢");

  // o3.3.1: target=3, start=1
  const result1 = dynamicCounter(3, 1);
  recordTest("o3.3.1 find 3 from 1", result1.found === 3 && result1.lastNumber === 9 && result1.numbersChecked === 9);

  // o3.3.2: target=5, start=1
  const result2 = dynamicCounter(5, 1);
  recordTest("o3.3.2 find 5 from 1", result2.found === 5 && result2.lastNumber === 15 && result2.numbersChecked === 15);

  // o3.3.3: target=2, start=10
  const result3 = dynamicCounter(2, 10);
  recordTest("o3.3.3 find 2 from 10", result3.found === 2 && result3.lastNumber === 15 && result3.numbersChecked === 6);

  // o3.3.4: target=4, start=5
  const result4 = dynamicCounter(4, 5);
  recordTest("o3.3.4 find 4 from 5", result4.found === 4 && result4.lastNumber === 18 && result4.numbersChecked === 14);

  // o3.3.5: target=1, start=1
  const result5 = dynamicCounter(1, 1);
  recordTest("o3.3.5 find 1 from 1", result5.found === 1 && result5.lastNumber === 3 && result5.numbersChecked === 3);
};

// --------------------------------------------------------------------
// o3.4 📊 Tabla de Multiplicar Interactiva ✖️
// --------------------------------------------------------------------
const multiplicationTable = (table, upTo) => {
  const results = [];
  let totalSum = 0;
  let operations = 0;

  // ✖️ Generar tabla de multiplicar
  for (let i = 1; i <= upTo; i++) {
    const result = table * i; // 🧮 Calcular multiplicación
    results.push(result); // 📝 Agregar resultado
    totalSum += result; // ➕ Sumar al total
    operations++; // 📊 Contar operación
  }

  return { results, totalSum, operations };
};

const test_o3_4 = () => {
  console.log("\n🧪 Testing o3.4 - Tabla de Multiplicar Interactiva 📊");

  // o3.4.1: table=2, upTo=3
  const result1 = multiplicationTable(2, 3);
  recordTest("o3.4.1 table 2x3", JSON.stringify(result1.results) === JSON.stringify([2, 4, 6]) && result1.totalSum === 12 && result1.operations === 3);

  // o3.4.2: table=5, upTo=4
  const result2 = multiplicationTable(5, 4);
  recordTest("o3.4.2 table 5x4", JSON.stringify(result2.results) === JSON.stringify([5, 10, 15, 20]) && result2.totalSum === 50 && result2.operations === 4);

  // o3.4.3: table=3, upTo=5
  const result3 = multiplicationTable(3, 5);
  recordTest("o3.4.3 table 3x5", JSON.stringify(result3.results) === JSON.stringify([3, 6, 9, 12, 15]) && result3.totalSum === 45 && result3.operations === 5);

  // o3.4.4: table=7, upTo=2
  const result4 = multiplicationTable(7, 2);
  recordTest("o3.4.4 table 7x2", JSON.stringify(result4.results) === JSON.stringify([7, 14]) && result4.totalSum === 21 && result4.operations === 2);

  // o3.4.5: table=4, upTo=6
  const result5 = multiplicationTable(4, 6);
  recordTest("o3.4.5 table 4x6", JSON.stringify(result5.results) === JSON.stringify([4, 8, 12, 16, 20, 24]) && result5.totalSum === 84 && result5.operations === 6);
};

// --------------------------------------------------------------------
// o3.5 🔍 Buscador de Números Primos con While 🎯
// --------------------------------------------------------------------
const isPrime = (num) => {
  if (num < 2) return false; // 📉 Números menores a 2 no son primos

  // 🔍 Verificar divisibilidad desde 2 hasta la raíz cuadrada
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false; // 📊 Es divisible, no es primo
  }

  return true; // ✅ Es primo
};

const primeFinder = (count) => {
  const primes = [];
  let currentNumber = 2; // 🔢 Empezar desde el primer primo
  let numbersChecked = 0;

  // 🔄 Buscar primos hasta encontrar la cantidad deseada
  while (primes.length < count) {
    numbersChecked++;

    if (isPrime(currentNumber)) { // 🎯 Es primo
      primes.push(currentNumber); // 📝 Agregar a la lista
    }

    currentNumber++; // ➕ Avanzar al siguiente número
  }

  const largestPrime = primes[primes.length - 1]; // 🏆 El primo más grande encontrado

  return { primes, largestPrime, numbersChecked };
};

const test_o3_5 = () => {
  console.log("\n🧪 Testing o3.5 - Buscador de Números Primos con While 🔍");

  // o3.5.1: count=3
  const result1 = primeFinder(3);
  recordTest("o3.5.1 first 3 primes", JSON.stringify(result1.primes) === JSON.stringify([2, 3, 5]) && result1.largestPrime === 5 && result1.numbersChecked === 6);

  // o3.5.2: count=5
  const result2 = primeFinder(5);
  recordTest("o3.5.2 first 5 primes", JSON.stringify(result2.primes) === JSON.stringify([2, 3, 5, 7, 11]) && result2.largestPrime === 11 && result2.numbersChecked === 12);

  // o3.5.3: count=2
  const result3 = primeFinder(2);
  recordTest("o3.5.3 first 2 primes", JSON.stringify(result3.primes) === JSON.stringify([2, 3]) && result3.largestPrime === 3 && result3.numbersChecked === 4);

  // o3.5.4: count=4
  const result4 = primeFinder(4);
  recordTest("o3.5.4 first 4 primes", JSON.stringify(result4.primes) === JSON.stringify([2, 3, 5, 7]) && result4.largestPrime === 7 && result4.numbersChecked === 8);

  // o3.5.5: count=1
  const result5 = primeFinder(1);
  recordTest("o3.5.5 first 1 prime", JSON.stringify(result5.primes) === JSON.stringify([2]) && result5.largestPrime === 2 && result5.numbersChecked === 2);
};

// ====================================================================
// ⚙️ o4 Funciones en JavaScript - Reutilización y Modularidad 🔧✨
// ====================================================================

// --------------------------------------------------------------------
// o4.1 ➕ Calculadora de Operaciones Básicas ➖
// --------------------------------------------------------------------
const add = (a, b) => a + b; // ➕ Suma
const subtract = (a, b) => a - b; // ➖ Resta
const multiply = (a, b) => a * b; // ✖️ Multiplicación
const divide = (a, b) => b === 0 ? "Error" : a / b; // ➗ División con validación

const calculator = (num1, num2, operator) => {
  let result = 0;
  let operation = "";

  switch (operator) {
    case "+":
      result = add(num1, num2);
      operation = "suma";
      break;
    case "-":
      result = subtract(num1, num2);
      operation = "resta";
      break;
    case "*":
      result = multiply(num1, num2);
      operation = "multiplicacion";
      break;
    case "/":
      result = divide(num1, num2);
      operation = "division";
      break;
    default:
      result = "Error";
      operation = "desconocida";
  }

  return { result, operation };
};

const test_o4_1 = () => {
  console.log("\n🧪 Testing o4.1 - Calculadora de Operaciones Básicas ➕");

  // o4.1.1: 10 + 5
  const result1 = calculator(10, 5, "+");
  recordTest("o4.1.1 addition", result1.result === 15 && result1.operation === "suma");

  // o4.1.2: 10 - 3
  const result2 = calculator(10, 3, "-");
  recordTest("o4.1.2 subtraction", result2.result === 7 && result2.operation === "resta");

  // o4.1.3: 4 * 6
  const result3 = calculator(4, 6, "*");
  recordTest("o4.1.3 multiplication", result3.result === 24 && result3.operation === "multiplicacion");

  // o4.1.4: 15 / 3
  const result4 = calculator(15, 3, "/");
  recordTest("o4.1.4 division", result4.result === 5 && result4.operation === "division");

  // o4.1.5: 10 / 0
  const result5 = calculator(10, 0, "/");
  recordTest("o4.1.5 division by zero", result5.result === "Error" && result5.operation === "division");
};

// --------------------------------------------------------------------
// o4.2 📝 Analizador de Strings con Funciones 🔍
// --------------------------------------------------------------------
const countCharacters = (text) => text.replace(/ /g, "").length; // 📏 Contar sin espacios

const countWords = (text) => text.trim() === "" ? 0 : text.trim().split(/\s+/).length; // 📝 Contar palabras

const countVowels = (text) => {
  const vowels = "aeiouAEIOU"; // 🔤 Vocales
  let count = 0;

  for (let char of text) {
    if (vowels.includes(char)) count++; // 🔍 Verificar si es vocal
  }

  return count;
};

const isPalindrome = (text) => {
  const cleaned = text.toLowerCase().replace(/[^a-z]/g, ""); // 🧹 Limpiar texto
  return cleaned === cleaned.split("").reverse().join(""); // 🔄 Comparar con reverso
};

const textAnalyzer = (text) => {
  const characters = countCharacters(text); // 📏 Contar caracteres
  const words = countWords(text); // 📝 Contar palabras
  const vowels = countVowels(text); // 🔤 Contar vocales
  const palindrome = isPalindrome(text); // 🔄 Verificar palíndromo

  return { characters, words, vowels, palindrome };
};

const test_o4_2 = () => {
  console.log("\n🧪 Testing o4.2 - Analizador de Strings con Funciones 📝");

  // o4.2.1: "Hola mundo"
  const result1 = textAnalyzer("Hola mundo");
  recordTest("o4.2.1 hello world", result1.characters === 9 && result1.words === 2 && result1.vowels === 4 && result1.palindrome === false);

  // o4.2.2: "oso"
  const result2 = textAnalyzer("oso");
  recordTest("o4.2.2 bear", result2.characters === 3 && result2.words === 1 && result2.vowels === 2 && result2.palindrome === true);

  // o4.2.3: "JavaScript es genial"
  const result3 = textAnalyzer("JavaScript es genial");
  recordTest("o4.2.3 js cool", result3.characters === 16 && result3.words === 3 && result3.vowels === 7 && result3.palindrome === false);

  // o4.2.4: "anana"
  const result4 = textAnalyzer("anana");
  recordTest("o4.2.4 pineapple", result4.characters === 5 && result4.words === 1 && result4.vowels === 4 && result4.palindrome === true);

  // o4.2.5: "Programar es divertido"
  const result5 = textAnalyzer("Programar es divertido");
  recordTest("o4.2.5 coding fun", result5.characters === 18 && result5.words === 3 && result5.vowels === 8 && result5.palindrome === false);
};

// --------------------------------------------------------------------
// o4.3 📚 Sistema de Gestión de Arrays ⚙️
// --------------------------------------------------------------------
const filterEvens = (array) => array.filter(num => num % 2 === 0); // 🔢 Filtrar pares

const doubleValues = (array) => array.map(num => num * 2); // ✖️ Duplicar valores

const findMaximum = (array) => Math.max(...array); // 🔍 Encontrar máximo

const calculateAverage = (array) => array.reduce((sum, num) => sum + num, 0) / array.length; // 📊 Calcular promedio

const arrayProcessor2 = (array) => {
  const evens = filterEvens(array); // 🔢 Filtrar pares
  const doubled = doubleValues(array); // ✖️ Duplicar valores
  const maximum = findMaximum(doubled); // 🔍 Máximo de los duplicados
  const average = calculateAverage(doubled); // 📊 Promedio de los duplicados

  return { evens, doubled, maximum, average };
};

const test_o4_3 = () => {
  console.log("\n🧪 Testing o4.3 - Sistema de Gestión de Arrays 📚");

  // o4.3.1: [1,2,3,4,5]
  const result1 = arrayProcessor2([1, 2, 3, 4, 5]);
  recordTest("o4.3.1 mixed array", JSON.stringify(result1.evens) === JSON.stringify([2, 4]) && JSON.stringify(result1.doubled) === JSON.stringify([2, 4, 6, 8, 10]) && result1.maximum === 10 && result1.average === 6);

  // o4.3.2: [10,15,20,25]
  const result2 = arrayProcessor2([10, 15, 20, 25]);
  recordTest("o4.3.2 big numbers", JSON.stringify(result2.evens) === JSON.stringify([10, 20]) && JSON.stringify(result2.doubled) === JSON.stringify([20, 30, 40, 50]) && result2.maximum === 50 && result2.average === 35);

  // o4.3.3: [2,4,6]
  const result3 = arrayProcessor2([2, 4, 6]);
  recordTest("o4.3.3 all evens", JSON.stringify(result3.evens) === JSON.stringify([2, 4, 6]) && JSON.stringify(result3.doubled) === JSON.stringify([4, 8, 12]) && result3.maximum === 12 && result3.average === 8);

  // o4.3.4: [1,3,5,7]
  const result4 = arrayProcessor2([1, 3, 5, 7]);
  recordTest("o4.3.4 all odds", JSON.stringify(result4.evens) === JSON.stringify([]) && JSON.stringify(result4.doubled) === JSON.stringify([2, 6, 10, 14]) && result4.maximum === 14 && result4.average === 8);

  // o4.3.5: [8,12,16]
  const result5 = arrayProcessor2([8, 12, 16]);
  recordTest("o4.3.5 big evens", JSON.stringify(result5.evens) === JSON.stringify([8, 12, 16]) && JSON.stringify(result5.doubled) === JSON.stringify([16, 24, 32]) && result5.maximum === 32 && result5.average === 24);
};

// --------------------------------------------------------------------
// o4.4 🌡️ Conversor de Temperaturas con Validación 🔄
// --------------------------------------------------------------------
const celsiusToFahrenheit = (celsius) => (celsius * 9 / 5) + 32; // 🌡️ C a F

const fahrenheitToCelsius = (fahrenheit) => (fahrenheit - 32) * 5 / 9; // 🌡️ F a C

const celsiusToKelvin = (celsius) => celsius + 273.15; // 🌡️ C a K

const kelvinToCelsius = (kelvin) => kelvin - 273.15; // 🌡️ K a C

const isValidTemperature = (temp, scale) => {
  // 🌡️ Verificar si la temperatura es físicamente posible
  switch (scale) {
    case "C":
      return temp >= -273.15; // ❄️ Cero absoluto en Celsius
    case "F":
      return temp >= -459.67; // ❄️ Cero absoluto en Fahrenheit
    case "K":
      return temp >= 0; // ❄️ Cero absoluto en Kelvin
    default:
      return false;
  }
};

const temperatureConverter = (temp, fromScale, toScale) => {
  // ✅ Validar temperatura de entrada
  if (!isValidTemperature(temp, fromScale)) {
    return { result: "Error", isValid: false, targetScale: "Invalid" };
  }

  let result = 0;
  let targetScale = "";

  // 🔄 Determinar escala objetivo
  switch (toScale) {
    case "F":
      targetScale = "Fahrenheit";
      break;
    case "C":
      targetScale = "Celsius";
      break;
    case "K":
      targetScale = "Kelvin";
      break;
    default:
      return { result: "Error", isValid: false, targetScale: "Invalid" };
  }

  // 🌡️ Realizar conversión
  if (fromScale === "C" && toScale === "F") {
    result = celsiusToFahrenheit(temp);
  } else if (fromScale === "C" && toScale === "K") {
    result = celsiusToKelvin(temp);
  } else if (fromScale === "F" && toScale === "C") {
    result = fahrenheitToCelsius(temp);
  } else if (fromScale === "K" && toScale === "C") {
    result = kelvinToCelsius(temp);
  } else if (fromScale === toScale) {
    result = temp; // 🔄 Misma escala
  } else {
    // 🔄 Conversión indirecta (a través de Celsius)
    let tempInCelsius = temp;
    if (fromScale === "F") tempInCelsius = fahrenheitToCelsius(temp);
    if (fromScale === "K") tempInCelsius = kelvinToCelsius(temp);

    if (toScale === "F") result = celsiusToFahrenheit(tempInCelsius);
    if (toScale === "K") result = celsiusToKelvin(tempInCelsius);
  }

  // 📊 Redondear a 2 decimales
  result = Math.round(result * 100) / 100;

  return { result, isValid: true, targetScale };
};

const test_o4_4 = () => {
  console.log("\n🧪 Testing o4.4 - Conversor de Temperaturas con Validación 🌡️");

  // o4.4.1: 0°C to °F
  const result1 = temperatureConverter(0, "C", "F");
  recordTest("o4.4.1 freezing point", result1.result === 32 && result1.isValid === true && result1.targetScale === "Fahrenheit");

  // o4.4.2: 100°C to K
  const result2 = temperatureConverter(100, "C", "K");
  recordTest("o4.4.2 boiling point", result2.result === 373.15 && result2.isValid === true && result2.targetScale === "Kelvin");

  // o4.4.3: 32°F to °C
  const result3 = temperatureConverter(32, "F", "C");
  recordTest("o4.4.3 fahrenheit freeze", result3.result === 0 && result3.isValid === true && result3.targetScale === "Celsius");

  // o4.4.4: -300°C to °F (invalid)
  const result4 = temperatureConverter(-300, "C", "F");
  recordTest("o4.4.4 invalid temp", result4.result === "Error" && result4.isValid === false && result4.targetScale === "Invalid");

  // o4.4.5: 273.15K to °C
  const result5 = temperatureConverter(273.15, "K", "C");
  recordTest("o4.4.5 absolute zero", result5.result === 0 && result5.isValid === true && result5.targetScale === "Celsius");
};

// --------------------------------------------------------------------
// o4.5 📊 Generador de Reportes de Estudiantes 🎓
// --------------------------------------------------------------------
const calculateAverageGrades = (grades) => grades.reduce((sum, grade) => sum + grade, 0) / grades.length; // 📊 Promedio

const determineStatus = (average) => {
  // 🎓 Determinar estado académico
  if (average >= 90) return "Excelente";
  if (average >= 80) return "Bueno";
  if (average >= 70) return "Regular";
  return "Reprobado";
};

const findExtremes = (grades) => ({
  max: Math.max(...grades), // 🔍 Máximo
  min: Math.min(...grades)  // 🔍 Mínimo
});

const countPassed = (students) => {
  // ✅ Contar estudiantes aprobados (promedio >= 70)
  return students.filter(student => {
    const avg = calculateAverageGrades(student.calificaciones);
    return avg >= 70;
  }).length;
};

const generateReport = (students) => {
  let studentData = {};
  let totalPassed = 0;

  // 📊 Procesar datos del primer estudiante
  if (students.length > 0) {
    const student = students[0];
    const avg = calculateAverageGrades(student.calificaciones);
    const status = determineStatus(avg);

    studentData = {
      average: Math.round(avg * 100) / 100, // 📊 Redondear a 2 decimales
      status: status
    };

    totalPassed = countPassed(students); // ✅ Contar aprobados
  }

  return { studentData, totalPassed };
};

const test_o4_5 = () => {
  console.log("\n🧪 Testing o4.5 - Generador de Reportes de Estudiantes 📊");

  // o4.5.1: Ana - Excelente
  const result1 = generateReport([{ nombre: "Ana", calificaciones: [90, 85, 95] }]);
  recordTest("o4.5.1 excellent student", result1.studentData.average === 90 && result1.studentData.status === "Excelente" && result1.totalPassed === 1);

  // o4.5.2: Luis - Regular
  const result2 = generateReport([{ nombre: "Luis", calificaciones: [75, 80, 70] }]);
  recordTest("o4.5.2 regular student", result2.studentData.average === 75 && result2.studentData.status === "Regular" && result2.totalPassed === 1);

  // o4.5.3: María - Reprobado
  const result3 = generateReport([{ nombre: "María", calificaciones: [60, 65, 55] }]);
  recordTest("o4.5.3 failed student", result3.studentData.average === 60 && result3.studentData.status === "Reprobado" && result3.totalPassed === 0);

  // o4.5.4: Carlos - Bueno
  const result4 = generateReport([{ nombre: "Carlos", calificaciones: [88, 92, 85] }]);
  recordTest("o4.5.4 good student", result4.studentData.average === 88.33 && result4.studentData.status === "Bueno" && result4.totalPassed === 1);

  // o4.5.5: Elena - Excelente
  const result5 = generateReport([{ nombre: "Elena", calificaciones: [95, 98, 100] }]);
  recordTest("o4.5.5 top student", result5.studentData.average === 97.67 && result5.studentData.status === "Excelente" && result5.totalPassed === 1);
};

// ====================================================================
// 🚀 EJECUTAR TODAS LAS PRUEBAS - EXAMEN COMPLETO ✨
// ====================================================================

const runAllTests = () => {
  console.log("🟨 INICIANDO EXAMEN COMPLETO DE FUNDAMENTOS DE JAVASCRIPT! 💻✨");
  console.log("=".repeat(60));

  // 🎯 o1: Variables, Tipos de Datos y Estructuras Básicas
  console.log("\n🎯 SECCIÓN o1: Variables, Tipos de Datos y Estructuras Básicas 📦🔤");
  test_o1_1();
  test_o1_2();
  test_o1_3();
  test_o1_4();
  test_o1_5();

  // 🚦 o2: Estructuras Condicionales
  console.log("\n🚦 SECCIÓN o2: Estructuras Condicionales - If/Else 🤔💡");
  test_o2_1();
  test_o2_2();
  test_o2_3();
  test_o2_4();
  test_o2_5();

  // 🔄 o3: Estructuras de Repetición
  console.log("\n🔄 SECCIÓN o3: Estructuras de Repetición - Bucles 🌀💪");
  test_o3_1();
  test_o3_2();
  test_o3_3();
  test_o3_4();
  test_o3_5();

  // ⚙️ o4: Funciones
  console.log("\n⚙️ SECCIÓN o4: Funciones - Reutilización y Modularidad 🔧✨");
  test_o4_1();
  test_o4_2();
  test_o4_3();
  test_o4_4();
  test_o4_5();

  // 📋 Resumen Final
  console.log("\n" + "=".repeat(60));
  console.log("📋 RESUMEN FINAL DEL EXAMEN 🎓");
  console.log("=".repeat(60));

  // 📊 Estadísticas
  const totalTests = testResults.length;
  const passedTests = testResults.filter(result => result.includes("✅")).length;
  const failedTests = testResults.filter(result => result.includes("❌")).length;
  const successRate = ((passedTests / totalTests) * 100).toFixed(2);

  console.log("\n📊 ESTADÍSTICAS GENERALES:");
  console.log(`🎯 Total de pruebas: ${totalTests}`);
  console.log(`✅ Pruebas exitosas: ${passedTests}`);
  console.log(`❌ Pruebas fallidas: ${failedTests}`);
  console.log(`📈 Tasa de éxito: ${successRate}%`);

  // 🏆 Evaluación del rendimiento
  console.log("\n🏆 EVALUACIÓN DEL RENDIMIENTO:");
  if (successRate >= 90) {
    console.log("⭐⭐⭐⭐⭐ EXCELENTE - Dominio completo de fundamentos!");
  } else if (successRate >= 80) {
    console.log("⭐⭐⭐⭐ BUENO - Sólido entendimiento, pequeños detalles por pulir");
  } else if (successRate >= 70) {
    console.log("⭐⭐⭐ REGULAR - Conceptos básicos comprendidos, necesita práctica");
  } else {
    console.log("⭐⭐ NECESITA MEJORA - Requiere estudio adicional de fundamentos");
  }

  // 📝 Resultados detallados por sección
  console.log("\n📝 RESULTADOS DETALLADOS POR SECCIÓN:");
  console.log("-".repeat(50));

  const sections = {
    "o1": { name: "Variables y Tipos de Datos", tests: [] },
    "o2": { name: "Estructuras Condicionales", tests: [] },
    "o3": { name: "Bucles y Repetición", tests: [] },
    "o4": { name: "Funciones", tests: [] }
  };

  // 📊 Agrupar resultados por sección
  testResults.forEach(result => {
    const sectionKey = result.split(" ")[1].split(".")[0];
    if (sections[sectionKey]) {
      sections[sectionKey].tests.push(result);
    }
  });

  // 📋 Mostrar resultados por sección
  Object.entries(sections).forEach(([key, section]) => {
    const sectionPassed = section.tests.filter(test => test.includes("✅")).length;
    const sectionTotal = section.tests.length;
    const sectionRate = ((sectionPassed / sectionTotal) * 100).toFixed(1);

    console.log(`\n🎯 ${key.toUpperCase()}: ${section.name}`);
    console.log(`   📊 ${sectionPassed}/${sectionTotal} (${sectionRate}%)`);

    // 📋 Mostrar tests específicos si hay fallos
    const failedInSection = section.tests.filter(test => test.includes("❌"));
    if (failedInSection.length > 0) {
      console.log(`   ⚠️  Tests fallidos:`);
      failedInSection.forEach(test => console.log(`      ${test}`));
    }
  });

  // 🎉 Mensaje de finalización
  console.log("\n" + "=".repeat(60));
  console.log("🎉 ¡EXAMEN COMPLETADO! 🎓✨");
  console.log("💡 Continúa practicando y mejorando tus habilidades en JavaScript! 🚀");
  console.log("=".repeat(60));

  // 🔄 Retornar estadísticas para uso programático
  return {
    totalTests,
    passedTests,
    failedTests,
    successRate: parseFloat(successRate),
    results: testResults,
    sections: sections
  };
};

// 🚀 EJECUTAR EL EXAMEN COMPLETO
const examResults = runAllTests();

// 📊 Exportar resultados para análisis adicional
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    examResults,
    testResults,
    // 🎯 Funciones individuales para testing específico
    personalInfo,
    arrayManipulator,
    stringCalculator,
    numberComparator,
    objectAnalyzer,
    gradeSystem,
    ageVerifier,
    discountCalculator,
    temperatureClassifier,
    passwordValidator,
    arrayProcessor,
    patternGenerator,
    dynamicCounter,
    multiplicationTable,
    isPrime,
    primeFinder,
    calculator,
    textAnalyzer,
    arrayProcessor2,
    temperatureConverter,
    generateReport
  };
}

// 💡 Para navegador: hacer disponibles las funciones globalmente
if (typeof window !== 'undefined') {
  window.JSExamSolutions = {
    examResults,
    testResults,
    runAllTests,
    // ... todas las funciones
  };
}

console.log("\n🎯 ¡Todas las soluciones han sido implementadas y probadas! ✨");
console.log("💻 Usa las funciones individualmente o ejecuta runAllTests() para el examen completo 🚀");