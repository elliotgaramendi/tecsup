# 🐍 Examen Final Python - Fundamentos Completos 🐍

```
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║        ███████╗██╗███╗   ██╗ █████╗ ██╗                    ║
    ║        ██╔════╝██║████╗  ██║██╔══██╗██║                    ║
    ║        █████╗  ██║██╔██╗ ██║███████║██║                    ║
    ║        ██╔══╝  ██║██║╚██╗██║██╔══██║██║                    ║
    ║        ██║     ██║██║ ╚████║██║  ██║███████╗               ║
    ║        ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝               ║
    ║                                                            ║
    ║           🏆 PYTHON FINAL CHALLENGE 🏆                     ║
    ║                                                            ║
    ║         ✨ Demuestra todo lo que has aprendido ✨          ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
```

---

## 📋 Instrucciones del Examen

**🎯 Objetivo:** Resolver retos de programación que evalúan todos los conceptos aprendidos.

**📌 Reglas:**
- ⏰ Tiempo recomendado: 1 hora
- 🧪 Cada reto tiene 5 tests obligatorios
- ✅ Debes pasar los 5 tests para aprobar el reto
- 💯 Puntuación: Se evalúan acorde a la cantidad de tests correctos
- 🏆 Aprobado: >=13 retos completos

**💻 Formato:**
Cada reto incluye:
- Función que debes implementar
- Descripción clara del problema
- Ejemplos de uso
- 5 test cases públicos
- Playground para programar
- Tips estratégicos
- Motivación para seguir adelante

---

## 1️⃣ Algorithms & Code

### 🔢 Reto 1.1: Calculadora de Propina

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Fe 👨‍🍳 terminó de cenar en un restaurante y quiere calcular cuánto debe dejar de propina. El total de su cuenta es $150 y quiere dejar el 15% de propina. Ayúdalo a calcular el monto total a pagar (cuenta + propina).

**📝 Descripción:**
Implementa la función `calculate_tip(bill, tip_percent)` que recibe el monto de la cuenta y el porcentaje de propina, y retorna el total a pagar (cuenta + propina calculada).

**Ejemplos:**
```python
print(calculate_tip(100, 15))    # 115.0
print(calculate_tip(200, 20))    # 240.0
print(calculate_tip(50, 10))     # 55.0
```

**🧪 Tests:**
| Test | Input                          | Expected |
| ---- | ------------------------------ | -------- |
| 1    | `calculate_tip(100, 15)`       | `115.0`  |
| 2    | `calculate_tip(200, 20)`       | `240.0`  |
| 3    | `calculate_tip(50, 10)`        | `55.0`   |
| 4    | `calculate_tip(80, 18)`        | `94.4`   |
| 5    | `type(calculate_tip(100, 15))` | `float`  |

**💻 Playground:**
```python
def calculate_tip(bill, tip_percent):
    # Tu código aquí
    return 0.0

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        calculate_tip(100, 15) == 115.0,
        calculate_tip(200, 20) == 240.0,
        calculate_tip(50, 10) == 55.0,
        calculate_tip(80, 18) == 94.4,
        type(calculate_tip(100, 15)) == float
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Convierte ambas a sets: `set1 = set(list1)`, `set2 = set(list2)`
* 🔹 Usa operador de intersección: `common = set1 & set2`
* 🔹 Ordena y retorna lista: `return sorted(list(common))`
* 🔹 Una línea: `return sorted(list(set(list1) & set(list2)))`

**🚀 Motivación:**  
¡Doky y Chocolate comparten juguetes! 🐕🐕🎾 La intersección de sets es pura magia matemática. ¡Aplícala! 🎩✨

---

### 🌡️ Reto 1.2: Conversor de Temperatura

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Elliot ⚡ está programando un termómetro digital. Necesita convertir temperaturas de Celsius a Fahrenheit usando la fórmula: F = C × 9/5 + 32.

**📝 Descripción:**
Implementa la función `celsius_to_fahrenheit(celsius)` que convierte grados Celsius a Fahrenheit y retorna el resultado redondeado a 1 decimal.

**Ejemplos:**
```python
print(celsius_to_fahrenheit(0))      # 32.0
print(celsius_to_fahrenheit(100))    # 212.0
print(celsius_to_fahrenheit(37))     # 98.6
```

**🧪 Tests:**
| Test | Input                             | Expected |
| ---- | --------------------------------- | -------- |
| 1    | `celsius_to_fahrenheit(0)`        | `32.0`   |
| 2    | `celsius_to_fahrenheit(100)`      | `212.0`  |
| 3    | `celsius_to_fahrenheit(37)`       | `98.6`   |
| 4    | `celsius_to_fahrenheit(-40)`      | `-40.0`  |
| 5    | `type(celsius_to_fahrenheit(25))` | `float`  |

**💻 Playground:**
```python
def celsius_to_fahrenheit(celsius):
    # Tu código aquí
    return 0.0

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        celsius_to_fahrenheit(0) == 32.0,
        celsius_to_fahrenheit(100) == 212.0,
        celsius_to_fahrenheit(37) == 98.6,
        celsius_to_fahrenheit(-40) == -40.0,
        type(celsius_to_fahrenheit(25)) == float
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Aplica la fórmula: `fahrenheit = celsius * 9/5 + 32`
* 🔹 Redondea a 1 decimal: `round(resultado, 1)`
* 🔹 El test -40 es especial: ¡ambas escalas coinciden!
* 🔹 Una línea lo resuelve todo 🎯

**🚀 Motivación:**  
¡Elliot confía en tu habilidad matemática! ⚡ Las conversiones son pan comido para ti. ¡A por ello! 🔥

---

## 2️⃣ Conditionals

### 🎟️ Reto 2.1: Clasificador de Edad

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Fernanda 🧙‍♀️ organiza una fiesta y necesita clasificar a los invitados por grupos de edad: 'niño' (0-12), 'adolescente' (13-17), 'adulto' (18-64), 'senior' (65+).

**📝 Descripción:**
Implementa la función `classify_age(age)` que retorna la categoría correspondiente según la edad. Si la edad es negativa, retorna 'inválido'.

**Ejemplos:**
```python
print(classify_age(10))    # 'niño'
print(classify_age(15))    # 'adolescente'
print(classify_age(25))    # 'adulto'
```

**🧪 Tests:**
| Test | Input              | Expected        |
| ---- | ------------------ | --------------- |
| 1    | `classify_age(10)` | `'niño'`        |
| 2    | `classify_age(15)` | `'adolescente'` |
| 3    | `classify_age(25)` | `'adulto'`      |
| 4    | `classify_age(70)` | `'senior'`      |
| 5    | `classify_age(-5)` | `'inválido'`    |

**💻 Playground:**
```python
def classify_age(age):
    # Tu código aquí
    return ''

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        classify_age(10) == 'niño',
        classify_age(15) == 'adolescente',
        classify_age(25) == 'adulto',
        classify_age(70) == 'senior',
        classify_age(-5) == 'inválido'
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Verifica primero `if age < 0:` para casos inválidos
* 🔹 Usa `elif` para cada rango: 0-12, 13-17, 18-64, 65+
* 🔹 Los rangos son inclusivos: 12 es niño, 13 es adolescente
* 🔹 El último caso (senior) puede ser simplemente `else:`

**🚀 Motivación:**  
¡Fernanda cuenta contigo para organizar su fiesta! 🧙‍♀️🎉 Los condicionales son tu superpoder. ¡Úsalos! ✨

---

### 📊 Reto 2.2: Calificación a Letra

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Mijael 🧑‍💻 necesita convertir calificaciones numéricas (0-100) a letras: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59).

**📝 Descripción:**
Implementa la función `grade_to_letter(score)` que retorna la letra correspondiente. Si el score está fuera de rango (0-100), retorna 'X'.

**Ejemplos:**
```python
print(grade_to_letter(95))    # 'A'
print(grade_to_letter(82))    # 'B'
print(grade_to_letter(55))    # 'F'
```

**🧪 Tests:**
| Test | Input                  | Expected |
| ---- | ---------------------- | -------- |
| 1    | `grade_to_letter(95)`  | `'A'`    |
| 2    | `grade_to_letter(82)`  | `'B'`    |
| 3    | `grade_to_letter(75)`  | `'C'`    |
| 4    | `grade_to_letter(55)`  | `'F'`    |
| 5    | `grade_to_letter(150)` | `'X'`    |

**💻 Playground:**
```python
def grade_to_letter(score):
    # Tu código aquí
    return ''

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        grade_to_letter(95) == 'A',
        grade_to_letter(82) == 'B',
        grade_to_letter(75) == 'C',
        grade_to_letter(55) == 'F',
        grade_to_letter(150) == 'X'
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Primero valida rango: `if score < 0 or score > 100:`
* 🔹 Ordena de mayor a menor: A(>=90), B(>=80), C(>=70), D(>=60)
* 🔹 Todo lo demás en rango válido es 'F'
* 🔹 Recuerda: 90 es 'A', 89 es 'B' 🎯

**🚀 Motivación:**  
¡Mijael necesita tu sistema de calificaciones! 🧑‍💻 Cada `if` te acerca más al éxito. ¡Sigue así! 📈

---

## 3️⃣ Loops I

### 🔢 Reto 3.1: Suma de Rango

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Chocolate 🐕 está aprendiendo matemáticas y quiere sumar todos los números desde `start` hasta `end` (inclusivos). Por ejemplo, de 1 a 5 sería: 1+2+3+4+5 = 15.

**📝 Descripción:**
Implementa la función `sum_range(start, end)` que retorna la suma de todos los números en el rango [start, end]. Si start > end, retorna 0.

**Ejemplos:**
```python
print(sum_range(1, 5))      # 15
print(sum_range(10, 15))    # 75
print(sum_range(5, 1))      # 0
```

**🧪 Tests:**
| Test | Input               | Expected |
| ---- | ------------------- | -------- |
| 1    | `sum_range(1, 5)`   | `15`     |
| 2    | `sum_range(10, 15)` | `75`     |
| 3    | `sum_range(1, 100)` | `5050`   |
| 4    | `sum_range(5, 1)`   | `0`      |
| 5    | `sum_range(7, 7)`   | `7`      |

**💻 Playground:**
```python
def sum_range(start, end):
    # Tu código aquí
    return 0

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        sum_range(1, 5) == 15,
        sum_range(10, 15) == 75,
        sum_range(1, 100) == 5050,
        sum_range(5, 1) == 0,
        sum_range(7, 7) == 7
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Valida primero: `if start > end: return 0`
* 🔹 Inicializa acumulador: `total = 0`
* 🔹 Usa `for i in range(start, end + 1):` (el +1 incluye el final)
* 🔹 Suma cada número: `total += i`

**🚀 Motivación:**  
¡Chocolate aprende contigo! 🐕📚 Los loops son tu mejor amigo para tareas repetitivas. ¡Domínalos! 🔄

---

### ⭐ Reto 3.2: Contador de Vocales

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Doky 🐕 está jugando con palabras y quiere contar cuántas vocales (a, e, i, o, u) hay en una palabra. Debe considerar mayúsculas y minúsculas.

**📝 Descripción:**
Implementa la función `count_vowels(text)` que retorna el número total de vocales en el texto (sin importar mayúsculas/minúsculas).

**Ejemplos:**
```python
print(count_vowels("Python"))        # 1
print(count_vowels("Programación"))  # 5
print(count_vowels("XYZ"))           # 0
```

**🧪 Tests:**
| Test | Input                          | Expected |
| ---- | ------------------------------ | -------- |
| 1    | `count_vowels("Python")`       | `1`      |
| 2    | `count_vowels("Programación")` | `5`      |
| 3    | `count_vowels("XYZ")`          | `0`      |
| 4    | `count_vowels("AEIOUaeiou")`   | `10`     |
| 5    | `count_vowels("")`             | `0`      |

**💻 Playground:**
```python
def count_vowels(text):
    # Tu código aquí
    return 0

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        count_vowels("Python") == 1,
        count_vowels("Programación") == 5,
        count_vowels("XYZ") == 0,
        count_vowels("AEIOUaeiou") == 10,
        count_vowels("") == 0
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Define vocales: `vowels = "aeiouAEIOU"`
* 🔹 Inicializa contador: `count = 0`
* 🔹 Recorre cada letra: `for char in text:`
* 🔹 Verifica: `if char in vowels: count += 1`

**🚀 Motivación:**  
¡Doky se divierte con las palabras! 🐕📝 Cada letra es una oportunidad de aprender. ¡Adelante! 🎯

---

## 4️⃣ Integration

### 🎮 Reto 4.1: Validador de Contraseña

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Amorosa 💖 crea un sistema de seguridad. Una contraseña es válida si: tiene al menos 8 caracteres, contiene al menos una letra mayúscula, una minúscula y un número.

**📝 Descripción:**
Implementa la función `is_valid_password(password)` que retorna `True` si cumple todos los requisitos, `False` si no.

**Ejemplos:**
```python
print(is_valid_password("Abc12345"))    # True
print(is_valid_password("abc12345"))    # False (sin mayúscula)
print(is_valid_password("ABC"))         # False (corta, sin minúscula ni número)
```

**🧪 Tests:**
| Test | Input                              | Expected |
| ---- | ---------------------------------- | -------- |
| 1    | `is_valid_password("Abc12345")`    | `True`   |
| 2    | `is_valid_password("abc12345")`    | `False`  |
| 3    | `is_valid_password("ABCDEFGH")`    | `False`  |
| 4    | `is_valid_password("Abcd")`        | `False`  |
| 5    | `is_valid_password("Pass123Word")` | `True`   |

**💻 Playground:**
```python
def is_valid_password(password):
    # Tu código aquí
    return False

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        is_valid_password("Abc12345") == True,
        is_valid_password("abc12345") == False,
        is_valid_password("ABCDEFGH") == False,
        is_valid_password("Abcd") == False,
        is_valid_password("Pass123Word") == True
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Verifica longitud: `if len(password) < 8: return False`
* 🔹 Usa flags: `has_upper = False`, `has_lower = False`, `has_digit = False`
* 🔹 Recorre cada carácter y verifica: `.isupper()`, `.islower()`, `.isdigit()`
* 🔹 Al final: `return has_upper and has_lower and has_digit`

**🚀 Motivación:**  
¡Amorosa protege los datos con tu código! 💖🔐 La seguridad empieza con validaciones sólidas. ¡Tú lo lograrás! 🛡️

---

### 💰 Reto 4.2: Calculadora de Descuento

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Fe 👨‍🍳 tiene una tienda online. Los descuentos son: 5% (compra ≥$100), 10% (≥$200), 15% (≥$300). Calcula el precio final después del descuento.

**📝 Descripción:**
Implementa la función `apply_discount(price)` que retorna el precio final con el descuento aplicado (redondeado a 2 decimales).

**Ejemplos:**
```python
print(apply_discount(50))     # 50.0 (sin descuento)
print(apply_discount(150))    # 142.5 (5% off)
print(apply_discount(250))    # 225.0 (10% off)
```

**🧪 Tests:**
| Test | Input                 | Expected |
| ---- | --------------------- | -------- |
| 1    | `apply_discount(50)`  | `50.0`   |
| 2    | `apply_discount(150)` | `142.5`  |
| 3    | `apply_discount(250)` | `225.0`  |
| 4    | `apply_discount(350)` | `297.5`  |
| 5    | `apply_discount(100)` | `95.0`   |

**💻 Playground:**
```python
def apply_discount(price):
    # Tu código aquí
    return 0.0

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        apply_discount(50) == 50.0,
        apply_discount(150) == 142.5,
        apply_discount(250) == 225.0,
        apply_discount(350) == 297.5,
        apply_discount(100) == 95.0
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Inicializa: `discount = 0`
* 🔹 Verifica de mayor a menor: `if price >= 300:`, luego `elif price >= 200:`, etc.
* 🔹 Calcula: `final_price = price - (price * discount / 100)`
* 🔹 Redondea: `round(final_price, 2)`

**🚀 Motivación:**  
¡Fe aumenta sus ventas gracias a ti! 👨‍🍳💰 Los descuentos bien calculados son magia pura. ¡A vender! 🛒✨

---

## 5️⃣ Conditionals II

### 🎫 Reto 5.1: Acceso a Evento

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Elliot ⚡ gestiona la entrada a un concierto. Se permite acceso si: (edad ≥ 18 Y tiene ticket) O es VIP (sin importar edad o ticket).

**📝 Descripción:**
Implementa la función `can_enter(age, has_ticket, is_vip)` que retorna `True` si puede entrar, `False` si no.

**Ejemplos:**
```python
print(can_enter(25, True, False))     # True
print(can_enter(16, True, False))     # False
print(can_enter(16, False, True))     # True
```

**🧪 Tests:**
| Test | Input                         | Expected |
| ---- | ----------------------------- | -------- |
| 1    | `can_enter(25, True, False)`  | `True`   |
| 2    | `can_enter(16, True, False)`  | `False`  |
| 3    | `can_enter(16, False, True)`  | `True`   |
| 4    | `can_enter(20, False, False)` | `False`  |
| 5    | `can_enter(30, True, True)`   | `True`   |

**💻 Playground:**
```python
def can_enter(age, has_ticket, is_vip):
    # Tu código aquí
    return False

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        can_enter(25, True, False) == True,
        can_enter(16, True, False) == False,
        can_enter(16, False, True) == True,
        can_enter(20, False, False) == False,
        can_enter(30, True, True) == True
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 VIP tiene acceso siempre: `if is_vip: return True`
* 🔹 Si no es VIP, necesita: edad ≥ 18 AND ticket
* 🔹 Una línea lo resuelve: `return is_vip or (age >= 18 and has_ticket)`
* 🔹 Operadores lógicos: `and`, `or` son tus aliados

**🚀 Motivación:**  
¡Elliot confía en tu lógica booleana! ⚡🎟️ Los operadores lógicos son el poder detrás de decisiones complejas. ¡Rock on! 🎸

---

### 🌡️ Reto 5.2: Estado del Clima

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Chocolate 🐕 monitorea el clima. Retorna 'peligro' si: temp > 35 O humidity < 20 O wind > 60. Si no, retorna 'seguro'.

**📝 Descripción:**
Implementa la función `weather_status(temp, humidity, wind)` que retorna 'peligro' o 'seguro' según las condiciones.

**Ejemplos:**
```python
print(weather_status(30, 50, 40))    # 'seguro'
print(weather_status(40, 50, 40))    # 'peligro'
print(weather_status(25, 15, 30))    # 'peligro'
```

**🧪 Tests:**
| Test | Input                        | Expected    |
| ---- | ---------------------------- | ----------- |
| 1    | `weather_status(30, 50, 40)` | `'seguro'`  |
| 2    | `weather_status(40, 50, 40)` | `'peligro'` |
| 3    | `weather_status(25, 15, 30)` | `'peligro'` |
| 4    | `weather_status(30, 50, 70)` | `'peligro'` |
| 5    | `weather_status(35, 20, 60)` | `'seguro'`  |

**💻 Playground:**
```python
def weather_status(temp, humidity, wind):
    # Tu código aquí
    return ''

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        weather_status(30, 50, 40) == 'seguro',
        weather_status(40, 50, 40) == 'peligro',
        weather_status(25, 15, 30) == 'peligro',
        weather_status(30, 50, 70) == 'peligro',
        weather_status(35, 20, 60) == 'seguro'
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Peligro si cualquier condición se cumple (usa `or`)
* 🔹 `if temp > 35 or humidity < 20 or wind > 60: return 'peligro'`
* 🔹 Nota: Los límites son estrictos (> y <, no >=  ni <=)
* 🔹 Todo lo demás: `return 'seguro'`

**🚀 Motivación:**  
¡Chocolate predice tormentas como un experto! 🐕🌪️ Tu código puede salvar el día. ¡Sigue adelante! 🌤️

---

## 6️⃣ Loops II

### 🔍 Reto 6.1: Buscar Número

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Fernanda 🧙‍♀️ busca un número en una lista. Debe retornar el índice donde lo encuentra (usa `break` al encontrarlo). Si no existe, retorna -1.

**📝 Descripción:**
Implementa la función `find_number(numbers, target)` que retorna el índice del target en la lista, o -1 si no existe.

**Ejemplos:**
```python
print(find_number([1,2,3,4,5], 3))      # 2
print(find_number([10,20,30], 25))      # -1
print(find_number([5,5,5], 5))          # 0 (primera ocurrencia)
```

**🧪 Tests:**
| Test | Input                         | Expected |
| ---- | ----------------------------- | -------- |
| 1    | `find_number([1,2,3,4,5], 3)` | `2`      |
| 2    | `find_number([10,20,30], 25)` | `-1`     |
| 3    | `find_number([5,5,5], 5)`     | `0`      |
| 4    | `find_number([7,8,9,10], 10)` | `3`      |
| 5    | `find_number([], 5)`          | `-1`     |

**💻 Playground:**
```python
def find_number(numbers, target):
    # Tu código aquí
    return -1

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        find_number([1,2,3,4,5], 3) == 2,
        find_number([10,20,30], 25) == -1,
        find_number([5,5,5], 5) == 0,
        find_number([7,8,9,10], 10) == 3,
        find_number([], 5) == -1
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Usa `enumerate()` para obtener índice y valor: `for i, num in enumerate(numbers):`
* 🔹 Cuando encuentres el valor: `if num == target: return i`
* 🔹 Usa `break` implícitamente con `return` (sale inmediatamente)
* 🔹 Si termina el loop sin encontrar: `return -1`

**🚀 Motivación:**  
¡Fernanda necesita tu búsqueda rápida! 🧙‍♀️🔍 `break` es tu herramienta para optimizar. ¡Encuéntralo! 🎯

---

### ⏭️ Reto 6.2: Filtrar Pares

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Mijael 🧑‍💻 quiere una lista solo con números pares de otra lista. Debe saltar (con `continue`) los impares.

**📝 Descripción:**
Implementa la función `filter_evens(numbers)` que retorna una nueva lista solo con los números pares del input.

**Ejemplos:**
```python
print(filter_evens([1,2,3,4,5,6]))      # [2, 4, 6]
print(filter_evens([1,3,5]))            # []
print(filter_evens([2,4,6]))            # [2, 4, 6]
```

**🧪 Tests:**
| Test | Input                            | Expected     |
| ---- | -------------------------------- | ------------ |
| 1    | `filter_evens([1,2,3,4,5,6])`    | `[2,4,6]`    |
| 2    | `filter_evens([1,3,5])`          | `[]`         |
| 3    | `filter_evens([2,4,6])`          | `[2,4,6]`    |
| 4    | `filter_evens([])`               | `[]`         |
| 5    | `filter_evens([10,15,20,25,30])` | `[10,20,30]` |

**💻 Playground:**
```python
def filter_evens(numbers):
    # Tu código aquí
    return []

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        filter_evens([1,2,3,4,5,6]) == [2,4,6],
        filter_evens([1,3,5]) == [],
        filter_evens([2,4,6]) == [2,4,6],
        filter_evens([]) == [],
        filter_evens([10,15,20,25,30]) == [10,20,30]
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Crea lista vacía: `result = []`
* 🔹 Recorre: `for num in numbers:`
* 🔹 Si es impar, salta: `if num % 2 != 0: continue`
* 🔹 Si llegaste aquí, es par: `result.append(num)`

**🚀 Motivación:**  
¡Mijael filtra datos como un pro! 🧑‍💻⚡ `continue` hace tu código más eficiente. ¡Domínalo! 🚀

---

## 7️⃣ Loops III

### 📇 Reto 7.1: Enumerar con Índices

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Doky 🐕 quiere mostrar una lista con índices: ["a", "b", "c"] → ["0: a", "1: b", "2: c"]. Usa `enumerate()`.

**📝 Descripción:**
Implementa la función `enumerate_list(items)` que retorna una lista de strings formateados como "índice: valor".

**Ejemplos:**
```python
print(enumerate_list(["a", "b", "c"]))           # ['0: a', '1: b', '2: c']
print(enumerate_list(["Python"]))                # ['0: Python']
print(enumerate_list([]))                        # []
```

**🧪 Tests:**
| Test | Input                                       | Expected                   |
| ---- | ------------------------------------------- | -------------------------- |
| 1    | `enumerate_list(["a", "b", "c"])`           | `['0: a', '1: b', '2: c']` |
| 2    | `enumerate_list(["Python"])`                | `['0: Python']`            |
| 3    | `enumerate_list([])`                        | `[]`                       |
| 4    | `enumerate_list(["x", "y"])`                | `['0: x', '1: y']`         |
| 5    | `len(enumerate_list(["a", "b", "c", "d"]))` | `4`                        |

**💻 Playground:**
```python
def enumerate_list(items):
    # Tu código aquí
    return []

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        enumerate_list(["a", "b", "c"]) == ['0: a', '1: b', '2: c'],
        enumerate_list(["Python"]) == ['0: Python'],
        enumerate_list([]) == [],
        enumerate_list(["x", "y"]) == ['0: x', '1: y'],
        len(enumerate_list(["a", "b", "c", "d"])) == 4
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Crea lista vacía: `result = []`
* 🔹 Usa `enumerate()`: `for i, item in enumerate(items):`
* 🔹 Formatea string: `f"{i}: {item}"`
* 🔹 Agrega a resultado: `result.append(formatted)`

**🚀 Motivación:**  
¡Doky organiza todo con índices! 🐕📇 `enumerate()` es magia pura para listas. ¡Úsala bien! ✨

---

### 🔢 Reto 7.2: Múltiplos con Step

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Amorosa 💖 quiere generar todos los múltiplos de `n` entre `start` y `end`. Por ejemplo, múltiplos de 3 entre 0 y 10: [0, 3, 6, 9].

**📝 Descripción:**
Implementa la función `get_multiples(n, start, end)` que retorna lista de múltiplos de n en el rango [start, end). Usa `range()` con step.

**Ejemplos:**
```python
print(get_multiples(3, 0, 10))      # [0, 3, 6, 9]
print(get_multiples(5, 0, 20))      # [0, 5, 10, 15]
print(get_multiples(7, 7, 30))      # [7, 14, 21, 28]
```

**🧪 Tests:**
| Test | Input                       | Expected                                  |
| ---- | --------------------------- | ----------------------------------------- |
| 1    | `get_multiples(3, 0, 10)`   | `[0, 3, 6, 9]`                            |
| 2    | `get_multiples(5, 0, 20)`   | `[0, 5, 10, 15]`                          |
| 3    | `get_multiples(7, 7, 30)`   | `[7, 14, 21, 28]`                         |
| 4    | `get_multiples(10, 0, 100)` | `[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]` |
| 5    | `get_multiples(4, 0, 5)`    | `[0, 4]`                                  |

**💻 Playground:**
```python
def get_multiples(n, start, end):
    # Tu código aquí
    return []

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        get_multiples(3, 0, 10) == [0, 3, 6, 9],
        get_multiples(5, 0, 20) == [0, 5, 10, 15],
        get_multiples(7, 7, 30) == [7, 14, 21, 28],
        get_multiples(10, 0, 100) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
        get_multiples(4, 0, 5) == [0, 4]
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 `range()` con 3 parámetros: `range(start, end, step)`
* 🔹 El step es `n` (el múltiplo que buscas)
* 🔹 Convierte a lista: `list(range(start, end, n))`
* 🔹 Una sola línea lo resuelve 🎯

**🚀 Motivación:**  
¡Amorosa genera secuencias como matemática! 💖🔢 `range()` con step es poderoso. ¡Aprovéchalo! 💪

---

## 8️⃣ Lists

### ➕ Reto 8.1: Agregar Únicos

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Fe 👨‍🍳 tiene una lista y quiere agregar elementos solo si no existen ya (evitar duplicados). Retorna la lista final.

**📝 Descripción:**
Implementa la función `add_unique(original, items_to_add)` que agrega elementos de `items_to_add` a `original` solo si no existen. Retorna la lista modificada.

**Ejemplos:**
```python
print(add_unique([1,2,3], [3,4,5]))      # [1, 2, 3, 4, 5]
print(add_unique([1,2], [1,2]))          # [1, 2]
print(add_unique([], [1,2,3]))           # [1, 2, 3]
```

**🧪 Tests:**
| Test | Input                          | Expected      |
| ---- | ------------------------------ | ------------- |
| 1    | `add_unique([1,2,3], [3,4,5])` | `[1,2,3,4,5]` |
| 2    | `add_unique([1,2], [1,2])`     | `[1,2]`       |
| 3    | `add_unique([], [1,2,3])`      | `[1,2,3]`     |
| 4    | `add_unique([5], [5,5,5])`     | `[5]`         |
| 5    | `add_unique([1,2,3], [])`      | `[1,2,3]`     |

**💻 Playground:**
```python
def add_unique(original, items_to_add):
    # Tu código aquí
    return []

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        add_unique([1,2,3], [3,4,5]) == [1,2,3,4,5],
        add_unique([1,2], [1,2]) == [1,2],
        add_unique([], [1,2,3]) == [1,2,3],
        add_unique([5], [5,5,5]) == [5],
        add_unique([1,2,3], []) == [1,2,3]
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Recorre `items_to_add`: `for item in items_to_add:`
* 🔹 Verifica si NO está: `if item not in original:`
* 🔹 Agrega: `original.append(item)`
* 🔹 Retorna la lista modificada: `return original`

**🚀 Motivación:**  
¡Fe evita duplicados como chef profesional! 👨‍🍳📋 Las listas son tu lienzo. ¡Píntalo bien! 🎨

---

### ✂️ Reto 8.2: Extraer Sección

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Elliot ⚡ quiere extraer una sección de una lista desde índice `start` hasta `end` (sin incluir `end`). Usa slicing.

**📝 Descripción:**
Implementa la función `extract_section(items, start, end)` que retorna una nueva lista con la sección [start:end].

**Ejemplos:**
```python
print(extract_section([1,2,3,4,5], 1, 4))      # [2, 3, 4]
print(extract_section([10,20,30], 0, 2))       # [10, 20]
print(extract_section([1,2,3], 2, 5))          # [3]
```

**🧪 Tests:**
| Test | Input                                | Expected    |
| ---- | ------------------------------------ | ----------- |
| 1    | `extract_section([1,2,3,4,5], 1, 4)` | `[2,3,4]`   |
| 2    | `extract_section([10,20,30], 0, 2)`  | `[10,20]`   |
| 3    | `extract_section([1,2,3], 2, 5)`     | `[3]`       |
| 4    | `extract_section([5,6,7,8], 0, 4)`   | `[5,6,7,8]` |
| 5    | `extract_section([1,2,3], 5, 10)`    | `[]`        |

**💻 Playground:**
```python
def extract_section(items, start, end):
    # Tu código aquí
    return []

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        extract_section([1,2,3,4,5], 1, 4) == [2,3,4],
        extract_section([10,20,30], 0, 2) == [10,20],
        extract_section([1,2,3], 2, 5) == [3],
        extract_section([5,6,7,8], 0, 4) == [5,6,7,8],
        extract_section([1,2,3], 5, 10) == []
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Usa slicing de Python: `items[start:end]`
* 🔹 El slicing automáticamente maneja índices fuera de rango
* 🔹 Es tan simple como: `return items[start:end]`
* 🔹 Una sola línea 🎯

**🚀 Motivación:**  
¡Elliot corta listas como un ninja! ⚡✂️ El slicing es tu superpoder de Python. ¡Úsalo! 🥷

---

## 9️⃣ Tuples

### 📦 Reto 9.1: Intercambiar Valores

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Chocolate 🐕 tiene dos variables `a` y `b` y quiere intercambiarlas. Usa desempaquetado de tuplas para hacerlo en una línea.

**📝 Descripción:**
Implementa la función `swap_values(a, b)` que retorna una tupla con los valores intercambiados.

**Ejemplos:**
```python
print(swap_values(10, 20))      # (20, 10)
print(swap_values(5, 15))       # (15, 5)
print(swap_values("a", "b"))    # ("b", "a")
```

**🧪 Tests:**
| Test | Input                     | Expected     |
| ---- | ------------------------- | ------------ |
| 1    | `swap_values(10, 20)`     | `(20, 10)`   |
| 2    | `swap_values(5, 15)`      | `(15, 5)`    |
| 3    | `swap_values("a", "b")`   | `("b", "a")` |
| 4    | `swap_values(100, 200)`   | `(200, 100)` |
| 5    | `type(swap_values(1, 2))` | `tuple`      |

**💻 Playground:**
```python
def swap_values(a, b):
    # Tu código aquí
    return ()

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        swap_values(10, 20) == (20, 10),
        swap_values(5, 15) == (15, 5),
        swap_values("a", "b") == ("b", "a"),
        swap_values(100, 200) == (200, 100),
        type(swap_values(1, 2)) == tuple
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Python permite intercambio directo: `b, a = a, b`
* 🔹 Retorna tupla: `return (b, a)`
* 🔹 O más simple: `return b, a` (Python crea la tupla automáticamente)
* 🔹 ¡Una línea magistral! 🎯

**🚀 Motivación:**  
¡Chocolate intercambia valores como mago! 🐕🎩 Las tuplas son elegancia en Python. ¡Brilla! ✨

---

### 📅 Reto 9.2: Desempaquetar Fecha

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Fernanda 🧙‍♀️ tiene una tupla con (día, mes, año) y quiere separar cada valor. Retorna un diccionario con las claves 'day', 'month', 'year'.

**📝 Descripción:**
Implementa la función `unpack_date(date_tuple)` que desempaqueta la tupla y retorna un diccionario.

**Ejemplos:**
```python
print(unpack_date((15, 8, 2008)))      # {'day': 15, 'month': 8, 'year': 2008}
print(unpack_date((1, 1, 2000)))       # {'day': 1, 'month': 1, 'year': 2000}
```

**🧪 Tests:**
| Test | Input                                 | Expected                                 |
| ---- | ------------------------------------- | ---------------------------------------- |
| 1    | `unpack_date((15, 8, 2008))`          | `{'day': 15, 'month': 8, 'year': 2008}`  |
| 2    | `unpack_date((1, 1, 2000))`           | `{'day': 1, 'month': 1, 'year': 2000}`   |
| 3    | `unpack_date((25, 12, 2025))`         | `{'day': 25, 'month': 12, 'year': 2025}` |
| 4    | `unpack_date((10, 5, 1990))['month']` | `5`                                      |
| 5    | `type(unpack_date((1, 1, 2000)))`     | `dict`                                   |

**💻 Playground:**
```python
def unpack_date(date_tuple):
    # Tu código aquí
    return {}

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        unpack_date((15, 8, 2008)) == {'day': 15, 'month': 8, 'year': 2008},
        unpack_date((1, 1, 2000)) == {'day': 1, 'month': 1, 'year': 2000},
        unpack_date((25, 12, 2025)) == {'day': 25, 'month': 12, 'year': 2025},
        unpack_date((10, 5, 1990))['month'] == 5,
        type(unpack_date((1, 1, 2000))) == dict
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Desempaqueta: `day, month, year = date_tuple`
* 🔹 Crea diccionario: `return {'day': day, 'month': month, 'year': year}`
* 🔹 O en una línea: `d, m, y = date_tuple; return {'day': d, 'month': m, 'year': y}`
* 🔹 El orden importa: día primero, año último

**🚀 Motivación:**  
¡Fernanda organiza fechas como experta! 🧙‍♀️📅 Tuplas + diccionarios = combo perfecto. ¡Domínalo! 🎯

---

## 🔟 Sets

### 🎯 Reto 10.1: Elementos Únicos

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Mijael 🧑‍💻 tiene una lista con duplicados [1,2,2,3,4,3,5] y quiere solo los valores únicos. Usa set y retorna una lista ordenada.

**📝 Descripción:**
Implementa la función `get_unique(items)` que retorna una lista ordenada con solo valores únicos.

**Ejemplos:**
```python
print(get_unique([1,2,2,3,4,3,5]))      # [1, 2, 3, 4, 5]
print(get_unique([1,1,1]))              # [1]
print(get_unique([]))                   # []
```

**🧪 Tests:**
| Test | Input                               | Expected      |
| ---- | ----------------------------------- | ------------- |
| 1    | `get_unique([1,2,2,3,4,3,5])`       | `[1,2,3,4,5]` |
| 2    | `get_unique([1,1,1])`               | `[1]`         |
| 3    | `get_unique([])`                    | `[]`          |
| 4    | `get_unique([5,4,3,2,1,1,2,3,4,5])` | `[1,2,3,4,5]` |
| 5    | `type(get_unique([1,2,3]))`         | `list`        |

**💻 Playground:**
```python
def get_unique(items):
    # Tu código aquí
    return []

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        get_unique([1,2,2,3,4,3,5]) == [1,2,3,4,5],
        get_unique([1,1,1]) == [1],
        get_unique([]) == [],
        get_unique([5,4,3,2,1,1,2,3,4,5]) == [1,2,3,4,5],
        type(get_unique([1,2,3])) == list
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Convierte a set para eliminar duplicados: `unique_set = set(items)`
* 🔹 Ordena y convierte a lista: `sorted(list(unique_set))`
* 🔹 O más simple: `return sorted(list(set(items)))`
* 🔹 Una línea poderosa 🎯

**🚀 Motivación:**  
¡Mijael limpia datos como profesional! 🧑‍💻✨ Los sets son perfectos para eliminar duplicados. ¡Úsalos! 🧹

---

### 🤝 Reto 10.2: Intersección de Listas

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Doky 🐕 y Chocolate 🐕 tienen listas de juguetes favoritos. Quieren saber cuáles tienen en común. Usa sets e intersección.

**📝 Descripción:**
Implementa la función `common_items(list1, list2)` que retorna una lista ordenada con elementos que están en ambas listas.

**Ejemplos:**
```python
print(common_items([1,2,3,4], [3,4,5,6]))          # [3, 4]
print(common_items([1,2], [3,4]))                  # []
print(common_items(['a','b','c'], ['b','c','d']))  # ['b', 'c']
```

**🧪 Tests:**
| Test | Input                                        | Expected    |
| ---- | -------------------------------------------- | ----------- |
| 1    | `common_items([1,2,3,4], [3,4,5,6])`         | `[3,4]`     |
| 2    | `common_items([1,2], [3,4])`                 | `[]`        |
| 3    | `common_items(['a','b','c'], ['b','c','d'])` | `['b','c']` |
| 4    | `common_items([5,5,5], [5])`                 | `[5]`       |
| 5    | `common_items([], [1,2,3])`                  | `[]`        |

**💻 Playground:**
```python
def common_items(list1, list2):
    # Tu código aquí
    return []

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        common_items([1,2,3,4], [3,4,5,6]) == [3,4],
        common_items([1,2], [3,4]) == [],
        common_items(['a','b','c'], ['b','c','d']) == ['b','c'],
        common_items([5,5,5], [5]) == [5],
        common_items([], [1,2,3]) == []
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

---

## 1️⃣1️⃣ Dictionaries

### 👤 Reto 11.1: Contar Ocurrencias

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Amorosa 💖 tiene una lista de frutas y quiere contar cuántas veces aparece cada una. Retorna un diccionario {fruta: cantidad}.

**📝 Descripción:**
Implementa la función `count_items(items)` que retorna un diccionario con la frecuencia de cada elemento.

**Ejemplos:**
```python
print(count_items(['a','b','a','c','b','a']))      # {'a': 3, 'b': 2, 'c': 1}
print(count_items([1,1,2,2,2,3]))                  # {1: 2, 2: 3, 3: 1}
print(count_items([]))                             # {}
```

**🧪 Tests:**
| Test | Input                                    | Expected                   |
| ---- | ---------------------------------------- | -------------------------- |
| 1    | `count_items(['a','b','a','c','b','a'])` | `{'a': 3, 'b': 2, 'c': 1}` |
| 2    | `count_items([1,1,2,2,2,3])`             | `{1: 2, 2: 3, 3: 1}`       |
| 3    | `count_items([])`                        | `{}`                       |
| 4    | `count_items(['x'])`                     | `{'x': 1}`                 |
| 5    | `count_items(['z','z'])`                 | `{'z': 2}`                 |

**💻 Playground:**
```python
def count_items(items):
    # Tu código aquí
    return {}

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        count_items(['a','b','a','c','b','a']) == {'a': 3, 'b': 2, 'c': 1},
        count_items([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1},
        count_items([]) == {},
        count_items(['x']) == {'x': 1},
        count_items(['z','z']) == {'z': 2}
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Crea diccionario vacío: `counter = {}`
* 🔹 Recorre items: `for item in items:`
* 🔹 Si existe, incrementa: `if item in counter: counter[item] += 1`
* 🔹 Si no existe, inicializa: `else: counter[item] = 1`

**🚀 Motivación:**  
¡Amorosa cuenta frutas como experta! 💖🍎 Los diccionarios son perfectos para frecuencias. ¡Cuenta todo! 📊

---

### 🏆 Reto 11.2: Encontrar Máximo

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Fe 👨‍🍳 tiene un diccionario de jugadores con sus puntos: {'Elliot': 100, 'Fe': 150, 'Mijael': 120}. Quiere el nombre del jugador con más puntos.

**📝 Descripción:**
Implementa la función `get_max_player(scores)` que retorna el nombre del jugador con la puntuación más alta. Si está vacío, retorna None.

**Ejemplos:**
```python
print(get_max_player({'Elliot': 100, 'Fe': 150, 'Mijael': 120}))  # 'Fe'
print(get_max_player({'A': 50, 'B': 75}))                         # 'B'
print(get_max_player({}))                                         # None
```

**🧪 Tests:**
| Test | Input                                                       | Expected |
| ---- | ----------------------------------------------------------- | -------- |
| 1    | `get_max_player({'Elliot': 100, 'Fe': 150, 'Mijael': 120})` | `'Fe'`   |
| 2    | `get_max_player({'A': 50, 'B': 75})`                        | `'B'`    |
| 3    | `get_max_player({})`                                        | `None`   |
| 4    | `get_max_player({'X': 100})`                                | `'X'`    |
| 5    | `get_max_player({'P1': 200, 'P2': 200}) in ['P1', 'P2']`    | `True`   |

**💻 Playground:**
```python
def get_max_player(scores):
    # Tu código aquí
    return None

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        get_max_player({'Elliot': 100, 'Fe': 150, 'Mijael': 120}) == 'Fe',
        get_max_player({'A': 50, 'B': 75}) == 'B',
        get_max_player({}) == None,
        get_max_player({'X': 100}) == 'X',
        get_max_player({'P1': 200, 'P2': 200}) in ['P1', 'P2']
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Valida vacío: `if not scores: return None`
* 🔹 Usa `max()` con key: `max(scores, key=scores.get)`
* 🔹 Esto retorna la clave con el valor máximo
* 🔹 Una línea (con validación): 2 líneas total 🎯

**🚀 Motivación:**  
¡Fe encuentra campeones con tu ayuda! 👨‍🍳🏆 Los diccionarios + max() = combinación ganadora. ¡Brilla! 🌟

---

## 1️⃣2️⃣ Functions

### 🧮 Reto 12.1: Calculadora Básica

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Elliot ⚡ necesita una función calculadora que recibe dos números y una operación ('+', '-', '*', '/') y retorna el resultado. Si la operación es inválida, retorna None.

**📝 Descripción:**
Implementa la función `calculate(a, b, operation)` que realiza la operación matemática y retorna el resultado (float para división).

**Ejemplos:**
```python
print(calculate(10, 5, '+'))      # 15
print(calculate(10, 5, '-'))      # 5
print(calculate(10, 5, '*'))      # 50
print(calculate(10, 5, '/'))      # 2.0
```

**🧪 Tests:**
| Test | Input                   | Expected |
| ---- | ----------------------- | -------- |
| 1    | `calculate(10, 5, '+')` | `15`     |
| 2    | `calculate(10, 5, '-')` | `5`      |
| 3    | `calculate(10, 5, '*')` | `50`     |
| 4    | `calculate(10, 5, '/')` | `2.0`    |
| 5    | `calculate(10, 5, '%')` | `None`   |

**💻 Playground:**
```python
def calculate(a, b, operation):
    # Tu código aquí
    return None

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        calculate(10, 5, '+') == 15,
        calculate(10, 5, '-') == 5,
        calculate(10, 5, '*') == 50,
        calculate(10, 5, '/') == 2.0,
        calculate(10, 5, '%') == None
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Usa `if-elif` para cada operación: `if operation == '+':`
* 🔹 Retorna resultado directo: `return a + b`
* 🔹 División retorna float automáticamente
* 🔹 Si ninguna coincide: `return None` al final

**🚀 Motivación:**  
¡Elliot calcula con tu función! ⚡🔢 Las funciones son bloques de código reutilizables. ¡Crea las mejores! 🛠️

---

### 📊 Reto 12.2: Estadísticas de Lista

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Chocolate 🐕 tiene una lista de números y quiere calcular: promedio, máximo y mínimo. Retorna un diccionario con estas 3 estadísticas.

**📝 Descripción:**
Implementa la función `get_stats(numbers)` que retorna {'avg': promedio, 'max': máximo, 'min': mínimo}. Si la lista está vacía, retorna None.

**Ejemplos:**
```python
print(get_stats([1,2,3,4,5]))      # {'avg': 3.0, 'max': 5, 'min': 1}
print(get_stats([10]))             # {'avg': 10.0, 'max': 10, 'min': 10}
print(get_stats([]))               # None
```

**🧪 Tests:**
| Test | Input                         | Expected                              |
| ---- | ----------------------------- | ------------------------------------- |
| 1    | `get_stats([1,2,3,4,5])`      | `{'avg': 3.0, 'max': 5, 'min': 1}`    |
| 2    | `get_stats([10])`             | `{'avg': 10.0, 'max': 10, 'min': 10}` |
| 3    | `get_stats([])`               | `None`                                |
| 4    | `get_stats([5,10,15])['avg']` | `10.0`                                |
| 5    | `get_stats([2,8,5])['max']`   | `8`                                   |

**💻 Playground:**
```python
def get_stats(numbers):
    # Tu código aquí
    return None

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        get_stats([1,2,3,4,5]) == {'avg': 3.0, 'max': 5, 'min': 1},
        get_stats([10]) == {'avg': 10.0, 'max': 10, 'min': 10},
        get_stats([]) == None,
        get_stats([5,10,15])['avg'] == 10.0 if get_stats([5,10,15]) else False,
        get_stats([2,8,5])['max'] == 8 if get_stats([2,8,5]) else False
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Valida vacío: `if not numbers: return None`
* 🔹 Calcula promedio: `avg = sum(numbers) / len(numbers)`
* 🔹 Usa funciones built-in: `max(numbers)`, `min(numbers)`
* 🔹 Retorna diccionario: `return {'avg': avg, 'max': max(numbers), 'min': min(numbers)}`

**🚀 Motivación:**  
¡Chocolate analiza datos como científico! 🐕📊 Las estadísticas son el lenguaje de los datos. ¡Habla ese lenguaje! 📈

---

## 1️⃣3️⃣ Date & Time

### 📅 Reto 13.1: Días Entre Fechas

**Dificultad:** ⭐⭐⭐ Difícil  
**Puntos:** 5 tests

**📖 Historia:**
Fernanda 🧙‍♀️ quiere saber cuántos días hay entre dos fechas. Recibe dos strings en formato 'YYYY-MM-DD' y retorna la diferencia en días (positiva).

**📝 Descripción:**
Implementa la función `days_between(date1, date2)` que calcula los días de diferencia entre dos fechas. Usa el módulo `datetime`.

**Ejemplos:**
```python
print(days_between('2026-01-01', '2026-01-10'))      # 9
print(days_between('2025-12-25', '2026-01-01'))      # 7
print(days_between('2026-01-15', '2026-01-15'))      # 0
```

**🧪 Tests:**
| Test | Input                                      | Expected |
| ---- | ------------------------------------------ | -------- |
| 1    | `days_between('2026-01-01', '2026-01-10')` | `9`      |
| 2    | `days_between('2025-12-25', '2026-01-01')` | `7`      |
| 3    | `days_between('2026-01-15', '2026-01-15')` | `0`      |
| 4    | `days_between('2026-01-01', '2026-02-01')` | `31`     |
| 5    | `days_between('2026-01-10', '2026-01-01')` | `9`      |

**💻 Playground:**
```python
from datetime import datetime

def days_between(date1, date2):
    # Tu código aquí
    return 0

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        days_between('2026-01-01', '2026-01-10') == 9,
        days_between('2025-12-25', '2026-01-01') == 7,
        days_between('2026-01-15', '2026-01-15') == 0,
        days_between('2026-01-01', '2026-02-01') == 31,
        days_between('2026-01-10', '2026-01-01') == 9
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Convierte strings a fechas: `d1 = datetime.strptime(date1, '%Y-%m-%d')`
* 🔹 Resta fechas: `diff = d2 - d1` (o `d1 - d2`)
* 🔹 Obtén días: `diff.days`
* 🔹 Usa `abs()` para resultado positivo: `return abs(diff.days)`

**🚀 Motivación:**  
¡Fernanda viaja en el tiempo con fechas! 🧙‍♀️📅 El módulo datetime es tu máquina del tiempo. ¡Úsala sabiamente! ⏰✨

---

### ⏰ Reto 13.2: Formatear Fecha

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Mijael 🧑‍💻 tiene una fecha en formato 'YYYY-MM-DD' y quiere convertirla a formato legible 'DD/MM/YYYY'.

**📝 Descripción:**
Implementa la función `format_date(date_str)` que convierte de formato ISO (YYYY-MM-DD) a formato DD/MM/YYYY.

**Ejemplos:**
```python
print(format_date('2026-01-15'))      # '15/01/2026'
print(format_date('2025-12-25'))      # '25/12/2025'
print(format_date('2026-03-08'))      # '08/03/2026'
```

**🧪 Tests:**
| Test | Input                       | Expected       |
| ---- | --------------------------- | -------------- |
| 1    | `format_date('2026-01-15')` | `'15/01/2026'` |
| 2    | `format_date('2025-12-25')` | `'25/12/2025'` |
| 3    | `format_date('2026-03-08')` | `'08/03/2026'` |
| 4    | `format_date('2026-10-01')` | `'01/10/2026'` |
| 5    | `format_date('2000-01-01')` | `'01/01/2000'` |

**💻 Playground:**
```python
from datetime import datetime

def format_date(date_str):
    # Tu código aquí
    return ''

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        format_date('2026-01-15') == '15/01/2026',
        format_date('2025-12-25') == '25/12/2025',
        format_date('2026-03-08') == '08/03/2026',
        format_date('2026-10-01') == '01/10/2026',
        format_date('2000-01-01') == '01/01/2000'
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Parsea la fecha: `date = datetime.strptime(date_str, '%Y-%m-%d')`
* 🔹 Formatea al nuevo formato: `return date.strftime('%d/%m/%Y')`
* 🔹 `%d` = día, `%m` = mes, `%Y` = año completo
* 🔹 Dos líneas, solución elegante 🎯

**🚀 Motivación:**  
¡Mijael formatea fechas como diseñador! 🧑‍💻🎨 strftime/strptime son tus pinceles para fechas. ¡Pinta! 🖌️

---

## 1️⃣4️⃣ Modules

### 🎲 Reto 14.1: Dado Aleatorio

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Doky 🐕 está jugando un juego de mesa y necesita simular el lanzamiento de un dado de 6 caras. Retorna un número aleatorio entre 1 y 6.

**📝 Descripción:**
Implementa la función `roll_dice()` que retorna un número aleatorio entre 1 y 6 usando el módulo `random`.

**Ejemplos:**
```python
print(roll_dice())      # 4 (aleatorio)
print(roll_dice())      # 2 (aleatorio)
print(roll_dice())      # 6 (aleatorio)
```

**🧪 Tests:**
| Test | Input                                             | Expected |
| ---- | ------------------------------------------------- | -------- |
| 1    | `1 <= roll_dice() <= 6`                           | `True`   |
| 2    | `type(roll_dice())`                               | `int`    |
| 3    | `len(set([roll_dice() for _ in range(100)])) > 1` | `True`   |
| 4    | `all(1 <= roll_dice() <= 6 for _ in range(20))`   | `True`   |
| 5    | `max([roll_dice() for _ in range(50)]) <= 6`      | `True`   |

**💻 Playground:**
```python
import random

def roll_dice():
    # Tu código aquí
    return 0

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        1 <= roll_dice() <= 6,
        type(roll_dice()) == int,
        len(set([roll_dice() for _ in range(100)])) > 1,
        all(1 <= roll_dice() <= 6 for _ in range(20)),
        max([roll_dice() for _ in range(50)]) <= 6
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Usa `random.randint(a, b)`: incluye ambos extremos
* 🔹 `return random.randint(1, 6)`
* 🔹 ¡Una línea mágica! 🎲
* 🔹 Cada llamada da resultado diferente (probablemente)

**🚀 Motivación:**  
¡Doky juega con dados virtuales! 🐕🎲 El módulo random trae azar a tu código. ¡Lánzalo! 🎯

---

### 🔢 Reto 14.2: Raíz Cuadrada

**Dificultad:** ⭐ Fácil  
**Puntos:** 5 tests

**📖 Historia:**
Amorosa 💖 está resolviendo problemas matemáticos y necesita calcular la raíz cuadrada de números. Usa el módulo `math`.

**📝 Descripción:**
Implementa la función `square_root(n)` que retorna la raíz cuadrada del número usando `math.sqrt()`. Redondea a 2 decimales.

**Ejemplos:**
```python
print(square_root(144))      # 12.0
print(square_root(25))       # 5.0
print(square_root(2))        # 1.41
```

**🧪 Tests:**
| Test | Input              | Expected |
| ---- | ------------------ | -------- |
| 1    | `square_root(144)` | `12.0`   |
| 2    | `square_root(25)`  | `5.0`    |
| 3    | `square_root(2)`   | `1.41`   |
| 4    | `square_root(100)` | `10.0`   |
| 5    | `square_root(9)`   | `3.0`    |

**💻 Playground:**
```python
import math

def square_root(n):
    # Tu código aquí
    return 0.0

# ✓ Test Runner (solo para verificación)
def run_tests():
    tests = [
        square_root(144) == 12.0,
        square_root(25) == 5.0,
        square_root(2) == 1.41,
        square_root(100) == 10.0,
        square_root(9) == 3.0
    ]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Calcula raíz: `result = math.sqrt(n)`
* 🔹 Redondea: `return round(result, 2)`
* 🔹 O en una línea: `return round(math.sqrt(n), 2)`
* 🔹 `math` es tu calculadora científica 🧮

**🚀 Motivación:**  
¡Amorosa resuelve ecuaciones con estilo! 💖🔢 El módulo math es poder matemático puro. ¡Úsalo! 📐

---

## 1️⃣5️⃣ Files

### 📝 Reto 15.1: Escribir Lista

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Fe 👨‍🍳 tiene una lista de ingredientes ['sal', 'pimienta', 'azúcar'] y quiere guardarla en un archivo, una por línea. Retorna True si se guardó correctamente.

**📝 Descripción:**
Implementa la función `write_list_to_file(items, filename)` que escribe cada elemento de la lista en una línea del archivo. Retorna True al finalizar.

**Ejemplos:**
```python
print(write_list_to_file(['a', 'b', 'c'], 'test.txt'))      # True
# Archivo test.txt contiene:
# a
# b
# c
```

**🧪 Tests:**
| Test | Input                                              | Expected      |
| ---- | -------------------------------------------------- | ------------- |
| 1    | `write_list_to_file(['a', 'b', 'c'], 'test1.txt')` | `True`        |
| 2    | `write_list_to_file(['x'], 'test2.txt')`           | `True`        |
| 3    | `write_list_to_file([], 'test3.txt')`              | `True`        |
| 4    | `Verificar contenido del archivo test1.txt`        | `'a\nb\nc\n'` |
| 5    | `write_list_to_file(['1', '2'], 'test4.txt')`      | `True`        |

**💻 Playground:**
```python
def write_list_to_file(items, filename):
    # Tu código aquí
    return False

# ✓ Test Runner (solo para verificación)
def run_tests():
    test1 = write_list_to_file(['a', 'b', 'c'], 'test1.txt') == True
    test2 = write_list_to_file(['x'], 'test2.txt') == True
    test3 = write_list_to_file([], 'test3.txt') == True
    
    # Verificar contenido
    try:
        with open('test1.txt', 'r') as f:
            test4 = f.read() == 'a\nb\nc\n'
    except:
        test4 = False
    
    test5 = write_list_to_file(['1', '2'], 'test4.txt') == True
    
    tests = [test1, test2, test3, test4, test5]
    for i, result in enumerate(tests, 1):
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Abre archivo en modo escritura: `with open(filename, 'w') as f:`
* 🔹 Escribe cada item con salto de línea: `f.write(item + '\n')`
* 🔹 O usa un loop: `for item in items:`
* 🔹 Retorna True al final

**🚀 Motivación:**  
¡Fe guarda recetas para siempre! 👨‍🍳📝 Los archivos son memoria persistente. ¡Escribe historia! 📜

---

### 📖 Reto 15.2: Contar Líneas

**Dificultad:** ⭐⭐ Medio  
**Puntos:** 5 tests

**📖 Historia:**
Elliot ⚡ tiene un archivo de texto y quiere saber cuántas líneas contiene. Lee el archivo y retorna el número de líneas.

**📝 Descripción:**
Implementa la función `count_lines(filename)` que lee un archivo y retorna el número de líneas. Si el archivo no existe, retorna 0.

**Ejemplos:**
```python
# Archivo con 3 líneas
print(count_lines('file.txt'))      # 3
# Archivo vacío
print(count_lines('empty.txt'))     # 0
```

**🧪 Tests:**
| Test | Input                                  | Expected |
| ---- | -------------------------------------- | -------- |
| 1    | `count_lines('test_3lines.txt')`       | `3`      |
| 2    | `count_lines('test_empty.txt')`        | `0`      |
| 3    | `count_lines('nonexistent.txt')`       | `0`      |
| 4    | `count_lines('test_1line.txt')`        | `1`      |
| 5    | `type(count_lines('test_3lines.txt'))` | `int`    |

**💻 Playground:**
```python
def count_lines(filename):
    # Tu código aquí
    return 0

# ✓ Test Runner (solo para verificación)
def run_tests():
    # Crear archivos de prueba
    with open('test_3lines.txt', 'w') as f:
        f.write('line1\nline2\nline3\n')
    with open('test_empty.txt', 'w') as f:
        f.write('')
    with open('test_1line.txt', 'w') as f:
        f.write('single line')
    
    tests = [
        count_lines('test_3lines.txt')
        print(f"Test {i}: {'✅' if result else '❌'}")

run_tests()
```

**💡 Tips:**
* 🔹 Calcula: `propina = bill * (tip_percent / 100)`
* 🔹 Suma: `total = bill + propina`
* 🔹 Retorna el total como tipo `float`
* 🔹 Puedes resolver en 1 línea: `return bill + (bill * tip_percent / 100)`

**🚀 Motivación:**  
¡Fe necesita tu ayuda en el restaurante! 👨‍🍳 Este reto es tu calentamiento perfecto. ¡Tú puedes! 💪✨
