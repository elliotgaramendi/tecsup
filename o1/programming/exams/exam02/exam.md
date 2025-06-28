# **🐍 Examen de Fundamentos de Python - Estructuras de Control y Tuplas 📚💻**

Este examen está diseñado para evaluar tus conocimientos esenciales en programación con Python. A través de cuatro secciones temáticas, practicarás estructuras condicionales, bucles for, bucles while con bucles anidados, y trabajarás con tuplas. Cada reto te ayudará a aplicar conceptos fundamentales mediante ejercicios prácticos y situaciones cotidianas. Los casos de prueba automatizados te permitirán verificar que tu código funciona correctamente al instante ✅. ¡Demuestra tu dominio de Python paso a paso! 🎯🐍✨

---

## 🎯 o1 Estructuras Condicionales - Toma de Decisiones con If/Else ⚖️🔀

⚙️ En esta sección aprenderás a usar estructuras condicionales en Python para que tu programa tome decisiones según diferentes situaciones. Usarás `if`, `elif` y `else` para ejecutar código diferente dependiendo de las condiciones que evalúes. Este tipo de lógica es esencial para crear programas que respondan de manera diferente según los datos que reciban 🧩🔍.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### Reto o1.1: Verificador de Edad para Votar 🗳️👤

**Problema**: Verifica si una persona puede votar según su edad y muestra un mensaje apropiado 🎯📊

**Descripción**: En muchos países la edad mínima para votar es 18 años. Tu programa debe verificar la edad de una persona y determinar si puede votar o no, mostrando un mensaje claro en cada caso.

🗳️ **Reglas de votación**:

```plaintext
- Si edad >= 18: Puede votar
- Si edad < 18: No puede votar
```

Tu programa debe:

* 🔢 Recibir la edad como número
* ✅ Verificar si es mayor o igual a 18
* 💬 Mostrar "Puede votar" o "No puede votar"
* 🎯 Retornar True o False según corresponda

**Casos de prueba**:

1. Entrada ➡️ edad=20 → puede_votar=True, mensaje="Puede votar"
2. Entrada ➡️ edad=17 → puede_votar=False, mensaje="No puede votar"
3. Entrada ➡️ edad=18 → puede_votar=True, mensaje="Puede votar"
4. Entrada ➡️ edad=15 → puede_votar=False, mensaje="No puede votar"
5. Entrada ➡️ edad=25 → puede_votar=True, mensaje="Puede votar"

**Código base**:

```python
# Reto 1: Verificador de Edad para Votar 🗳️👤
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

can_vote = False        # Esta variable debe calcularse en base a la lógica del problema
message = ""            # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", can_vote == True and message == "Puede votar")
print("🧪 ", can_vote == False and message == "No puede votar")
print("🧪 ", can_vote == True and message == "Puede votar")
print("🧪 ", can_vote == False and message == "No puede votar")
print("🧪 ", can_vote == True and message == "Puede votar")
```

🧠 **Tips útiles**:

* 🔢 Usa `if edad >= 18:` para la condición principal
* ✅ Asigna `can_vote = True` cuando pueda votar
* 💬 Asigna el mensaje correspondiente en cada caso
* 🎯 Usa `else:` para el caso contrario

🗳️ ¡Construye democracia con código! 🏛️✨

---

### Reto o1.2: Clasificador de Números 🔢⚖️

**Problema**: Determina si un número es positivo, negativo o cero y muestra la clasificación correspondiente 📊🎯

**Descripción**: Los números se pueden clasificar según su signo. Tu programa debe recibir un número y determinar si es mayor que cero (positivo), menor que cero (negativo) o igual a cero.

🔢 **Clasificaciones**:

```plaintext
- Si número > 0: "Positivo"
- Si número < 0: "Negativo"  
- Si número == 0: "Cero"
```

Tu programa debe:

* 🔢 Recibir un número (puede ser decimal)
* 🔍 Comparar el número con cero
* 📝 Asignar la clasificación correcta
* 🎯 Retornar la categoría como texto

**Casos de prueba**:

1. Entrada ➡️ número=15 → clasificación="Positivo"
2. Entrada ➡️ número=-8 → clasificación="Negativo"
3. Entrada ➡️ número=0 → clasificación="Cero"
4. Entrada ➡️ número=3.5 → clasificación="Positivo"
5. Entrada ➡️ número=-2.1 → clasificación="Negativo"

**Código base**:

```python
# Reto 2: Clasificador de Números 🔢⚖️
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

classification = ""     # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", classification == "Positivo")
print("🧪 ", classification == "Negativo")
print("🧪 ", classification == "Cero")
print("🧪 ", classification == "Positivo")
print("🧪 ", classification == "Negativo")
```

🧠 **Tips útiles**:

* ➕ Usa `if numero > 0:` para números positivos
* ➖ Usa `elif numero < 0:` para números negativos
* 0️⃣ Usa `else:` para el cero (o `elif numero == 0:`)
* 📝 Asigna el texto exacto en cada caso

🔢 ¡Clasifica números como un matemático! 📐✨

---

### Reto o1.3: Verificador de Contraseñas 🔒🛡️

**Problema**: Evalúa la fortaleza de una contraseña según su longitud y determina si es segura o no 🔐💪

**Descripción**: Las contraseñas seguras suelen tener al menos 8 caracteres. Tu programa debe verificar la longitud de una contraseña y clasificarla como "Segura" o "Insegura" según este criterio.

🔒 **Criterios de seguridad**:

```plaintext
- Si longitud >= 8: "Segura"
- Si longitud < 8: "Insegura"
```

Tu programa debe:

* 🔤 Recibir una contraseña como texto
* 📏 Calcular su longitud con `len()`
* 🔍 Comparar la longitud con 8
* 🛡️ Clasificar como "Segura" o "Insegura"

**Casos de prueba**:

1. Entrada ➡️ password="python123" → longitud=9, seguridad="Segura"
2. Entrada ➡️ password="abc" → longitud=3, seguridad="Insegura"
3. Entrada ➡️ password="password" → longitud=8, seguridad="Segura"
4. Entrada ➡️ password="12345" → longitud=5, seguridad="Insegura"
5. Entrada ➡️ password="mipassword2024" → longitud=14, seguridad="Segura"

**Código base**:

```python
# Reto 3: Verificador de Contraseñas 🔒🛡️
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

password_length = 0     # Esta variable debe calcularse en base a la lógica del problema
security_level = ""     # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", password_length == 9 and security_level == "Segura")
print("🧪 ", password_length == 3 and security_level == "Insegura")
print("🧪 ", password_length == 8 and security_level == "Segura")
print("🧪 ", password_length == 5 and security_level == "Insegura")
print("🧪 ", password_length == 14 and security_level == "Segura")
```

🧠 **Tips útiles**:

* 📏 Usa `len(password)` para obtener la longitud
* 🔍 Compara con `if longitud >= 8:`
* 🛡️ Asigna "Segura" o "Insegura" según corresponda
* 📝 Guarda tanto la longitud como la clasificación

🔒 ¡Protege datos con verificaciones inteligentes! 🛡️💻

---

### Reto o1.4: Calculadora de Descuentos 💰🏷️

**Problema**: Calcula el precio final de un producto aplicando descuentos según el monto de compra 🛍️💸

**Descripción**: Muchas tiendas ofrecen descuentos por volumen de compra. Tu programa debe aplicar diferentes porcentajes de descuento según el monto total de la compra.

💰 **Escala de descuentos**:

```plaintext
- Si compra >= $100: 20% de descuento
- Si compra >= $50: 10% de descuento
- Si compra < $50: Sin descuento (0%)
```

Tu programa debe:

* 💵 Recibir el monto original de compra
* 🔍 Determinar qué descuento aplicar
* 🧮 Calcular el descuento en dinero
* 💸 Calcular el precio final

**Casos de prueba**:

1. Entrada ➡️ monto=$120 → descuento_pct=20, precio_final=$96.0
2. Entrada ➡️ monto=$75 → descuento_pct=10, precio_final=$67.5
3. Entrada ➡️ monto=$30 → descuento_pct=0, precio_final=$30.0
4. Entrada ➡️ monto=$100 → descuento_pct=20, precio_final=$80.0
5. Entrada ➡️ monto=$50 → descuento_pct=10, precio_final=$45.0

**Código base**:

```python
# Reto 4: Calculadora de Descuentos 💰🏷️
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

discount_percentage = 0  # Esta variable debe calcularse en base a la lógica del problema
final_price = 0.0       # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", discount_percentage == 20 and final_price == 96.0)
print("🧪 ", discount_percentage == 10 and final_price == 67.5)
print("🧪 ", discount_percentage == 0 and final_price == 30.0)
print("🧪 ", discount_percentage == 20 and final_price == 80.0)
print("🧪 ", discount_percentage == 10 and final_price == 45.0)
```

🧠 **Tips útiles**:

* 💰 Usa `if monto >= 100:` para el mayor descuento
* 🔍 Usa `elif monto >= 50:` para el descuento medio
* 🧮 Calcula: `precio_final = monto * (1 - descuento/100)`
* 📊 Prueba cada condición en orden de mayor a menor

💰 ¡Crea ofertas irresistibles con lógica! 🛍️✨

---

### Reto o1.5: Evaluador de Calificaciones 🎓📝

**Problema**: Convierte una calificación numérica a letra según la escala académica estándar 📊🔤

**Descripción**: Los sistemas educativos usan letras para representar rangos de calificaciones. Tu programa debe convertir una nota numérica (0-100) a su letra correspondiente.

🎓 **Escala de calificaciones**:

```plaintext
- 90-100: "A" (Excelente)
- 80-89: "B" (Bueno)
- 70-79: "C" (Regular)
- 60-69: "D" (Deficiente)
- 0-59: "F" (Reprobado)
```

Tu programa debe:

* 📊 Recibir una calificación numérica
* 🔍 Determinar en qué rango está
* 🔤 Asignar la letra correspondiente
* 💬 Mostrar también la descripción

**Casos de prueba**:

1. Entrada ➡️ nota=95 → letra="A", descripción="Excelente"
2. Entrada ➡️ nota=82 → letra="B", descripción="Bueno"
3. Entrada ➡️ nota=75 → letra="C", descripción="Regular"
4. Entrada ➡️ nota=65 → letra="D", descripción="Deficiente"
5. Entrada ➡️ nota=45 → letra="F", descripción="Reprobado"

**Código base**:

```python
# Reto 5: Evaluador de Calificaciones 🎓📝
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

letter_grade = ""       # Esta variable debe calcularse en base a la lógica del problema
description = ""        # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", letter_grade == "A" and description == "Excelente")
print("🧪 ", letter_grade == "B" and description == "Bueno")
print("🧪 ", letter_grade == "C" and description == "Regular")
print("🧪 ", letter_grade == "D" and description == "Deficiente")
print("🧪 ", letter_grade == "F" and description == "Reprobado")
```

🧠 **Tips útiles**:

* 📊 Usa `if nota >= 90:` para empezar desde la nota más alta
* 🔍 Continúa con `elif nota >= 80:`, `elif nota >= 70:`, etc.
* 🔤 Asigna tanto la letra como la descripción en cada caso
* 🎯 El último `else:` será para las notas menores a 60

🎓 ¡Evalúa el conocimiento con precisión! 📚⭐

---


## 🔄 o2 Bucles For Loop en Python - Repetición y Acumulación de Datos 📊💪

🎯 En esta sección aprenderás a usar bucles `for` para repetir código y procesar listas de datos. Los bucles `for` te permiten ejecutar el mismo código varias veces con diferentes valores, y los acumuladores te ayudan a sumar, contar o guardar resultados mientras el bucle se ejecuta. Estos conceptos son fundamentales para trabajar con conjuntos de datos 📈🔍.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### Reto o2.1: Suma de Números en una Lista 📊➕

**Problema**: Usa un bucle `for` para sumar todos los números de una lista y calcular el promedio 🧮📈

**Descripción**: Los bucles `for` son perfectos para recorrer listas de números. En este ejercicio usarás un acumulador para sumar todos los números de una lista y luego calcular el promedio dividiendo la suma entre la cantidad de números.

🔢 **Proceso de suma**:

```plaintext
1. Crear un acumulador en 0
2. Para cada número en la lista:
   - Sumar el número al acumulador
3. Calcular promedio = suma / cantidad de números
```

Tu programa debe:

* ➕ Sumar todos los números de la lista
* 📊 Contar cuántos números hay
* 🧮 Calcular el promedio
* 🎯 Mostrar la suma total y el promedio

**Casos de prueba**:

1. Entrada ➡️ números=[1,2,3,4,5] → suma=15, promedio=3.0
2. Entrada ➡️ números=[10,20,30] → suma=60, promedio=20.0
3. Entrada ➡️ números=[2,4,6,8] → suma=20, promedio=5.0
4. Entrada ➡️ números=[5,10,15,20,25] → suma=75, promedio=15.0
5. Entrada ➡️ números=[1,3,5,7,9,11] → suma=36, promedio=6.0

**Código base**:

```python
# Reto 1: Suma de Números en una Lista 📊➕
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

total_sum = 0           # Esta variable debe calcularse en base a la lógica del problema
average = 0.0           # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", total_sum == 15 and average == 3.0)
print("🧪 ", total_sum == 60 and average == 20.0)
print("🧪 ", total_sum == 20 and average == 5.0)
print("🧪 ", total_sum == 75 and average == 15.0)
print("🧪 ", total_sum == 36 and average == 6.0)
```

🧠 **Tips útiles**:

* ➕ Inicializa `suma = 0` antes del bucle
* 🔄 Usa `for numero in lista:` para recorrer
* 📊 Suma con `suma += numero` dentro del bucle
* 🧮 Calcula promedio después del bucle con `suma / len(lista)`

📊 ¡Suma con precisión usando bucles! 🎯✨

---

### Reto o2.2: Contador de Números Pares e Impares 🔢⚖️

**Problema**: Recorre una lista de números y cuenta cuántos son pares y cuántos son impares usando contadores 📈🔍

**Descripción**: En este ejercicio usarás dos contadores (acumuladores que cuentan en lugar de sumar) para clasificar números. Dentro del bucle, verificarás si cada número es par o impar y aumentarás el contador correspondiente.

🔢 **Lógica de conteo**:

```plaintext
1. Crear contador_pares = 0 y contador_impares = 0
2. Para cada número en la lista:
   - Si número % 2 == 0: aumentar contador_pares
   - Si no: aumentar contador_impares
3. Mostrar ambos contadores
```

Tu programa debe:

* 🔄 Recorrer la lista con un bucle `for`
* ✅ Verificar si cada número es par o impar
* 📊 Contar pares e impares por separado
* 🎯 Mostrar ambos contadores

**Casos de prueba**:

1. Entrada ➡️ números=[1,2,3,4,5,6] → pares=3, impares=3
2. Entrada ➡️ números=[2,4,6,8] → pares=4, impares=0
3. Entrada ➡️ números=[1,3,5,7,9] → pares=0, impares=5
4. Entrada ➡️ números=[10,15,20,25,30] → pares=3, impares=2
5. Entrada ➡️ números=[11,12,13,14] → pares=2, impares=2

**Código base**:

```python
# Reto 2: Contador de Números Pares e Impares 🔢⚖️
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

even_count = 0          # Esta variable debe calcularse en base a la lógica del problema
odd_count = 0           # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", even_count == 3 and odd_count == 3)
print("🧪 ", even_count == 4 and odd_count == 0)
print("🧪 ", even_count == 0 and odd_count == 5)
print("🧪 ", even_count == 3 and odd_count == 2)
print("🧪 ", even_count == 2 and odd_count == 2)
```

🧠 **Tips útiles**:

* 📊 Inicializa ambos contadores en 0
* 🔍 Usa `if numero % 2 == 0:` para verificar si es par
* ➕ Incrementa con `contador += 1`
* ⚖️ Usa `else:` para contar impares

🔢 ¡Clasifica números como un matemático! 📐✨

---

### Reto o2.3: Buscador del Número Mayor 🔍🏆

**Problema**: Encuentra el número más grande de una lista usando un bucle `for` y una variable para guardar el mayor 📈🎯

**Descripción**: Para encontrar el número mayor, empezarás asumiendo que el primer número es el mayor, y luego compararás cada número siguiente. Si encuentras uno mayor, lo guardas como el nuevo mayor.

🏆 **Algoritmo de búsqueda**:

```plaintext
1. El mayor = primer número de la lista
2. Para cada número en la lista (desde el segundo):
   - Si número > mayor: mayor = número
3. El mayor contiene el resultado
```

Tu programa debe:

* 🏆 Inicializar el mayor con el primer número
* 🔄 Recorrer la lista comparando números
* 🔍 Actualizar el mayor cuando encuentre uno más grande
* 📊 También encontrar la posición donde está el mayor

**Casos de prueba**:

1. Entrada ➡️ números=[5,2,8,1,9] → mayor=9, posición=4
2. Entrada ➡️ números=[10,30,20,5] → mayor=30, posición=1
3. Entrada ➡️ números=[7,7,7,7] → mayor=7, posición=0
4. Entrada ➡️ números=[15,25,35,45] → mayor=45, posición=3
5. Entrada ➡️ números=[100,50,75] → mayor=100, posición=0

**Código base**:

```python
# Reto 3: Buscador del Número Mayor 🔍🏆
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

largest_number = 0      # Esta variable debe calcularse en base a la lógica del problema
position = 0            # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", largest_number == 9 and position == 4)
print("🧪 ", largest_number == 30 and position == 1)
print("🧪 ", largest_number == 7 and position == 0)
print("🧪 ", largest_number == 45 and position == 3)
print("🧪 ", largest_number == 100 and position == 0)
```

🧠 **Tips útiles**:

* 🏆 Inicializa `mayor = lista[0]` y `posicion_mayor = 0`
* 🔄 Usa `for i in range(len(lista)):` para tener índices
* 🔍 Compara con `if lista[i] > mayor:`
* 📊 Actualiza tanto el mayor como su posición

🏆 ¡Encuentra el campeón de los números! 🥇🔢

---

### Reto o2.4: Generador de Tabla de Multiplicar 📊✖️

**Problema**: Genera la tabla de multiplicar de un número dado usando un bucle `for` y guarda los resultados en una lista 📈🔢

**Descripción**: Las tablas de multiplicar son perfectas para practicar bucles. Usarás un bucle `for` para multiplicar un número por 1, 2, 3, hasta 10, y guardarás cada resultado en una lista.

✖️ **Generación de tabla**:

```plaintext
Para un número N:
N x 1 = N
N x 2 = N*2
...
N x 10 = N*10
```

Tu programa debe:

* ✖️ Multiplicar el número por cada valor de 1 a 10
* 📝 Guardar cada resultado en una lista
* ➕ Calcular la suma de todos los resultados
* 📊 Mostrar la tabla completa y la suma

**Casos de prueba**:

1. Entrada ➡️ número=2 → tabla=[2,4,6,8,10,12,14,16,18,20], suma=110
2. Entrada ➡️ número=5 → tabla=[5,10,15,20,25,30,35,40,45,50], suma=275
3. Entrada ➡️ número=3 → tabla=[3,6,9,12,15,18,21,24,27,30], suma=165
4. Entrada ➡️ número=7 → tabla=[7,14,21,28,35,42,49,56,63,70], suma=385
5. Entrada ➡️ número=1 → tabla=[1,2,3,4,5,6,7,8,9,10], suma=55

**Código base**:

```python
# Reto 4: Generador de Tabla de Multiplicar 📊✖️
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

multiplication_table = []  # Esta variable debe calcularse en base a la lógica del problema
table_sum = 0              # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", multiplication_table == [2,4,6,8,10,12,14,16,18,20] and table_sum == 110)
print("🧪 ", multiplication_table == [5,10,15,20,25,30,35,40,45,50] and table_sum == 275)
print("🧪 ", multiplication_table == [3,6,9,12,15,18,21,24,27,30] and table_sum == 165)
print("🧪 ", multiplication_table == [7,14,21,28,35,42,49,56,63,70] and table_sum == 385)
print("🧪 ", multiplication_table == [1,2,3,4,5,6,7,8,9,10] and table_sum == 55)
```

🧠 **Tips útiles**:

* 🔄 Usa `for i in range(1, 11):` para números del 1 al 10
* ✖️ Calcula `resultado = numero * i`
* 📝 Agrega a la lista con `tabla.append(resultado)`
* ➕ Suma todos los resultados al final

✖️ ¡Multiplica tu conocimiento! 📊🚀

---

### Reto o2.5: Contador de Palabras por Longitud 📝📏

**Problema**: Cuenta cuántas palabras de diferentes longitudes hay en una lista usando bucles y contadores 🔤📊

**Descripción**: En este ejercicio clasificarás palabras según su longitud: cortas (1-4 letras), medianas (5-7 letras) y largas (8+ letras). Usarás un bucle para recorrer las palabras y contadores para cada categoría.

📏 **Clasificación de palabras**:

```plaintext
- Cortas: 1 a 4 letras
- Medianas: 5 a 7 letras  
- Largas: 8 o más letras
```

Tu programa debe:

* 🔄 Recorrer la lista de palabras
* 📏 Medir la longitud de cada palabra con `len()`
* 📊 Clasificar cada palabra según su longitud
* 🎯 Contar cuántas hay de cada tipo

**Casos de prueba**:

1. Entrada ➡️ palabras=["hola","python","si","programación"] → cortas=2, medianas=1, largas=1
2. Entrada ➡️ palabras=["a","casa","computadora","sol"] → cortas=2, medianas=1, largas=1
3. Entrada ➡️ palabras=["perro","gato","elefante"] → cortas=0, medianas=2, largas=1
4. Entrada ➡️ palabras=["yo","tu","nosotros","vosotros"] → cortas=2, medianas=2, largas=0
5. Entrada ➡️ palabras=["universidad","la","escuela","estudiante"] → cortas=1, medianas=1, largas=2

**Código base**:

```python
# Reto 5: Contador de Palabras por Longitud 📝📏
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

short_words = 0         # Esta variable debe calcularse en base a la lógica del problema
medium_words = 0        # Esta variable debe calcularse en base a la lógica del problema
long_words = 0          # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", short_words == 2 and medium_words == 1 and long_words == 1)
print("🧪 ", short_words == 2 and medium_words == 1 and long_words == 1)
print("🧪 ", short_words == 0 and medium_words == 2 and long_words == 1)
print("🧪 ", short_words == 2 and medium_words == 2 and long_words == 0)
print("🧪 ", short_words == 1 and medium_words == 1 and long_words == 2)
```

🧠 **Tips útiles**:

* 📏 Usa `len(palabra)` para obtener la longitud
* 🔍 Usa `if len(palabra) <= 4:` para palabras cortas
* 📊 Usa `elif len(palabra) <= 7:` para medianas
* 📝 Usa `else:` para largas

📝 ¡Mide palabras como un lingüista! 🔤✨

---

## 🌀 o3 Bucles While Loop y Nested Loops - Iteración Dinámica y Estructuras Anidadas 🔄💫

🎯 En esta sección aprenderás a usar bucles `while` para repetir código mientras una condición sea verdadera y combinarás bucles para crear patrones y resolver problemas que requieren múltiples niveles de repetición. Estos conceptos son esenciales para crear programas que se adapten a diferentes situaciones y procesen datos organizados en filas y columnas 🧠🔄.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### Reto o3.1: Contador de Números Pares con While 🔢⚡

**Problema**: Cuenta cuántos números pares hay desde 1 hasta un número dado usando un bucle `while` 🎯🔍

**Descripción**: Los bucles `while` son útiles cuando no sabemos exactamente cuántas veces necesitamos repetir algo, pero sabemos la condición que debe cumplirse. En este ejercicio usarás `while` para contar números pares en un rango.

🔢 **Lógica del problema**:

```plaintext
1. Empezar desde el número 1
2. Mientras el número sea menor o igual al límite:
   - Si el número es par, incrementar contador
   - Incrementar el número
3. Retornar el total de pares encontrados
```

Tu programa debe:

* 🔢 Usar un bucle `while` para recorrer números
* ✅ Verificar si cada número es par
* 📊 Contar cuántos números pares encuentra
* 🖥️ Mostrar el total de números pares

**Casos de prueba**:

1. Entrada ➡️ límite=10 → pares_encontrados=5 (2,4,6,8,10)
2. Entrada ➡️ límite=15 → pares_encontrados=7 (2,4,6,8,10,12,14)
3. Entrada ➡️ límite=20 → pares_encontrados=10 (2,4,6,8,10,12,14,16,18,20)
4. Entrada ➡️ límite=5 → pares_encontrados=2 (2,4)
5. Entrada ➡️ límite=1 → pares_encontrados=0 (no hay pares)

**Código base**:

```python
# Contador de Números Pares con While 🔢⚡
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

even_count = 0          # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", even_count == 5)
print("🧪 ", even_count == 7)
print("🧪 ", even_count == 10)
print("🧪 ", even_count == 2)
print("🧪 ", even_count == 0)
```

🧠 **Tips útiles**:

* 🔢 Inicializa una variable contador en 1
* 🔄 Usa `while contador <= limite:`
* ✅ Dentro del bucle, verifica `if contador % 2 == 0:`
* ➕ No olvides incrementar el contador con `contador += 1`

🔢 ¡Cuenta con precisión usando while! 🎯✨

---

### Reto o3.2: Generador de Tablas de Multiplicar con Bucles Anidados ✖️📊

**Problema**: Genera múltiples tablas de multiplicar usando bucles anidados (`for` dentro de `for`) para crear un patrón organizado 📈🔢

**Descripción**: Los bucles anidados nos permiten trabajar con estructuras bidimensionales como tablas. En este ejercicio crearás varias tablas de multiplicar de forma organizada usando un bucle exterior para las tablas y un bucle interior para los multiplicadores.

✖️ **Estructura de bucles anidados**:

```plaintext
Para cada tabla (del 2 al número dado):
    Para cada multiplicador (del 1 al 5):
        Calcular: tabla × multiplicador
        Guardar el resultado
```

Tu programa debe:

* 🔄 Usar un bucle exterior para seleccionar qué tabla generar
* 🔄 Usar un bucle interior para los multiplicadores (1 al 5)
* ✖️ Calcular cada multiplicación
* 📊 Sumar todos los resultados de todas las tablas

**Casos de prueba**:

1. Entrada ➡️ hasta_tabla=2 → suma_total=45 (tabla 2: 2+4+6+8+10=30, total=30)
2. Entrada ➡️ hasta_tabla=3 → suma_total=75 (tabla 2: 30, tabla 3: 45, total=75)
3. Entrada ➡️ hasta_tabla=4 → suma_total=135 (tabla 2: 30, tabla 3: 45, tabla 4: 60, total=135)
4. Entrada ➡️ hasta_tabla=5 → suma_total=210 (suma de tablas 2,3,4,5)
5. Entrada ➡️ hasta_tabla=6 → suma_total=300 (suma de tablas 2,3,4,5,6)

**Código base**:

```python
# Generador de Tablas de Multiplicar con Bucles Anidados ✖️📊
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

total_sum = 0           # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", total_sum == 45)
print("🧪 ", total_sum == 75)
print("🧪 ", total_sum == 135)
print("🧪 ", total_sum == 210)
print("🧪 ", total_sum == 300)
```

🧠 **Tips útiles**:

* 🔄 Usa `for tabla in range(2, hasta_tabla + 1):`
* 🔄 Dentro, usa `for multiplicador in range(1, 6):`
* ✖️ Calcula `resultado = tabla * multiplicador`
* ➕ Suma cada resultado al total

✖️ ¡Multiplica tu conocimiento con bucles anidados! 📊🚀

---

### Reto o3.3: Adivinanza de Números con While 🎲🤔

**Problema**: Crea un juego que genere un número secreto y use un bucle `while` para que el usuario adivine hasta acertar o agotar intentos 🎮🔍

**Descripción**: Los bucles `while` son perfectos para juegos donde no sabemos cuándo terminará la partida. El bucle continúa hasta que el usuario adivine el número o se queden sin intentos.

🎲 **Mecánica del juego**:

```plaintext
1. Generar un número secreto (del 1 al 10)
2. Dar al usuario máximo 3 intentos
3. Mientras tenga intentos y no haya adivinado:
   - Pedir un número
   - Comparar con el número secreto
   - Dar pista (mayor/menor) si no acierta
   - Reducir intentos
4. Indicar si ganó o perdió
```

Tu programa debe:

* 🎲 Generar un número secreto
* 🔄 Usar `while` para controlar los intentos
* 🎯 Comparar la adivinanza con el número secreto
* 💬 Dar retroalimentación al usuario

**Casos de prueba**:

1. Entrada ➡️ secreto=5, intentos=[5] → ganó=True, intentos_usados=1
2. Entrada ➡️ secreto=7, intentos=[3,7] → ganó=True, intentos_usados=2
3. Entrada ➡️ secreto=9, intentos=[1,5,9] → ganó=True, intentos_usados=3
4. Entrada ➡️ secreto=4, intentos=[1,2,3] → ganó=False, intentos_usados=3
5. Entrada ➡️ secreto=8, intentos=[8] → ganó=True, intentos_usados=1

**Código base**:

```python
# Adivinanza de Números con While 🎲🤔
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

won = False             # Esta variable debe calcularse en base a la lógica del problema
attempts_used = 0       # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", won == True and attempts_used == 1)
print("🧪 ", won == True and attempts_used == 2)
print("🧪 ", won == True and attempts_used == 3)
print("🧪 ", won == False and attempts_used == 3)
print("🧪 ", won == True and attempts_used == 1)
```

🧠 **Tips útiles**:

* 🎯 Inicializa `intentos_restantes = 3` y `adivinado = False`
* 🔄 Usa `while intentos_restantes > 0 and not adivinado:`
* 🎲 Simula la entrada del usuario con una lista predefinida
* 📊 Cuenta los intentos usados

🎲 ¡Crea juegos divertidos con while! 🎮✨

---

### Reto o3.4: Patrón de Estrellas con Bucles Anidados ⭐🔺

**Problema**: Dibuja un patrón triangular de estrellas usando bucles anidados donde cada fila tiene más estrellas que la anterior 🌟📐

**Descripción**: Los bucles anidados son excelentes para crear patrones visuales. El bucle exterior controla las filas y el bucle interior controla cuántas estrellas imprimir en cada fila.

⭐ **Patrón a crear**:

```plaintext
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

* 🔄 Usar un bucle exterior para las filas (1 hasta n)
* ⭐ Usar un bucle interior para las estrellas en cada fila
* 📝 Construir cada línea del patrón
* 📊 Contar el total de estrellas dibujadas

**Casos de prueba**:

1. Entrada ➡️ filas=3 → total_estrellas=6, lineas=["*","**","***"]
2. Entrada ➡️ filas=4 → total_estrellas=10, lineas=["*","**","***","****"]
3. Entrada ➡️ filas=5 → total_estrellas=15, lineas=["*","**","***","****","*****"]
4. Entrada ➡️ filas=2 → total_estrellas=3, lineas=["*","**"]
5. Entrada ➡️ filas=1 → total_estrellas=1, lineas=["*"]

**Código base**:

```python
# Patrón de Estrellas con Bucles Anidados ⭐🔺
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

total_stars = 0         # Esta variable debe calcularse en base a la lógica del problema
pattern_lines = []      # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", total_stars == 6 and pattern_lines == ["*","**","***"])
print("🧪 ", total_stars == 10 and pattern_lines == ["*","**","***","****"])
print("🧪 ", total_stars == 15 and pattern_lines == ["*","**","***","****","*****"])
print("🧪 ", total_stars == 3 and pattern_lines == ["*","**"])
print("🧪 ", total_stars == 1 and pattern_lines == ["*"])
```

🧠 **Tips útiles**:

* 🔄 Usa `for fila in range(1, filas + 1):`
* ⭐ Dentro, usa `for estrella in range(fila):`
* 📝 Construye cada línea concatenando estrellas: `linea += "*"`
* 📊 Suma el número de estrellas: `total += fila`

⭐ ¡Dibuja patrones hermosos con código! 🎨🌟

---

### Reto o3.5: Suma de Números hasta Condición con While 🔢➕

**Problema**: Suma números consecutivos empezando desde 1 hasta que la suma supere un límite dado, usando un bucle `while` 📊🎯

**Descripción**: Este ejercicio simula situaciones donde necesitamos acumular valores hasta alcanzar una meta. El bucle `while` es perfecto porque no sabemos de antemano cuántos números necesitaremos sumar.

🔢 **Proceso de suma**:

```plaintext
1. Empezar con suma = 0 y número = 1
2. Mientras la suma sea menor al límite:
   - Sumar el número actual a la suma total
   - Incrementar el número
3. Reportar cuántos números se sumaron y la suma final
```

Tu programa debe:

* 🔢 Usar `while` para controlar cuándo parar
* ➕ Ir sumando números consecutivos
* 📊 Contar cuántos números se sumaron
* 🎯 Parar cuando se supere el límite

**Casos de prueba**:

1. Entrada ➡️ límite=10 → números_sumados=4, suma_final=10 (1+2+3+4=10)
2. Entrada ➡️ límite=15 → números_sumados=5, suma_final=15 (1+2+3+4+5=15)
3. Entrada ➡️ límite=20 → números_sumados=6, suma_final=21 (1+2+3+4+5+6=21)
4. Entrada ➡️ límite=5 → números_sumados=3, suma_final=6 (1+2+3=6)
5. Entrada ➡️ límite=25 → números_sumados=7, suma_final=28 (1+2+3+4+5+6+7=28)

**Código base**:

```python
# Suma de Números hasta Condición con While 🔢➕
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

numbers_added = 0       # Esta variable debe calcularse en base a la lógica del problema
final_sum = 0           # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", numbers_added == 4 and final_sum == 10)
print("🧪 ", numbers_added == 5 and final_sum == 15)
print("🧪 ", numbers_added == 6 and final_sum == 21)
print("🧪 ", numbers_added == 3 and final_sum == 6)
print("🧪 ", numbers_added == 7 and final_sum == 28)
```

🧠 **Tips útiles**:

* 🔢 Inicializa `suma = 0`, `numero = 1`, `contador = 0`
* 🔄 Usa `while suma < limite:`
* ➕ Dentro del bucle: suma el número, incrementa contador y número
* 🎯 El bucle se detiene automáticamente al superar el límite

🔢 ¡Suma inteligentemente hasta alcanzar tu meta! 🎯📈


## 📦 o4 Tuplas en Python - Colecciones Ordenadas e Inmutables 🔒✨

🎯 En esta sección aprenderás a trabajar con tuplas, que son colecciones ordenadas de elementos que no se pueden modificar después de crear. Las tuplas son perfectas para almacenar datos que no deben cambiar, como coordenadas, información personal o configuraciones. Aprenderás a crearlas, acceder a sus elementos y usar sus métodos básicos 📋🔍.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### Reto o4.1: Creación y Acceso Básico a Tuplas 📦🔑

**Problema**: Crea tuplas con diferentes tipos de datos y accede a elementos específicos usando índices 🎯📍

**Descripción**: Las tuplas se crean usando paréntesis `()` y pueden contener diferentes tipos de datos como números, texto y booleanos. Una vez creadas, puedes acceder a sus elementos usando índices que empiezan en 0.

📦 **Sintaxis básica**:

```plaintext
# Crear tupla
mi_tupla = (elemento1, elemento2, elemento3)

# Acceder a elementos
primer_elemento = mi_tupla[0]
segundo_elemento = mi_tupla[1]
ultimo_elemento = mi_tupla[-1]
```

Tu programa debe:

* 📦 Crear una tupla con información personal (nombre, edad, ciudad)
* 🔑 Acceder al primer, segundo y último elemento
* 📊 Obtener el tipo de dato de la tupla
* 📏 Calcular la longitud de la tupla

**Casos de prueba**:

1. Entrada ➡️ tupla=("Ana", 25, "Madrid") → primer="Ana", segundo=25, longitud=3
2. Entrada ➡️ tupla=("Carlos", 30, "Barcelona") → primer="Carlos", segundo=30, longitud=3
3. Entrada ➡️ tupla=("María", 22, "Sevilla") → primer="María", segundo=22, longitud=3
4. Entrada ➡️ tupla=("Luis", 28, "Valencia") → primer="Luis", segundo=28, longitud=3
5. Entrada ➡️ tupla=("Elena", 35, "Bilbao") → primer="Elena", segundo=35, longitud=3

**Código base**:

```python
# Reto 1: Creación y Acceso Básico a Tuplas 📦🔑
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

first_element = ""      # Esta variable debe calcularse en base a la lógica del problema
second_element = 0      # Esta variable debe calcularse en base a la lógica del problema
tuple_length = 0        # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", first_element == "Ana" and second_element == 25 and tuple_length == 3)
print("🧪 ", first_element == "Carlos" and second_element == 30 and tuple_length == 3)
print("🧪 ", first_element == "María" and second_element == 22 and tuple_length == 3)
print("🧪 ", first_element == "Luis" and second_element == 28 and tuple_length == 3)
print("🧪 ", first_element == "Elena" and second_element == 35 and tuple_length == 3)
```

🧠 **Tips útiles**:

* 📦 Crea la tupla con `tupla = (nombre, edad, ciudad)`
* 🔑 Accede con `tupla[0]`, `tupla[1]`, `tupla[2]`
* 📏 Usa `len(tupla)` para obtener la longitud
* 📍 Recuerda que los índices empiezan en 0

📦 ¡Las tuplas son como cajas organizadas que no se pueden abrir! 🔒✨

---

### Reto o4.2: Desempaquetado de Tuplas 📤🎁

**Problema**: Desempaqueta tuplas asignando cada elemento a variables individuales de forma directa y sencilla 🎯📋

**Descripción**: El desempaquetado es una característica muy útil de Python que permite asignar todos los elementos de una tupla a variables separadas en una sola línea. Es como abrir una caja y sacar cada elemento a su propio lugar.

🎁 **Sintaxis de desempaquetado**:

```plaintext
# Tupla con datos
coordenadas = (10, 20, 30)

# Desempaquetado
x, y, z = coordenadas

# Ahora x=10, y=20, z=30
```

Tu programa debe:

* 🎁 Crear tuplas con coordenadas (x, y, z)
* 📤 Desempaquetar cada tupla en variables separadas
* 🧮 Calcular la suma de las coordenadas
* 📊 Determinar cuál coordenada es la mayor

**Casos de prueba**:

1. Entrada ➡️ coordenadas=(5, 10, 15) → x=5, suma=30, mayor=15
2. Entrada ➡️ coordenadas=(3, 7, 2) → x=3, suma=12, mayor=7
3. Entrada ➡️ coordenadas=(8, 8, 8) → x=8, suma=24, mayor=8
4. Entrada ➡️ coordenadas=(1, 9, 4) → x=1, suma=14, mayor=9
5. Entrada ➡️ coordenadas=(6, 2, 11) → x=6, suma=19, mayor=11

**Código base**:

```python
# Reto 2: Desempaquetado de Tuplas 📤🎁
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

x_coord = 0             # Esta variable debe calcularse en base a la lógica del problema
coord_sum = 0           # Esta variable debe calcularse en base a la lógica del problema
max_coord = 0           # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", x_coord == 5 and coord_sum == 30 and max_coord == 15)
print("🧪 ", x_coord == 3 and coord_sum == 12 and max_coord == 7)
print("🧪 ", x_coord == 8 and coord_sum == 24 and max_coord == 8)
print("🧪 ", x_coord == 1 and coord_sum == 14 and max_coord == 9)
print("🧪 ", x_coord == 6 and coord_sum == 19 and max_coord == 11)
```

🧠 **Tips útiles**:

* 🎁 Usa `x, y, z = tupla` para desempaquetar
* ➕ Calcula la suma con `x + y + z`
* 🔍 Encuentra el mayor con `max(x, y, z)`
* 📦 Asegúrate de que la tupla tenga exactamente 3 elementos

🎁 ¡Desempaqueta como si fuera Navidad! 🎄📦

---

### Reto o4.3: Métodos Básicos de Tuplas 🔍📊

**Problema**: Usa los métodos `count()` e `index()` para buscar y contar elementos dentro de tuplas 🎯🔢

**Descripción**: Las tuplas tienen métodos útiles para buscar información. El método `count()` cuenta cuántas veces aparece un elemento, y `index()` te dice en qué posición está la primera aparición de un elemento.

🔍 **Métodos disponibles**:

```plaintext
# Contar elementos
tupla.count(elemento)  # Retorna cuántas veces aparece

# Buscar posición
tupla.index(elemento)  # Retorna el índice de la primera aparición
```

Tu programa debe:

* 🔢 Crear tuplas con números repetidos
* 🔍 Contar cuántas veces aparece un número específico
* 📍 Encontrar la posición de la primera aparición
* ✅ Verificar si un elemento existe en la tupla

**Casos de prueba**:

1. Entrada ➡️ números=(1,2,3,2,4,2), buscar=2 → count=3, index=1, existe=True
2. Entrada ➡️ números=(5,5,7,8,5), buscar=5 → count=3, index=0, existe=True
3. Entrada ➡️ números=(1,3,5,7,9), buscar=6 → count=0, index=-1, existe=False
4. Entrada ➡️ números=(4,4,4,4), buscar=4 → count=4, index=0, existe=True
5. Entrada ➡️ números=(2,6,8,2,6), buscar=8 → count=1, index=2, existe=True

**Código base**:

```python
# Reto 3: Métodos Básicos de Tuplas 🔍📊
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

element_count = 0       # Esta variable debe calcularse en base a la lógica del problema
element_index = -1      # Esta variable debe calcularse en base a la lógica del problema
element_exists = False  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", element_count == 3 and element_index == 1 and element_exists == True)
print("🧪 ", element_count == 3 and element_index == 0 and element_exists == True)
print("🧪 ", element_count == 0 and element_index == -1 and element_exists == False)
print("🧪 ", element_count == 4 and element_index == 0 and element_exists == True)
print("🧪 ", element_count == 1 and element_index == 2 and element_exists == True)
```

🧠 **Tips útiles**:

* 🔢 Usa `tupla.count(elemento)` para contar
* 📍 Usa `tupla.index(elemento)` para encontrar posición
* ⚠️ Si el elemento no existe, `index()` da error, usa `try/except` o verifica primero
* ✅ Verifica existencia con `elemento in tupla`

🔍 ¡Busca y encuentra como un detective! 🕵️‍♂️🔎

---

### Reto o4.4: Slicing (Rebanado) de Tuplas 🍰✂️

**Problema**: Extrae partes específicas de tuplas usando slicing (rebanado) para obtener sub-tuplas 🎯📏

**Descripción**: El slicing te permite extraer una porción de la tupla especificando índices de inicio y fin. Es como cortar una rebanada de pastel - obtienes una parte específica manteniendo el orden original.

🍰 **Sintaxis de slicing**:

```plaintext
tupla[inicio:fin]     # Desde inicio hasta fin-1
tupla[inicio:]        # Desde inicio hasta el final
tupla[:fin]           # Desde el principio hasta fin-1
tupla[inicio:fin:paso] # Con saltos específicos
```

Tu programa debe:

* ✂️ Crear una tupla con números del 1 al 10
* 🍰 Extraer los primeros 3 elementos
* 📏 Extraer los últimos 3 elementos
* 🎯 Extraer elementos del medio (índices 3 al 6)

**Casos de prueba**:

1. Entrada ➡️ tupla=(1,2,3,4,5,6,7,8,9,10) → primeros_3=(1,2,3), ultimos_3=(8,9,10), medio=(4,5,6,7)
2. Entrada ➡️ tupla=(10,20,30,40,50,60,70,80,90,100) → primeros_3=(10,20,30), ultimos_3=(80,90,100), medio=(40,50,60,70)
3. Entrada ➡️ tupla=(5,10,15,20,25,30,35,40,45,50) → primeros_3=(5,10,15), ultimos_3=(40,45,50), medio=(20,25,30,35)
4. Entrada ➡️ tupla=(2,4,6,8,10,12,14,16,18,20) → primeros_3=(2,4,6), ultimos_3=(16,18,20), medio=(8,10,12,14)
5. Entrada ➡️ tupla=(11,12,13,14,15,16,17,18,19,20) → primeros_3=(11,12,13), ultimos_3=(18,19,20), medio=(14,15,16,17)

**Código base**:

```python
# Reto 4: Slicing (Rebanado) de Tuplas 🍰✂️
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

first_three = ()        # Esta variable debe calcularse en base a la lógica del problema
last_three = ()         # Esta variable debe calcularse en base a la lógica del problema
middle_slice = ()       # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", first_three == (1,2,3) and last_three == (8,9,10) and middle_slice == (4,5,6,7))
print("🧪 ", first_three == (10,20,30) and last_three == (80,90,100) and middle_slice == (40,50,60,70))
print("🧪 ", first_three == (5,10,15) and last_three == (40,45,50) and middle_slice == (20,25,30,35))
print("🧪 ", first_three == (2,4,6) and last_three == (16,18,20) and middle_slice == (8,10,12,14))
print("🧪 ", first_three == (11,12,13) and last_three == (18,19,20) and middle_slice == (14,15,16,17))
```

🧠 **Tips útiles**:

* ✂️ Usa `tupla[:3]` para los primeros 3
* 📏 Usa `tupla[-3:]` para los últimos 3  
* 🎯 Usa `tupla[3:7]` para el medio (índices 3,4,5,6)
* 🍰 Recuerda que el slicing no incluye el índice final

🍰 ¡Corta tuplas como un chef experto! 👨‍🍳✂️

---

### Reto o4.5: Iteración y Conversión de Tuplas 🔄📝

**Problema**: Recorre tuplas usando bucles y convierte tuplas a otros tipos de datos como listas y strings 🔄🔀

**Descripción**: Puedes recorrer tuplas con bucles `for` para procesar cada elemento. También puedes convertir tuplas a listas (mutables) o strings para diferentes propósitos, manteniendo siempre el orden de los elementos.

🔄 **Operaciones básicas**:

```plaintext
# Iterar tupla
for elemento in mi_tupla:
    print(elemento)

# Conversiones
lista = list(mi_tupla)      # Tupla a lista
texto = str(mi_tupla)       # Tupla a string
```

Tu programa debe:

* 🔄 Iterar sobre una tupla de números
* ➕ Sumar todos los elementos de la tupla
* 📝 Convertir la tupla a lista
* 🔢 Contar cuántos números son mayores que 5

**Casos de prueba**:

1. Entrada ➡️ números=(1,4,7,2,9,3) → suma=26, lista=[1,4,7,2,9,3], mayores_5=2
2. Entrada ➡️ números=(6,8,3,5,7,9) → suma=38, lista=[6,8,3,5,7,9], mayores_5=4
3. Entrada ➡️ números=(2,2,2,2,2) → suma=10, lista=[2,2,2,2,2], mayores_5=0
4. Entrada ➡️ números=(10,1,8,6,4) → suma=29, lista=[10,1,8,6,4], mayores_5=3
5. Entrada ➡️ números=(5,5,6,7,8) → suma=31, lista=[5,5,6,7,8], mayores_5=3

**Código base**:

```python
# Reto 5: Iteración y Conversión de Tuplas 🔄📝
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

total_sum = 0           # Esta variable debe calcularse en base a la lógica del problema
tuple_as_list = []      # Esta variable debe calcularse en base a la lógica del problema
count_greater_5 = 0     # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", total_sum == 26 and tuple_as_list == [1,4,7,2,9,3] and count_greater_5 == 2)
print("🧪 ", total_sum == 38 and tuple_as_list == [6,8,3,5,7,9] and count_greater_5 == 4)
print("🧪 ", total_sum == 10 and tuple_as_list == [2,2,2,2,2] and count_greater_5 == 0)
print("🧪 ", total_sum == 29 and tuple_as_list == [10,1,8,6,4] and count_greater_5 == 3)
print("🧪 ", total_sum == 31 and tuple_as_list == [5,5,6,7,8] and count_greater_5 == 3)
```

🧠 **Tips útiles**:

* 🔄 Usa `for numero in tupla:` para iterar
* ➕ Acumula la suma con `total += numero`
* 📝 Convierte con `list(tupla)`
* 🔢 Cuenta con `if numero > 5:` dentro del bucle

🔄 ¡Recorre y transforma como un mago de datos! 🎩✨