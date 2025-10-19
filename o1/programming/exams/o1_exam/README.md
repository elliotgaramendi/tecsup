# 📝 🐍 Examen de Python - Fundamentos de Programación 🐍 📝

```
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║          🎓 EXAMEN DE FUNDAMENTOS PYTHON 🐍 🎓            ║
    ║                                                          ║
    ║            🌟 Demuestra lo que has aprendido 🌟           ║
    ║                                                          ║
    ║      ✨ Sé valiente, confía en ti y ¡sorpréndete! ✨      ║
    ║                                                          ║
    ║       ╔═════════════════════════════════════════╗        ║
    ║       ║  🚀 ¡TÚ PUEDES LOGRARLO PROGRAMADOR! 🚀  ║        ║
    ║       ╚═════════════════════════════════════════╝        ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
```

---

## 📋 Instrucciones Generales

¡Bienvenido al examen de Python, futuro desarrollador! 🐍✨ En este examen pondrás a prueba todo lo que has aprendido durante tu formación. Recuerda que cada desafío es una oportunidad para crecer como programador.

**📌 Recomendaciones Importantes:**
- 🔍 Lee cuidadosamente cada problema antes de comenzar
- 📐 Sigue la estructura del código base proporcionado
- ✅ Prueba tu código con todos los casos de prueba
- 💭 No tengas miedo de experimentar y cometer errores
- 🎯 Recuerda los tips útiles para cada ejercicio
- **🏆 ¡Tú puedes lograrlo! ADELANTE PROGRAMADOR! 💪**

---

# 🧩 Tema 1️⃣ : Algoritmos y Representación en Código 🐍

## 📊 o1.1: 🔴 Área y Perímetro del Círculo

### 🎯 Problema
Crear un programa que calcule tanto el área como el perímetro de un círculo a partir del radio ingresado por el usuario.

### 📝 Descripción
Tu programa debe solicitar el radio de un círculo y calcular dos valores importantes:
- **El área del círculo** usando la fórmula: **A = π × r²**
- **El perímetro del círculo** usando la fórmula: **P = 2 × π × r**

Utiliza `pi = 3.14159` para los cálculos. Ambos resultados deben almacenarse en variables separadas.

### ⚙️ Funcionalidades
- 📥 Solicitar el radio del círculo al usuario
- 🧮 Calcular el área usando la fórmula matemática
- 📏 Calcular el perímetro usando la fórmula matemática
- 💾 Almacenar ambos resultados en variables separadas

### 🧪 Casos de Prueba
| Test | Radio | Área Esperada | Perímetro Esperado |
|------|-------|---------------|--------------------|
| 1️⃣ | 5 | 78.54875 | 31.4159 |
| 2️⃣ | 10 | 314.159 | 62.8318 |
| 3️⃣ | 2 | 12.56636 | 12.56636 |
| 4️⃣ | 7 | 153.938 | 43.98226 |

### 💻 Código Base
```python
# Circle Area and Perimeter Calculator 🔴
print("🔴 Calculadora de Círculo")
print("=" * 40)

# Your code here 👇
pi = 3.14159
area = 0
perimeter = 0

# Example output:
# El área del círculo es: 78.54875 cm² 🔴
# El perímetro del círculo es: 31.4159 cm 📏

# Test cases:
print("=" * 40)
print(area == 78.54875 and perimeter == 31.4159)
print(area == 314.159 and perimeter == 62.8318)
print(area == 12.56636 and perimeter == 12.56636)
print(area == 153.938 and perimeter == 43.98226)
```

### 💡 Tips Útiles
- ✏️ Convierte el radio a float con `float(input())`
- 🔧 Recuerda usar `**` para elevar a una potencia: `radio ** 2`
- ✖️ El símbolo `*` multiplica: `2 * pi * radio`
- 📍 Almacena cada resultado en una variable diferente

### 🎉 Motivación
¡Combinas múltiples fórmulas matemáticas en un solo programa! 🌟 Los círculos son fundamentales en geometría, física e ingeniería. ¡Vas muy bien en tu camino programador! 🚀✨

---

## 💱 o1.2: 💵 Conversión de Monedas (Soles a Dólares y Euros)

### 🎯 Problema
Crear un programa que convierta una cantidad de dinero en soles peruanos a dólares estadounidenses y a euros.

### 📝 Descripción
Tu programa debe solicitar una cantidad en soles al usuario y convertirla a dos monedas diferentes usando tasas de cambio fijas. Usa las tasas internacionales:
- **1 sol = 0.3 dólares** 💵
- **1 sol = 0.25 euros** 💶

Almacena ambas conversiones en variables separadas y muestra los resultados con precisión.

### ⚙️ Funcionalidades
- 📥 Solicitar cantidad en soles peruanos al usuario
- 🔄 Convertir a dólares usando la tasa de cambio
- 🔄 Convertir a euros usando la tasa de cambio
- 💾 Almacenar ambas conversiones en variables

### 🧪 Casos de Prueba
| Test | Soles | Dólares Esperados | Euros Esperados |
|------|-------|-------------------|-----------------|
| 1️⃣ | 1000 | 300.0 | 250.0 |
| 2️⃣ | 500 | 150.0 | 125.0 |
| 3️⃣ | 2000 | 600.0 | 500.0 |
| 4️⃣ | 800 | 240.0 | 200.0 |

### 💻 Código Base
```python
# Currency Converter 💱
print("💱 Conversor de Monedas Peruanas 🇵🇪")
print("=" * 40)

# Your code here 👇
dollars = 0
euros = 0

# Example output:
# 1000 soles equivale a:
# 300.0 dólares 💵
# 250.0 euros 💶

# Test cases:
print("=" * 40)
print(dollars == 300.0 and euros == 250.0)
print(dollars == 150.0 and euros == 125.0)
print(dollars == 600.0 and euros == 500.0)
print(dollars == 240.0 and euros == 200.0)
```

### 💡 Tips Útiles
- ✏️ Define las tasas como variables: `rate_dollars = 0.3` y `rate_euros = 0.25`
- ✖️ Multiplica los soles por la tasa correspondiente
- 🔧 Usa `round()` si necesitas redondear a 2 decimales
- 📍 Almacena cada conversión en su propia variable

### 🎉 Motivación
¡Trabajas con dinero y tasas de cambio internacionales! 💰 Las conversiones de monedas son esenciales en comercio internacional y finanzas. ¡Como peruano, dominas tu economía local en código! 🇵🇪✨

---

# 🔀 Tema 2️⃣ : Estructuras Condicionales Básicas 🐍

## 🎓 o2.1: 📊 Calificación y Recomendación

### 🎯 Problema
Crear un programa que reciba una calificación numérica (0-100) y asigne una letra de calificación (A, B, C, D, F) con una recomendación específica.

### 📝 Descripción
Tu programa debe solicitar una calificación numérica y clasificarla según estos rangos:
- 🌟 **90-100: Excelente (A)** - Desempeño excepcional
- ⭐ **80-89: Muy Bien (B)** - Desempeño sobresaliente
- ✨ **70-79: Bien (C)** - Desempeño satisfactorio
- 👍 **60-69: Suficiente (D)** - Desempeño mínimo aceptable
- ❌ **0-59: Insuficiente (F)** - Necesita mejorar

Además, debe guardar una recomendación diferente para cada rango.

### ⚙️ Funcionalidades
- 📥 Solicitar calificación numérica (0-100)
- 🔀 Clasificar en la letra de calificación correspondiente
- 💭 Asignar una recomendación basada en el rango
- 💾 Almacenar tanto la letra como la recomendación

### 🧪 Casos de Prueba
| Test | Calificación | Letra | Recomendación |
|------|--------------|-------|---------------|
| 1️⃣ | 95 | A | excelente |
| 2️⃣ | 75 | C | bien |
| 3️⃣ | 50 | F | insuficiente |
| 4️⃣ | 82 | B | muy bien |

### 💻 Código Base
```python
# Grade Classifier 📊
print("📊 Clasificador de Calificaciones 🎓")
print("=" * 40)

# Your code here 👇
letter = ""
recommendation = ""

# Example output:
# Tu calificación es: A 🌟
# Recomendación: ¡Excelente desempeño! Sigue así

# Test cases:
print("=" * 40)
print(letter == "A" and recommendation == "excelente")
print(letter == "C" and recommendation == "bien")
print(letter == "F" and recommendation == "insuficiente")
print(letter == "B" and recommendation == "muy bien")
```

### 💡 Tips Útiles
- 🔀 Usa `if grade >= 90:` para verificar los rangos
- 🔀 Usa `elif grade >= 80:` para el siguiente rango
- 🔀 Continúa con `elif` para cada rango
- ✏️ Asigna tanto la letra como la recomendación en cada rama

### 🎉 Motivación
¡Clasificas de forma inteligente! 🧠 Tu programa ahora puede evaluar desempeño académico con recomendaciones personalizadas. Los sistemas de calificación como este son usados en universidades de todo el mundo. 🎓✨

---

## 🔺 o2.2: 📐 Detector de Triángulo Válido

### 🎯 Problema
Crear un programa que determine si tres valores ingresados pueden formar un triángulo válido.

### 📝 Descripción
Tu programa debe solicitar tres valores (lados de un posible triángulo) y verificar si pueden formar un triángulo válido. Según el teorema de desigualdad triangular, tres lados forman un triángulo válido si:
- ✅ La suma de dos lados cualesquiera es mayor que el tercer lado
- ✅ Todos los lados son positivos

Si es válido, clasifica el triángulo como:
- 🔺 **Equilátero** - todos los lados iguales
- 🔺 **Isósceles** - dos lados iguales
- 🔺 **Escaleno** - todos los lados diferentes

### ⚙️ Funcionalidades
- 📥 Solicitar tres valores al usuario
- ✔️ Verificar si forman un triángulo válido
- 📐 Clasificar el tipo de triángulo
- 💾 Almacenar el resultado en una variable

### 🧪 Casos de Prueba
| Test | Lado 1 | Lado 2 | Lado 3 | Tipo |
|------|--------|--------|--------|------|
| 1️⃣ | 5 | 5 | 5 | equilátero |
| 2️⃣ | 5 | 5 | 8 | isósceles |
| 3️⃣ | 3 | 4 | 5 | escaleno |
| 4️⃣ | 6 | 6 | 6 | equilátero |

### 💻 Código Base
```python
# Triangle Validator 🔺
print("🔺 Validador de Triángulos 📐")
print("=" * 40)

# Your code here 👇
triangle_type = ""

# Example output:
# ¡Triángulo válido! Es equilátero 🔺

# Test cases:
print("=" * 40)
print(triangle_type == "equilátero")
print(triangle_type == "isósceles")
print(triangle_type == "escaleno")
print(triangle_type == "equilátero")
```

### 💡 Tips Útiles
- ✔️ Primero verifica si es válido: `if (a + b > c) and (a + c > b) and (b + c > a):`
- 🔀 Luego clasifica: compara si `a == b == c` (equilátero)
- 🔀 Verifica si dos son iguales (isósceles)
- 🔀 Si no coincide nada anterior, es escaleno

### 🎉 Motivación
¡Aplicas geometría pura en código! 📐 Tu programa valida propiedades matemáticas fundamentales. Esto es lo que usan los ingenieros y arquitectos para diseñar estructuras. ¡Eres un especialista en matemáticas computacionales! 🏗️✨

---

# 🔁 Tema 3️⃣ : Estructuras Repetitivas Básicas 🐍

## 🧮 o3.1: ➕ Suma de Números Pares en Rango

### 🎯 Problema
Crear un programa que sume todos los números pares entre dos valores dados por el usuario.

### 📝 Descripción
Tu programa debe solicitar dos números (inicio y fin de un rango) y sumar únicamente los números pares que se encuentren entre ellos. Por ejemplo, si el usuario ingresa 1 y 10, debe sumar: **2 + 4 + 6 + 8 + 10 = 30**.

### ⚙️ Funcionalidades
- 📥 Solicitar número de inicio del rango
- 📥 Solicitar número de fin del rango
- 🔁 Recorrer el rango con un bucle
- 🔍 Identificar números pares usando módulo
- ➕ Acumular la suma de pares

### 🧪 Casos de Prueba
| Test | Inicio | Final | Suma Esperada |
|------|--------|-------|---------------|
| 1️⃣ | 1 | 10 | 30 |
| 2️⃣ | 5 | 15 | 50 |
| 3️⃣ | 2 | 8 | 20 |
| 4️⃣ | 1 | 20 | 110 |

### 💻 Código Base
```python
# Even Numbers Sum 🧮
print("🧮 Suma de Números Pares ➕")
print("=" * 35)

# Your code here 👇
even_sum = 0

# Example output:
# La suma de números pares entre 1 y 10 es: 30 ✅

# Test cases:
print("=" * 35)
print(even_sum == 30)
print(even_sum == 50)
print(even_sum == 20)
print(even_sum == 110)
```

### 💡 Tips Útiles
- 🔁 Usa `for i in range(start, end + 1):` para incluir el final
- 🔍 Verifica si es par con `if i % 2 == 0:`
- ➕ Acumula con `even_sum += i`
- 🎯 Recuerda iniciar `even_sum = 0`

### 🎉 Motivación
¡Filtras y acumulas datos inteligentemente! 📊 Combinas bucles con condicionales para procesar rangos de números. ¡Estás dominando el análisis de datos! 🚀✨

---

## 🔺 o3.2: 🎨 Pirámide Numérica

### 🎯 Problema
Crear un programa que genere una pirámide numérica según el número ingresado por el usuario.

### 📝 Descripción
Tu programa debe solicitar un número n al usuario y generar una pirámide donde cada fila contiene números del 1 hasta el número de fila. Por ejemplo, si n = 5:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

Usa **bucles anidados** para lograr esto. Debes contar el total de números impresos.

### ⚙️ Funcionalidades
- 📥 Solicitar número para el tamaño de la pirámide
- 🔁 Usar bucles anidados (exterior para filas, interior para números)
- 🎨 Generar cada fila con números ascendentes
- 🔢 Contar el total de números impresos

### 🧪 Casos de Prueba
| Test | n | Total Números |
|------|---|----------------|
| 1️⃣ | 3 | 6 (1+2+3) |
| 2️⃣ | 4 | 10 (1+2+3+4) |
| 3️⃣ | 5 | 15 (1+2+3+4+5) |
| 4️⃣ | 6 | 21 (1+2+3+4+5+6) |

### 💻 Código Base
```python
# Number Pyramid 🔺
print("🔺 Pirámide Numérica 🎨")
print("=" * 30)

# Your code here 👇
total_count = 0

# Example output:
# 1
# 1 2
# 1 2 3

# Test cases:
print("=" * 30)
print(total_count == 6)
print(total_count == 10)
print(total_count == 15)
print(total_count == 21)
```

### 💡 Tips Útiles
- 🔁 Usa `for i in range(1, n + 1):` para las filas
- 🔁 Dentro, usa `for j in range(1, i + 1):` para los números de cada fila
- ✏️ Usa `print(j, end=" ")` para imprimir en la misma línea
- 🔢 Incrementa contador con cada número: `total_count += 1`
- 📍 Usa `print()` después de cada fila para saltar a la siguiente

### 🎉 Motivación
¡Dominas bucles anidados! 🎨 Generar patrones visuales es lo que usan los programadores para crear gráficos, juegos y visualizaciones. ¡Eres un artista del código! 🌈✨

---

# 🚀 Tema 4️⃣ : Integración de Conocimientos 🐍

## 🛒 o4.1: 💰 Sistema de Venta con Descuento

### 🎯 Problema
Crear un programa que calcule el precio final de una compra después de aplicar un descuento basado en la cantidad de artículos.

### 📝 Descripción
Tu programa debe solicitar el precio unitario de un artículo y la cantidad de artículos a comprar. Luego, debe aplicar un descuento según la cantidad:
- 📦 **1-5 artículos**: sin descuento (0%)
- 📦📦 **6-10 artículos**: descuento del 10%
- 📦📦📦 **11-20 artículos**: descuento del 15%
- 📦📦📦📦 **más de 20 artículos**: descuento del 20%

Finalmente, calcula el precio total después del descuento y muestra el ahorro.

### ⚙️ Funcionalidades
- 📥 Solicitar precio unitario
- 📥 Solicitar cantidad de artículos
- 🔀 Determinar el descuento según la cantidad
- 🧮 Calcular precio total sin descuento
- 💰 Calcular precio final con descuento
- 📊 Mostrar el ahorro total

### 🧪 Casos de Prueba
| Test | Precio Unit. | Cantidad | Precio Final | Descuento |
|------|--------------|----------|--------------|-----------|
| 1️⃣ | 100 | 5 | 500 | 0 |
| 2️⃣ | 100 | 10 | 900 | 100 |
| 3️⃣ | 100 | 25 | 2000 | 500 |
| 4️⃣ | 50 | 15 | 425 | 75 |

### 💻 Código Base
```python
# Sales System with Discount 🛒
print("🛒 Sistema de Venta con Descuento 💰")
print("=" * 40)

# Your code here 👇
final_price = 0
discount = 0

# Example output:
# Precio sin descuento: $500
# Descuento aplicado: 0%
# Precio final: $500 ✅

# Test cases:
print("=" * 40)
print(final_price == 500 and discount == 0)
print(final_price == 900 and discount == 100)
print(final_price == 2000 and discount == 500)
print(final_price == 425 and discount == 75)
```

### 💡 Tips Útiles
- 🧮 Calcula subtotal: `subtotal = unit_price * quantity`
- 🔀 Usa `if/elif/else` para determinar el descuento porcentual
- 💵 Calcula descuento: `discount = subtotal * (discount_percent / 100)`
- 💰 Calcula final: `final_price = subtotal - discount`
- 🔧 Redondea si es necesario

### 🎉 Motivación
¡Creaste un sistema real de ventas! 🛍️ Las tiendas usan lógica exactamente como esta para calcular precios con descuentos. ¡Eres un desarrollador de software comercial! 💼✨

---

## 🎮 o4.2: 🎲 Adivina el Número Mejorado

### 🎯 Problema
Crear un juego donde el usuario debe adivinar un número secreto entre 1 y 100 con máximo 7 intentos, recibiendo pistas después de cada intento fallido.

### 📝 Descripción
Tu programa debe generar un número secreto fijo (usa 42 como ejemplo). El usuario tiene **7 intentos** para adivinarlo. Después de cada intento incorrecto, el programa debe decir si el número es **"mayor"** o **"menor"** al número secreto. El programa debe:
- 🔢 Contar los intentos realizados
- ✅ Determinar si el usuario ganó o perdió
- 📊 Mostrar el número de intentos usados

### ⚙️ Funcionalidades
- 🎯 Definir número secreto fijo
- 🔁 Usar bucle para permitir múltiples intentos
- 🔍 Comparar cada intento con el número secreto
- 💬 Dar pistas (mayor/menor)
- 🔢 Contar intentos realizados
- 🏆 Determinar ganador o perdedor

### 🧪 Casos de Prueba
| Test | Secret | Intento | Resultado | Intentos |
|------|--------|---------|-----------|----------|
| 1️⃣ | 42 | 42 | ganaste | 1 |
| 2️⃣ | 42 | 30 | mayor | 1 |
| 3️⃣ | 42 | 50 | menor | 1 |
| 4️⃣ | 42 | 35 | mayor | 1 |

### 💻 Código Base
```python
# Improved Guessing Game 🎮
print("🎮 Juego de Adivinanza Mejorado 🎲")
print("=" * 40)
print("Adivina el número entre 1 y 100 🎯")
print("¡Tienes 7 intentos! 💪")

# Your code here 👇
secret_number = 42
result = ""
attempts = 0

# Example output:
# Intento 1: ¿Cuál es tu número? 30
# ¡El número es mayor! 📈

# Test cases:
print("=" * 40)
print(result == "ganaste" and attempts == 1)
print(result == "mayor" and attempts == 1)
print(result == "menor" and attempts == 1)
print(result == "mayor" and attempts == 1)
```

### 💡 Tips Útiles
- 🔁 Usa `while attempts < 7:` para limitar intentos
- 🎯 Compara con `if guess == secret_number:` para ganar
- 📈 Usa `elif guess < secret_number:` para dar pista mayor
- 📉 Usa `else:` para dar pista menor
- ➕ Incrementa `attempts += 1` en cada iteración
- 🛑 Usa `break` para salir cuando adivine correctamente

### 🎉 Motivación
¡Creaste un juego interactivo completo! 🎮 Combinas todas tus habilidades: bucles, condicionales, contadores y lógica. ¡Eres un desarrollador de videojuegos! 🕹️✨

---

## 🏆 ¡LO HICISTE, PROGRAMADOR! 🎊

```
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║            🌟 ¡FELICIDADES POR COMPLETAR               ║
    ║              EL EXAMEN DE PYTHON! 🐍 🌟                 ║
    ║                                                        ║
    ║    ✨ Cada reto que resolviste te acerca más a         ║
    ║       convertirte en un verdadero programador ✨       ║
    ║                                                        ║
    ║         Recuerda: La programación es un viaje,         ║
    ║           no un destino. ¡Sigue adelante! 🚀           ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
```

### 📚 Próximos Pasos:

- 🔄 Practica estos retos varias veces
- 🎨 Intenta modificarlos con tus propias ideas
- 💡 Comienza a crear tus propios programas
- ♾️ ¡Nunca dejes de aprender!
- 📖 Explora nuevos conceptos: Listas, Diccionarios, Funciones
- 🤝 Comparte tu código con otros programadores

### ✨ Recuerda Siempre:

> **"Cada experto fue una vez un principiante."**
>
> 🐍 Estás en el camino correcto.
>
> 💪 ¡Adelante, programador! 🚀
>
> 🌟 El mundo del código te espera. ¡Domínalo! ✨

---

## 🐍 ¡BIENVENIDO AL MUNDO DE LA PROGRAMACIÓN! 🐍

**¡GRACIAS POR TU DEDICACIÓN Y ESFUERZO!** 💚🇵🇪

*Con amor desde la comunidad de programadores Python* 🐍✨
