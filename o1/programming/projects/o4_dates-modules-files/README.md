# 🐍 Python Nivel 4: Fechas, Módulos y Archivos

```
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║           🐍  PYTHON PROGRAMMING COURSE  🐍             ║
    ║                                                        ║
    ║              ∩＿＿＿∩                                   ║
    ║             /        \                                 ║
    ║            /  ●    ●  \      Level 4                   ║
    ║           |     ▼      |     Professional              ║
    ║           |   \___/    |                               ║
    ║            \__________/                                ║
    ║                                                        ║
    ║         Dates • Modules • Files • Projects             ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
```

## 📖 Introducción

¡Bienvenido al Nivel 4! 🎉 Has conquistado estructuras de datos y funciones, ahora es momento de trabajar con fechas, organizar tu código en módulos y guardar información en archivos. Estas habilidades te convertirán en un programador profesional capaz de crear aplicaciones completas.

## 🎯 Descripción de la Guía

Esta guía está diseñada para estudiantes que completaron el Nivel 3 y están listos para herramientas profesionales.

### ✨ ¿Qué aprenderás?

- 📅 **o4.1 - Date & Time**: Manejo de fechas, horas y formateo
- 📦 **o4.2 - Modules**: Importar, crear y organizar código
- 💾 **o4.3 - Files**: Leer, escribir y gestionar archivos

**Tiempo estimado por tema: 1.5 horas**  
**Tiempo total del nivel: 4.5 horas**

---

## o4.1: Date & Time - Trabajando con Fechas

### 🎯 Descripción del Tema

El módulo `datetime` te permite trabajar con fechas y horas de forma profesional. Aprenderás a obtener la fecha actual, calcular diferencias entre fechas, formatear fechas como texto y crear recordatorios automáticos.

---

### o4.1.1: 🎂 Contador de Cumpleaños

**📖 Historia:** Fernanda 🧙‍♀️ está emocionada porque su cumpleaños se acerca. Nació el 15 de agosto de 2008 y quiere saber exactamente cuántos días faltan para su próximo cumpleaños. También quiere saber cuántos años va a cumplir.

**📝 Descripción:** Tu programa usa el módulo `datetime` para obtener la fecha actual, calcular la próxima fecha de cumpleaños, determinar cuántos días faltan y calcular la edad que cumplirá.

**⚙️ Funcionalidades:**
- Importar módulo `datetime`
- Obtener fecha actual con `datetime.now()`
- Crear fecha de próximo cumpleaños (15 de agosto)
- Calcular días faltantes usando resta de fechas
- Calcular edad que cumplirá

**✅ Casos de prueba:**

| Input                | Expected Output               |
| -------------------- | ----------------------------- |
| `birthday_month`     | `8`                           |
| `birthday_day`       | `15`                          |
| `age_turning`        | `18` (2026 - 2008)            |
| `days_until > 0`     | `True`                        |
| `type(current_date)` | `<class 'datetime.datetime'>` |

**💻 Código base:**

```python
# Birthday Countdown 🎂
from datetime import datetime

# Your code here 💻
current_date = None  # get current date
birthday_month = 0  # set to 8
birthday_day = 0  # set to 15
birth_year = 2008
next_birthday = None  # create datetime for next birthday
days_until = 0  # calculate difference
age_turning = 0  # calculate age

print(f"Hoy es: {current_date.strftime('%d/%m/%Y')}")
print(f"Próximo cumpleaños: {next_birthday.strftime('%d/%m/%Y')}")
print(f"Faltan {days_until} días para tu cumpleaños!")
print(f"Cumplirás {age_turning} años")

# Test cases
print(birthday_month == 8)
print(birthday_day == 15)
print(age_turning == 18)
print(days_until > 0)
print(type(current_date).__name__ == 'datetime')
```

**💡 Tips:**
- 🔹 Fecha actual: `datetime.now()`
- 🔹 Crear fecha: `datetime(2026, 8, 15)`
- 🔹 Diferencia: `(next_birthday - current_date).days`
- 🔹 Formatear: `.strftime('%d/%m/%Y')`

**🚀 Motivación:** ¡Fernanda cuenta los días para su fiesta! 🧙‍♀️🎂

---

### o4.1.2: ⏰ Registro de Aventura

**📖 Historia:** Elliot ⚡ está en una misión épica en su videojuego favorito. Comenzó a jugar a las 2:30 PM y quiere saber cuánto tiempo lleva jugando. Su mamá le dijo que solo puede jugar 2 horas, así que necesita calcular a qué hora debe parar.

**📝 Descripción:** Tu programa trabaja con objetos `time` y `timedelta` para calcular duraciones, sumar tiempo a una hora específica y determinar la hora límite.

**⚙️ Funcionalidades:**
- Crear hora de inicio con `time(14, 30)` (2:30 PM)
- Crear duración permitida con `timedelta(hours=2)`
- Combinar fecha actual con hora de inicio
- Calcular hora de finalización sumando duración
- Formatear horas en formato 12h (AM/PM)

**✅ Casos de prueba:**

| Input            | Expected Output                |
| ---------------- | ------------------------------ |
| `start_hour`     | `14`                           |
| `start_minute`   | `30`                           |
| `allowed_hours`  | `2`                            |
| `end_hour`       | `16` (4 PM)                    |
| `type(duration)` | `<class 'datetime.timedelta'>` |

**💻 Código base:**

```python
# Adventure Timer ⏰
from datetime import datetime, time, timedelta

# Your code here 💻
start_hour = 0  # set to 14
start_minute = 0  # set to 30
allowed_hours = 0  # set to 2
start_time = None  # create time object
current_date = datetime.now().date()
start_datetime = None  # combine date and time
duration = None  # create timedelta
end_datetime = None  # calculate end time
end_hour = 0  # extract hour from end_datetime

print(f"Inicio de juego: {start_time.strftime('%I:%M %p')}")
print(f"Duración permitida: {allowed_hours} horas")
print(f"Debe terminar a las: {end_datetime.strftime('%I:%M %p')}")

# Test cases
print(start_hour == 14)
print(start_minute == 30)
print(allowed_hours == 2)
print(end_hour == 16)
print(type(duration).__name__ == 'timedelta')
```

**💡 Tips:**
- 🔹 Crear hora: `time(14, 30)`
- 🔹 Duración: `timedelta(hours=2)`
- 🔹 Combinar: `datetime.combine(date, time)`
- 🔹 Sumar: `start_datetime + duration`

**🚀 Motivación:** ¡Elliot controla su tiempo de juego! ⚡⏰

---

## o4.2: Modules - Organizando el Código

### 🎯 Descripción del Tema

Los módulos te permiten organizar código en archivos separados y reutilizables. Aprenderás a importar módulos de Python, usar funciones de módulos populares como `math` y `random`, y crear tus propios módulos.

---

### o4.2.1: 🎲 Generador de Números de Suerte

**📖 Historia:** Chocolate 🐕 y sus amigos van a jugar a la lotería. Necesitan generar números de suerte aleatorios entre 1 y 50. Además, quieren calcular el promedio de sus números usando matemáticas avanzadas para ver si tienen "números mágicos".

**📝 Descripción:** Tu programa importa los módulos `random` y `math` para generar números aleatorios, calcularlos y redondearlos usando funciones matemáticas profesionales.

**⚙️ Funcionalidades:**
- Importar módulo `random` para números aleatorios
- Importar módulo `math` para operaciones matemáticas
- Generar 5 números aleatorios entre 1 y 50
- Calcular promedio de los números
- Redondear promedio hacia arriba con `math.ceil()`

**✅ Casos de prueba:**

| Input                                      | Expected Output  |
| ------------------------------------------ | ---------------- |
| `len(lucky_numbers)`                       | `5`              |
| `all(1 <= n <= 50 for n in lucky_numbers)` | `True`           |
| `average > 0`                              | `True`           |
| `rounded_avg >= average`                   | `True`           |
| `type(lucky_numbers)`                      | `<class 'list'>` |

**💻 Código base:**

```python
# Lucky Number Generator 🎲

# Your code here 💻 (import random and math)

lucky_numbers = []  # your code here 💻 (generate 5 random numbers 1-50)
average = 0  # your code here 💻 (calculate average)
rounded_avg = 0  # your code here 💻 (use math.ceil to round up)
max_number = 0  # your code here 💻 (find max with max())
min_number = 0  # your code here 💻 (find min with min())

print(f"Números de suerte: {lucky_numbers}")
print(f"Promedio: {average:.2f}")
print(f"Promedio redondeado: {rounded_avg}")
print(f"Mayor: {max_number}, Menor: {min_number}")

# Test cases
print(len(lucky_numbers) == 5)
print(all(1 <= n <= 50 for n in lucky_numbers))
print(average > 0)
print(rounded_avg >= average)
print(type(lucky_numbers) == list)
```

**💡 Tips:**
- 🔹 Importar: `import random, math`
- 🔹 Aleatorio: `random.randint(1, 50)`
- 🔹 Redondear arriba: `math.ceil(number)`
- 🔹 Generar varios: usa bucle con `append()`

**🚀 Motivación:** ¡Chocolate genera números mágicos! 🐕🎲

---

### o4.2.2: 🧮 Calculadora Científica

**📖 Historia:** Mijael 🧑‍💻 está ayudando a Fe con su tarea de matemáticas. Necesitan calcular la raíz cuadrada de números, elevar a potencias y calcular el factorial. Deciden crear una calculadora usando el módulo `math` en lugar de hacerlo manualmente.

**📝 Descripción:** Tu programa importa funciones específicas del módulo `math` (sqrt, pow, factorial) usando diferentes formas de import, realiza cálculos matemáticos avanzados y valida los resultados.

**⚙️ Funcionalidades:**
- Importar funciones específicas: `from math import sqrt, factorial`
- Importar módulo completo: `import math`
- Calcular raíz cuadrada de 144
- Calcular 2 elevado a la 10
- Calcular factorial de 5

**✅ Casos de prueba:**

| Input               | Expected Output   |
| ------------------- | ----------------- |
| `square_root`       | `12.0`            |
| `power_result`      | `1024.0`          |
| `factorial_result`  | `120`             |
| `pi_value`          | `3.14159...`      |
| `type(square_root)` | `<class 'float'>` |

**💻 Código base:**

```python
# Scientific Calculator 🧮

# Your code here 💻 (import necessary functions from math)

number = 144
square_root = 0  # your code here 💻 (sqrt of 144)
base = 2
exponent = 10
power_result = 0  # your code here 💻 (2^10)
n = 5
factorial_result = 0  # your code here 💻 (factorial of 5)
pi_value = 0  # your code here 💻 (get math.pi)
pi_rounded = 0  # your code here 💻 (round pi to 2 decimals)

print(f"√{number} = {square_root}")
print(f"{base}^{exponent} = {power_result}")
print(f"{n}! = {factorial_result}")
print(f"π ≈ {pi_rounded}")

# Test cases
print(square_root == 12.0)
print(power_result == 1024.0)
print(factorial_result == 120)
print(3.14 < pi_value < 3.15)
print(type(square_root) == float)
```

**💡 Tips:**
- 🔹 Importar específico: `from math import sqrt, factorial`
- 🔹 Raíz: `sqrt(144)`
- 🔹 Potencia: `pow(2, 10)` o `math.pow(2, 10)`
- 🔹 Factorial: `factorial(5)`
- 🔹 Constante: `math.pi`

**🚀 Motivación:** ¡Mijael y Fe resuelven matemáticas avanzadas! 🧑‍💻🧮

---

## o4.3: Files - Guardando Información

### 🎯 Descripción del Tema

Los archivos te permiten guardar datos de forma permanente. Aprenderás a crear archivos de texto, escribir información, leer contenido guardado y procesar datos línea por línea. Esto es fundamental para crear aplicaciones que recuerden información.

---

### o4.3.1: 📝 Diario de Amorosa

**📖 Historia:** Amorosa 💖 quiere escribir un diario digital donde guarde sus pensamientos cada día. Hoy escribe: "Hoy fue un día increíble, aprendí Python y me siento feliz". Quiere guardar esto en un archivo para nunca olvidarlo.

**📝 Descripción:** Tu programa crea un archivo de texto, escribe contenido en él, lo cierra apropiadamente, luego lo abre para leer y mostrar el contenido guardado.

**⚙️ Funcionalidades:**
- Abrir archivo en modo escritura ('w')
- Escribir texto en el archivo
- Cerrar archivo correctamente
- Abrir archivo en modo lectura ('r')
- Leer contenido completo del archivo

**✅ Casos de prueba:**

| Input                 | Expected Output |
| --------------------- | --------------- |
| `file_name`           | `'diary.txt'`   |
| `len(content) > 0`    | `True`          |
| `'Python' in content` | `True`          |
| `'feliz' in content`  | `True`          |
| `type(content)`       | `<class 'str'>` |

**💻 Código base:**

```python
# Amorosa's Diary 📝

file_name = 'diary.txt'
entry = "Hoy fue un día increíble, aprendí Python y me siento feliz"

# Your code here 💻
# Write to file
# (open file, write entry, close file)

# Your code here 💻
# Read from file
content = ''  # read content from file
word_count = 0  # count words in content
has_python = False  # check if 'Python' is in content

print(f"Contenido del diario:")
print(content)
print(f"\nTotal de palabras: {word_count}")
print(f"Menciona Python: {has_python}")

# Test cases
print(file_name == 'diary.txt')
print(len(content) > 0)
print('Python' in content)
print('feliz' in content)
print(type(content) == str)
```

**💡 Tips:**
- 🔹 Escribir: `file = open('diary.txt', 'w')`
- 🔹 Escribir contenido: `file.write(entry)`
- 🔹 Cerrar: `file.close()`
- 🔹 Leer: `file = open('diary.txt', 'r')`
- 🔹 Leer todo: `content = file.read()`

**🚀 Motivación:** ¡Amorosa guarda sus recuerdos para siempre! 💖📝

---

### o4.3.2: 🎮 Puntuaciones de Juego

**📖 Historia:** Doky 🐕 está jugando su videojuego favorito con sus amigos. Quiere guardar las mejores puntuaciones en un archivo para recordar quién es el campeón. Guarda: "Elliot: 1500", "Fe: 1200", "Chocolate: 1800" (¡Chocolate ganó!).

**📝 Descripción:** Tu programa crea un archivo de puntuaciones, escribe múltiples líneas (una por jugador), lee el archivo línea por línea, procesa cada línea para extraer nombres y puntos, y determina el ganador.

**⚙️ Funcionalidades:**
- Escribir múltiples líneas en archivo
- Usar '\n' para separar líneas
- Leer archivo línea por línea con `.readlines()`
- Procesar cada línea para extraer datos
- Encontrar puntuación máxima

**✅ Casos de prueba:**

| Input                | Expected Output  |
| -------------------- | ---------------- |
| `num_lines`          | `3`              |
| `max_score`          | `1800`           |
| `winner`             | `'Chocolate'`    |
| `'Elliot' in scores` | `True`           |
| `type(scores)`       | `<class 'list'>` |

**💻 Código base:**

```python
# Game Scores 🎮

file_name = 'scores.txt'
players_scores = [
    "Elliot: 1500",
    "Fe: 1200",
    "Chocolate: 1800"
]

# Your code here 💻
# Write all scores to file (one per line)

# Your code here 💻
# Read file and process
scores = []  # list with all lines
num_lines = 0  # count lines
max_score = 0  # find maximum score
winner = ''  # find player with max score
total_score = 0  # sum all scores

print(f"Puntuaciones guardadas:")
for score in scores:
    print(score.strip())

print(f"\n🏆 Ganador: {winner} con {max_score} puntos")
print(f"Total de jugadores: {num_lines}")
print(f"Puntuación total: {total_score}")

# Test cases
print(num_lines == 3)
print(max_score == 1800)
print(winner == 'Chocolate')
print('Elliot' in scores[0])
print(type(scores) == list)
```

**💡 Tips:**
- 🔹 Escribir líneas: `file.write(line + '\n')`
- 🔹 Leer líneas: `file.readlines()`
- 🔹 Procesar: usa `.split(':')` para separar nombre y puntos
- 🔹 Convertir: `int(score)` para números
- 🔹 Limpiar: `.strip()` quita espacios

**🚀 Motivación:** ¡Doky guarda el hall de la fama! 🐕🎮

---

## 🎉 ¡Felicidades! Has completado el Nivel 4

### 📊 Resumen de Logros

**✅ Has dominado:**
- 📅 **Date & Time**: Fechas actuales, cálculos, formateo, timedelta
- 📦 **Modules**: Import, random, math, funciones específicas
- 💾 **Files**: Escritura, lectura, procesamiento de archivos

**⏰ Tiempo completado:** 4.5 horas de práctica profesional

**🎓 Habilidades adquiridas:**
- Manejo profesional de fechas y horas
- Uso de módulos de Python estándar
- Persistencia de datos en archivos
- Organización de código modular

**🔜 Próximo nivel:** Proyectos Finales - Aplicaciones Completas

---

💪 **¡Excelente trabajo!** Fernanda, Elliot, Fe, Mijael, Chocolate, Doky y Amorosa están orgullosos de ti. ¡Eres un programador profesional! 🏆✨🚀
