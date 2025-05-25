# **🐍 Examen de Fundamentos de Python 🧠💻**

Este examen está diseñado para evaluar tus conocimientos esenciales en programación con Python. A lo largo de cuatro grupos temáticos, deberás resolver retos que combinan lógica, sintaxis, estructuras de control, bucles, entrada y salida de datos. Cada reto simula problemas reales que puedes encontrar como desarrollador, desde cálculos matemáticos hasta sistemas interactivos. Los casos de prueba te ayudarán a validar que tu solución es correcta ✅. Cada ejercicio incluye validaciones con `print(True)` para que puedas comprobar fácilmente tus resultados. ¡Demuestra tu talento y lógica! 💪🐍🚀

---

## **📚 Input y Print - Fundamentos de Entrada y Salida 🎯**

📥 En esta sección demostrarás tu dominio de los fundamentos de entrada y salida en Python. Resolverás ejercicios donde deberás capturar datos del usuario mediante `input()` y mostrar resultados claros con `print()`. Son los primeros pasos para interactuar con tus programas y transformar ideas en experiencias reales 💬✨.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

### **Reto: Calculadora de Índice de Masa Corporal (IMC) 🏋️‍♂️📏🧮**

**Problema**: Calcula el IMC a partir de datos ingresados por el usuario y muestra el resultado de forma clara, amigable y con estilo profesional 🩺📊✨

**Descripción**: El Índice de Masa Corporal (IMC) es una medida que ayuda a evaluar si una persona tiene un peso saludable en función de su altura. Es ampliamente utilizado por profesionales de la salud y apps de bienestar.

📐 **Fórmula del IMC**:

```plaintext
IMC = peso (kg) / altura² (m²)
```

Tu programa debe:

* 🧍‍♂️ Solicitar el **peso** al usuario (en kilogramos) ⚖️
* 📏 Solicitar la **altura** al usuario (en metros)
* 💡 Calcular el IMC con **dos decimales**
* 🖥️ Imprimir el resultado final con un mensaje claro, decorado con emojis 😄

🎯 Este ejercicio te ayudará a dominar `input()`, `float()` y `print()` con formato.

**Casos de prueba**:

1. Entrada ➡️ Peso: 70 kg, Altura: 1.75 m → Salida esperada: 22.86
2. Entrada ➡️ Peso: 85 kg, Altura: 1.80 m → Salida esperada: 26.23
3. Entrada ➡️ Peso: 55 kg, Altura: 1.65 m → Salida esperada: 20.20
4. Entrada ➡️ Peso: 90 kg, Altura: 1.72 m → Salida esperada: 30.42
5. Entrada ➡️ Peso: 65 kg, Altura: 1.70 m → Salida esperada: 22.49

**Código base**:

```python
# Calculadora de Índice de Masa Corporal (IMC) 🏋️‍♂️📏🧮
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

bmi = 0  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", bmi == 22.86)  # Peso: 70 kg, Altura: 1.75 m → IMC: 22.86
print("🧪 ", bmi == 26.23)  # Peso: 85 kg, Altura: 1.80 m → IMC: 26.23
print("🧪 ", bmi == 20.2)   # Peso: 55 kg, Altura: 1.65 m → IMC: 20.20
print("🧪 ", bmi == 30.42)  # Peso: 90 kg, Altura: 1.72 m → IMC: 30.42
print("🧪 ", bmi == 22.49)  # Peso: 65 kg, Altura: 1.70 m → IMC: 22.49
```

🧠 **Tips útiles**:

* 📝 Usa la función `input()` para capturar datos del usuario
* 🔢 Convierte la entrada con `float()` para manejar decimales
* 🎯 Aplica `round(valor, 2)` para mostrar solo dos decimales
* 🎨 Decora tu mensaje de salida con emojis y buen formato

🌟 ¡Conviértete en un programador saludable y con estilo! 💪📲

---

### **Reto: Conversor de Temperaturas 🌡️🔥❄️**

**Problema**: Convierte una temperatura ingresada por el usuario en grados Celsius a Fahrenheit y Kelvin, mostrando ambos resultados con claridad y precisión ❄️📏🔥

**Descripción**: Las conversiones de temperatura son fundamentales en ciencia, ingeniería y desarrollo de software. Este programa transforma una temperatura en grados Celsius a otras dos escalas ampliamente utilizadas: Fahrenheit y Kelvin.

📐 **Fórmulas**:

```plaintext
Fahrenheit = Celsius × 9/5 + 32
Kelvin = Celsius + 273.15
```

Tu programa debe:

* 🌡️ Solicitar la temperatura en grados Celsius
* 🔥 Calcular y mostrar la temperatura en Fahrenheit (dos decimales)
* ❄️ Calcular y mostrar la temperatura en Kelvin (dos decimales)

🎯 Te servirá para practicar operaciones aritméticas, entrada de datos y formateo de salida.

**Casos de prueba**:

1. Entrada ➡️ 25°C → Fahrenheit: 77.00°F, Kelvin: 298.15K
2. Entrada ➡️ 0°C → Fahrenheit: 32.00°F, Kelvin: 273.15K
3. Entrada ➡️ 100°C → Fahrenheit: 212.00°F, Kelvin: 373.15K
4. Entrada ➡️ -10°C → Fahrenheit: 14.00°F, Kelvin: 263.15K
5. Entrada ➡️ 37°C → Fahrenheit: 98.60°F, Kelvin: 310.15K

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

fahrenheit = 0  # Esta variable debe calcularse en base a la lógica del problema
kelvin = 0      # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", fahrenheit == 77.00 and kelvin == 298.15)
print("🧪 ", fahrenheit == 32.00 and kelvin == 273.15)
print("🧪 ", fahrenheit == 212.00 and kelvin == 373.15)
print("🧪 ", fahrenheit == 14.00 and kelvin == 263.15)
print("🧪 ", fahrenheit == 98.60 and kelvin == 310.15)
```

🧠 **Tips útiles**:

* 🧮 Usa operaciones aritméticas simples
* 🧊 Recuerda que Celsius puede ser negativo, ¡maneja bien los decimales!
* 🎯 Usa `round()` para asegurar los dos decimales

🔥 ¡Eres la temperatura exacta de la motivación! 💯❄️🔥

---

### **Reto: Calculadora de Propina 💰🧾🍽️**

**Problema**: Calcula la propina, el total de la cuenta y el monto por persona a partir del ingreso del usuario. Ideal para dividir la cuenta en grupo de amigos 😄🍴💳

**Descripción**: Este programa simula una calculadora de propinas muy útil en restaurantes. A partir del total de la cuenta, el porcentaje de propina y el número de personas, deberás calcular:

* 💵 El monto de propina
* 💰 El total a pagar
* 👥 El monto que debe pagar cada persona

📐 **Fórmulas**:

```plaintext
Tip = total × (porcentaje / 100)
TotalFinal = total + tip
PorPersona = totalFinal / personas
```

**Casos de prueba**:

1. Entrada ➡️ Total: \$100, Propina: 15%, Personas: 2 → Propina: \$15.00, Total: \$115.00, Por persona: \$57.50
2. Entrada ➡️ Total: \$75.50, Propina: 10%, Personas: 3 → Propina: \$7.55, Total: \$83.05, Por persona: \$27.68
3. Entrada ➡️ Total: \$45.75, Propina: 20%, Personas: 1 → Propina: \$9.15, Total: \$54.90, Por persona: \$54.90
4. Entrada ➡️ Total: \$200, Propina: 18%, Personas: 4 → Propina: \$36.00, Total: \$236.00, Por persona: \$59.00
5. Entrada ➡️ Total: \$350.25, Propina: 25%, Personas: 6 → Propina: \$87.56, Total: \$437.81, Por persona: \$72.97

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

tip = 0          # Esta variable debe calcularse en base a la lógica del problema
total = 0        # Esta variable debe calcularse en base a la lógica del problema
per_person = 0   # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", tip == 15.00 and total == 115.00 and per_person == 57.50)
print("🧪 ", tip == 7.55 and total == 83.05 and per_person == 27.68)
print("🧪 ", tip == 9.15 and total == 54.90 and per_person == 54.90)
print("🧪 ", tip == 36.00 and total == 236.00 and per_person == 59.00)
print("🧪 ", tip == 87.56 and total == 437.81 and per_person == 72.97)
```

🧠 **Tips útiles**:

* 📥 Usa `input()` para solicitar valores como float
* 🔢 Aplica `round(valor, 2)` para redondear correctamente
* 🧮 Organiza tus operaciones paso a paso

🍽️ ¡No dejes propinas vacías, deja soluciones brillantes! ✨💸

---

### **Reto: Conversor de Tiempo Total ⏱️⌛🕒**

**Problema**: Convierte una cantidad de segundos ingresada por el usuario en horas, minutos y segundos, mostrando el tiempo total de forma clara y ordenada ⌛🔁🧮

**Descripción**: Cuando trabajamos con duración de eventos, animaciones o registros, convertir segundos a un formato legible de horas, minutos y segundos es muy útil.

📐 **Conversión**:

```plaintext
1 hora = 3600 segundos
1 minuto = 60 segundos
```

Tu programa debe:

* 🕐 Solicitar una cantidad de segundos
* 🧠 Calcular cuántas horas completas hay
* 🧠 Calcular los minutos restantes
* 🧠 Calcular los segundos restantes
* 🖥️ Imprimir el tiempo en formato legible: `X horas, Y minutos, Z segundos`

🎯 Este reto es ideal para dominar la división entera `//` y el módulo `%`.

**Casos de prueba**:

1. Entrada ➡️ 3661 segundos → Salida esperada: 1 hora, 1 minuto, 1 segundo
2. Entrada ➡️ 7500 segundos → Salida esperada: 2 horas, 5 minutos, 0 segundos
3. Entrada ➡️ 45 segundos → Salida esperada: 0 horas, 0 minutos, 45 segundos
4. Entrada ➡️ 10800 segundos → Salida esperada: 3 horas, 0 minutos, 0 segundos
5. Entrada ➡️ 3723 segundos → Salida esperada: 1 hora, 2 minutos, 3 segundos

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

hours = 0     # Esta variable debe calcularse en base a la lógica del problema
minutes = 0   # Esta variable debe calcularse en base a la lógica del problema
seconds = 0   # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", (hours, minutes, seconds) == (1, 1, 1))
print("🧪 ", (hours, minutes, seconds) == (2, 5, 0))
print("🧪 ", (hours, minutes, seconds) == (0, 0, 45))
print("🧪 ", (hours, minutes, seconds) == (3, 0, 0))
print("🧪 ", (hours, minutes, seconds) == (1, 2, 3))
```

🧠 **Tips útiles**:

* 🧮 Usa `//` para obtener enteros y `%` para los restos
* 🗓️ Mantén el orden: primero las horas, luego los minutos, finalmente los segundos

🕓 ¡No desperdicies ni un segundo... conviértelo en conocimiento! 🚀✨

---

### **Reto: Conversor de Sistemas Numéricos 🔢📟📈**

**Problema**: Convierte un número entero positivo en sus representaciones **binaria** y **hexadecimal**, y muestra ambos resultados con claridad 🧠🖥️

**Descripción**: En informática, los sistemas binario y hexadecimal son fundamentales para el manejo interno de datos, almacenamiento y programación a bajo nivel. En este reto, deberás capturar un número decimal y convertirlo a sus equivalentes binario y hexadecimal sin prefijos como `0b` o `0x`.

Tu programa debe:

* 🧮 Solicitar un número decimal al usuario (entero positivo)
* 🔁 Convertirlo a binario y hexadecimal usando funciones de Python
* ✂️ Eliminar los prefijos (`0b`, `0x`) de las representaciones
* 🎯 Imprimir ambos resultados con un formato claro

🎓 Este reto te ayudará a trabajar conversiones numéricas, uso de funciones integradas, slicing de cadenas, y precisión en la salida.

**Casos de prueba**:

1. Entrada ➡️ 10 → Binario: 1010, Hexadecimal: a
2. Entrada ➡️ 255 → Binario: 11111111, Hexadecimal: ff
3. Entrada ➡️ 16 → Binario: 10000, Hexadecimal: 10
4. Entrada ➡️ 31 → Binario: 11111, Hexadecimal: 1f
5. Entrada ➡️ 64 → Binario: 1000000, Hexadecimal: 40

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

binary = ""      # Esta variable debe calcularse en base a la lógica del problema
hexadecimal = "" # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", binary == "1010" and hexadecimal == "a")
print("🧪 ", binary == "11111111" and hexadecimal == "ff")
print("🧪 ", binary == "10000" and hexadecimal == "10")
print("🧪 ", binary == "11111" and hexadecimal == "1f")
print("🧪 ", binary == "1000000" and hexadecimal == "40")
```

🧠 **Tips útiles**:

* 🔄 Usa `bin(numero)[2:]` para convertir a binario sin `0b`
* 🔁 Usa `hex(numero)[2:]` para hexadecimal sin `0x`
* 🧼 Asegúrate de que el resultado esté en **minúsculas** para que pase los tests

🌐 ¡Conviértete en un maestro de los sistemas numéricos! 💾🔢💪

---

## **🧭 Condicionales - Toma de Decisiones con if/else ⚖️🔀**

⚙️ En este grupo pondrás a prueba tu capacidad para tomar decisiones lógicas mediante estructuras condicionales en Python. Usarás `if`, `elif` y `else` para ejecutar acciones diferentes según los datos de entrada.
Aprenderás a simular sistemas de evaluación, clasificación, validación de rangos y mucho más. Este tipo de lógica es esencial para construir programas interactivos y adaptativos 🧩🔍.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### **Reto: Clasificador de Calificaciones 🎓📊⭐**

**Problema**: Evalúa el rendimiento de un estudiante a partir de su puntaje y determina su calificación alfabética y un mensaje motivador 🤓🎯💬

**Descripción**: En muchos sistemas académicos, las calificaciones se representan con letras según el rango de nota obtenida. Este programa debe recibir la calificación numérica de un estudiante y clasificarla usando las siguientes reglas:

📚 **Sistema de clasificación**:

```plaintext
A: 90 - 100   → "¡Excelente trabajo! 🌟"
B: 80 - 89    → "¡Muy buen rendimiento! 👍"
C: 70 - 79    → "Buen trabajo, sigue así 💪"
D: 60 - 69    → "Necesitas mejorar 🛠️"
F: Menos de 60 → "Debes estudiar más 📚"
```

Tu programa debe:

* 📝 Solicitar una puntuación entre 0 y 100
* 🔠 Determinar la calificación alfabética
* 💬 Mostrar también el mensaje correspondiente

**Casos de prueba**:

1. Entrada ➡️ 95 → Letra: A, Mensaje: "¡Excelente trabajo! 🌟"
2. Entrada ➡️ 82 → Letra: B, Mensaje: "¡Muy buen rendimiento! 👍"
3. Entrada ➡️ 75 → Letra: C, Mensaje: "Buen trabajo, sigue así 💪"
4. Entrada ➡️ 65 → Letra: D, Mensaje: "Necesitas mejorar 🛠️"
5. Entrada ➡️ 45 → Letra: F, Mensaje: "Debes estudiar más 📚"

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

grade_letter = ""  # Esta variable debe calcularse en base a la lógica del problema
feedback = ""      # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", grade_letter == "A" and feedback == "¡Excelente trabajo! 🌟")
print("🧪 ", grade_letter == "B" and feedback == "¡Muy buen rendimiento! 👍")
print("🧪 ", grade_letter == "C" and feedback == "Buen trabajo, sigue así 💪")
print("🧪 ", grade_letter == "D" and feedback == "Necesitas mejorar 🛠️")
print("🧪 ", grade_letter == "F" and feedback == "Debes estudiar más 📚")
```

🧠 **Tips útiles**:

* 🔎 Usa `if`, `elif`, `else` para evaluar los rangos
* 💡 Cuida bien los límites: incluye correctamente los extremos (ej: `>=`, `<=`)
* 🧼 Asegúrate de que el texto sea **exactamente igual** al esperado

🎯 ¡Aprender a evaluar… también se evalúa! 😉

---

### **Reto: Clasificador de IMC con Consejos de Salud 🏥⚖️🥗**

**Problema**: Calcula el IMC e interpreta el resultado según estándares de salud, mostrando una recomendación personalizada 🧘‍♂️📏🩺

**Descripción**: En medicina, el Índice de Masa Corporal no solo se calcula, también se interpreta para dar recomendaciones. Este reto amplía el anterior con un sistema de clasificación:

📚 **Clasificación IMC**:

```plaintext
< 18.5      → Bajo peso → "Consulta un nutricionista 🍎"
18.5 - 24.9 → Normal     → "Mantén tu peso actual 👍"
25.0 - 29.9 → Sobrepeso  → "Aumenta tu actividad física 🏃‍♂️"
≥ 30.0      → Obesidad   → "Consulta un médico 🩺"
```

Tu programa debe:

* 🧍 Solicitar peso (kg) y altura (m)
* 📐 Calcular el IMC redondeado a 2 decimales
* 🧠 Determinar la categoría y consejo

**Casos de prueba**:

1. Entrada ➡️ 45 kg, 1.65 m → IMC: 16.53, Clasificación: Bajo peso, Consejo: "Consulta un nutricionista 🍎"
2. Entrada ➡️ 65 kg, 1.70 m → IMC: 22.49, Clasificación: Normal, Consejo: "Mantén tu peso actual 👍"
3. Entrada ➡️ 85 kg, 1.75 m → IMC: 27.76, Clasificación: Sobrepeso, Consejo: "Aumenta tu actividad física 🏃‍♂️"
4. Entrada ➡️ 95 kg, 1.70 m → IMC: 32.87, Clasificación: Obesidad, Consejo: "Consulta un médico 🩺"
5. Entrada ➡️ 55 kg, 1.70 m → IMC: 19.03, Clasificación: Normal, Consejo: "Mantén tu peso actual 👍"

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

bmi = 0             # Esta variable debe calcularse en base a la lógica del problema
category = ""       # Esta variable debe calcularse en base a la lógica del problema
recommendation = "" # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", bmi == 16.53 and category == "Bajo peso" and recommendation == "Consulta un nutricionista 🍎")
print("🧪 ", bmi == 22.49 and category == "Normal" and recommendation == "Mantén tu peso actual 👍")
print("🧪 ", bmi == 27.76 and category == "Sobrepeso" and recommendation == "Aumenta tu actividad física 🏃‍♂️")
print("🧪 ", bmi == 32.87 and category == "Obesidad" and recommendation == "Consulta un médico 🩺")
print("🧪 ", bmi == 19.03 and category == "Normal" and recommendation == "Mantén tu peso actual 👍")
```

🧠 **Tips útiles**:

* 📥 Usa `input()` y `float()` para los datos
* 🧮 Redondea con `round()`
* 🧠 Aplica `if-elif-else` para categorizar

⚖️ ¡Las decisiones saludables también se codifican! 💪

---

¡Con mucho cariño y potencia lógica! 💻💙 Aquí tienes los **3 retos restantes del grupo de Condicionales** para completar el grupo 2. Todo con la misma estructura clara, didáctica y llena de estilo 🐍✨

---

### **Reto: Calculadora de Descuentos por Edad 🧓🧒🛍️**

**Problema**: Calcula el total a pagar aplicando un descuento según la edad del cliente. Ideal para promociones automáticas en tiendas o supermercados 🎯💳

**Descripción**: Las promociones según la edad son comunes: los niños, estudiantes o adultos mayores reciben descuentos especiales. Este programa aplicará un descuento al total de compra según la edad ingresada por el usuario:

📚 **Reglas de descuento**:

```plaintext
Edad 0-12     → 20% de descuento
Edad 13-25    → 15% de descuento
Edad 26-64    → Sin descuento
Edad 65 o más → 25% de descuento
```

Tu programa debe:

* 🧍 Solicitar la edad del cliente
* 💵 Solicitar el monto total de la compra
* 🔢 Calcular el monto con descuento
* 🖥️ Mostrar el total final redondeado a dos decimales

**Casos de prueba**:

1. Entrada ➡️ Edad: 10, Monto: \$100 → Total con descuento: \$80.00
2. Entrada ➡️ Edad: 20, Monto: \$150 → Total con descuento: \$127.50
3. Entrada ➡️ Edad: 40, Monto: \$200 → Total con descuento: \$200.00
4. Entrada ➡️ Edad: 70, Monto: \$120 → Total con descuento: \$90.00
5. Entrada ➡️ Edad: 15, Monto: \$80 → Total con descuento: \$68.00

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

final_price = 0  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", final_price == 80.00)
print("🧪 ", final_price == 127.50)
print("🧪 ", final_price == 200.00)
print("🧪 ", final_price == 90.00)
print("🧪 ", final_price == 68.00)
```

🧠 **Tips útiles**:

* 🧾 Usa condiciones encadenadas con `if-elif-else`
* 🪙 Usa `round(valor, 2)` para mantener dos decimales
* 🎯 No olvides convertir `input()` a `int` o `float`

🛍️ ¡Descuenta errores y suma aciertos! 🧠💸

---

### **Reto: Detector de Año Bisiesto 📆🧐💡**

**Problema**: Determina si un año ingresado por el usuario es bisiesto o no, y muestra un mensaje con emojis de calendario 🎯📅

**Descripción**: En el calendario gregoriano, los años bisiestos tienen 366 días y ocurren bajo reglas específicas. Este programa identificará si un año es bisiesto:

📚 **Reglas**:

```plaintext
Es bisiesto si es divisible por 4,
excepto los años divisibles por 100,
salvo que también sean divisibles por 400.
```

Tu programa debe:

* 📅 Solicitar un año
* 🧠 Aplicar las reglas para determinar si es bisiesto
* 💬 Imprimir si es bisiesto con un mensaje decorado

**Casos de prueba**:

1. Entrada ➡️ 2024 → Bisiesto: True
2. Entrada ➡️ 1900 → Bisiesto: False
3. Entrada ➡️ 2000 → Bisiesto: True
4. Entrada ➡️ 2023 → Bisiesto: False
5. Entrada ➡️ 2100 → Bisiesto: False

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

is_leap = False  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", is_leap == True)
print("🧪 ", is_leap == False)
print("🧪 ", is_leap == True)
print("🧪 ", is_leap == False)
print("🧪 ", is_leap == False)
```

🧠 **Tips útiles**:

* 🔍 Usa operadores lógicos `and`, `or`
* 📆 Ten cuidado con los años múltiplos de 100 y 400
* 🔄 Evalúa los casos en orden lógico

📅 ¡Tu código también puede marcar la diferencia en el calendario! 🔁🕰️

---

### **Reto: Clasificador de Números Positivos, Negativos o Cero ➕➖0️⃣**

**Problema**: Determina si un número ingresado por el usuario es positivo, negativo o cero, y muestra el resultado con estilo y claridad 🎯📈

**Descripción**: En muchos programas se necesita clasificar números según su signo. Este reto pide que tomes un número y muestres a qué grupo pertenece con un mensaje expresivo.

Tu programa debe:

* 🔢 Solicitar un número (puede ser decimal)
* 🔍 Evaluar si es mayor que cero, igual o menor
* 💬 Imprimir un mensaje adecuado con emojis

**Casos de prueba**:

1. Entrada ➡️ 10 → Resultado: "Positivo ➕"
2. Entrada ➡️ -3.5 → Resultado: "Negativo ➖"
3. Entrada ➡️ 0 → Resultado: "Es cero 0️⃣"
4. Entrada ➡️ 200 → Resultado: "Positivo ➕"
5. Entrada ➡️ -100 → Resultado: "Negativo ➖"

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

classification = ""  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", classification == "Positivo ➕")
print("🧪 ", classification == "Negativo ➖")
print("🧪 ", classification == "Es cero 0️⃣")
print("🧪 ", classification == "Positivo ➕")
print("🧪 ", classification == "Negativo ➖")
```

🧠 **Tips útiles**:

* ⚖️ Usa `if`, `elif`, `else` con operadores de comparación
* 🎯 Asegúrate que los mensajes sean exactamente como en el ejemplo

📈 ¡No importa si el número sube o baja, lo importante es que tú sigas creciendo! 🚀📊

---

## **🌀 Bucles - Repetición y Automatización con for/while 🔁💻**

🔄 En este grupo dominarás las estructuras repetitivas en Python: los bucles **`for`** y **`while`**. Aprenderás a automatizar tareas, procesar colecciones de datos y crear secuencias numéricas, ahorrando líneas de código y evitando errores manuales. Estos patrones son la base para trabajar con listas, archivos, gráficos y mucho más 📈✨.

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### **Reto: Suma de Números Pares en un Rango ➕🔢**

**Problema**: Calcula la suma de todos los números pares dentro de un rango dado por el usuario, usando un bucle `for` 🧮✅

**Descripción**: En análisis de datos o cálculos financieros, muchas veces necesitas sumar únicamente valores específicos (p. ej. pares). Este reto te ayudará a dominar los bucles `for`, las condiciones y la acumulación de un resultado.

Tu programa debe:

* 🔢 Solicitar al usuario un **inicio** y un **fin** de rango (enteros)
* 🔍 Recorrer todos los números del rango inclusivo con un `for`
* ✅ Sumar solo los números **pares**
* 🖥️ Imprimir la suma total

**Casos de prueba**:

1. Entrada ➡️ 1, 10 → Suma esperada: 30   (2+4+6+8+10)
2. Entrada ➡️ 5, 15 → Suma esperada: 60   (6+8+10+12+14)
3. Entrada ➡️ 0, 0  → Suma esperada: 0    (no hay pares)
4. Entrada ➡️ 2, 2  → Suma esperada: 2    (solo el 2)
5. Entrada ➡️ 3, 7  → Suma esperada: 10   (4+6)

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

total = 0  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", total == 30)
print("🧪 ", total == 60)
print("🧪 ", total == 0)
print("🧪 ", total == 2)
print("🧪 ", total == 10)
```

🧠 **Tips útiles**:

* 📝 Usa `range(start, end+1)` para incluir el límite superior
* 🔍 Dentro del bucle, filtra con `if n % 2 == 0`
* ➕ Incrementa `total += n` para acumular

🔢 ¡Repite y suma tu camino hacia el éxito! 🚀

---

### **Reto: Generador de Tabla de Multiplicar 📊✖️**

**Problema**: Genera e imprime la tabla de multiplicar de un número dado, del 1 al 12, usando un bucle `for` 📈🔢

**Descripción**: Las tablas de multiplicar son un clásico de la enseñanza. Este reto te entrenará en cómo usar bucles `for` para repetición controlada y formateo de salida.

Tu programa debe:

* 🔢 Pedir al usuario un número entero
* 🔁 Usar un bucle `for` de 1 a 12
* ✖️ Calcular en cada iteración el producto
* 🖥️ Imprimir cada línea con el formato: `n x i = resultado`

**Casos de prueba** (solo comprobamos un valor de *n* cada vez):

1. Entrada ➡️ 5 → Línea 5x1=5, …, 5x12=60  (suma de resultados = 390)
2. Entrada ➡️ 7 → Línea 7x1=7, …, 7x12=84  (suma de resultados = 546)
3. Entrada ➡️ 3 → Línea 3x1=3, …, 3x12=36  (suma de resultados = 234)
4. Entrada ➡️ 9 → Línea 9x1=9, …, 9x12=108 (suma de resultados = 702)
5. Entrada ➡️ 12→ Línea 12x1=12,…,12x12=144(suma de resultados = 936)

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

# Puedes opcionalmente sumar la serie o solo validar la tabla
sum_results = 0  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", sum_results == 390)
print("🧪 ", sum_results == 546)
print("🧪 ", sum_results == 234)
print("🧪 ", sum_results == 702)
print("🧪 ", sum_results == 936)
```

🧠 **Tips útiles**:

* 🔄 Bucle `for i in range(1, 13):`
* ✖️ Calcula `product = n * i` y muestra con `print()`
* ➕ Para validar, suma todos los `product` en `sum_results`

✖️ ¡Multiplica tu conocimiento! ✨

---

### **Reto: Calculadora de Factorial 🧮✨**

**Problema**: Calcula el factorial de un número entero no negativo usando un bucle `for` 📐🔢

**Descripción**: El factorial de un número *n* (denotado *n!*) es el producto de todos los enteros desde 1 hasta *n*. Se usa en combinatoria, probabilidad y análisis matemático. Este reto te hará practicar acumuladores y bucles.

Tu programa debe:

* 🔢 Solicitar al usuario un número entero `n` ≥ 0
* 🧠 Calcular `n!` usando un bucle `for`
* 🖥️ Devolver el resultado

**Casos de prueba**:

1. Entrada ➡️ 5  → Salida: 120
2. Entrada ➡️ 7  → Salida: 5040
3. Entrada ➡️ 0  → Salida: 1
4. Entrada ➡️ 1  → Salida: 1
5. Entrada ➡️ 10 → Salida: 3628800

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

factorial = 0  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", factorial == 120)      # 5! = 120
print("🧪 ", factorial == 5040)     # 7! = 5040
print("🧪 ", factorial == 1)        # 0! = 1
print("🧪 ", factorial == 1)        # 1! = 1
print("🧪 ", factorial == 3628800)  # 10! = 3628800
```

🧠 **Tips útiles**:

* 🔄 Inicializa `factorial = 1` y recorre `for i in range(1, n+1): factorial *= i`
* ⚠️ Ten en cuenta que `0!` = 1
* 📝 Usa `int(input())` para leer `n`

🎉 ¡Multiplica tu éxito factorial! 🥳

---

### **Reto: Generador de Secuencia Fibonacci 🌀🔢**

**Problema**: Genera una lista con los primeros *n* términos de la serie de Fibonacci usando `for` o `while` 📈✨

**Descripción**: La serie de Fibonacci comienza con 0 y 1, y cada término es la suma de los dos anteriores. Aparece en naturaleza, algoritmos y arte. Este reto refuerza manejo de listas y bucles.

Tu programa debe:

* 🔢 Solicitar al usuario la cantidad de términos `n` ≥ 1
* 🔁 Generar la lista `sequence` con los primeros *n* valores de Fibonacci
* 🖥️ Imprimir la lista

**Casos de prueba**:

1. Entrada ➡️ 1  → Salida: \[0]
2. Entrada ➡️ 2  → Salida: \[0, 1]
3. Entrada ➡️ 5  → Salida: \[0, 1, 1, 2, 3]
4. Entrada ➡️ 8  → Salida: \[0, 1, 1, 2, 3, 5, 8, 13]
5. Entrada ➡️ 3  → Salida: \[0, 1, 1]

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

sequence = []  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", sequence == [0])
print("🧪 ", sequence == [0, 1])
print("🧪 ", sequence == [0, 1, 1, 2, 3])
print("🧪 ", sequence == [0, 1, 1, 2, 3, 5, 8, 13])
print("🧪 ", sequence == [0, 1, 1])
```

🧠 **Tips útiles**:

* 👥 Usa dos variables `a, b = 0, 1` y actualízalas
* ➕ En cada iteración, añade `a` a la lista y actualiza `(a, b) = (b, a + b)`
* 🔄 Para `n == 1` maneja el caso especial antes del bucle

🚀 ¡Salta de término en término hacia la grandeza! 🌟

---

### **Reto: Verificador de Palíndromos Numéricos 🔄🔢**

**Problema**: Determina si un número entero es palíndromo (se lee igual al derecho y al revés) usando un bucle o manipulación de cadenas 🧐✨

**Descripción**: Los palíndromos aparecen en palabras, números y secuencias. Este reto te ayudará a convertir números a cadenas, recorrerlas o invertirlas y compararlas.

Tu programa debe:

* 🔢 Solicitar un número entero (puede ser positivo)
* 🔁 Verificar si su representación es igual al invertido
* 🖥️ Mostrar `True` o `False`

**Casos de prueba**:

1. Entrada ➡️ 121   → True
2. Entrada ➡️ 12321 → True
3. Entrada ➡️ 123   → False
4. Entrada ➡️ 10    → False
5. Entrada ➡️ 1111  → True

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

is_palindrome = False  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", is_palindrome == True)
print("🧪 ", is_palindrome == True)
print("🧪 ", is_palindrome == False)
print("🧪 ", is_palindrome == False)
print("🧪 ", is_palindrome == True)
```

🧠 **Tips útiles**:

* 🔤 Convierte con `s = str(numero)`
* 🔄 Invierte con `s[::-1]`
* ⚖️ Compara `s == s[::-1]`

🔁 ¡Que tu código sea palíndromo de eficiencia! 🎯

---

## **🔗 Integración - Combina tus habilidades 🚀**

🎯 En este último grupo pondrás en práctica **todos** los conceptos aprendidos: entrada/salida, condicionales y bucles. Resolverás retos que simulan sistemas reales, combinando cálculos, validaciones y procesamiento de datos. ¡Demuestra tu dominio completo de Python! 🐍💻

Cada ejercicio debe resolverse completando el código base proporcionado, sin modificar sus casos de prueba.
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### **Reto: Sistema de Gestión de Inventario 📦🏪📊**

**Problema**: Calcula el valor total del inventario y detecta qué productos tienen stock bajo, generando un resumen claro 🏷️🔍

**Descripción**: Un inventario almacena nombre de producto, precio unitario y cantidad. Este reto te pide:

* 📥 Leer una lista de 3 productos (nombre, precio, cantidad)
* 🔢 Calcular el valor total: suma de `precio × cantidad`
* ⚠️ Identificar productos con stock < 5
* 🖥️ Imprimir `total_value` y la lista `low_stock`

**Casos de prueba**:

1. Productos → \[("Laptop",800,10),("Mouse",25,15),("Teclado",50,3)]
   → total\_value=8875.00, low\_stock=\["Teclado"]
2. \[("Monitor",300,8),("Cable",15,20),("Silla",150,2)]
   → total\_value=3000.00, low\_stock=\["Silla"]
3. \[("Teléfono",400,12),("Funda",20,25),("Cargador",5,10)]
   → total\_value= (400×12)+(20×25)+(5×10)= 4800+500+50=5350.00, low\_stock=\[]
4. \[("Tablet",250,6),("Audífono",80,1),("Micrófono",60,3)]
   → total\_value= (250×6)+(80×1)+(60×3)=1500+80+180=1760.00, low\_stock=\["Audiófono","Micrófono"]
5. \[("Impresora",180,7),("Papel",10,50),("Tinta",45,2)]
   → total\_value= (180×7)+(10×50)+(45×2)=1260+500+90=1850.00, low\_stock=\["Tinta"]

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

total_value = 0    # Esta variable debe calcularse en base a la lógica del problema
low_stock = []     # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", round(total_value,2) == 8875.00 and low_stock == ["Teclado"])
print("🧪 ", round(total_value,2) == 3000.00 and low_stock == ["Silla"])
print("🧪 ", round(total_value,2) == 5350.00 and low_stock == [])
print("🧪 ", round(total_value,2) == 1760.00 and low_stock == ["Audiófono","Micrófono"])
print("🧪 ", round(total_value,2) == 1850.00 and low_stock == ["Tinta"])
```

🧠 **Tips útiles**:

* 🔄 Recorre la lista con un bucle `for`
* ➕ Acumula `price*qty` en `total_value`
* ⚠️ Usa `if qty < 5` para añadir a `low_stock`

📦 ¡Gestiona tu código y tu inventario con eficiencia!

---

### **Reto: Analizador de Calificaciones Estudiantiles 🎓📈**

**Problema**: Procesa las notas de varios estudiantes y calcula promedio, mejor y peor rendimiento 📊🏆

**Descripción**: A partir de una lista de tuplas (nombre, nota), este programa debe:

* 📥 Leer calificaciones de 3 estudiantes
* 🔢 Calcular `average` (promedio)
* 🏅 Determinar `best_student` y `worst_student`
* 🖥️ Imprimir `average`, `best_student`, `worst_student`

**Casos de prueba**:

1. \[("Ana",85),("Carlos",92),("María",78)] → average=85.00, best="Carlos", worst="María"
2. \[("Luis",95),("Elena",87),("Pedro",76)] → average=86.00, best="Luis", worst="Pedro"
3. \[("Diego",58),("Carmen",94),("Jane",82)] → average=78.00, best="Carmen", worst="Diego"
4. \[("Juan",82),("Laura",91),("Miguel",79)] → average=84.00, best="Laura", worst="Miguel"
5. \[("Patricia",96),("Fernando",84),("Gabriela",90)] → average=90.00, best="Patricia", worst="Fernando"

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

average = 0           # Esta variable debe calcularse en base a la lógica del problema
best_student = ""     # Esta variable debe calcularse en base a la lógica del problema
worst_student = ""    # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", round(average,2) == 85.00 and best_student=="Carlos" and worst_student=="María")
print("🧪 ", round(average,2) == 86.00 and best_student=="Luis" and worst_student=="Pedro")
print("🧪 ", round(average,2) == 78.00 and best_student=="Carmen" and worst_student=="Diego")
print("🧪 ", round(average,2) == 84.00 and best_student=="Laura" and worst_student=="Miguel")
print("🧪 ", round(average,2) == 90.00 and best_student=="Patricia" and worst_student=="Fernando")
```

🧠 **Tips útiles**:

* ➕ Suma todas las notas y divide por la cantidad
* 🔍 Usa `max()` y `min()` con una clave `key=lambda x: x[1]`
* 🗂️ Desempaqueta tuplas para nombre y nota

📚 ¡Analiza y mejora tu código educativo!

---

### **Reto: Simulador de Cajero Automático 🏧💵🔒**

**Problema**: Implementa funciones básicas de un cajero: PIN, saldo, retiro y depósito en un ciclo hasta salir ♻️🔑

**Descripción**: Este programa simula un cajero automático con:

* 🔐 Solicitud de PIN (fijo: 1234)
* 💵 Saldo inicial (p.ej. 1000)
* 🔄 Menú: consultar saldo, retirar, depositar, salir
* 🛑 Validar fondos en retiros y PIN

**Casos de prueba** (solo validamos PIN y saldo tras operaciones de ejemplo):

1. PIN=1234, Saldo=1000 → consulta → prints True
2. PIN=1234, Retiro=200 → Saldo final=800
3. PIN=1234, Depósito=300 → Saldo final=1300
4. PIN=0000 → fallo PIN
5. PIN=1234, Retiro=2000 → error fondos

*(Implementa pruebas dentro del flujo de menú para validar estas transacciones.)*

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

# Dadas las operaciones, aquí validamos el saldo final y errores
final_balance = 0    # Esta variable debe calcularse en base a la lógica del problema
pin_valid = False    # Esta variable debe calcularse en base a la lógica del problema
withdraw_ok = False  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", pin_valid and final_balance==1000)
print("🧪 ", final_balance==800)
print("🧪 ", final_balance==1300)
print("🧪 ", not pin_valid)
print("🧪 ", not withdraw_ok)
```

🧠 **Tips útiles**:

* 🛑 Usa un bucle `while True:` con `break` para el menú
* 🔐 Compara el PIN antes de permitir operaciones
* 💵 Verifica saldo antes de restar en retiros

🏦 ¡Tu código también puede dispensar éxito!

---

### **Reto: Clasificador de Números Pares e Impares 🔢⚖️🧮**

**Problema**: A partir de una lista de números ingresada por el usuario, cuenta cuántos son pares y cuántos son impares, y muestra ambos resultados con claridad 🎯🔢

**Descripción**: En muchos algoritmos necesitamos diferenciar valores según su paridad. Este reto te permite practicar:

* 📥 Lectura de listas (p. ej. ingresando valores separados por comas)
* 🔢 Conversión de cadenas a enteros
* 🔄 Uso de bucles y condicionales para clasificar cada número

Tu programa debe:

1. Solicitar al usuario una línea con números enteros separados por comas (por ejemplo: `1,2,3,4`).
2. Convertir cada fragmento a `int`.
3. Recorrerlos, y para cada uno:

   * Si `n % 2 == 0`, incrementar contador de pares
   * En otro caso, incrementar contador de impares
4. Imprimir los dos contadores: `evens` y `odds`

**Casos de prueba**:

1. Entrada ➡️ `1,2,3,4,5` → pares = 2, impares = 3
2. Entrada ➡️ `10,12,15` → pares = 2, impares = 1
3. Entrada ➡️ `1,3,5,7` → pares = 0, impares = 4
4. Entrada ➡️ `2,4,6,8` → pares = 4, impares = 0
5. Entrada ➡️ `0,1,2` → pares = 2, impares = 1

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

evens = 0  # Esta variable debe calcularse en base a la lógica del problema
odds  = 0  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", evens == 2 and odds == 3)
print("🧪 ", evens == 2 and odds == 1)
print("🧪 ", evens == 0 and odds == 4)
print("🧪 ", evens == 4 and odds == 0)
print("🧪 ", evens == 2 and odds == 1)
```

🧠 **Tips útiles**:

* ✂️ Usa `input().split(",")` para obtener una lista de cadenas
* 🔢 Convierte cada elemento con `int()`
* 🔄 Recorre con `for n in numbers:` y aplica `if n % 2 == 0`
* ➕ Incrementa `evens += 1` o `odds += 1` según corresponda

⚖️ ¡Equilibra tu lógica y domina la paridad! 🚀🐍

---

### **Reto: Menú Interactivo de Operaciones Básicas 📐➕➖✖️**

**Problema**: Crea un menú que permita al usuario elegir entre suma, resta, multiplicación y división de dos números, y muestre el resultado con claridad y estilo interactivo 🎮✨

**Descripción**: Los menús son fundamentales para aplicaciones interactivas. En este reto deberás:

1. Mostrar un menú con opciones:

   ```
   1) Sumar
   2) Restar
   3) Multiplicar
   4) Dividir
   ```
2. Solicitar al usuario que ingrese la **opción** (1–4).
3. Pedir dos números (pueden ser enteros o flotantes).
4. Ejecutar la operación seleccionada.
5. Mostrar el **resultado** en pantalla.

🎯 Practicarás `input()`, condicionales `if-elif-else`, conversión de tipos y formateo de salida.

**Casos de prueba**:

1. Opción 1 (Sumar), números 5 y 3  → Resultado: 8
2. Opción 2 (Restar), números 10 y 4 → Resultado: 6
3. Opción 3 (Multiplicar), números 7 y 6 → Resultado: 42
4. Opción 4 (Dividir), números 20 y 5 → Resultado: 4.0
5. Opción 4 (Dividir), números 7 y 2 → Resultado: 3.5

**Código base**:

```python
# 💻 Código inicial para validar tu programa
# 👇 Inserta tu código arriba de estas pruebas y verifica que pasen ✅

result = 0  # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", result == 8)    # Suma: 5 + 3
print("🧪 ", result == 6)    # Resta: 10 - 4
print("🧪 ", result == 42)   # Multiplicación: 7 * 6
print("🧪 ", result == 4.0)  # División: 20 / 5
print("🧪 ", result == 3.5)  # División: 7 / 2
```

🧠 **Tips útiles**:

* 🎛️ Usa `choice = input()` y `int(choice)` para la opción
* 🔢 Convierte los números con `float()` para manejar decimales
* 🧠 Emplea `if-elif-else` para elegir la operación adecuada
* ⚠️ Evita división por cero comprobando el segundo número antes

🚀 ¡Con este menú interactivo, tus programas serán más amigables y dinámicos! 💻🌟

## 🎉 ¡Excelente Trabajo! 🌟

Has demostrado un gran dominio de Python al resolver estos 20 retos que abarcan desde lo más básico hasta la integración de múltiples conceptos. Cada uno ha sido diseñado para retarte a pensar, planificar y codificar de manera clara y eficiente. ¡Felicidades por tu rendimiento y dedicación! 🚀💪

### 📝 Criterios de Evaluación:

* ✅ **Algoritmos**: Funcionan correctamente para todos los casos de prueba.
* 🎯 **Tipos y Variables**: Uso apropiado y consistente de `int`, `float` y nombres descriptivos.
* 🔄 **Estructuras de Control**: If/else y bucles usados de forma efectiva.
* 📥 **Validación**: Entradas del usuario correctamente convertidas y comprobadas.
* 🖥️ **Salida**: Formato limpio, mensajes claros y coherentes.
* 💬 **Comentarios**: Explican la lógica sin redundancias.
* 📊 **Pruebas**: Cada reto validado con `print(True)` para automatizar la verificación.
* ✨ **Calidad de Código**: Legible, modular y con buenas prácticas.

### 🏅 Niveles de Dominio:

* **🌱 Principiante**: Completa retos **1–5** (Input/Print)
* **🌿 Intermedio**: Completa retos **1–10** (+ Condicionales)
* **🌳 Avanzado**: Completa retos **1–15** (+ Bucles)
* **🌟 Experto**: Completa **1–20** (Integración Total)

### 💡 Consejos para Seguir Mejorando:

* 🎯 **Lee con atención** cada enunciado antes de empezar a programar.
* 🧪 **Prueba** y **depura** tu código con distintos escenarios.
* 📝 **Documenta** funciones y partes complejas para facilitar el mantenimiento.
* 🔄 **Refactoriza**: busca oportunidades para simplificar y optimizar tu solución.
* 🤝 **Colabora** y revisa código de otros para aprender nuevas técnicas.

### 🚀 Próximos Desafíos:

* 📚 Profundiza en **estructuras de datos** avanzadas (listas anidadas, diccionarios, conjuntos).
* 🔧 Aprende a **modularizar** tu código con funciones y paquetes.
* 🌐 Explora **desarrollo web** con frameworks como Flask o Django.
* 📈 Adéntrate en **análisis de datos** y automatización de tareas.
* 🎮 Crea **proyectos reales**: desde juegos sencillos hasta aplicaciones completas.

¡Adelante, el mundo del software te espera con infinitas posibilidades! 🎓✨
