# 🐍 Guía Completa: Introducción a la Programación con Python

```
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║        🚀 BIENVENIDO AL MUNDO DE PYTHON 🚀                ║
    ║                                                          ║
    ║    ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       ║
    ║    │  P  │ │  Y  │ │  T  │ │  H  │ │  O  │ │  N  │       ║
    ║    └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘       ║
    ║                                                          ║
    ║           Tu aventura de programación comienza aquí      ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
```

---

## 📖 Introducción

¡Hola futuro programador! 👋 Estás a punto de embarcarte en una aventura increíble que cambiará tu forma de pensar y resolver problemas. Python es un lenguaje de programación poderoso, elegante y fácil de aprender que te abrirá las puertas a un mundo de posibilidades infinitas.

En esta guía aprenderás desde cero cómo programar, empezando por los conceptos más básicos hasta crear tus primeros programas funcionales. No necesitas conocimientos previos, solo ganas de aprender y mucha curiosidad 🧠✨

---

## 🎯 Descripción de la Guía

Esta guía está diseñada especialmente para principiantes que quieren dominar los fundamentos de la programación con Python. A través de ejemplos prácticos, ejercicios progresivos y proyectos reales, desarrollarás las habilidades esenciales para convertirte en un programador competente.

### ✨ ¿Qué aprenderás?

- 🧩 **Pensamiento algorítmico**: Cómo descomponer problemas complejos en pasos simples
- 🔀 **Toma de decisiones**: Usar condicionales para que tus programas sean inteligentes
- 🔁 **Automatización**: Crear bucles que repitan tareas de forma eficiente
- 🚀 **Integración**: Combinar todos los conceptos en proyectos reales

### 🎓 Metodología

Cada tema incluye:
- 📚 Conceptos explicados de forma simple y clara
- 💻 5 ejercicios prácticos con casos de prueba
- 🏗️ Código base para que practiques
- 💡 Tips y trucos útiles
- 🎉 Motivación para mantenerte inspirado

---

## 🧠 Conceptos Básicos

Antes de sumergirnos en los temas específicos, es importante entender algunos conceptos fundamentales:

### 🤖 ¿Qué es la Programación?
La programación es el arte de comunicarse con las computadoras usando un lenguaje específico. Es como escribir una receta de cocina muy detallada que la computadora puede seguir paso a paso.

### 🐍 ¿Por qué Python?
Python es perfecto para principiantes porque:
- **Simple**: Su sintaxis es muy parecida al inglés
- **Poderoso**: Usado por empresas como Google, Netflix y NASA
- **Versátil**: Puedes hacer sitios web, inteligencia artificial, juegos y más
- **Comunidad**: Millones de programadores te pueden ayudar

### 📐 Algoritmos y Diagramas de Flujo
Un algoritmo es una serie de pasos ordenados para resolver un problema. Los diagramas de flujo nos ayudan a visualizar estos pasos usando símbolos gráficos.

```
Símbolos básicos:
┌─────────┐  ← Inicio/Fin (óvalo)
│ INICIO  │
└─────────┘

┌─────────┐  ← Proceso (rectángulo)
│ Acción  │
└─────────┘

◊─────────◊  ← Decisión (rombo)
│ ¿Sí/No? │
◊─────────◊
```

---

# 📚 TEMA 1: Algoritmos y Representación en Código

## 🎯 Descripción del Tema

En este tema aprenderás a pensar como un programador, descomponiendo problemas en pasos lógicos y traduciéndolos a código Python. Dominarás las operaciones básicas, variables y entrada/salida de datos.

---


## 💻 Ejercicio 1: Suma de Dos Números

### 🎯 Problema
Crear un programa que sume dos números ingresados por el usuario.

### 📝 Descripción
Tu programa debe pedir dos números al usuario, sumarlos y mostrar el resultado. Es uno de los programas más básicos pero fundamental para entender la entrada de datos y operaciones.

### ⚙️ Funcionalidades
- Solicitar primer número
- Solicitar segundo número  
- Sumar ambos números
- Mostrar el resultado

### 🧪 Casos de Prueba
1. Número1: 10, Número2: 5 → Suma: 15
2. Número1: 7.5, Número2: 2.5 → Suma: 10.0
3. Número1: 100, Número2: 200 → Suma: 300

### 💻 Código Base
```python
# Simple Addition Calculator ➕
print("➕ Calculadora de Suma Simple")
print("=" * 30)

# Your code here 👇
result = 0

# Example output:
# El resultado es: 15.0 🎉✅

# Test cases:
print("=" * 30)
print(result == 15)
print(result == 10.0)
print(result == 300)
```

### 💡 Tips Útiles
- Usa `float(input())` para aceptar decimales
- La suma se hace con el operador `+`
- Guarda el resultado en una variable

### 🎉 Motivación
¡Dominas las operaciones básicas! La suma es la base de todas las matemáticas computacionales. ¡Sigue construyendo! ➕

---

## 💻 Ejercicio 2: Calculadora de Área de un Rectángulo

### 🎯 Problema
Crear un programa que calcule el área de un rectángulo pidiendo al usuario la base y la altura.

### 📝 Descripción
El área de un rectángulo se calcula multiplicando su base por su altura. Tu programa debe solicitar estos valores al usuario y mostrar el resultado de forma clara.

### ⚙️ Funcionalidades
- Solicitar base y altura al usuario
- Calcular área = base × altura
- Mostrar el resultado con formato amigable

### 🧪 Casos de Prueba
1. Base: 5, Altura: 3 → Área: 15
2. Base: 10.5, Altura: 2.3 → Área: 24.15
3. Base: 7, Altura: 7 → Área: 49

### 💻 Código Base
```python
# Rectangle Area Calculator 📐
print("🏗️ Calculadora de Área de Rectángulo")
print("=" * 40)

# Your code here 👇
area = 0

# Example output:
# El área del rectángulo es: 15.0 metros cuadrados 📐✅

# Test cases:
print("=" * 40)
print(area == 15.0)
print(area == 24.15)
print(area == 49.0)
```

### 💡 Tips Útiles
- Usa `input()` para obtener datos del usuario
- Convierte a `float()` para manejar decimales
- Formula: area = base * altura

### 🎉 Motivación
¡Tu primer programa! Cada gran programador comenzó calculando áreas simples. ¡Estás dando el primer paso hacia crear software increíble! 🚀

---

## 💻 Ejercicio 3: Conversor de Celsius a Fahrenheit

### 🎯 Problema
Convertir una temperatura de Celsius a Fahrenheit usando la fórmula correspondiente.

### 📝 Descripción
La fórmula para convertir Celsius a Fahrenheit es: F = (C × 9/5) + 32. Tu programa debe pedir la temperatura en Celsius y mostrar su equivalente en Fahrenheit.

### ⚙️ Funcionalidades
- Solicitar temperatura en Celsius
- Aplicar la fórmula de conversión
- Mostrar el resultado con 1 decimal

### 🧪 Casos de Prueba
1. 0°C → 32.0°F
2. 25°C → 77.0°F
3. 100°C → 212.0°F

### 💻 Código Base
```python
# Temperature Converter 🌡️
print("🌡️ Conversor de Temperatura")
print("=" * 30)

# Your code here 👇
fahrenheit = 0

# Example output:
# Fahrenheit es: 32.0 °F 🌡️🔥

# Test cases:
print("=" * 30)
print(fahrenheit == 32.0)
print(fahrenheit == 77.0)
print(fahrenheit == 212.0)
```

### 💡 Tips Útiles
- Fórmula: F = (C * 9/5) + 32
- Usa paréntesis para el orden correcto de operaciones
- Redondea con `round(resultado, 1)`

### 🎉 Motivación
¡Las matemáticas cobran vida en tu código! Ahora puedes convertir temperaturas instantáneamente. 🔥

---

## 💻 Ejercicio 4: Calculadora de Promedio

### 🎯 Problema
Calcular el promedio de tres números ingresados por el usuario.

### 📝 Descripción
Tu programa debe solicitar tres números, sumarlos y dividir el resultado entre 3 para obtener el promedio. Es fundamental para entender operaciones múltiples.

### ⚙️ Funcionalidades
- Solicitar tres números
- Calcular la suma total
- Dividir entre 3 para obtener el promedio
- Mostrar el resultado con 2 decimales

### 🧪 Casos de Prueba
1. Números: 10, 20, 30 → Promedio: 20.0
2. Números: 5, 10, 15 → Promedio: 10.0
3. Números: 8, 9, 10 → Promedio: 9.0

### 💻 Código Base
```python
# Average Calculator 📊
print("📊 Calculadora de Promedio")
print("=" * 30)

# Your code here 👇
average = 0

# Test cases:
print("=" * 30)
print(average == 20.0)
print(average == 10.0)
print(average == 9.0)
```

### 💡 Tips Útiles
- Promedio = (num1 + num2 + num3) / 3
- Usa paréntesis para agrupar la suma
- La división siempre produce un float

### 🎉 Motivación
¡Calculas estadísticas básicas! Los promedios son esenciales en ciencia de datos y análisis. 📈

---

## 💻 Ejercicio 5: Calculadora de Perímetro de Rectángulo

### 🎯 Problema
Calcular el perímetro de un rectángulo conociendo su base y altura.

### 📝 Descripción
El perímetro de un rectángulo se calcula con la fórmula: P = 2 × (base + altura). Tu programa debe pedir las dimensiones y calcular el perímetro total.

### ⚙️ Funcionalidades
- Solicitar base del rectángulo
- Solicitar altura del rectángulo
- Calcular perímetro usando la fórmula
- Mostrar el resultado

### 🧪 Casos de Prueba
1. Base: 5, Altura: 3 → Perímetro: 16
2. Base: 10, Altura: 7 → Perímetro: 34
3. Base: 4, Altura: 4 → Perímetro: 16

### 💻 Código Base
```python
# Rectangle Perimeter Calculator 📏
print("📏 Calculadora de Perímetro")
print("=" * 30)

# Your code here 👇
perimeter = 0

# Test cases:
print("=" * 30)
print(perimeter == 16)
print(perimeter == 34)
print(perimeter == 16)
```

### 💡 Tips Útiles
- Fórmula: P = 2 * (base + altura)
- Usa paréntesis para el orden correcto
- El resultado siempre es positivo

### 🎉 Motivación
¡Dominas fórmulas geométricas! Tu código ya puede resolver problemas matemáticos reales. 📐

---

# 🔀 TEMA 2: Estructuras Condicionales Básicas

## 🎯 Descripción del Tema

Las estructuras condicionales permiten que tus programas tomen decisiones inteligentes. Aprenderás a usar `if`, `elif` y `else` para crear programas que se adapten a diferentes situaciones.

---

## 💻 Ejercicio 6: Detector de Número Positivo o Negativo

### 🎯 Problema
Determinar si un número ingresado por el usuario es positivo, negativo o cero.

### 📝 Descripción
Tu programa debe evaluar un número y clasificarlo en una de tres categorías: positivo (mayor que 0), negativo (menor que 0) o cero (igual a 0).

### ⚙️ Funcionalidades
- Solicitar un número al usuario
- Evaluar si es positivo, negativo o cero
- Mostrar la clasificación correspondiente

### 🧪 Casos de Prueba
1. Número: 5 → "positivo"
2. Número: -3 → "negativo"
3. Número: 0 → "cero"

### 💻 Código Base
```python
# Number Classifier ➕➖
print("➕➖ Clasificador de Números")
print("=" * 30)

# Your code here 👇
result = ""

# Test cases:
print("=" * 30)
print(result == "positivo")
print(result == "negativo")
print(result == "cero")
```

### 💡 Tips Útiles
- Usa `if numero > 0:` para positivo
- Usa `elif numero < 0:` para negativo
- Usa `else:` para cero

### 🎉 Motivación
¡Tu programa ahora puede pensar y tomar decisiones! Esto es lo que hace que los programas sean verdaderamente útiles. 🧠

---

## 💻 Ejercicio 7: Detector de Número Par o Impar

### 🎯 Problema
Determinar si un número entero es par o impar.

### 📝 Descripción
Un número es par si es divisible por 2 (el resto de la división es 0). Tu programa debe verificar esta condición y clasificar el número.

### ⚙️ Funcionalidades
- Solicitar un número entero
- Verificar si es divisible por 2
- Mostrar si es "par" o "impar"

### 🧪 Casos de Prueba
1. Número: 8 → "par"
2. Número: 7 → "impar"
3. Número: 0 → "par"

### 💻 Código Base
```python
# Even/Odd Detector 🔢
print("🔢 Detector Par/Impar")
print("=" * 25)

# Your code here 👇
result = ""

# Test cases:
print("=" * 25)
print(result == "par")
print(result == "impar")
print(result == "par")
```

### 💡 Tips Útiles
- Usa el operador módulo `%` para obtener el resto
- `numero % 2 == 0` significa que es par
- `numero % 2 != 0` significa que es impar

### 🎉 Motivación
¡Dominas la lógica matemática! Los números pares e impares son fundamentales en programación. 🔍

---

## 💻 Ejercicio 8: Comparador de Dos Números

### 🎯 Problema
Comparar dos números y determinar cuál es mayor, menor, o si son iguales.

### 📝 Descripción
Tu programa debe recibir dos números y compararlos, indicando la relación entre ellos: si el primero es mayor, menor, o si ambos son iguales.

### ⚙️ Funcionalidades
- Solicitar primer número
- Solicitar segundo número
- Comparar ambos números
- Mostrar el resultado de la comparación

### 🧪 Casos de Prueba
1. Número1: 10, Número2: 5 → "mayor"
2. Número1: 3, Número2: 8 → "menor"
3. Número1: 7, Número2: 7 → "igual"

### 💻 Código Base
```python
# Number Comparator ⚖️
print("⚖️ Comparador de Números")
print("=" * 28)

# Your code here 👇
result = ""

# Test cases:
print("=" * 28)
print(result == "mayor")
print(result == "menor")
print(result == "igual")
```

### 💡 Tips Útiles
- Usa `if num1 > num2:` para mayor
- Usa `elif num1 < num2:` para menor
- Usa `else:` para igual

### 🎉 Motivación
¡Tu código puede hacer comparaciones! Esta lógica es esencial para ordenamiento y búsqueda de datos. ⚖️

---

## 💻 Ejercicio 9: Clasificador de Edades Simple

### 🎯 Problema
Clasificar a una persona como "niño", "adulto" o "adulto mayor" según su edad.

### 📝 Descripción
Tu programa debe clasificar personas en tres categorías: niño (menor de 18), adulto (18 a 64), y adulto mayor (65 o más).

### ⚙️ Funcionalidades
- Solicitar edad de la persona
- Evaluar en qué categoría se encuentra
- Mostrar la clasificación

### 🧪 Casos de Prueba
1. Edad: 10 → "niño"
2. Edad: 25 → "adulto" 
3. Edad: 70 → "adulto mayor"

### 💻 Código Base
```python
# Age Classifier 👥
print("👥 Clasificador de Edades")
print("=" * 28)

# Your code here 👇
result = ""

# Test cases:
print("=" * 28)
print(result == "niño")
print(result == "adulto")
print(result == "adulto mayor")
```

### 💡 Tips Útiles
- Usa `if edad < 18:` para niño
- Usa `elif edad <= 64:` para adulto
- Usa `else:` para adulto mayor

### 🎉 Motivación
¡Tu programa entiende categorías humanas! Esto es útil para sistemas de registro y clasificación. 👤

---

## 💻 Ejercicio 10: Calculadora con Operación Simple

### 🎯 Problema
Crear una calculadora que realice suma o resta según la elección del usuario.

### 📝 Descripción
Tu programa debe pedir dos números y una operación (+ o -), luego realizar el cálculo correspondiente y mostrar el resultado.

### ⚙️ Funcionalidades
- Solicitar primer número
- Solicitar segundo número
- Solicitar operación (+ o -)
- Realizar el cálculo correspondiente

### 🧪 Casos de Prueba
1. Números: 10, 5, Operación: "+" → 15
2. Números: 10, 3, Operación: "-" → 7
3. Números: 8, 2, Operación: "+" → 10

### 💻 Código Base
```python
# Simple Calculator ➕➖
print("➕➖ Calculadora Simple")
print("=" * 25)

# Your code here 👇
result = 0

# Test cases:
print("=" * 25)
print(result == 15)
print(result == 7)
print(result == 10)
```

### 💡 Tips Útiles
- Usa `if operation == "+":` para suma
- Usa `elif operation == "-":` para resta
- Almacena el resultado en una variable

### 🎉 Motivación
¡Creaste tu primera calculadora! Ahora combinas entrada de usuario con lógica de decisión. 🧮

---

# 🔁 TEMA 3: Estructuras Repetitivas Básicas

## 🎯 Descripción del Tema

Los bucles son el poder de la automatización en programación. Aprenderás a usar `for` y `while` para repetir acciones y procesar datos de manera eficiente.

---

## 💻 Ejercicio 11: Contador del 1 al 10

### 🎯 Problema
Mostrar los números del 1 al 10 usando un bucle for.

### 📝 Descripción
Tu programa debe usar un bucle `for` para mostrar todos los números desde 1 hasta 10, uno por línea. Es el ejercicio más básico de bucles.

### ⚙️ Funcionalidades
- Usar bucle for con range(1, 11)
- Mostrar cada número en una línea
- Contar exactamente 10 números

### 🧪 Casos de Prueba
1. Mostrar: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
2. Total de números mostrados: 10
3. Rango correcto: de 1 a 10 inclusive

### 💻 Código Base
```python
# Number Counter 🔢
print("🔢 Contador de Números")
print("=" * 25)

# Your code here 👇
count = 0

# Test cases:
print("=" * 25)
print(count == 10)
```

### 💡 Tips Útiles
- Usa `for i in range(1, 11):`
- `range(1, 11)` va del 1 al 10
- Cuenta cada iteración con `count += 1`

### 🎉 Motivación
¡Tu primer bucle exitoso! Has automatizado una tarea repetitiva. Este es el verdadero poder de la programación. 🚀

---

## 💻 Ejercicio 12: Suma de Números del 1 al 5

### 🎯 Problema
Calcular la suma de los números del 1 al 5 usando un bucle.

### 📝 Descripción
Tu programa debe usar un bucle para sumar todos los números desde 1 hasta 5. El resultado debe ser 1+2+3+4+5 = 15.

### ⚙️ Funcionalidades
- Usar bucle for del 1 al 5
- Acumular la suma en cada iteración
- Mostrar el resultado final

### 🧪 Casos de Prueba
1. Suma del 1 al 5 → 15
2. Usando bucle for
3. Resultado almacenado en variable

### 💻 Código Base
```python
# Sum Calculator 🧮
print("🧮 Calculadora de Suma")
print("=" * 25)

# Your code here 👇
total = 0

# Test cases:
print("=" * 25)
print(total == 15)
```

### 💡 Tips Útiles
- Inicia `total = 0`
- Usa `for i in range(1, 6):`
- Acumula con `total += i`

### 🎉 Motivación
¡Dominas la acumulación! Puedes sumar series de números automáticamente. 📊

---

## 💻 Ejercicio 13: Tabla de Multiplicar del 2

### 🎯 Problema
Generar la tabla de multiplicar del 2 (del 2x1 al 2x10).

### 📝 Descripción
Tu programa debe mostrar la tabla completa del 2, desde 2x1=2 hasta 2x10=20, usando un bucle for.

### ⚙️ Funcionalidades
- Generar tabla del 2 del 1 al 10
- Mostrar cada multiplicación
- Calcular productos correctamente

### 🧪 Casos de Prueba
1. 2 x 1 = 2
2. 2 x 5 = 10  
3. 2 x 10 = 20

### 💻 Código Base
```python
# Multiplication Table ✖️
print("✖️ Tabla de Multiplicar del 2")
print("=" * 30)

# Your code here 👇
last_result = 0

# Test cases:
print("=" * 30)
print(last_result == 20)
```

### 💡 Tips Útiles
- Usa `for i in range(1, 11):`
- Calcula `result = 2 * i`
- Guarda el último resultado

### 🎉 Motivación
¡Recreaste las tablas de multiplicar digitalmente! Tu código puede enseñar matemáticas. 🎓

---

## 💻 Ejercicio 14: Contador de Números Pares

### 🎯 Problema
Contar cuántos números pares hay entre 1 y 10.

### 📝 Descripción
Tu programa debe recorrer los números del 1 al 10, verificar cuáles son pares, y contar cuántos encuentra en total.

### ⚙️ Funcionalidades
- Recorrer números del 1 al 10
- Verificar si cada número es par
- Contar total de números pares

### 🧪 Casos de Prueba
1. Números pares entre 1 y 10: 2, 4, 6, 8, 10
2. Total de pares: 5
3. Usar operador módulo para verificar

### 💻 Código Base
```python
# Even Counter 🔢
print("🔢 Contador de Pares")
print("=" * 23)

# Your code here 👇
even_count = 0

# Test cases:
print("=" * 23)
print(even_count == 5)
```

### 💡 Tips Útiles
- Usa `for i in range(1, 11):`
- Verifica con `if i % 2 == 0:`
- Incrementa contador con `even_count += 1`

### 🎉 Motivación
¡Combinas bucles con condicionales! Puedes filtrar y contar datos específicos. 🔍

---

## 💻 Ejercicio 15: Suma de Números Impares del 1 al 9

### 🎯 Problema
Calcular la suma de todos los números impares entre 1 y 9.

### 📝 Descripción
Tu programa debe encontrar los números impares (1, 3, 5, 7, 9) y sumar todos estos valores para obtener el total.

### ⚙️ Funcionalidades
- Recorrer números del 1 al 9
- Identificar números impares
- Sumar solo los números impares

### 🧪 Casos de Prueba
1. Números impares: 1, 3, 5, 7, 9
2. Suma total: 1+3+5+7+9 = 25
3. Solo contar impares

### 💻 Código Base
```python
# Odd Sum Calculator 🧮
print("🧮 Suma de Impares")
print("=" * 20)

# Your code here 👇
odd_sum = 0

# Test cases:
print("=" * 20)
print(odd_sum == 25)
```

### 💡 Tips Útiles
- Usa `for i in range(1, 10):`
- Verifica con `if i % 2 != 0:`
- Acumula con `odd_sum += i`

### 🎉 Motivación
¡Maestría en filtros y acumulación! Puedes procesar datos selectivamente con precisión matemática. ⚡

---

# 🚀 TEMA 4: Integración de Conocimientos

## 🎯 Descripción del Tema

En este tema final combinarás algoritmos básicos, condicionales y bucles para crear programas más completos que resuelven problemas reales.

---

## 💻 Ejercicio 16: Calculadora de Promedio de Calificaciones

### 🎯 Problema
Calcular el promedio de 5 calificaciones y determinar si el estudiante aprobó.

### 📝 Descripción
Tu programa debe pedir 5 calificaciones, calcular su promedio, y determinar si el estudiante aprobó (promedio ≥ 70) o reprobó.

### ⚙️ Funcionalidades
- Solicitar 5 calificaciones usando bucle
- Calcular promedio total
- Determinar si aprobó o reprobó

### 🧪 Casos de Prueba
1. Calificaciones: 80, 85, 90, 75, 70 → Promedio: 80.0 → "aprobado"
2. Calificaciones: 60, 65, 55, 70, 50 → Promedio: 60.0 → "reprobado"
3. Calificaciones: 70, 70, 70, 70, 70 → Promedio: 70.0 → "aprobado"

### 💻 Código Base
```python
# Grade Average Calculator 📊
print("📊 Calculadora de Promedio")
print("=" * 30)

# Your code here 👇
average = 0
status = ""

# Test cases:
print("=" * 30)
print(average == 80.0 and status == "aprobado")
print(average == 60.0 and status == "reprobado") 
print(average == 70.0 and status == "aprobado")
```

### 💡 Tips Útiles
- Usa bucle for para pedir 5 calificaciones
- Promedio = suma_total / 5
- Aprobado si promedio >= 70

### 🎉 Motivación
¡Integras bucles, cálculos y decisiones! Tu código ahora evalúa rendimiento académico. 🎓

---

## 💻 Ejercicio 17: Contador de Números Positivos y Negativos

### 🎯 Problema
Solicitar 5 números al usuario y contar cuántos son positivos y cuántos son negativos.

### 📝 Descripción
Tu programa debe pedir 5 números usando un bucle, clasificar cada uno como positivo o negativo, y mantener contadores separados para cada categoría.

### ⚙️ Funcionalidades
- Solicitar 5 números usando bucle
- Clasificar cada número como positivo o negativo
- Contar totales de cada categoría

### 🧪 Casos de Prueba
1. Números: 5, -3, 8, -1, 2 → Positivos: 3, Negativos: 2
2. Números: -2, -4, -6, 1, 3 → Positivos: 2, Negativos: 3
3. Números: 10, 20, 30, 40, 50 → Positivos: 5, Negativos: 0

### 💻 Código Base
```python
# Positive/Negative Counter ➕➖
print("➕➖ Contador Positivos/Negativos")
print("=" * 35)

# Your code here 👇
positive_count = 0
negative_count = 0

# Test cases:
print("=" * 35)
print(positive_count == 3 and negative_count == 2)
print(positive_count == 2 and negative_count == 3)
print(positive_count == 5 and negative_count == 0)
```

### 💡 Tips Útiles
- Usa bucle for con range(5)
- Incrementa positive_count si número > 0
- Incrementa negative_count si número < 0

### 🎉 Motivación
¡Clasificas y cuentas datos automáticamente! Esta habilidad es fundamental en análisis de datos. 📊

---

## 💻 Ejercicio 18: Tabla de Multiplicar Elegida por Usuario

### 🎯 Problema
Permitir al usuario elegir qué tabla de multiplicar generar (del 1 al 5).

### 📝 Descripción
Tu programa debe pedir al usuario un número entre 1 y 5, luego generar la tabla de multiplicar completa de ese número del 1 al 5.

### ⚙️ Funcionalidades
- Solicitar número para la tabla (1-5)
- Validar que esté en rango válido
- Generar tabla completa del número elegido

### 🧪 Casos de Prueba
1. Tabla del 3: 3x1=3, 3x2=6, 3x3=9, 3x4=12, 3x5=15
2. Tabla del 2: 2x1=2, 2x2=4, 2x3=6, 2x4=8, 2x5=10
3. Tabla del 5: 5x1=5, 5x2=10, 5x3=15, 5x4=20, 5x5=25

### 💻 Código Base
```python
# Custom Multiplication Table ✖️
print("✖️ Tabla de Multiplicar Personalizada")
print("=" * 40)

# Your code here 👇
last_result = 0

# Test cases:
print("=" * 40)
print(last_result == 15)  # Table of 3: 3x5=15
print(last_result == 10)  # Table of 2: 2x5=10
print(last_result == 25)  # Table of 5: 5x5=25
```

### 💡 Tips Útiles
- Pide número con input() y convierte a int()
- Usa for i in range(1, 6) para generar tabla
- Guarda el último resultado (número x 5)

### 🎉 Motivación
¡Tu programa es interactivo y personalizable! Los usuarios pueden elegir qué calcular. 🎮

---

## 💻 Ejercicio 19: Calculadora de Factorial Simple

### 🎯 Problema
Calcular el factorial de un número entre 1 y 5 ingresado por el usuario.

### 📝 Descripción
El factorial de n (n!) es la multiplicación de todos los números desde 1 hasta n. Tu programa debe calcular factoriales de números pequeños (1-5).

### ⚙️ Funcionalidades
- Solicitar número entre 1 y 5
- Calcular factorial usando bucle
- Mostrar el resultado final

### 🧪 Casos de Prueba
1. Número: 3 → 3! = 1×2×3 = 6
2. Número: 4 → 4! = 1×2×3×4 = 24
3. Número: 5 → 5! = 1×2×3×4×5 = 120

### 💻 Código Base
```python
# Simple Factorial Calculator 🧮
print("🧮 Calculadora de Factorial")
print("=" * 30)

# Your code here 👇
factorial = 0

# Test cases:
print("=" * 30)
print(factorial == 6)    # 3! = 6
print(factorial == 24)   # 4! = 24
print(factorial == 120)  # 5! = 120
```

### 💡 Tips Útiles
- Inicia factorial = 1 (no 0)
- Usa for i in range(1, numero + 1)
- Multiplica: factorial *= i

### 🎉 Motivación
¡Dominas matemáticas avanzadas computacionales! Los factoriales son base de estadística y probabilidad. 📐

---

## 💻 Ejercicio 20: Juego de Adivinanza Simple

### 🎯 Problema
Crear un juego donde el usuario debe adivinar un número secreto entre 1 y 10.

### 📝 Descripción
Tu programa tiene un número secreto fijo. El usuario tiene 3 intentos para adivinarlo. Después de cada intento incorrecto, debe decir si el número es mayor o menor.

### ⚙️ Funcionalidades
- Número secreto fijo (ej: 7)
- Máximo 3 intentos
- Dar pistas: "mayor" o "menor"
- Determinar si ganó o perdió

### 🧪 Casos de Prueba
1. Número secreto: 7, Intento: 7 → "ganaste"
2. Número secreto: 7, Intento: 5 → "mayor"
3. Número secreto: 7, Intento: 9 → "menor"

### 💻 Código Base
```python
# Number Guessing Game 🎯
print("🎯 Juego de Adivinanza")
print("=" * 25)
print("Adivina el número secreto entre 1 y 10")

# Your code here 👇
secret_number = 7  # Fixed secret number
result = ""

# Test cases:
print("=" * 25)
print(result == "ganaste")
print(result == "mayor")
print(result == "menor")
```

### 💡 Tips Útiles
- Define secret_number = 7
- Compara guess con secret_number
- Usa if/elif/else para las respuestas

### 🎉 Motivación
¡Creaste tu primer videojuego! Combinas lógica, bucles y interacción con el usuario. ¡Eres oficialmente un desarrollador de juegos! 🎮

---

# 🎯 PROYECTO INTEGRADOR: Sistema de Calificaciones Básico

## 📋 Descripción del Proyecto

Desarrolla un sistema simple que maneje calificaciones de 3 estudiantes, calcule estadísticas básicas y genere un reporte.

### 🎯 Requerimientos del Sistema

Tu sistema debe:

1. **Registro de Estudiantes**
   - Pedir nombres de 3 estudiantes
   - Almacenar en variables separadas

2. **Captura de Calificaciones**
   - Pedir 1 calificación por estudiante
   - Validar que estén entre 0 y 100

3. **Cálculos Estadísticos**
   - Calcular promedio del grupo
   - Identificar la calificación más alta
   - Contar cuántos aprobaron (≥70)

4. **Reporte Final**
   - Mostrar información de cada estudiante
   - Mostrar estadísticas del grupo

### 🧪 Casos de Prueba del Proyecto

1. Estudiantes: Ana(85), Carlos(92), María(78) → Promedio: 85.0, Más alta: 92, Aprobados: 3
2. Estudiantes: Luis(65), Elena(88), Pedro(45) → Promedio: 66.0, Más alta: 88, Aprobados: 1
3. Estudiantes: Juan(70), Laura(70), Miguel(70) → Promedio: 70.0, Más alta: 70, Aprobados: 3

### 💻 Código Base del Proyecto

```python
# 🏫 Student Grade Management System
print("🏫 SISTEMA DE CALIFICACIONES")
print("=" * 30)

# Your code here 👇
# Variables for students
student1_name = ""
student1_grade = 0
student2_name = ""
student2_grade = 0
student3_name = ""
student3_grade = 0

# Statistics
average = 0
highest_grade = 0
passed_count = 0

# Test cases:
print("=" * 30)
print("Test Case 1:")
print(average == 85.0 and highest_grade == 92 and passed_count == 3)
print("Test Case 2:")  
print(average == 66.0 and highest_grade == 88 and passed_count == 1)
print("Test Case 3:")
print(average == 70.0 and highest_grade == 70 and passed_count == 3)
```

### 🏆 Criterios de Evaluación

- ✅ **Entrada de Datos**: Captura correcta de nombres y calificaciones
- ✅ **Cálculos**: Promedio, máximo y conteo correctos
- ✅ **Lógica**: Uso apropiado de condicionales y bucles
- ✅ **Salida**: Reporte claro y organizado

---

# 🏃‍♂️ RETO PERSONAL: Expansión del Sistema

## 🚀 Desafío Final

Mejora tu sistema de calificaciones agregando UNA de estas características:

### 🎯 Opción A: Clasificador de Rendimiento
Clasifica cada estudiante como "Excelente" (90+), "Bueno" (80-89), "Regular" (70-79), o "Deficiente" (<70).

### 📊 Opción B: Estadísticas Avanzadas
Agrega cálculo de la calificación más baja y el rango (diferencia entre más alta y más baja).

### 🏆 Opción C: Sistema de Reconocimientos
Identifica y muestra quién obtuvo la calificación más alta con un mensaje especial.

### 💻 Opción D: Interfaz Mejorada
Agrega un menú que permita ver estadísticas generales o información individual de cada estudiante.

## 🎯 Requisitos del Reto

Tu mejora debe incluir:
- Uso de todos los conceptos aprendidos
- Código limpio con comentarios
- Casos de prueba funcionales
- Interfaz clara para el usuario

---

# 🎉 ¡FELICITACIONES!

```
    🎊 ¡MISIÓN COMPLETADA! 🎊
    
    ┌─────────────────────────────────────┐
    │  🏆 PROGRAMADOR PYTHON BÁSICO 🏆   │
    │                                     │
    │      Has completado exitosamente    │
    │   FUNDAMENTOS DE PROGRAMACIÓN       │
    │           CON PYTHON                │
    │                                     │
    │  ✅ Variables y operaciones         │
    │  ✅ Estructuras condicionales       │
    │  ✅ Bucles y repetición             │
    │  ✅ Integración de conceptos        │
    │                                     │
    │  ¡Estás listo para proyectos        │
    │       más avanzados!                │
    └─────────────────────────────────────┘
```

## 🚀 Próximos Pasos Recomendados

1. **🔧 Funciones** - Organiza tu código en funciones reutilizables
2. **📝 Listas y Diccionarios** - Maneja colecciones de datos
3. **📁 Archivos** - Lee y guarda información permanentemente
4. **🌐 Proyectos Web** - Crea aplicaciones web básicas
5. **🤖 Automatización** - Scripts para tareas repetitivas

## 💭 Reflexión Final

Has completado un viaje increíble desde los conceptos más básicos hasta crear sistemas funcionales. Cada ejercicio te ha preparado para enfrentar problemas más complejos con confianza.

### 🌟 Lo que has logrado:
- **20 ejercicios** completados exitosamente
- **4 temas fundamentales** dominados
- **1 proyecto integrador** desarrollado
- **Pensamiento lógico** fortalecido

### 📚 Recursos para Continuar:
- **Práctica diaria**: Codewars, HackerRank
- **Documentación**: docs.python.org
- **Comunidad**: Stack Overflow, Reddit r/learnpython
- **Proyectos**: GitHub para compartir tu código

**¡Tu aventura de programación apenas comienza! Sigue practicando y creando cosas increíbles! 🌟💻**