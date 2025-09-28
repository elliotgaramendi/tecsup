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

## 💻 Ejercicio 1: Calculadora de Área de un Rectángulo

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
# Calculadora de Área de Rectángulo 📐
print("🏗️ Calculadora de Área de Rectángulo")
print("=" * 40)

# Tu código aquí 👇


# Ejemplo de salida:
# El área del rectángulo es: 15 metros cuadrados
```

### 💡 Tips Útiles
- Usa `input()` para obtener datos del usuario
- Convierte a `float()` para manejar decimales
- Usa `print()` con mensajes claros y emojis

### 🎉 Motivación
¡Tu primer programa! Cada gran programador comenzó calculando áreas simples. ¡Estás dando el primer paso hacia crear software increíble! 🚀

---

## 💻 Ejercicio 2: Conversor de Temperatura

### 🎯 Problema
Convertir una temperatura de Celsius a Fahrenheit usando la fórmula matemática correspondiente.

### 📝 Descripción
La fórmula para convertir Celsius a Fahrenheit es: F = (C × 9/5) + 32. Tu programa debe pedir la temperatura en Celsius y mostrar su equivalente en Fahrenheit.

### ⚙️ Funcionalidades
- Solicitar temperatura en Celsius
- Aplicar la fórmula de conversión
- Mostrar el resultado con 2 decimales

### 🧪 Casos de Prueba
1. 0°C → 32.00°F
2. 25°C → 77.00°F
3. 100°C → 212.00°F

### 💻 Código Base
```python
# Conversor de Temperatura 🌡️
print("🌡️ Conversor de Celsius a Fahrenheit")
print("=" * 40)

# Tu código aquí 👇


# Ejemplo de salida:
# 25°C equivale a 77.00°F
```

### 💡 Tips Útiles
- Recuerda el orden de operaciones: multiplicación antes que suma
- Usa `round()` para controlar los decimales
- Incluye el símbolo de grados (°) en tu salida

### 🎉 Motivación
¡Las matemáticas cobran vida en tu código! Ahora puedes convertir temperaturas instantáneamente. ¡Tu programación está calentándose! 🔥

---

## 💻 Ejercicio 3: Calculadora de Propinas

### 🎯 Problema
Calcular la propina y el total a pagar en un restaurante basado en el monto de la cuenta y el porcentaje de propina.

### 📝 Descripción
En los restaurantes es común dejar propina. Tu programa debe calcular cuánto es la propina (monto × porcentaje) y cuál es el total a pagar (monto + propina).

### ⚙️ Funcionalidades
- Solicitar el monto total de la cuenta
- Solicitar el porcentaje de propina (ejemplo: 15 para 15%)
- Calcular y mostrar la propina y el total final

### 🧪 Casos de Prueba
1. Cuenta: $100, Propina: 15% → Propina: $15.00, Total: $115.00
2. Cuenta: $45.50, Propina: 20% → Propina: $9.10, Total: $54.60
3. Cuenta: $80, Propina: 10% → Propina: $8.00, Total: $88.00

### 💻 Código Base
```python
# Calculadora de Propinas 💰
print("💰 Calculadora de Propinas")
print("=" * 30)

# Tu código aquí 👇


# Ejemplo de salida:
# Propina: $15.00
# Total a pagar: $115.00
```

### 💡 Tips Útiles
- Para calcular porcentaje: (monto × porcentaje) / 100
- Usa variables descriptivas como `cuenta`, `propina`, `total`
- Formatea los números como dinero con 2 decimales

### 🎉 Motivación
¡Ahora puedes calcular propinas como un profesional! Tu código está ayudando a resolver problemas de la vida real. ¡Eso es programación útil! 💪

---

## 💻 Ejercicio 4: Conversor de Tiempo

### 🎯 Problema
Convertir una cantidad de minutos en horas y minutos restantes de forma legible.

### 📝 Descripción
Cuando tienes una cantidad grande de minutos, es útil saber cuántas horas y minutos representa. Tu programa debe tomar minutos totales y mostrar el formato "X horas y Y minutos".

### ⚙️ Funcionalidades
- Solicitar cantidad total de minutos
- Calcular horas completas (división entera)
- Calcular minutos restantes (módulo)
- Mostrar resultado en formato legible

### 🧪 Casos de Prueba
1. 90 minutos → 1 hora y 30 minutos
2. 150 minutos → 2 horas y 30 minutos
3. 45 minutos → 0 horas y 45 minutos

### 💻 Código Base
```python
# Conversor de Tiempo ⏰
print("⏰ Conversor de Minutos a Horas")
print("=" * 35)

# Tu código aquí 👇


# Ejemplo de salida:
# 90 minutos son: 1 hora y 30 minutos
```

### 💡 Tips Útiles
- Usa `//` para división entera (horas completas)
- Usa `%` para obtener el resto (minutos restantes)
- 1 hora = 60 minutos

### 🎉 Motivación
¡Dominas las operaciones matemáticas en Python! Cada operador que aprendes te da más poder para resolver problemas complejos. ¡Sigue así! ⚡

---

## 💻 Ejercicio 5: Calculadora de IMC (Índice de Masa Corporal)

### 🎯 Problema
Calcular el Índice de Masa Corporal de una persona usando su peso y altura.

### 📝 Descripción
El IMC es una medida que relaciona el peso y la altura de una persona. La fórmula es: IMC = peso (kg) / altura² (m²). Tu programa debe calcular y mostrar el IMC con 2 decimales.

### ⚙️ Funcionalidades
- Solicitar peso en kilogramos
- Solicitar altura en metros
- Calcular IMC usando la fórmula
- Mostrar resultado redondeado a 2 decimales

### 🧪 Casos de Prueba
1. Peso: 70kg, Altura: 1.75m → IMC: 22.86
2. Peso: 80kg, Altura: 1.80m → IMC: 24.69
3. Peso: 65kg, Altura: 1.70m → IMC: 22.49

### 💻 Código Base
```python
# Calculadora de IMC 🏋️
print("🏋️ Calculadora de Índice de Masa Corporal")
print("=" * 45)

# Tu código aquí 👇


# Ejemplo de salida:
# Tu IMC es: 22.86
```

### 💡 Tips Útiles
- Para elevar al cuadrado usa `**2` o multiplica `altura * altura`
- El IMC siempre debe ser un número positivo
- Redondea con `round(resultado, 2)`

### 🎉 Motivación
¡Felicidades! Has completado tu primer tema. Ya puedes crear programas que resuelven problemas reales usando matemáticas y lógica. ¡Eres oficialmente un programador! 🎊

---

# 🔀 TEMA 2: Estructuras Condicionales Básicas

## 🎯 Descripción del Tema

Las estructuras condicionales permiten que tus programas tomen decisiones inteligentes. Aprenderás a usar `if`, `elif` y `else` para crear programas que se adapten a diferentes situaciones y datos de entrada.

---

## 💻 Ejercicio 6: Clasificador de Edades

### 🎯 Problema
Clasificar a una persona según su edad en diferentes categorías: niño, adolescente, adulto o adulto mayor.

### 📝 Descripción
Tu programa debe solicitar la edad de una persona y determinar en qué categoría se encuentra según estos rangos:
- 0-12: Niño 👶
- 13-17: Adolescente 🧒
- 18-64: Adulto 👤
- 65+: Adulto mayor 👴

### ⚙️ Funcionalidades
- Solicitar edad del usuario
- Evaluar en qué rango se encuentra
- Mostrar la categoría correspondiente con emoji

### 🧪 Casos de Prueba
1. Edad: 8 → "Eres un niño 👶"
2. Edad: 15 → "Eres un adolescente 🧒"
3. Edad: 30 → "Eres un adulto 👤"
4. Edad: 70 → "Eres un adulto mayor 👴"

### 💻 Código Base
```python
# Clasificador de Edades 👥
print("👥 Clasificador de Edades")
print("=" * 25)

# Tu código aquí 👇


# Ejemplo de salida:
# Eres un adulto 👤
```

### 💡 Tips Útiles
- Usa `if`, `elif`, `else` en ese orden
- Los rangos deben ser excluyentes entre sí
- Convierte la entrada a `int()`

### 🎉 Motivación
¡Tu programa ahora puede pensar y tomar decisiones! Esto es lo que hace que los programas sean verdaderamente útiles e inteligentes. 🧠

---

## 💻 Ejercicio 7: Evaluador de Calificaciones

### 🎯 Problema
Convertir una calificación numérica en una calificación con letras y determinar si el estudiante aprobó o reprobó.

### 📝 Descripción
Tu programa debe evaluar la calificación de un estudiante según esta escala:
- 90-100: A (Excelente) ✅
- 80-89: B (Muy Bueno) ✅
- 70-79: C (Bueno) ✅
- 60-69: D (Suficiente) ⚠️
- 0-59: F (Reprobado) ❌

### ⚙️ Funcionalidades
- Solicitar calificación numérica (0-100)
- Determinar la letra correspondiente
- Indicar si aprobó o reprobó
- Mostrar mensaje motivacional

### 🧪 Casos de Prueba
1. Calificación: 95 → "A - ¡Excelente trabajo! ✅"
2. Calificación: 83 → "B - Muy buen trabajo ✅"
3. Calificación: 75 → "C - Buen trabajo ✅"
4. Calificación: 65 → "D - Necesitas mejorar ⚠️"
5. Calificación: 45 → "F - Debes estudiar más ❌"

### 💻 Código Base
```python
# Evaluador de Calificaciones 📊
print("📊 Evaluador de Calificaciones")
print("=" * 30)

# Tu código aquí 👇


# Ejemplo de salida:
# Calificación: A - ¡Excelente trabajo! ✅
```

### 💡 Tips Útiles
- Usa rangos con `>=` y `<=`
- Ordena las condiciones de mayor a menor
- Valida que la calificación esté entre 0 y 100

### 🎉 Motivación
¡Ahora puedes crear sistemas de evaluación automática! Tu código puede ser tan justo y preciso como el mejor profesor. 🎓

---

## 💻 Ejercicio 8: Detector de Números Pares e Impares

### 🎯 Problema
Determinar si un número ingresado por el usuario es par o impar, y mostrar propiedades adicionales.

### 📝 Descripción
Tu programa debe analizar un número entero y determinar:
- Si es par o impar
- Si es positivo, negativo o cero
- Un mensaje descriptivo con la información

### ⚙️ Funcionalidades
- Solicitar un número entero
- Verificar si es par o impar usando módulo (%)
- Determinar si es positivo, negativo o cero
- Mostrar toda la información de forma organizada

### 🧪 Casos de Prueba
1. Número: 8 → "8 es par y positivo ✅"
2. Número: -5 → "-5 es impar y negativo ➖"
3. Número: 0 → "0 es par y neutro ⚖️"
4. Número: 7 → "7 es impar y positivo ➕"

### 💻 Código Base
```python
# Detector de Números 🔢
print("🔢 Detector de Números")
print("=" * 25)

# Tu código aquí 👇


# Ejemplo de salida:
# 8 es par y positivo ✅
```

### 💡 Tips Útiles
- Un número es par si `numero % 2 == 0`
- Puedes combinar condiciones con `and` y `or`
- Usa `elif` para manejar múltiples casos

### 🎉 Motivación
¡Dominas la lógica booleana! Ahora tus programas pueden analizar datos desde múltiples perspectivas. ¡Tu pensamiento lógico está creciendo! 🔍

---

## 💻 Ejercicio 9: Sistema de Descuentos por Edad

### 🎯 Problema
Calcular el precio final de un producto aplicando descuentos automáticos según la edad del comprador.

### 📝 Descripción
Tu tienda virtual aplica descuentos por edad:
- Menores de 18: 10% de descuento 🧒
- Estudiantes (18-25): 15% de descuento 🎓
- Adultos (26-60): Sin descuento 👤
- Adultos mayores (61+): 20% de descuento 👴

### ⚙️ Funcionalidades
- Solicitar edad y precio original
- Determinar el descuento según la edad
- Calcular precio final
- Mostrar desglose completo

### 🧪 Casos de Prueba
1. Edad: 16, Precio: $100 → Descuento: 10%, Precio final: $90.00
2. Edad: 22, Precio: $150 → Descuento: 15%, Precio final: $127.50
3. Edad: 35, Precio: $200 → Descuento: 0%, Precio final: $200.00
4. Edad: 65, Precio: $120 → Descuento: 20%, Precio final: $96.00

### 💻 Código Base
```python
# Sistema de Descuentos 💰
print("💰 Sistema de Descuentos por Edad")
print("=" * 35)

# Tu código aquí 👇


# Ejemplo de salida:
# Precio original: $100.00
# Descuento aplicado: 10%
# Precio final: $90.00
```

### 💡 Tips Útiles
- Calcula el descuento: `precio * (descuento / 100)`
- Precio final: `precio - descuento_calculado`
- Usa `f-strings` para formatear dinero: `f"${precio:.2f}"`

### 🎉 Motivación
¡Tu código ahora maneja dinero real y automatiza decisiones comerciales! Esto es exactamente lo que hacen las aplicaciones profesionales. 💼

---

## 💻 Ejercicio 10: Clasificador de IMC con Recomendaciones

### 🎯 Problema
Ampliar la calculadora de IMC para incluir clasificación según estándares médicos y recomendaciones personalizadas.

### 📝 Descripción
Tu programa debe calcular el IMC y clasificarlo según estos rangos:
- Menos de 18.5: Bajo peso 📉
- 18.5-24.9: Peso normal ✅
- 25.0-29.9: Sobrepeso ⚠️
- 30.0 o más: Obesidad 🚨

Incluye una recomendación específica para cada categoría.

### ⚙️ Funcionalidades
- Calcular IMC (peso/altura²)
- Clasificar según rangos médicos
- Dar recomendación personalizada
- Mostrar información completa y clara

### 🧪 Casos de Prueba
1. Peso: 50kg, Altura: 1.70m → IMC: 17.30, "Bajo peso - Consulta un médico 📉"
2. Peso: 70kg, Altura: 1.75m → IMC: 22.86, "Peso normal - ¡Mantén tu estilo de vida! ✅"
3. Peso: 85kg, Altura: 1.75m → IMC: 27.76, "Sobrepeso - Considera hacer más ejercicio ⚠️"
4. Peso: 95kg, Altura: 1.70m → IMC: 32.87, "Obesidad - Te recomendamos consultar un especialista 🚨"

### 💻 Código Base
```python
# Clasificador de IMC con Recomendaciones 🏥
print("🏥 Clasificador de IMC con Recomendaciones")
print("=" * 45)

# Tu código aquí 👇


# Ejemplo de salida:
# Tu IMC es: 22.86
# Clasificación: Peso normal ✅
# Recomendación: ¡Mantén tu estilo de vida!
```

### 💡 Tips Útiles
- Calcula primero el IMC, luego evalúa rangos
- Usa `elif` para rangos exclusivos
- Redondea el IMC a 2 decimales para mejor legibilidad

### 🎉 Motivación
¡Increíble! Has creado un sistema de diagnóstico básico que podría usarse en aplicaciones de salud reales. Tu código ahora puede impactar positivamente la vida de las personas. 🌟

---

# 🔁 TEMA 3: Estructuras Repetitivas Básicas

## 🎯 Descripción del Tema

Los bucles son el poder de la automatización en programación. Aprenderás a usar `for` y `while` para repetir acciones, procesar listas de datos y crear patrones complejos sin escribir código repetitivo.

---

## 💻 Ejercicio 11: Contador Progresivo

### 🎯 Problema
Crear un contador que muestre números desde 1 hasta un número especificado por el usuario, con mensajes motivacionales.

### 📝 Descripción
Tu programa debe contar desde 1 hasta el número ingresado por el usuario, mostrando cada número junto con un mensaje especial para ciertos números (múltiplos de 5).

### ⚙️ Funcionalidades
- Solicitar número final al usuario
- Contar desde 1 hasta ese número
- Mostrar mensaje especial en múltiplos de 5
- Mensaje final de felicitación

### 🧪 Casos de Prueba
1. Hasta: 3 → "1", "2", "3", "¡Conteo completado!"
2. Hasta: 7 → "1", "2", "3", "4", "5 🎉", "6", "7", "¡Conteo completado!"
3. Hasta: 10 → Incluye "5 🎉" y "10 🎉"

### 💻 Código Base
```python
# Contador Progresivo 🔢
print("🔢 Contador Progresivo")
print("=" * 25)

# Tu código aquí 👇


# Ejemplo de salida:
# 1
# 2
# 3
# 4
# 5 🎉
# ¡Conteo completado!
```

### 💡 Tips Útiles
- Usa `for i in range(1, numero + 1):`
- Verifica múltiplos de 5 con `i % 5 == 0`
- `range()` empieza en 1 y va hasta `numero + 1`

### 🎉 Motivación
¡Tu primer bucle exitoso! Acabas de automatizar una tarea que tomaría mucho tiempo hacer manualmente. ¡Este es el verdadero poder de la programación! 🚀

---

## 💻 Ejercicio 12: Calculadora de Factorial

### 🎯 Problema
Calcular el factorial de un número usando un bucle, explicando el proceso paso a paso.

### 📝 Descripción
El factorial de un número n (escrito n!) es la multiplicación de todos los números enteros desde 1 hasta n. Por ejemplo: 5! = 1 × 2 × 3 × 4 × 5 = 120.

### ⚙️ Funcionalidades
- Solicitar número al usuario
- Calcular factorial usando bucle for
- Mostrar el proceso paso a paso
- Mostrar resultado final

### 🧪 Casos de Prueba
1. Número: 3 → Proceso: "3! = 1 × 2 × 3 = 6"
2. Número: 5 → Proceso: "5! = 1 × 2 × 3 × 4 × 5 = 120"
3. Número: 0 → "0! = 1" (caso especial)

### 💻 Código Base
```python
# Calculadora de Factorial 🧮
print("🧮 Calculadora de Factorial")
print("=" * 30)

# Tu código aquí 👇


# Ejemplo de salida:
# Calculando 5!
# 5! = 1 × 2 × 3 × 4 × 5 = 120
```

### 💡 Tips Útiles
- Inicia factorial en 1, no en 0
- 0! = 1 por definición matemática
- Usa `factorial *= i` para acumular el producto

### 🎉 Motivación
¡Dominas las matemáticas computacionales! Los factoriales son fundamentales en estadística, probabilidad e inteligencia artificial. ¡Estás construyendo bases sólidas! 📊

---

## 💻 Ejercicio 13: Generador de Tablas de Multiplicar

### 🎯 Problema
Generar y mostrar la tabla de multiplicar completa de un número dado por el usuario.

### 📝 Descripción
Tu programa debe crear la tabla de multiplicar de un número desde 1 hasta 12, mostrando cada operación de forma clara y organizada, como las tablas que aprendiste en la escuela.

### ⚙️ Funcionalidades
- Solicitar el número base al usuario
- Generar tabla del 1 al 12
- Mostrar cada multiplicación con formato claro
- Incluir encabezado decorativo

### 🧪 Casos de Prueba
1. Número: 3 → "3 × 1 = 3", "3 × 2 = 6", ..., "3 × 12 = 36"
2. Número: 7 → "7 × 1 = 7", "7 × 2 = 14", ..., "7 × 12 = 84"

### 💻 Código Base
```python
# Generador de Tablas de Multiplicar ✖️
print("✖️ Generador de Tablas de Multiplicar")
print("=" * 40)

# Tu código aquí 👇


# Ejemplo de salida:
# 📋 Tabla del 3
# ================
# 3 × 1 = 3
# 3 × 2 = 6
# ...
# 3 × 12 = 36
```

### 💡 Tips Útiles
- Usa `for i in range(1, 13):` para ir del 1 al 12
- Formatea con `f"{numero} × {i} = {numero * i}"`
- Añade decoración para hacer más atractivo el resultado

### 🎉 Motivación
¡Acabas de recrear digitalmente las tablas de multiplicar! Tu código ahora puede enseñar matemáticas a otros estudiantes. ¡Eres un educador digital! 🎓

---

## 💻 Ejercicio 14: Acumulador de Números

### 🎯 Problema
Permitir al usuario ingresar varios números y calcular su suma total, promedio y cantidad ingresada hasta que escriba "fin".

### 📝 Descripción
Tu programa debe usar un bucle `while` para permitir al usuario ingresar números uno por uno. Cuando escriba "fin", debe mostrar estadísticas: suma total, cantidad de números y promedio.

### ⚙️ Funcionalidades
- Solicitar números continuamente hasta que el usuario escriba "fin"
- Acumular la suma total
- Contar cuántos números se ingresaron
- Calcular y mostrar el promedio

### 🧪 Casos de Prueba
1. Números: 10, 20, 30, fin → Suma: 60, Cantidad: 3, Promedio: 20.0
2. Números: 5, 15, fin → Suma: 20, Cantidad: 2, Promedio: 10.0
3. Números: 100, fin → Suma: 100, Cantidad: 1, Promedio: 100.0

### 💻 Código Base
```python
# Acumulador de Números 🔢
print("🔢 Acumulador de Números")
print("=" * 25)
print("Ingresa números (escribe 'fin' para terminar)")

# Tu código aquí 👇


# Ejemplo de salida:
# Suma total: 60
# Cantidad de números: 3
# Promedio: 20.0
```

### 💡 Tips Útiles
- Usa `while True:` con `break` cuando el usuario escriba "fin"
- Valida que la entrada sea un número antes de procesarla
- Evita división por cero al calcular el promedio

### 🎉 Motivación
¡Manejas bucles dinámicos! Ahora tus programas pueden procesar datos de tamaño variable. ¡Este es un patrón muy usado en aplicaciones reales! 📊

---

## 💻 Ejercicio 15: Generador de Patrones Visuales

### 🎯 Problema
Crear patrones visuales usando asteriscos (*) y bucles anidados para formar figuras geométricas.

### 📝 Descripción
Tu programa debe generar diferentes patrones usando bucles anidados:
- Triángulo creciente
- Triángulo decreciente  
- Cuadrado hueco
El usuario puede elegir qué patrón crear y de qué tamaño.

### ⚙️ Funcionalidades
- Menú para elegir tipo de patrón
- Solicitar tamaño del patrón
- Generar el patrón usando bucles anidados
- Mostrar el resultado visualmente

### 🧪 Casos de Prueba
1. Triángulo creciente, tamaño 4:
```
*
**
***
****
```

2. Triángulo decreciente, tamaño 4:
```
****
***
**
*
```

### 💻 Código Base
```python
# Generador de Patrones Visuales ⭐
print("⭐ Generador de Patrones Visuales")
print("=" * 35)

# Tu código aquí 👇


# Ejemplo de salida para triángulo creciente:
# *
# **
# ***
# ****
```

### 💡 Tips Útiles
- Para triángulo creciente: `print("*" * i)` donde i va de 1 a tamaño
- Para triángulo decreciente: `print("*" * i)` donde i va de tamaño a 1
- Usa bucles anidados `for` para mayor control

### 🎉 Motivación
¡Eres un artista del código! Los patrones visuales son la base de los gráficos por computadora y el arte generativo. ¡Tu creatividad no tiene límites! 🎨

---

# 🚀 TEMA 4: Integración de Conocimientos

## 🎯 Descripción del Tema

En este tema final combinarás todo lo aprendido: algoritmos, condicionales y bucles para crear programas completos y funcionales que resuelven problemas complejos del mundo real.

---

## 💻 Ejercicio 16: Sistema de Gestión de Calificaciones

### 🎯 Problema
Crear un sistema completo para manejar calificaciones de estudiantes con múltiples funcionalidades.

### 📝 Descripción
Tu programa debe permitir:
- Ingresar calificaciones de múltiples estudiantes
- Calcular estadísticas (promedio, mejor, peor)
- Mostrar quiénes aprobaron y reprobaron
- Generar reporte final completo

### ⚙️ Funcionalidades
- Registro de estudiantes con sus calificaciones
- Cálculo automático de estadísticas
- Clasificación automática (aprobado/reprobado)
- Reporte detallado y organizado

### 🧪 Casos de Prueba
1. 3 estudiantes: Ana(85), Carlos(92), María(78) → Promedio: 85.0, Mejor: Carlos(92), Todos aprobaron
2. 2 estudiantes: Luis(55), Elena(75) → Promedio: 65.0, Luis reprobó, Elena aprobó

### 💻 Código Base
```python
# Sistema de Gestión de Calificaciones 📚
print("📚 Sistema de Gestión de Calificaciones")
print("=" * 40)

# Tu código aquí 👇


# Ejemplo de salida:
# === REPORTE DE CALIFICACIONES ===
# Total estudiantes: 3
# Promedio general: 85.0
# Mejor calificación: Carlos (92)
# Aprobaron: Ana, Carlos, María
# Reprobaron: Ninguno
```

### 💡 Tips Útiles
- Usa listas para almacenar nombres y calificaciones
- Considera 70 como nota mínima para aprobar
- Usa bucles para procesar todos los estudiantes

### 🎉 Motivación
¡Construiste un sistema real de gestión académica! Este tipo de programas se usan en escuelas y universidades todos los días. 🎓

---

## 💻 Ejercicio 17: Calculadora de Finanzas Personales

### 🎯 Problema
Desarrollar una calculadora que ayude a las personas a planificar sus finanzas personales.

### 📝 Descripción
Tu programa debe calcular:
- Ingresos totales mensuales
- Gastos por categorías (vivienda, comida, transporte, entretenimiento)
- Dinero disponible para ahorro
- Porcentaje de cada categoría del presupuesto
- Recomendaciones financieras

### ⚙️ Funcionalidades
- Registro de ingresos y gastos por categoría
- Cálculos automáticos de porcentajes
- Balance final (sobra/falta dinero)
- Consejos personalizados según el balance

### 🧪 Casos de Prueba
1. Ingresos: $3000, Gastos: $2500 → Ahorro: $500, Consejo: "¡Excelente! Tienes un 16.7% para ahorrar"
2. Ingresos: $2000, Gastos: $2200 → Déficit: $200, Consejo: "Necesitas reducir gastos"

### 💻 Código Base
```python
# Calculadora de Finanzas Personales 💰
print("💰 Calculadora de Finanzas Personales")
print("=" * 40)

# Tu código aquí 👇


# Ejemplo de salida:
# === RESUMEN FINANCIERO ===
# Ingresos totales: $3,000.00
# Gastos totales: $2,500.00
# Disponible para ahorro: $500.00
# Porcentaje de ahorro: 16.7%
# Consejo: ¡Excelente manejo financiero!
```

### 💡 Tips Útiles
- Usa diccionarios para organizar categorías de gastos
- Calcula porcentajes: `(valor / total) * 100`
- Formatea dinero con 2 decimales

### 🎉 Motivación
¡Creaste una herramienta que puede cambiar la vida financiera de las personas! La tecnología al servicio del bienestar personal. 💪

---

## 💻 Ejercicio 18: Juego de Adivinanza Numérica

### 🎯 Problema
Crear un juego interactivo donde la computadora piensa un número y el usuario debe adivinarlo.

### 📝 Descripción
Tu programa debe:
- Generar un número aleatorio entre 1 y 100
- Dar pistas ("muy alto", "muy bajo", "cerca")
- Contar los intentos del usuario
- Felicitar según el desempeño

### ⚙️ Funcionalidades
- Generación de número aleatorio
- Sistema de pistas inteligentes
- Contador de intentos
- Diferentes niveles de felicitación

### 🧪 Casos de Prueba
1. Número secreto: 50, Usuario adivina en 5 intentos → "¡Excelente!"
2. Número secreto: 25, Usuario adivina en 10 intentos → "¡Bien hecho!"

### 💻 Código Base
```python
import random

# Juego de Adivinanza Numérica 🎯
print("🎯 Juego de Adivinanza Numérica")
print("=" * 35)
print("He pensado un número entre 1 y 100")
print("¡Trata de adivinarlo!")

# Tu código aquí 👇


# Ejemplo de salida:
# Tu número: 75
# ¡Muy alto! Intenta con uno menor
# Tu número: 25
# ¡Muy bajo! Intenta con uno mayor
# Tu número: 50
# ¡CORRECTO! Lo adivinaste en 3 intentos
```

### 💡 Tips Útiles
- Usa `random.randint(1, 100)` para generar el número
- Implementa pistas: "alto", "bajo", "muy cerca"
- Usa bucle `while` hasta que adivine

### 🎉 Motivación
¡Creaste tu primer videojuego! Los juegos son una de las aplicaciones más divertidas de la programación. ¡Sigue desarrollando tu creatividad! 🎮

---

## 💻 Ejercicio 19: Analizador de Texto

### 🎯 Problema
Desarrollar un analizador que examine un texto y proporcione estadísticas detalladas sobre él.

### 📝 Descripción
Tu programa debe analizar un texto ingresado por el usuario y mostrar:
- Número total de caracteres
- Número de palabras
- Número de oraciones
- Palabra más larga
- Frecuencia de vocales
- Porcentaje de espacios

### ⚙️ Funcionalidades
- Análisis completo de texto
- Conteo de diferentes elementos
- Identificación de patrones
- Reporte estadístico organizado

### 🧪 Casos de Prueba
1. Texto: "Hola mundo" → 10 caracteres, 2 palabras, palabra más larga: "mundo"
2. Texto: "Python es genial" → 15 caracteres, 3 palabras, palabra más larga: "Python"

### 💻 Código Base
```python
# Analizador de Texto 📝
print("📝 Analizador de Texto")
print("=" * 25)

# Tu código aquí 👇


# Ejemplo de salida:
# === ANÁLISIS DE TEXTO ===
# Texto: "Hola mundo"
# Caracteres totales: 10
# Palabras: 2
# Palabra más larga: mundo (5 letras)
# Vocales: a(1), e(0), i(0), o(2), u(1)
```

### 💡 Tips Útiles
- Usa `.split()` para separar palabras
- Usa `.count()` para contar caracteres específicos
- Recorre cada carácter con un bucle `for`

### 🎉 Motivación
¡Construiste una herramienta de análisis de texto! Estas técnicas son la base del procesamiento de lenguaje natural y la inteligencia artificial. 🤖

---

## 💻 Ejercicio 20: Sistema de Inventario

### 🎯 Problema
Crear un sistema completo de gestión de inventario para una tienda pequeña.

### 📝 Descripción
Tu programa debe manejar:
- Lista de productos con nombres, cantidades y precios
- Agregar nuevos productos
- Actualizar cantidades existentes
- Calcular valor total del inventario
- Generar alertas de stock bajo
- Reporte completo del inventario

### ⚙️ Funcionalidades
- Gestión completa de productos
- Cálculos automáticos de valores
- Sistema de alertas
- Reportes organizados y claros

### 🧪 Casos de Prueba
1. 3 productos: Laptop($800, 5), Mouse($25, 20), Teclado($50, 2) → Valor total: $4550, Alerta: Teclado (stock bajo)

### 💻 Código Base
```python
# Sistema de Inventario 📦
print("📦 Sistema de Inventario")
print("=" * 25)

# Tu código aquí 👇


# Ejemplo de salida:
# === INVENTARIO ACTUAL ===
# Laptop: $800.00 x 5 = $4,000.00
# Mouse: $25.00 x 20 = $500.00
# Teclado: $50.00 x 2 = $100.00 ⚠️ STOCK BAJO
# 
# Valor total: $4,600.00
# Productos con stock bajo: Teclado
```

### 💡 Tips Útiles
- Usa listas de diccionarios para almacenar productos
- Considera stock bajo cuando cantidad < 5
- Suma todos los valores para obtener el total

### 🎉 Motivación
¡Felicitaciones! Has creado un sistema de gestión empresarial completo. Este tipo de software es esencial para cualquier negocio moderno. 🏪

---

# 🎯 PROYECTO INTEGRADOR: Sistema de Gestión Escolar Completo

## 📋 Descripción del Proyecto

Desarrolla un sistema completo que combine todos los conceptos aprendidos para gestionar información escolar básica.

### 🎯 Requerimientos del Sistema

Tu sistema debe incluir:

1. **Módulo de Estudiantes**
   - Registrar estudiantes con nombre y edad
   - Clasificar por categoría de edad

2. **Módulo de Calificaciones**
   - Ingresar calificaciones por materia
   - Calcular promedios individuales
   - Generar reportes de rendimiento

3. **Módulo de Estadísticas**
   - Calcular promedio general del grupo
   - Identificar mejor y peor estudiante
   - Contar aprobados y reprobados

4. **Módulo de Reportes**
   - Generar reporte individual por estudiante
   - Generar reporte grupal
   - Mostrar estadísticas completas

### 🧪 Casos de Prueba del Proyecto

1. Registrar 3 estudiantes con 3 calificaciones cada uno
2. Generar todos los reportes
3. Verificar que los cálculos sean correctos
4. Confirmar que la clasificación funcione

### 💻 Estructura Base del Proyecto

```python
# 🏫 Sistema de Gestión Escolar Completo
print("🏫 SISTEMA DE GESTIÓN ESCOLAR")
print("=" * 35)

# Variables globales para almacenar datos
estudiantes = []
calificaciones = []

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    # Tu código aquí
    pass

def registrar_estudiante():
    """Registra un nuevo estudiante"""
    # Tu código aquí
    pass

def ingresar_calificaciones():
    """Ingresa calificaciones para un estudiante"""
    # Tu código aquí
    pass

def generar_reporte_individual():
    """Genera reporte de un estudiante específico"""
    # Tu código aquí
    pass

def generar_reporte_grupal():
    """Genera reporte de todo el grupo"""
    # Tu código aquí
    pass

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        # Tu lógica del menú aquí
        
if __name__ == "__main__":
    main()
```

### 🏆 Criterios de Evaluación

- ✅ **Funcionalidad**: Todas las características funcionan correctamente
- ✅ **Integración**: Combina algoritmos, condicionales y bucles
- ✅ **Interfaz**: Menús claros y fáciles de usar
- ✅ **Cálculos**: Matemáticas precisas y validadas
- ✅ **Reportes**: Información organizada y comprensible

---

# 🏃‍♂️ RETO PERSONAL: Expansión Creativa

## 🚀 Desafío Final

Ahora que dominas los fundamentos, ¡es hora de ser creativo! Elige UNO de estos retos adicionales para demostrar tu maestría:

### 🎮 Opción A: Mini Juego de Aventura
Crea un juego de texto donde el jugador toma decisiones que afectan la historia.

### 📊 Opción B: Dashboard Personal
Desarrolla una aplicación que rastree hábitos diarios (ejercicio, lectura, etc.).

### 💰 Opción C: Simulador de Inversiones
Construye un programa que simule inversiones y calcule ganancias futuras.

### 🌟 Opción D: Tu Propia Idea
¡Sorpréndeme con tu creatividad! Diseña algo único que resuelva un problema que te interese.

## 🎯 Requisitos del Reto

Tu proyecto debe incluir:
- Al menos 100 líneas de código
- Uso de todos los conceptos del curso
- Interfaz de usuario amigable
- Documentación básica (comentarios explicativos)
- Casos de prueba para validar funcionamiento

---

# 🎉 ¡FELICITACIONES! 

```
    🎊 ¡LO LOGRASTE! 🎊
    
    ┌─────────────────────────────────────┐
    │  🏆 CERTIFICADO DE COMPLETACIÓN 🏆  │
    │                                     │
    │      Has dominado exitosamente      │
    │   FUNDAMENTOS DE PROGRAMACIÓN       │
    │           CON PYTHON                │
    │                                     │
    │  ✅ Algoritmos y lógica             │
    │  ✅ Estructuras condicionales       │
    │  ✅ Bucles y repetición             │
    │  ✅ Integración de conceptos        │
    │                                     │
    │  ¡Estás listo para el siguiente     │
    │       nivel de programación!        │
    └─────────────────────────────────────┘
```

## 🚀 Próximos Pasos

Ahora que dominas los fundamentos, puedes continuar con:

1. **🔧 Funciones y Modularidad** - Organiza mejor tu código
2. **📊 Estructuras de Datos Avanzadas** - Listas, diccionarios, conjuntos
3. **📁 Manejo de Archivos** - Lee y escribe datos persistentes
4. **🌐 Programación Web** - Crea aplicaciones web con Flask
5. **🤖 Inteligencia Artificial** - Machine Learning con Python

## 💭 Reflexión Final

Has recorrido un camino increíble desde escribir tu primer `print("Hola Mundo")` hasta crear sistemas completos de gestión. Cada línea de código que escribiste te ha hecho más fuerte como programador.

Recuerda: **la programación es un superpoder**, y ahora tienes las herramientas básicas para cambiar el mundo, una línea de código a la vez.

---

### 📚 Recursos Adicionales

- **Documentación oficial de Python**: python.org
- **Práctica diaria**: HackerRank, LeetCode, Codewars
- **Comunidad**: Stack Overflow, Reddit r/Python
- **Proyectos**: GitHub para compartir tu código

### 🤝 Mantente Conectado

Tu viaje de programación apenas comienza. Mantén la curiosidad, practica regularmente y nunca dejes de aprender. ¡El mundo tech te espera con los brazos abiertos!

**¡Sigue programando y cambiando el mundo! 🌟💻🚀**