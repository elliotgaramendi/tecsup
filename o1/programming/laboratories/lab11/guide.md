# **📚 o11 Diccionarios 🐍✨**

Los diccionarios son colecciones mutables que almacenan pares clave-valor, permitiendo acceso rápido y eficiente a datos mediante claves únicas. Son ideales para representar información estructurada, configuraciones, bases de datos simples y cualquier mapeo entre conceptos relacionados. ¡Son una de las estructuras más poderosas de Python! 💪📊

## 🎯 Objetivos

* 📚 **Crear y manipular diccionarios** usando claves para acceder y modificar valores
* 🔑 **Trabajar con claves y valores** usando métodos como keys(), values() e items()
* 🔄 **Actualizar información** agregando, modificando y eliminando elementos dinámicamente
* 🔍 **Buscar y validar** existencia de claves usando in y métodos get()
* 🎯 **Combinar diccionarios** fusionando información de múltiples fuentes

---

## 🔍 Visualizando el Concepto

```
📚 ESTRUCTURA DE UN DICCIONARIO

    mi_dict = {
        "nombre": "Ana",     ← clave: valor
        "edad": 25,          ← diferentes tipos
        "activo": True,      ← claves únicas
        "hobbies": ["leer"]  ← valores pueden ser listas
    }
              ↑
        🔑 Claves inmutables (strings, números, tuplas)
        📊 Valores mutables (cualquier tipo)

🔧 OPERACIONES BÁSICAS:
┌─────────────────────────────┐
│ dict[clave]     → Acceder   │
│ dict[clave] = x → Asignar   │  
│ del dict[clave] → Eliminar  │
│ clave in dict   → Verificar │
│ dict.keys()     → Claves    │
│ dict.values()   → Valores   │
│ dict.items()    → Pares     │
│ dict.get(k, d)  → Seguro    │
└─────────────────────────────┘

📊 CASOS DE USO COMUNES:
┌──────────────────────────────┐
│ • Perfiles de usuario        │
│ • Configuraciones sistema    │
│ • Conteo de elementos        │
│ • Mapeo de datos             │
│ • Cache/almacenamiento       │
└──────────────────────────────┘
```

---

### o11.1 👤 **Creador de Perfiles** 📝✨

---

#### ❓ Problema 🤔

Implementa una función `create_profile(nombre, edad, email)` que cree un diccionario de perfil de usuario con validaciones básicas. 🎯📋

---

#### 📜 Descripción 📖

* **Función**: `create_profile(nombre, edad, email) → dict or None` 🛠️
* **Entradas**:
  * `nombre`: string no vacío 🎯
  * `edad`: entero positivo (≥ 0) 🎯  
  * `email`: string que contenga "@" 🎯
* **Salidas**:
  * **diccionario**: perfil válido con estructura fija 📊
  * **None**: si algún parámetro es inválido ❌
* **Casos especiales**:
  * Datos inválidos → retorna `None` ⚠️
  * Email debe contener "@" 🔍
* **Restricciones**:
  * Debe validar cada entrada antes de crear el perfil 🔗
* **Validación de entrada**:
  * Nombre no puede estar vacío ❌⚙️
  * Edad debe ser número no negativo ❌⚙️
  * Email debe contener "@" ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o11.1.1**: Datos válidos
   * Entrada: `("Ana", 25, "ana@email.com")`
   * Espera: diccionario con estructura correcta ✅

2. **o11.1.2**: Edad cero
   * Entrada: `("Bebé", 0, "bebe@email.com")`
   * Espera: diccionario válido ✅

3. **o11.1.3**: Estructura del diccionario
   * Entrada: `("Test", 30, "test@email.com")`
   * Verificar: contiene claves "nombre", "edad", "email", "activo" ✅

4. **o11.1.4**: Verificación de tipos
   * Entrada: `("Juan", 20, "juan@test.com")`
   * Verificar: resultado es diccionario ✅

5. **o11.1.5**: Datos inválidos
   * Entrada: `("", -5, "email-sin-arroba")`
   * Espera: `None` para cada caso inválido ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def create_profile(nombre, edad, email):
    """👤 Create user profile dictionary with validation.
    Returns dict with profile data or None if invalid."""
    # Your solution here 🛠️
    pass

def test_o11_1():
    # o11.1.1: Datos válidos
    result = create_profile("Ana", 25, "ana@email.com")
    valid_profile = (isinstance(result, dict) and 
                    result.get("nombre") == "Ana" and
                    result.get("edad") == 25 and
                    result.get("email") == "ana@email.com")
    record_test("o11.1.1 datos válidos", valid_profile)
    
    # o11.1.2: Edad cero
    result = create_profile("Bebé", 0, "bebe@email.com")
    record_test("o11.1.2 edad cero", isinstance(result, dict))
    
    # o11.1.3: Estructura del diccionario
    result = create_profile("Test", 30, "test@email.com")
    keys_ok = (isinstance(result, dict) and 
              all(key in result for key in ["nombre", "edad", "email", "activo"]))
    record_test("o11.1.3 estructura correcta", keys_ok)
    
    # o11.1.4: Verificación de tipos
    result = create_profile("Juan", 20, "juan@test.com")
    record_test("o11.1.4 retorna dict", isinstance(result, dict))
    
    # o11.1.5: Datos inválidos
    invalid_cases = [
        create_profile("", 25, "test@email.com"),  # nombre vacío
        create_profile("Juan", -5, "juan@test.com"),  # edad negativa
        create_profile("Ana", 25, "email-sin-arroba")  # email sin @
    ]
    all_none = all(result is None for result in invalid_cases)
    record_test("o11.1.5 datos inválidos", all_none)

# 🚀 Run tests
test_o11_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Valida cada parámetro antes de crear el diccionario 🔍
* Usa `len(nombre) > 0` para verificar que no esté vacío 📝
* `"@" in email` verifica que contenga el símbolo requerido ✉️
* Incluye clave "activo": True por defecto en el perfil 👍

---

#### 🧠 Motivación 💭

* **Validación de datos**: fundamental en aplicaciones reales 🔒
* **Estructura de datos**: base para sistemas de usuarios 👥
* **Programación defensiva**: prevenir errores con validaciones ⚡

---

### o11.2 📊 **Contador de Elementos** 🔢🎯

---

#### ❓ Problema 🤔

Implementa una función `count_elements(lista)` que cuente la frecuencia de cada elemento en una lista y retorne un diccionario con los conteos. 🔍📈

---

#### 📜 Descripción 📖

* **Función**: `count_elements(lista) → dict` 🛠️
* **Entradas**:
  * `lista`: lista con elementos a contar 🎯
* **Salidas**:
  * **diccionario**: cada elemento como clave, su frecuencia como valor 📊
* **Casos especiales**:
  * Lista vacía → diccionario vacío `{}` ⚠️
  * Elementos de diferentes tipos → todos se cuentan 🔍
* **Restricciones**:
  * No usar Counter de collections 🔗
  * Manejar cualquier tipo de elemento hashable ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o11.2.1**: Lista con repeticiones
   * Entrada: `[1, 2, 2, 3, 3, 3]`
   * Espera: `{1: 1, 2: 2, 3: 3}` ✅

2. **o11.2.2**: Lista de strings
   * Entrada: `["a", "b", "a", "c", "b", "a"]`
   * Espera: `{"a": 3, "b": 2, "c": 1}` ✅

3. **o11.2.3**: Elementos únicos
   * Entrada: `[1, 2, 3, 4]`
   * Espera: todos con conteo 1 ✅

4. **o11.2.4**: Verificación de tipos
   * Entrada: `[1, 2, 1]`
   * Verificar: resultado es diccionario ✅

5. **o11.2.5**: Lista vacía
   * Entrada: `[]`
   * Espera: `{}` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def count_elements(lista):
    """📊 Count frequency of each element in list.
    Returns dict with element: count pairs."""
    # Your solution here 🛠️
    pass

def test_o11_2():
    # o11.2.1: Lista con repeticiones
    result = count_elements([1, 2, 2, 3, 3, 3])
    record_test("o11.2.1 con repeticiones", result == {1: 1, 2: 2, 3: 3})
    
    # o11.2.2: Lista de strings
    result = count_elements(["a", "b", "a", "c", "b", "a"])
    record_test("o11.2.2 strings", result == {"a": 3, "b": 2, "c": 1})
    
    # o11.2.3: Elementos únicos
    result = count_elements([1, 2, 3, 4])
    expected = {1: 1, 2: 1, 3: 1, 4: 1}
    record_test("o11.2.3 elementos únicos", result == expected)
    
    # o11.2.4: Verificación de tipos
    result = count_elements([1, 2, 1])
    record_test("o11.2.4 retorna dict", isinstance(result, dict))
    
    # o11.2.5: Lista vacía
    result = count_elements([])
    record_test("o11.2.5 lista vacía", result == {})

# 🚀 Run tests
test_o11_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Itera sobre la lista y usa `elemento in diccionario` para verificar existencia 🔍
* Si existe: incrementa con `diccionario[elemento] += 1` ➕
* Si no existe: inicializa con `diccionario[elemento] = 1` 🆕
* Retorna el diccionario al final 📊

---

#### 🧠 Motivación 💭

* **Análisis de datos**: contar frecuencias es fundamental en estadística 📊
* **Procesamiento de texto**: contar palabras en documentos 📝
* **Optimización**: los diccionarios son muy eficientes para conteo 🚀

---

### o11.3 🔍 **Buscador de Información** 🎯📋

---

#### ❓ Problema 🤔

Implementa una función `find_user_info(usuarios, nombre_buscar)` que busque información de un usuario en una lista de diccionarios y retorne sus datos. 🔍👤

---

#### 📜 Descripción 📖

* **Función**: `find_user_info(usuarios, nombre_buscar) → dict or None` 🛠️
* **Entradas**:
  * `usuarios`: lista de diccionarios con datos de usuarios 🎯
  * `nombre_buscar`: string con nombre a buscar 🔍
* **Salidas**:
  * **diccionario**: datos del usuario encontrado 📊
  * **None**: si no se encuentra el usuario ❌
* **Casos especiales**:
  * Lista vacía → `None` ⚠️
  * Múltiples usuarios con mismo nombre → retorna el primero 🔍
* **Restricciones**:
  * Búsqueda debe ser case-insensitive 🔗
  * Cada usuario debe tener clave "nombre" ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o11.3.1**: Usuario encontrado
   * Entrada: usuarios con Ana, búsqueda "Ana"
   * Espera: diccionario de Ana ✅

2. **o11.3.2**: Búsqueda case-insensitive
   * Entrada: usuarios con "Juan", búsqueda "juan"
   * Espera: diccionario de Juan ✅

3. **o11.3.3**: Usuario no encontrado
   * Entrada: usuarios sin "Pedro", búsqueda "Pedro"
   * Espera: `None` ✅

4. **o11.3.4**: Verificación de tipos
   * Entrada: búsqueda exitosa
   * Verificar: resultado es diccionario ✅

5. **o11.3.5**: Lista vacía
   * Entrada: `[], "cualquier"`
   * Espera: `None` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def find_user_info(usuarios, nombre_buscar):
    """🔍 Find user info by name in list of user dictionaries.
    Returns user dict or None if not found."""
    # Your solution here 🛠️
    pass

def test_o11_3():
    # Datos de prueba
    usuarios_test = [
        {"nombre": "Ana", "edad": 25, "ciudad": "Lima"},
        {"nombre": "Juan", "edad": 30, "ciudad": "Cusco"},
        {"nombre": "María", "edad": 22, "ciudad": "Arequipa"}
    ]
    
    # o11.3.1: Usuario encontrado
    result = find_user_info(usuarios_test, "Ana")
    found_ana = (isinstance(result, dict) and result.get("nombre") == "Ana")
    record_test("o11.3.1 usuario encontrado", found_ana)
    
    # o11.3.2: Búsqueda case-insensitive
    result = find_user_info(usuarios_test, "juan")
    found_juan = (isinstance(result, dict) and result.get("nombre") == "Juan")
    record_test("o11.3.2 case-insensitive", found_juan)
    
    # o11.3.3: Usuario no encontrado
    result = find_user_info(usuarios_test, "Pedro")
    record_test("o11.3.3 no encontrado", result is None)
    
    # o11.3.4: Verificación de tipos
    result = find_user_info(usuarios_test, "María")
    record_test("o11.3.4 retorna dict", isinstance(result, dict))
    
    # o11.3.5: Lista vacía
    result = find_user_info([], "cualquier")
    record_test("o11.3.5 lista vacía", result is None)

# 🚀 Run tests
test_o11_3()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Itera sobre la lista de usuarios con un bucle for 🔄
* Usa `usuario["nombre"].lower() == nombre_buscar.lower()` para case-insensitive 🔍
* Retorna el usuario inmediatamente cuando lo encuentres 📊
* Si termina el bucle sin encontrar nada, retorna `None` ❌

---

#### 🧠 Motivación 💭

* **Búsqueda en bases de datos**: operación fundamental en aplicaciones 🔍
* **Sistemas de usuarios**: encontrar perfiles específicos 👤
* **Filtrado de información**: base para sistemas más complejos 🎯

---

### o11.4 🔄 **Actualizador de Datos** ✏️📊

---

#### ❓ Problema 🤔

Implementa una función `update_inventory(inventario, producto, cantidad)` que actualice el inventario agregando o restando cantidad de un producto. 🎯📦

---

#### 📜 Descripción 📖

* **Función**: `update_inventory(inventario, producto, cantidad) → dict` 🛠️
* **Entradas**:
  * `inventario`: diccionario con productos y sus cantidades 🎯
  * `producto`: string con nombre del producto 📦
  * `cantidad`: entero (positivo=agregar, negativo=restar) ➕➖
* **Salidas**:
  * **diccionario**: inventario actualizado 📊
* **Casos especiales**:
  * Producto nuevo → se agrega al inventario ⚠️
  * Cantidad negativa mayor al stock → se pone en 0 🔍
* **Restricciones**:
  * No permitir cantidades negativas en el inventario final 🔗
  * Modificar el diccionario original ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o11.4.1**: Agregar a producto existente
   * Entrada: inventario con "manzanas": 10, agregar 5
   * Espera: "manzanas": 15 ✅

2. **o11.4.2**: Producto nuevo
   * Entrada: inventario sin "naranjas", agregar 8
   * Espera: "naranjas": 8 en inventario ✅

3. **o11.4.3**: Restar cantidad
   * Entrada: inventario con "peras": 12, restar 7
   * Espera: "peras": 5 ✅

4. **o11.4.4**: Verificación de tipos
   * Entrada: operación válida
   * Verificar: resultado es diccionario ✅

5. **o11.4.5**: Restar más de lo disponible
   * Entrada: inventario con "uvas": 3, restar 10
   * Espera: "uvas": 0 ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def update_inventory(inventario, producto, cantidad):
    """🔄 Update inventory by adding/subtracting product quantity.
    Returns updated inventory dict."""
    # Your solution here 🛠️
    pass

def test_o11_4():
    # o11.4.1: Agregar a producto existente
    inv1 = {"manzanas": 10, "peras": 5}
    result = update_inventory(inv1, "manzanas", 5)
    record_test("o11.4.1 agregar existente", result["manzanas"] == 15)
    
    # o11.4.2: Producto nuevo
    inv2 = {"manzanas": 10}
    result = update_inventory(inv2, "naranjas", 8)
    record_test("o11.4.2 producto nuevo", result.get("naranjas") == 8)
    
    # o11.4.3: Restar cantidad
    inv3 = {"peras": 12}
    result = update_inventory(inv3, "peras", -7)
    record_test("o11.4.3 restar cantidad", result["peras"] == 5)
    
    # o11.4.4: Verificación de tipos
    inv4 = {"test": 5}
    result = update_inventory(inv4, "test", 2)
    record_test("o11.4.4 retorna dict", isinstance(result, dict))
    
    # o11.4.5: Restar más de lo disponible
    inv5 = {"uvas": 3}
    result = update_inventory(inv5, "uvas", -10)
    record_test("o11.4.5 no negativo", result["uvas"] == 0)

# 🚀 Run tests
test_o11_4()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Verifica si el producto existe con `producto in inventario` 🔍
* Si no existe, inicialízalo: `inventario[producto] = 0` 🆕
* Suma la cantidad: `inventario[producto] += cantidad` ➕
* Usa `max(0, inventario[producto])` para evitar negativos 📊

---

#### 🧠 Motivación 💭

* **Gestión de inventarios**: aplicación directa en comercio 📦
* **Mutabilidad de diccionarios**: modificar datos dinámicamente 🔄
* **Validación de negocio**: reglas como "no stock negativo" 📋

---

### o11.5 🤝 **Combinador de Diccionarios** 🔗✨

---

#### ❓ Problema 🤔

Implementa una función `merge_configs(config1, config2, config3)` que combine tres diccionarios de configuración dando prioridad al último. 🎯🔗

---

#### 📜 Descripción 📖

* **Función**: `merge_configs(config1, config2, config3) → dict` 🛠️
* **Entradas**:
  * `config1`, `config2`, `config3`: diccionarios de configuración 🎯
* **Salidas**:
  * **diccionario**: configuración combinada con prioridades 📊
* **Casos especiales**:
  * Claves duplicadas → config3 > config2 > config1 ⚠️
  * Diccionarios vacíos → se ignoran 🔍
* **Restricciones**:
  * No modificar los diccionarios originales 🔗
  * Mantener todas las claves únicas ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o11.5.1**: Sin conflictos
   * Entrada: configs con claves diferentes
   * Espera: todas las claves presentes ✅

2. **o11.5.2**: Con conflictos de prioridad
   * Entrada: misma clave en múltiples configs
   * Espera: valor del último config ✅

3. **o11.5.3**: Algunos diccionarios vacíos
   * Entrada: config1={}, config2={"a": 1}, config3={}
   * Espera: {"a": 1} ✅

4. **o11.5.4**: Verificación de tipos
   * Entrada: operación válida
   * Verificar: resultado es diccionario ✅

5. **o11.5.5**: Todos vacíos
   * Entrada: {}, {}, {}
   * Espera: {} ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def merge_configs(config1, config2, config3):
    """🤝 Merge three config dictionaries with priority.
    Returns merged dict with config3 > config2 > config1 priority."""
    # Your solution here 🛠️
    pass

def test_o11_5():
    # o11.5.1: Sin conflictos
    c1 = {"host": "localhost"}
    c2 = {"port": 8080}
    c3 = {"debug": True}
    result = merge_configs(c1, c2, c3)
    no_conflicts = (result.get("host") == "localhost" and 
                   result.get("port") == 8080 and 
                   result.get("debug") == True)
    record_test("o11.5.1 sin conflictos", no_conflicts)
    
    # o11.5.2: Con conflictos de prioridad
    c1 = {"timeout": 30}
    c2 = {"timeout": 60}
    c3 = {"timeout": 90}
    result = merge_configs(c1, c2, c3)
    record_test("o11.5.2 prioridad config3", result["timeout"] == 90)
    
    # o11.5.3: Algunos diccionarios vacíos
    result = merge_configs({}, {"a": 1}, {})
    record_test("o11.5.3 algunos vacíos", result == {"a": 1})
    
    # o11.5.4: Verificación de tipos
    result = merge_configs({"x": 1}, {"y": 2}, {"z": 3})
    record_test("o11.5.4 retorna dict", isinstance(result, dict))
    
    # o11.5.5: Todos vacíos
    result = merge_configs({}, {}, {})
    record_test("o11.5.5 todos vacíos", result == {})

# 🚀 Run tests
test_o11_5()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Crea un diccionario resultado vacío: `resultado = {}` 🆕
* Actualiza secuencialmente: `resultado.update(config1)`, luego config2, luego config3 🔄
* `dict.update()` sobrescribe claves existentes automáticamente 📊
* El orden importa: el último update tiene prioridad 🎯

---

#### 🧠 Motivación 💭

* **Configuración de aplicaciones**: combinar settings de múltiples fuentes 🔧
* **Sistemas de prioridades**: manejar precedencia de datos 🎯
* **Arquitectura modular**: fusionar configuraciones por módulos 🏗️

---

## 🎯 **¡Felicitaciones!**

Has completado todos los retos de diccionarios en Python. Ahora dominas:

✅ **Crear y validar** diccionarios con estructuras de datos complejas  
✅ **Contar y analizar** elementos usando diccionarios como contadores  
✅ **Buscar información** eficientemente en colecciones de datos  
✅ **Actualizar contenido** dinámicamente modificando valores  
✅ **Combinar información** de múltiples fuentes con prioridades  

## 🚀 **Siguientes Pasos**

Ahora que has dominado los diccionarios, tienes una herramienta poderosa para manejar datos estructurados. Los diccionarios son la base de muchas aplicaciones avanzadas:

### 🎯 **Lo que has aprendido te servirá para:**

**⏰ Gestión de fechas y hora (Tema 12)**: Los diccionarios son perfectos para almacenar información temporal estructurada, configuraciones de zona horaria y datos de calendarios.

**🔧 Funciones (Tema 13)**: Podrás pasar diccionarios como parámetros complejos, retornar datos estructurados y usar **kwargs para argumentos nombrados.

**📁 Módulos (Tema 14)**: Los diccionarios serán útiles para configuraciones de módulos, datos compartidos entre archivos y sistemas de cache.

### 💡 **Conceptos clave que dominas:**

- **Mapeo clave-valor**: Relaciones eficientes entre conceptos
- **Mutabilidad controlada**: Modificar datos manteniendo estructura
- **Validación de datos**: Verificar información antes de procesarla
- **Búsqueda eficiente**: Acceso O(1) por claves
- **Combinación de fuentes**: Fusionar información de múltiples orígenes

### 🌟 **Aplicaciones en el mundo real:**

- **APIs REST**: Manejo de JSON y respuestas estructuradas
- **Bases de datos**: Representación de registros y consultas
- **Configuración de sistemas**: Settings y parámetros de aplicaciones
- **Cache y almacenamiento**: Datos en memoria para acceso rápido
- **Análisis de datos**: Conteos, agrupaciones y estadísticas

¡Continúa con fechas y hora para aprender a manejar información temporal, y después podrás crear sistemas completos combinando todas las estructuras de datos! 💪🐍✨