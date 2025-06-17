# 🎓✨ JavaScript Modern Exam 🌟📚

Welcome to the ultimate JavaScript-based exam! 🚀 Each week contains 2 exciting challenges 🔥 focused on a specific topic. Students will implement arrow functions, validate inputs, and pass the given tests. Below is Week 1 (o1) with its two lively challenges! 🎉🧩

---

## o1: Variables, Types & Operators Challenges 🔢⚡

### o1.1 🧩 **Smart Calculator with Type Safety** 🔢➕🛡️

---

#### ❓ Problem 🤔

Implement `smartCalculator(a, b, operation)` to perform basic arithmetic operations with **type validation** and **safe error handling**. 🧮✨

---

#### 📜 Description 📖

* **Function**: `const smartCalculator = (a, b, operation) => { ... }` 🛠️
* **Inputs**:
  * `a`: number (any numeric value) 🎯
  * `b`: number (any numeric value) 🎯
  * `operation`: string (`'+', '-', '*', '/'`) 🔤
* **Outputs**:
  * **result**: calculated value as number 🔢
  * **error**: return `null` if inputs invalid or division by zero ❌
* **Expected Operations**: Addition, subtraction, multiplication, division ➕➖✖️➗
* **Edge cases**:
  * Division by zero → return `null` ⚠️
  * Invalid operation string → return `null` ❌
  * Non-numeric inputs → return `null` 🚫
* **Constraints**:
  * Must use **arrow function** syntax ✔️
  * Use **typeof** for type checking 🔍
  * Use **ternary operators** where possible 🔄
* **Input validation**:
  * Check if `a` and `b` are numbers using `typeof` and `isNaN()` 🧐
  * Validate `operation` is one of the allowed strings 📝

---

#### 🧪 Tests to Pass ✅

1. **o1.1.1**: Ideal case 1 🌱
   * Input: `a = 10, b = 5, operation = '+'`
   * Expect: returns `15` ✅
2. **o1.1.2**: Ideal case 2 🌟
   * Input: `a = 20, b = 4, operation = '/'`
   * Expect: returns `5` ✅
3. **o1.1.3**: Ideal case 3 🔥
   * Input: `a = 7, b = 3, operation = '*'`
   * Expect: returns `21` ✅
4. **o1.1.4**: Type-check test 🧐
   * Input: `a = 8, b = 2, operation = '-'`
   * Verify: return type is `number` 🆗
5. **o1.1.5**: Error-handling test ⚠️
   * Input: `a = 10, b = 0, operation = '/'` and `a = "hello", b = 5, operation = '+'`
   * Expect: returns `null` for both cases ❌

---

#### 💻 Base Code 🖥️

```javascript
// 📝 Global test harness
const testResults = [];
const recordTest = (name, cond) =>
  testResults.push(`${cond ? '✅' : '❌'} ${name}`);

const smartCalculator = (a, b, operation) => {
  // 🛠️ Your solution here
  return;
};

// 🧪 Tests to Pass ✅
const test_o1_1 = () => {
  // o1.1.1: Addition case
  recordTest('o1.1.1 — 10 + 5 = 15', smartCalculator(10, 5, '+') === 15);

  // o1.1.2: Division case
  recordTest('o1.1.2 — 20 / 4 = 5', smartCalculator(20, 4, '/') === 5);

  // o1.1.3: Multiplication case
  recordTest('o1.1.3 — 7 * 3 = 21', smartCalculator(7, 3, '*') === 21);

  // o1.1.4: Type verification
  const result = smartCalculator(8, 2, '-');
  recordTest('o1.1.4 — returns number type', typeof result === 'number');

  // o1.1.5: Error handling
  const divByZero = smartCalculator(10, 0, '/');
  const invalidType = smartCalculator("hello", 5, '+');
  recordTest('o1.1.5 — handles errors correctly',
    divByZero === null && invalidType === null);
};

// 🚀 Run tests
test_o1_1();

// 📋 Summary
testResults.forEach(r => console.log(r));
```

---

#### 💡 Tips ✨

* Use **ternary operators** for clean validation:
  ```javascript
  const isValidNumber = (num) => typeof num === 'number' && !isNaN(num);
  ```
* **Switch** or **object lookup** for operations:
  ```javascript
  const operations = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => b !== 0 ? a / b : null
  };
  ```
* **Early returns** for invalid inputs 🔄
* Use **const** for immutable values 🔒

---

#### 🧠 Motivation 💭

* **Type safety** is crucial in JavaScript for preventing runtime errors 🛡️
* **Input validation** mirrors real-world API development practices 🌐
* **Ternary operators** and **arrow functions** showcase modern ES6+ syntax 🚀
* Foundation for building robust calculator apps and form validation 📱

---

### o1.2 🧩 **String Manipulator with Destructuring** 🔤✨🎯

---

#### ❓ Problem 🤔

Implement `stringStats(text)` to analyze a string and return an object with various statistics using **destructuring** and **modern JavaScript features**. 📊🔤

---

#### 📜 Description 📖

* **Function**: `const stringStats = (text) => { ... }` 🛠️
* **Inputs**:
  * `text`: string to analyze 📝
* **Outputs**:
  * **object**: `{ length, words, vowels, consonants, firstChar, lastChar }` 📦
  * **error**: return `null` if input invalid ❌
* **Expected Properties**:
  * `length`: total character count 🔢
  * `words`: number of words (split by spaces) 📊
  * `vowels`: count of vowels (a,e,i,o,u - case insensitive) 🔤
  * `consonants`: count of consonants (letters that aren't vowels) 🎯
  * `firstChar`: first character of string 🥇
  * `lastChar`: last character of string 🏁
* **Edge cases**:
  * Empty string → return object with zero/empty values ⚠️
  * Single character → handle gracefully 🔧
  * Numbers and special characters → count as neither vowels nor consonants 🔍
* **Constraints**:
  * Must use **destructuring** in the implementation ✔️
  * Use **arrow functions** for helper logic 🔄
  * Use **template literals** where helpful 📝
* **Input validation**:
  * If `text` is not a string, return `null` ❌

---

#### 🧪 Tests to Pass ✅

1. **o1.2.1**: Ideal case 1 🌱
   * Input: `text = "Hello World"`
   * Expect: returns `{ length: 11, words: 2, vowels: 3, consonants: 7, firstChar: 'H', lastChar: 'd' }` ✅
2. **o1.2.2**: Ideal case 2 🌟
   * Input: `text = "JavaScript"`
   * Expect: `vowels: 3, consonants: 7` ✅
3. **o1.2.3**: Ideal case 3 🔥
   * Input: `text = "a"`
   * Expect: `{ length: 1, words: 1, vowels: 1, consonants: 0, firstChar: 'a', lastChar: 'a' }` ✅
4. **o1.2.4**: Type-check test 🧐
   * Input: `text = "test"`
   * Verify: return is an object with correct properties 🆗
5. **o1.2.5**: Error-handling test ⚠️
   * Input: `text = 123` and `text = null`
   * Expect: returns `null` for both cases ❌

---

#### 💻 Base Code 🖥️

```javascript
// 📝 Global test harness continues...
const stringStats = (text) => {
  // 🛠️ Your solution here
  return;
};

// 🧪 Tests to Pass ✅
const test_o1_2 = () => {
  // o1.2.1: Basic string analysis
  const result1 = stringStats("Hello World");
  const expected1 = { length: 11, words: 2, vowels: 3, consonants: 7, firstChar: 'H', lastChar: 'd' };
  recordTest('o1.2.1 — "Hello World" analysis', 
    JSON.stringify(result1) === JSON.stringify(expected1));
  
  // o1.2.2: Vowel/consonant count
  const result2 = stringStats("JavaScript");
  recordTest('o1.2.2 — "JavaScript" vowels=3, consonants=7', 
    result2.vowels === 3 && result2.consonants === 7);
  
  // o1.2.3: Single character
  const result3 = stringStats("a");
  recordTest('o1.2.3 — single char "a"', 
    result3.length === 1 && result3.vowels === 1 && result3.consonants === 0);
  
  // o1.2.4: Type verification
  const result4 = stringStats("test");
  recordTest('o1.2.4 — returns object with properties', 
    typeof result4 === 'object' && result4.hasOwnProperty('length') && result4.hasOwnProperty('vowels'));
  
  // o1.2.5: Error handling
  const invalid1 = stringStats(123);
  const invalid2 = stringStats(null);
  recordTest('o1.2.5 — handles invalid inputs', 
    invalid1 === null && invalid2 === null);
};

// 🚀 Run tests
test_o1_2();

// 📋 Summary
testResults.forEach(r => console.log(r));
```

---

#### 💡 Tips ✨

* Use **destructuring** to extract string properties:
  ```javascript
  const [firstChar, ...restChars] = text;
  const lastChar = text[text.length - 1];
  ```
* **Array methods** with **arrow functions**:
  ```javascript
  const vowelCount = [...text.toLowerCase()].filter(char => 'aeiou'.includes(char)).length;
  ```
* **Spread operator** to convert string to array:
  ```javascript
  const chars = [...text];
  ```
* **Template literals** for cleaner string operations 📝
* **Regular expressions** for word counting:
  ```javascript
  const words = text.trim().split(/\s+/).length;
  ```

---

#### 🧠 Motivation 💭

* **Destructuring** and **spread syntax** are essential modern JavaScript features 🚀
* **String analysis** is fundamental for text processing and validation 📝
* **Object creation** with computed properties mirrors real API responses 🌐
* **Functional programming** patterns with array methods build cleaner code 🧹
* Useful for building text editors, form validators, and content analyzers 📊
