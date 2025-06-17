// 📝 Global test harness
const testResults = [];
const recordTest = (name, cond) =>
  testResults.push(`${cond ? '✅' : '❌'} ${name}`);

// ====================================================================
// o1 Variables, Types & Operators Challenges 🔢⚡
// ====================================================================

// --------------------------------------------------------------------
// o1.1 🧩 Smart Calculator with Type Safety 🌟
// --------------------------------------------------------------------

const smartCalculator = (a, b, operation) => {
  // Validate inputs using typeof and isNaN
  const isValidNumber = (num) => typeof num === 'number' && !isNaN(num);

  if (!isValidNumber(a) || !isValidNumber(b) || typeof operation !== 'string') {
    return null;
  }

  // Operations object using arrow functions
  const operations = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => b !== 0 ? a / b : null
  };

  // Check if operation exists and execute
  return operations.hasOwnProperty(operation) ? operations[operation](a, b) : null;
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

// --------------------------------------------------------------------
// o1.2 🧩 String Manipulator with Destructuring 🌟
// --------------------------------------------------------------------

const stringStats = (text) => {
  // Input validation
  if (typeof text !== 'string') return null;

  // Handle empty string edge case
  if (text.length === 0) {
    return {
      length: 0,
      words: 0,
      vowels: 0,
      consonants: 0,
      firstChar: '',
      lastChar: ''
    };
  }

  // Destructuring for first and last character
  const [firstChar] = text;
  const lastChar = text[text.length - 1];

  // Word count using regex to handle multiple spaces
  const words = text.trim() === '' ? 0 : text.trim().split(/\s+/).length;

  // Convert to array for easier processing
  const chars = [...text.toLowerCase()];

  // Count vowels using filter and arrow function
  const vowelCount = chars.filter(char => 'aeiou'.includes(char)).length;

  // Count consonants (only letters that aren't vowels)
  const consonantCount = chars.filter(char =>
    /[a-z]/.test(char) && !'aeiou'.includes(char)
  ).length;

  return {
    length: text.length,
    words,
    vowels: vowelCount,
    consonants: consonantCount,
    firstChar,
    lastChar
  };
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
console.log('🎓 Running o1.1 Tests...');
test_o1_1();

console.log('\n🎓 Running o1.2 Tests...');
test_o1_2();

// 📋 Summary
console.log('\n📋 Final Test Summary:');
testResults.forEach(r => console.log(r));

const approved = testResults.filter(r => r.includes('✅')).length;
const failed = testResults.filter(r => r.includes('❌')).length;

console.log(`\n🎯 Results: ${approved} ✅ | ${failed} ❌`);
console.log(failed === 0 ? '🎉 All tests passed!' : '🔧 Some tests need attention.');