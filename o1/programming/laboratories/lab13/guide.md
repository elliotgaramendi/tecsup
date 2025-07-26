# **🔧 o13 Funciones 🐍✨**

Las funciones son bloques de código reutilizables que nos permiten organizar nuestros programas de manera eficiente y modular. Son como pequeñas máquinas que reciben datos (parámetros), procesan información y devuelven resultados. ¡Imagina tener chanchitos especializados que realizan tareas específicas cuando los necesites! 🐷⚙️ Las funciones son fundamentales para crear código limpio, mantenible y libre de repetición.

## 🎯 Objetivos

* 📦 **Crear funciones básicas** definiendo bloques de código reutilizables con def
* 🎯 **Manejar parámetros y argumentos** pasando datos de entrada a las funciones
* 🔄 **Usar valores de retorno** devolviendo resultados procesados con return
* 📝 **Implementar documentación** escribiendo docstrings claros y descriptivos
* 🛠️ **Aplicar buenas prácticas** creando funciones modulares y específicas

---

## 🔍 Visualizando el Concepto

```
🔧 ANATOMÍA DE UNA FUNCIÓN

    def nombre_funcion(parametro1, parametro2):
        """📝 Docstring explicativo"""
        # Procesamiento
        resultado = parametro1 + parametro2
        return resultado
        
    ↑     ↑           ↑            ↑         ↑
  def  nombre    parámetros   docstring   return

🛠️ COMPONENTES ESENCIALES:
┌─────────────────────────────────┐
│ def → palabra clave             │
│ nombre() → identificador único  │
│ parámetros → datos de entrada   │
│ docstring → documentación       │
│ return → valor de salida        │
└─────────────────────────────────┘

⚡ OPERACIONES BÁSICAS:
┌─────────────────────────────────┐
│ definir → def nombre():         │
│ llamar → nombre(argumentos)     │
│ documentar → """docstring"""    │
│ devolver → return valor         │
│ validar → if conditions         │
└─────────────────────────────────┘

🚀 CASOS DE USO COMUNES:
┌──────────────────────────────────┐
│ • Cálculos matemáticos           │
│ • Validación de datos            │
│ • Formateo de información        │
│ • Procesamiento de listas        │
│ • Operaciones repetitivas        │
└──────────────────────────────────┘
```

---

### o13.1 🧮 **Calculadora de Área** 📐✨

---

#### ❓ Problema 🤔

Implementa una función `calculate_area(shape, **dimensions)` que calcule el área de diferentes figuras geométricas para ayudar a Elliot con sus proyectos de construcción de casitas para chanchitos. 🏠🐷

---

#### 📜 Descripción 📖

* **Función**: `calculate_area(shape, **dimensions) → float` 🛠️
* **Entradas**:
  * `shape`: string con tipo de figura ("rectangle", "circle", "triangle") 🎯
  * `**dimensions`: dimensiones específicas según la figura 📏
* **Salidas**:
  * **float**: área calculada de la figura geométrica 📊
* **Casos especiales**:
  * "rectangle" → requiere width y height ⚠️
  * "circle" → requiere radius 🔍
  * "triangle" → requiere base y height ⚠️
* **Restricciones**:
  * Figura no soportada → retornar 0.0 🔗
  * Dimensiones negativas → retornar 0.0 ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o13.1.1**: Área de rectángulo
   * Entrada: `("rectangle", width=5, height=3)`
   * Espera: `15.0` ✅

2. **o13.1.2**: Área de círculo
   * Entrada: `("circle", radius=2)`
   * Espera: `12.566370614359172` (π × 2²) ✅

3. **o13.1.3**: Área de triángulo
   * Entrada: `("triangle", base=4, height=6)`
   * Espera: `12.0` ✅

4. **o13.1.4**: Verificación de tipos
   * Entrada: `("rectangle", width=2, height=3)`
   * Verificar: resultado es float ✅

5. **o13.1.5**: Figura no soportada
   * Entrada: `("pentagon", side=5)`
   * Espera: `0.0` ✅

---

#### 💻 Código Base 🖥️

```python
import math

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def calculate_area(shape, **dimensions):
    """🧮 Calculate area of geometric shapes.
    Returns area as float."""
    # Your solution here 🛠️
    pass

def test_o13_1():
    # o13.1.1: Área de rectángulo
    result = calculate_area("rectangle", width=5, height=3)
    record_test("o13.1.1 rectángulo", result == 15.0)
    
    # o13.1.2: Área de círculo
    result = calculate_area("circle", radius=2)
    expected = math.pi * 4  # π × 2²
    record_test("o13.1.2 círculo", abs(result - expected) < 0.001)
    
    # o13.1.3: Área de triángulo
    result = calculate_area("triangle", base=4, height=6)
    record_test("o13.1.3 triángulo", result == 12.0)
    
    # o13.1.4: Verificación de tipos
    result = calculate_area("rectangle", width=2, height=3)
    record_test("o13.1.4 retorna float", isinstance(result, float))
    
    # o13.1.5: Figura no soportada
    result = calculate_area("pentagon", side=5)
    record_test("o13.1.5 no soportada", result == 0.0)

# 🚀 Run tests
test_o13_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Usa `**dimensions` para recibir argumentos con nombre variable 🔍
* Para rectángulo: `width * height`, círculo: `math.pi * radius**2` 📊
* Para triángulo: `(base * height) / 2` ✨
* Verifica que las dimensiones requeridas estén en `dimensions` antes de calcular 🚀

---

#### 🧠 Motivación 💭

* **Aplicaciones CAD**: cálculos automáticos en programas de diseño 🏗️
* **Arquitectura**: estimación de materiales basada en áreas 📐
* **Videojuegos**: detección de colisiones y cálculos de física 🎮

---

### o13.2 🔒 **Validador de contraseñas** 🛡️🎯

---

#### ❓ Problema 🤔

Implementa una función `validate_password(password, min_length=8, require_special=True)` que valide si una contraseña cumple con los criterios de seguridad para proteger las cuentas de las ratitas del sistema. 🐭🔐

---

#### 📜 Descripción 📖

* **Función**: `validate_password(password, min_length=8, require_special=True) → dict` 🛠️
* **Entradas**:
  * `password`: string con la contraseña a validar 🎯
  * `min_length`: int longitud mínima (default 8) 📏
  * `require_special`: bool si requiere caracteres especiales (default True) 🔍
* **Salidas**:
  * **dict**: resultado con is_valid (bool) y errors (list) 📊
* **Casos especiales**:
  * Debe contener mayúscula, minúscula y número ⚠️
  * Si require_special=True → debe tener !@#$%^&* 🔍
* **Restricciones**:
  * min_length debe ser positivo 🔗
  * password no puede ser None o vacío ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o13.2.1**: Contraseña válida completa
   * Entrada: `("Password123!", 8, True)`
   * Espera: `{"is_valid": True, "errors": []}` ✅

2. **o13.2.2**: Muy corta
   * Entrada: `("Pass1!", 8, True)`
   * Espera: `{"is_valid": False, "errors": ["Too short"]}` ✅

3. **o13.2.3**: Sin caracteres especiales
   * Entrada: `("Password123", 8, True)`
   * Espera: `{"is_valid": False, "errors": ["Missing special character"]}` ✅

4. **o13.2.4**: Verificación de tipos
   * Entrada: `("ValidPass1!", 8, True)`
   * Verificar: resultado es dict ✅

5. **o13.2.5**: Sin requerir especiales
   * Entrada: `("Password123", 8, False)`
   * Espera: `{"is_valid": True, "errors": []}` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def validate_password(password, min_length=8, require_special=True):
    """🔒 Validate password strength and security requirements.
    Returns dict with validation result and errors."""
    # Your solution here 🛠️
    pass

def test_o13_2():
    # o13.2.1: Contraseña válida completa
    result = validate_password("Password123!", 8, True)
    expected = {"is_valid": True, "errors": []}
    record_test("o13.2.1 válida completa", result == expected)
    
    # o13.2.2: Muy corta
    result = validate_password("Pass1!", 8, True)
    record_test("o13.2.2 muy corta", not result["is_valid"] and "Too short" in result["errors"])
    
    # o13.2.3: Sin caracteres especiales
    result = validate_password("Password123", 8, True)
    record_test("o13.2.3 sin especiales", not result["is_valid"] and "Missing special character" in result["errors"])
    
    # o13.2.4: Verificación de tipos
    result = validate_password("ValidPass1!", 8, True)
    record_test("o13.2.4 retorna dict", isinstance(result, dict))
    
    # o13.2.5: Sin requerir especiales
    result = validate_password("Password123", 8, False)
    record_test("o13.2.5 sin requerir especiales", result["is_valid"])

# 🚀 Run tests
test_o13_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Inicializa `errors = []` y ve agregando errores encontrados 🔍
* Usa `any(c.isupper() for c in password)` para verificar mayúsculas 📊
* Para caracteres especiales: `any(c in "!@#$%^&*" for c in password)` ✨
* Retorna `{"is_valid": len(errors) == 0, "errors": errors}` 🚀

---

#### 🧠 Motivación 💭

* **Seguridad web**: validación de contraseñas en aplicaciones 🔐
* **Sistemas empresariales**: políticas de seguridad automatizadas 🏢
* **APIs de autenticación**: validación en tiempo real 🌐

---

### o13.3 📊 **Analizador de estadísticas** 📈🔍

---

#### ❓ Problema 🤔

Implementa una función `analyze_numbers(numbers, operations=["mean", "median", "mode"])` que calcule estadísticas descriptivas de una lista de números para ayudar a Chocolate con sus análisis de datos. 🍫📊

---

#### 📜 Descripción 📖

* **Función**: `analyze_numbers(numbers, operations=["mean", "median", "mode"]) → dict` 🛠️
* **Entradas**:
  * `numbers`: lista de números (int/float) para analizar 🎯
  * `operations`: lista de operaciones a realizar 📏
* **Salidas**:
  * **dict**: resultados con las estadísticas calculadas 📊
* **Casos especiales**:
  * "mean" → promedio aritmético ⚠️
  * "median" → valor central ordenado 🔍
  * "mode" → valor más frecuente (primero si empate) ⚠️
* **Restricciones**:
  * Lista vacía → retornar dict vacío 🔗
  * Operación no soportada → ignorar ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o13.3.1**: Análisis completo
   * Entrada: `([1, 2, 2, 3, 4], ["mean", "median", "mode"])`
   * Espera: `{"mean": 2.4, "median": 2, "mode": 2}` ✅

2. **o13.3.2**: Solo promedio
   * Entrada: `([5, 10, 15], ["mean"])`
   * Espera: `{"mean": 10.0}` ✅

3. **o13.3.3**: Lista con números decimales
   * Entrada: `([1.5, 2.5, 3.5], ["mean", "median"])`
   * Espera: `{"mean": 2.5, "median": 2.5}` ✅

4. **o13.3.4**: Verificación de tipos
   * Entrada: `([1, 2, 3], ["mean"])`
   * Verificar: resultado es dict ✅

5. **o13.3.5**: Lista vacía
   * Entrada: `([], ["mean", "median"])`
   * Espera: `{}` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def analyze_numbers(numbers, operations=["mean", "median", "mode"]):
    """📊 Analyze list of numbers with statistical operations.
    Returns dict with calculated statistics."""
    # Your solution here 🛠️
    pass

def test_o13_3():
    # o13.3.1: Análisis completo
    result = analyze_numbers([1, 2, 2, 3, 4], ["mean", "median", "mode"])
    expected = {"mean": 2.4, "median": 2, "mode": 2}
    record_test("o13.3.1 análisis completo", result == expected)
    
    # o13.3.2: Solo promedio
    result = analyze_numbers([5, 10, 15], ["mean"])
    expected = {"mean": 10.0}
    record_test("o13.3.2 solo promedio", result == expected)
    
    # o13.3.3: Números decimales
    result = analyze_numbers([1.5, 2.5, 3.5], ["mean", "median"])
    expected = {"mean": 2.5, "median": 2.5}
    record_test("o13.3.3 decimales", result == expected)
    
    # o13.3.4: Verificación de tipos
    result = analyze_numbers([1, 2, 3], ["mean"])
    record_test("o13.3.4 retorna dict", isinstance(result, dict))
    
    # o13.3.5: Lista vacía
    result = analyze_numbers([], ["mean", "median"])
    record_test("o13.3.5 lista vacía", result == {})

# 🚀 Run tests
test_o13_3()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Para media: `sum(numbers) / len(numbers)` 🔍
* Para mediana: ordena la lista y toma el elemento central 📊
* Para moda: usa un diccionario para contar frecuencias y encuentra el máximo ✨
* Verifica `if not numbers: return {}` al inicio 🚀

---

#### 🧠 Motivación 💭

* **Ciencia de datos**: análisis exploratorio automatizado 📈
* **Investigación**: cálculos estadísticos rápidos 🔬
* **Reportes empresariales**: métricas automáticas de rendimiento 💼

---

### o13.4 🎨 **Generador de patrones** 🌈📝

---

#### ❓ Problema 🤔

Implementa una función `generate_pattern(pattern_type, size, char="*")` que genere diferentes patrones visuales para decorar los proyectos artísticos de Amorosa. 💕🎭

---

#### 📜 Descripción 📖

* **Función**: `generate_pattern(pattern_type, size, char="*") → str` 🛠️
* **Entradas**:
  * `pattern_type`: string con tipo ("triangle", "diamond", "square") 🎯
  * `size`: int tamaño del patrón 📏
  * `char`: string carácter para dibujar (default "*") 🔍
* **Salidas**:
  * **string**: patrón visual generado con saltos de línea 📊
* **Casos especiales**:
  * "triangle" → triángulo creciente ⚠️
  * "diamond" → rombo completo 🔍
  * "square" → cuadrado hueco (solo bordes) ⚠️
* **Restricciones**:
  * size debe ser positivo 🔗
  * pattern_type no soportado → retornar string vacío ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o13.4.1**: Triángulo tamaño 3
   * Entrada: `("triangle", 3, "*")`
   * Espera: `"*\n**\n***"` ✅

2. **o13.4.2**: Rombo tamaño 3
   * Entrada: `("diamond", 3, "#")`
   * Espera: `" #\n###\n #"` ✅

3. **o13.4.3**: Cuadrado hueco tamaño 3
   * Entrada: `("square", 3, "+")`
   * Espera: `"+++\n+ +\n+++"` ✅

4. **o13.4.4**: Verificación de tipos
   * Entrada: `("triangle", 2, "*")`
   * Verificar: resultado es string ✅

5. **o13.4.5**: Patrón no soportado
   * Entrada: `("circle", 3, "*")`
   * Espera: `""` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def generate_pattern(pattern_type, size, char="*"):
    """🎨 Generate visual patterns with specified character.
    Returns pattern as string with newlines."""
    # Your solution here 🛠️
    pass

def test_o13_4():
    # o13.4.1: Triángulo tamaño 3
    result = generate_pattern("triangle", 3, "*")
    expected = "*\n**\n***"
    record_test("o13.4.1 triángulo", result == expected)
    
    # o13.4.2: Rombo tamaño 3
    result = generate_pattern("diamond", 3, "#")
    expected = " #\n###\n #"
    record_test("o13.4.2 rombo", result == expected)
    
    # o13.4.3: Cuadrado hueco tamaño 3
    result = generate_pattern("square", 3, "+")
    expected = "+++\n+ +\n+++"
    record_test("o13.4.3 cuadrado hueco", result == expected)
    
    # o13.4.4: Verificación de tipos
    result = generate_pattern("triangle", 2, "*")
    record_test("o13.4.4 retorna str", isinstance(result, str))
    
    # o13.4.5: Patrón no soportado
    result = generate_pattern("circle", 3, "*")
    record_test("o13.4.5 no soportado", result == "")

# 🚀 Run tests
test_o13_4()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Para triángulo: usa bucle `for i in range(1, size+1): lines.append(char * i)` 🔍
* Para rombo: combina parte superior (espacios + caracteres) e inferior 📊
* Para cuadrado hueco: primera y última línea completas, intermedias solo bordes ✨
* Une las líneas con `"\n".join(lines)` al final 🚀

---

#### 🧠 Motivación 💭

* **Arte ASCII**: generación automática de patrones decorativos 🎨
* **Interfaces de texto**: elementos visuales en consola 💻
* **Herramientas educativas**: visualización de conceptos matemáticos 📚

---

### o13.5 🔄 **Procesador de texto avanzado** 📝⚡

---

#### ❓ Problema 🤔

Implementa una función `process_text(text, transformations=["clean", "count"])` que procese y analice texto de múltiples maneras para ayudar a Leo con sus proyectos de procesamiento de lenguaje natural. 🦁📖

---

#### 📜 Descripción 📖

* **Función**: `process_text(text, transformations=["clean", "count"]) → dict` 🛠️
* **Entradas**:
  * `text`: string con el texto a procesar 🎯
  * `transformations`: lista de transformaciones a aplicar 📏
* **Salidas**:
  * **dict**: resultados de las transformaciones aplicadas 📊
* **Casos especiales**:
  * "clean" → texto sin espacios extra y en minúsculas ⚠️
  * "count" → diccionario con conteos (chars, words, sentences) 🔍
  * "reverse" → texto invertido ⚠️
* **Restricciones**:
  * Texto vacío → procesar normalmente 🔗
  * Transformación no soportada → ignorar ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o13.5.1**: Limpieza básica
   * Entrada: `("  Hello   World!  ", ["clean"])`
   * Espera: `{"clean": "hello world!"}` ✅

2. **o13.5.2**: Conteo de elementos
   * Entrada: `("Hello world. How are you?", ["count"])`
   * Espera: `{"count": {"chars": 25, "words": 5, "sentences": 2}}` ✅

3. **o13.5.3**: Texto invertido
   * Entrada: `("Python", ["reverse"])`
   * Espera: `{"reverse": "nohtyP"}` ✅

4. **o13.5.4**: Verificación de tipos
   * Entrada: `("test", ["clean"])`
   * Verificar: resultado es dict ✅

5. **o13.5.5**: Múltiples transformaciones
   * Entrada: `("Hello!", ["clean", "reverse"])`
   * Espera: `{"clean": "hello!", "reverse": "!olleH"}` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def process_text(text, transformations=["clean", "count"]):
    """🔄 Process text with multiple transformation operations.
    Returns dict with transformation results."""
    # Your solution here 🛠️
    pass

def test_o13_5():
    # o13.5.1: Limpieza básica
    result = process_text("  Hello   World!  ", ["clean"])
    expected = {"clean": "hello world!"}
    record_test("o13.5.1 limpieza", result == expected)
    
    # o13.5.2: Conteo de elementos
    result = process_text("Hello world. How are you?", ["count"])
    expected = {"count": {"chars": 25, "words": 5, "sentences": 2}}
    record_test("o13.5.2 conteo", result == expected)
    
    # o13.5.3: Texto invertido
    result = process_text("Python", ["reverse"])
    expected = {"reverse": "nohtyP"}
    record_test("o13.5.3 invertido", result == expected)
    
    # o13.5.4: Verificación de tipos
    result = process_text("test", ["clean"])
    record_test("o13.5.4 retorna dict", isinstance(result, dict))
    
    # o13.5.5: Múltiples transformaciones
    result = process_text("Hello!", ["clean", "reverse"])
    expected = {"clean": "hello!", "reverse": "!olleH"}
    record_test("o13.5.5 múltiples", result == expected)

# 🚀 Run tests
test_o13_5()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Para "clean": usa `" ".join(text.split()).lower()` 🔍
* Para "count": chars=`len(text)`, words=`len(text.split())`, sentences=`text.count('.')+text.count('!')+text.count('?')` 📊
* Para "reverse": simplemente `text[::-1]` ✨
* Itera sobre transformations y aplica cada una según corresponda 🚀

---

#### 🧠 Motivación 💭

* **Procesamiento de lenguaje natural**: análisis automático de textos 🤖
* **Sistemas de búsqueda**: normalización y análisis de consultas 🔍
* **Herramientas de escritura**: estadísticas y corrección automática ✍️

---

## 🎯 **¡Felicitaciones, arquitecto de funciones!** 🏗️🎉

Has completado exitosamente todos los retos de funciones en Python. Ahora eres capaz de crear bloques de código modulares, reutilizables y bien organizados como un verdadero chanchito programador profesional! 🐷✨ 

Dominas habilidades fundamentales como definir funciones con diferentes tipos de parámetros, manejar valores de retorno complejos, implementar validaciones robustas, crear utilidades matemáticas y de procesamiento, y documentar tu código de manera clara. Estas son las bases para construir programas más grandes y mantenibles. 🚀📦

## 🚀 **Siguientes Pasos en tu Aventura Modular**

Ahora que dominas las funciones, estás listo para explorar cómo organizar tu código en archivos separados y crear bibliotecas reutilizables. En el próximo tema descubriremos **Módulos**, donde aprenderás a importar funcionalidades, crear tus propios módulos, y estructurar proyectos más grandes de manera profesional.

### 🌟 **El poder de las funciones te llevará a:**

- **🎯 Aplicaciones web modulares**: APIs REST con funciones especializadas para diferentes endpoints, validadores de datos reutilizables y utilidades de formateo que funcionan en toda la aplicación
- **📊 Bibliotecas de análisis**: Colecciones de funciones matemáticas y estadísticas que puedes reutilizar en múltiples proyectos de ciencia de datos y análisis numérico
- **🔔 Sistemas de automatización**: Scripts con funciones para tareas específicas como procesamiento de archivos, envío de emails automáticos y generación de reportes programados
- **🏢 Software empresarial**: Aplicaciones grandes con funciones bien organizadas para diferentes módulos como autenticación, procesamiento de pagos y gestión de inventarios
- **🎮 Desarrollo de juegos**: Funciones especializadas para mecánicas de juego, sistemas de puntuación, generación de contenido y manejo de eventos de usuario

Con los **Módulos** que vienen a continuación, podrás organizar todas estas funciones en archivos separados, crear bibliotecas personalizadas que puedes compartir entre proyectos, e importar funcionalidades externas para expandir las capacidades de tus programas. ¡El mundo de la programación modular te espera! 💪🐍✨