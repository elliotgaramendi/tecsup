# **🔗 Guía de Retos - Sets en Python 🐍✨**

Esta guía está diseñada para que practiques y domines el uso de sets en Python. Los sets son colecciones desordenadas de elementos únicos que no permiten duplicados. Son ideales para eliminar elementos repetidos, realizar operaciones matemáticas entre conjuntos y verificar membresías de manera eficiente. ¡Cada reto te ayudará a fortalecer tus habilidades paso a paso! 💪📊

## 🎯 Objetivos

* 🔗 **Crear y manipular sets** usando métodos básicos como add(), remove() y discard()
* 🔍 **Eliminar duplicados** de colecciones y trabajar solo con elementos únicos
* 📊 **Realizar operaciones de conjuntos** como unión, intersección y diferencia
* 🔎 **Verificar membresías** usando el operador in de manera eficiente
* 🗂️ **Convertir entre tipos** de datos transformando listas a sets y viceversa

---

## 🔍 Visualizando el Concepto con ASCII Art

```
🔗 ESTRUCTURA DE UN SET

    mi_set = {🍎, 🍌, 🍊}  ← Sin duplicados, sin orden
             ↑   ↑   ↑
         únicos únicos únicos

🔧 OPERACIONES BÁSICAS:
┌─────────────────────┐
│ add()     → Agregar │
│ remove()  → Eliminar│  
│ len()     → Tamaño  │
│ in        → Buscar  │
│ union()   → Unir    │
│ &         → Común   │
└─────────────────────┘
```

---

### s10.1 🗑️ **Eliminador de Duplicados** 🔄✨

---

#### ❓ Problema 🤔

Implementa una función `remove_duplicates(lista)` que elimine elementos duplicados de una lista usando sets y devuelva información sobre el proceso. 🎯📋

---

#### 📜 Descripción 📖

* **Función**: `remove_duplicates(lista) → tuple` 🛠️
* **Entradas**:
  * `lista`: lista que puede contener elementos duplicados 🎯
* **Salidas**:
  * Tupla con: `(elementos_únicos, total_original, porcentaje_duplicados)` 📊
* **Casos especiales**:
  * Lista vacía → `(0, 0, 0.0)` ⚠️
  * Sin duplicados → porcentaje = 0.0 🔍
* **Restricciones**:
  * Debe usar sets para eliminar duplicados 🔗
  * Debe validar entrada ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **s10.1.1**: Lista con duplicados variados
   * Entrada: `[1,2,2,3,3,3]`
   * Espera: `(3, 6, 50.0)` ✅

2. **s10.1.2**: Todos elementos iguales
   * Entrada: `[1,1,1,1]`
   * Espera: `(1, 4, 75.0)` ✅

3. **s10.1.3**: Sin duplicados
   * Entrada: `[1,2,3,4,5]`
   * Espera: `(5, 5, 0.0)` ✅

4. **s10.1.4**: Verificación de tipos
   * Entrada: `[1,2,3]`
   * Verificar: todos los valores son números ✅

5. **s10.1.5**: Lista vacía
   * Entrada: `[]`
   * Espera: `(0, 0, 0.0)` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def remove_duplicates(lista):
    """🗑️ Remove duplicates from list using sets.
    Returns (unique_count, original_count, duplicate_percentage)"""
    # Your solution here 🛠️
    return 0, 0, 0.0

def test_s10_1():
    # s10.1.1: Lista con duplicados variados
    result = remove_duplicates([1,2,2,3,3,3])
    record_test("s10.1.1 duplicados variados", result == (3, 6, 50.0))
    
    # s10.1.2: Todos elementos iguales
    result = remove_duplicates([1,1,1,1])
    record_test("s10.1.2 todos iguales", result == (1, 4, 75.0))
    
    # s10.1.3: Sin duplicados
    result = remove_duplicates([1,2,3,4,5])
    record_test("s10.1.3 sin duplicados", result == (5, 5, 0.0))
    
    # s10.1.4: Verificación de tipos
    unicos, original, porcentaje = remove_duplicates([1,2,3])
    types_ok = isinstance(unicos, int) and isinstance(original, int) and isinstance(porcentaje, float)
    record_test("s10.1.4 tipos correctos", types_ok)
    
    # s10.1.5: Lista vacía
    result = remove_duplicates([])
    record_test("s10.1.5 lista vacía", result == (0, 0, 0.0))

# 🚀 Run tests
test_s10_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Usa `set(lista)` para eliminar duplicados automáticamente 🔄
* Calcula porcentaje: `((original - únicos) / original) * 100` si original > 0 📊
* Maneja el caso especial de lista vacía para evitar división por cero ⚠️
* `len(set(lista))` te da el número de elementos únicos 🔍

---

#### 🧠 Motivación 💭

* **Limpieza de datos**: fundamental en análisis de datos 📊
* **Eficiencia**: los sets eliminan duplicados automáticamente 🚀
* **Base para operaciones**: preparación para operaciones más complejas 🌱

---

### s10.2 🤝 **Analizador de Intersecciones** 🔍📊

---

#### ❓ Problema 🤔

Implementa una función `find_common_elements(set1, set2)` que encuentre elementos comunes entre dos sets y analice su relación. 🔗🤝

---

#### 📜 Descripción 📖

* **Función**: `find_common_elements(set1, set2) → tuple` 🛠️
* **Entradas**:
  * `set1`, `set2`: sets para comparar 🎯
* **Salidas**:
  * Tupla con: `(elementos_comunes, total_comunes, porcentaje_similitud)` 📊
* **Casos especiales**:
  * Sets vacíos → `(set(), 0, 0.0)` ⚠️
  * Sets idénticos → porcentaje = 100.0 🔍
* **Restricciones**:
  * Debe usar operaciones de sets 🔗
  * Similitud basada en la unión total ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **s10.2.1**: Sets con elementos comunes
   * Entrada: `{1,2,3}, {2,3,4}`
   * Espera: `({2,3}, 2, 50.0)` ✅

2. **s10.2.2**: Sets sin elementos comunes
   * Entrada: `{1,2}, {3,4}`
   * Espera: `(set(), 0, 0.0)` ✅

3. **s10.2.3**: Sets idénticos
   * Entrada: `{1,2,3}, {1,2,3}`
   * Espera: `({1,2,3}, 3, 100.0)` ✅

4. **s10.2.4**: Verificación de tipos
   * Entrada: `{1,2}, {2,3}`
   * Verificar: primer elemento es set ✅

5. **s10.2.5**: Un set vacío
   * Entrada: `set(), {1,2}`
   * Espera: `(set(), 0, 0.0)` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def find_common_elements(set1, set2):
    """🤝 Find common elements between two sets.
    Returns (common_elements, count_common, similarity_percentage)"""
    # Your solution here 🛠️
    pass

def test_s10_2():
    # s10.2.1: Sets con elementos comunes
    result = find_common_elements({1,2,3}, {2,3,4})
    record_test("s10.2.1 elementos comunes", result == ({2,3}, 2, 50.0))
    
    # s10.2.2: Sets sin elementos comunes
    result = find_common_elements({1,2}, {3,4})
    record_test("s10.2.2 sin comunes", result == (set(), 0, 0.0))
    
    # s10.2.3: Sets idénticos
    result = find_common_elements({1,2,3}, {1,2,3})
    record_test("s10.2.3 sets idénticos", result == ({1,2,3}, 3, 100.0))
    
    # s10.2.4: Verificación de tipos
    comunes, total, porcentaje = find_common_elements({1,2}, {2,3})
    types_ok = isinstance(comunes, set) and isinstance(total, int) and isinstance(porcentaje, float)
    record_test("s10.2.4 tipos correctos", types_ok)
    
    # s10.2.5: Un set vacío
    result = find_common_elements(set(), {1,2})
    record_test("s10.2.5 set vacío", result == (set(), 0, 0.0))

# 🚀 Run tests
test_s10_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Usa `set1 & set2` o `set1.intersection(set2)` para encontrar comunes 🤝
* La similitud se calcula sobre la unión: `(comunes / (set1 | set2)) * 100` 📊
* Maneja sets vacíos para evitar división por cero ⚠️
* `len(intersección)` te da el número de elementos comunes 🔍

---

#### 🧠 Motivación 💭

* **Análisis de datos**: encontrar elementos en común entre grupos 📊
* **Filtros**: identificar overlaps en colecciones 🔍
* **Fundamento matemático**: operaciones de conjuntos 🧮

---

### s10.3 ➕ **Constructor de Uniones** 🔗🌟

---

#### ❓ Problema 🤔

Implementa una función `combine_sets(lista_sets)` que combine múltiples sets en uno solo y analice el resultado de la unión. 🎯🔗

---

#### 📜 Descripción 📖

* **Función**: `combine_sets(lista_sets) → tuple` 🛠️
* **Entradas**:
  * `lista_sets`: lista que contiene sets para combinar 🎯
* **Salidas**:
  * Tupla con: `(set_union, elementos_únicos, total_elementos_originales)` 📊
* **Casos especiales**:
  * Lista vacía → `(set(), 0, 0)` ⚠️
  * Sets con solapamiento → elimina duplicados automáticamente 🔍
* **Restricciones**:
  * Debe usar operaciones de unión de sets 🔗
  * Contar elementos totales antes de la unión ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **s10.3.1**: Sets con solapamiento
   * Entrada: `[{1,2}, {2,3}, {3,4}]`
   * Espera: `({1,2,3,4}, 4, 6)` ✅

2. **s10.3.2**: Sets idénticos
   * Entrada: `[{1,2,3}, {1,2,3}]`
   * Espera: `({1,2,3}, 3, 6)` ✅

3. **s10.3.3**: Sets diferentes
   * Entrada: `[{1}, {2}, {3}]`
   * Espera: `({1,2,3}, 3, 3)` ✅

4. **s10.3.4**: Verificación de tipos
   * Entrada: `[{1,2}, {3}]`
   * Verificar: primer elemento es set ✅

5. **s10.3.5**: Lista vacía
   * Entrada: `[]`
   * Espera: `(set(), 0, 0)` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def combine_sets(lista_sets):
    """➕ Combine multiple sets into one.
    Returns (union_set, unique_elements, total_original_elements)"""
    # Your solution here 🛠️
    pass

def test_s10_3():
    # s10.3.1: Sets con solapamiento
    result = combine_sets([{1,2}, {2,3}, {3,4}])
    record_test("s10.3.1 sets con solapamiento", result == ({1,2,3,4}, 4, 6))
    
    # s10.3.2: Sets idénticos
    result = combine_sets([{1,2,3}, {1,2,3}])
    record_test("s10.3.2 sets idénticos", result == ({1,2,3}, 3, 6))
    
    # s10.3.3: Sets diferentes
    result = combine_sets([{1}, {2}, {3}])
    record_test("s10.3.3 sets diferentes", result == ({1,2,3}, 3, 3))
    
    # s10.3.4: Verificación de tipos
    union, unicos, total = combine_sets([{1,2}, {3}])
    types_ok = isinstance(union, set) and isinstance(unicos, int) and isinstance(total, int)
    record_test("s10.3.4 tipos correctos", types_ok)
    
    # s10.3.5: Lista vacía
    result = combine_sets([])
    record_test("s10.3.5 lista vacía", result == (set(), 0, 0))

# 🚀 Run tests
test_s10_3()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Usa `set()` para crear un set vacío inicial 🔗
* Combina con `union_set |= s` o `union_set = union_set.union(s)` ➕
* Suma `len(s)` de cada set para obtener total original 📊
* `len(union_final)` te da los elementos únicos finales 🔍

---

#### 🧠 Motivación 💭

* **Combinación de datos**: fusionar múltiples fuentes 📊
* **Eliminación automática**: los sets manejan duplicados 🚀
* **Arquitectura de información**: combinar colecciones 🏗️

---

### s10.4 ⚖️ **Detector de Diferencias** 🔍🎯

---

#### ❓ Problema 🤔

Implementa una función `find_differences(set1, set2)` que encuentre elementos que están en un set pero no en otro, analizando las diferencias. 📊🔍

---

#### 📜 Descripción 📖

* **Función**: `find_differences(set1, set2) → tuple` 🛠️
* **Entradas**:
  * `set1`, `set2`: sets para comparar diferencias 🎯
* **Salidas**:
  * Tupla con: `(solo_en_set1, solo_en_set2, diferencia_simétrica)` 📊
* **Casos especiales**:
  * Sets idénticos → `(set(), set(), set())` ⚠️
  * Sets disjuntos → diferencia simétrica = unión 🔍
* **Restricciones**:
  * Debe usar operaciones de diferencia de sets 🔗
  * Diferencia simétrica = elementos únicos totales ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **s10.4.1**: Sets con algunos comunes
   * Entrada: `{1,2,3}, {3,4,5}`
   * Espera: `({1,2}, {4,5}, {1,2,4,5})` ✅

2. **s10.4.2**: Sets idénticos
   * Entrada: `{1,2,3}, {1,2,3}`
   * Espera: `(set(), set(), set())` ✅

3. **s10.4.3**: Sets diferentes
   * Entrada: `{1,2}, {3,4}`
   * Espera: `({1,2}, {3,4}, {1,2,3,4})` ✅

4. **s10.4.4**: Verificación de tipos
   * Entrada: `{1}, {2}`
   * Verificar: todos elementos son sets ✅

5. **s10.4.5**: Un set vacío
   * Entrada: `set(), {1,2}`
   * Espera: `(set(), {1,2}, {1,2})` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def find_differences(set1, set2):
    """⚖️ Find differences between two sets.
    Returns (only_in_set1, only_in_set2, symmetric_difference)"""
    # Your solution here 🛠️
    pass

def test_s10_4():
    # s10.4.1: Sets con algunos comunes
    result = find_differences({1,2,3}, {3,4,5})
    record_test("s10.4.1 algunos comunes", result == ({1,2}, {4,5}, {1,2,4,5}))
    
    # s10.4.2: Sets idénticos
    result = find_differences({1,2,3}, {1,2,3})
    record_test("s10.4.2 sets idénticos", result == (set(), set(), set()))
    
    # s10.4.3: Sets diferentes
    result = find_differences({1,2}, {3,4})
    record_test("s10.4.3 sets diferentes", result == ({1,2}, {3,4}, {1,2,3,4}))
    
    # s10.4.4: Verificación de tipos
    solo1, solo2, simetrica = find_differences({1}, {2})
    types_ok = isinstance(solo1, set) and isinstance(solo2, set) and isinstance(simetrica, set)
    record_test("s10.4.4 tipos correctos", types_ok)
    
    # s10.4.5: Un set vacío
    result = find_differences(set(), {1,2})
    record_test("s10.4.5 set vacío", result == (set(), {1,2}, {1,2}))

# 🚀 Run tests
test_s10_4()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Usa `set1 - set2` para elementos solo en set1 🔍
* Usa `set2 - set1` para elementos solo en set2 🔍  
* Usa `set1 ^ set2` o `set1.symmetric_difference(set2)` para diferencia simétrica ⚖️
* La diferencia simétrica también es `(set1 - set2) | (set2 - set1)` 📊

---

#### 🧠 Motivación 💭

* **Análisis comparativo**: encontrar diferencias entre grupos 📊
* **Detección de cambios**: identificar elementos únicos 🔍
* **Lógica de conjuntos**: operaciones matemáticas fundamentales ⚖️

---

### s10.5 ✅ **Validador de Membresías** 🔐🎯

---

#### ❓ Problema 🤔

Implementa una función `validate_membership(set_datos, lista_buscar)` que valide si ciertos elementos están presentes en un set y analice patrones de membresía. 🔍✅

---

#### 📜 Descripción 📖

* **Función**: `validate_membership(set_datos, lista_buscar) → tuple` 🛠️
* **Entradas**:
  * `set_datos`: set donde buscar elementos 🎯
  * `lista_buscar`: lista de elementos a verificar 📝
* **Salidas**:
  * Tupla con: `(elementos_encontrados, total_encontrados, porcentaje_encontrado)` 📊
* **Casos especiales**:
  * Lista vacía → `([], 0, 0.0)` ⚠️
  * Set vacío → `([], 0, 0.0)` 🔍
* **Restricciones**:
  * Debe usar el operador `in` para verificar membresía 🔗
  * Mantener orden de lista original ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **s10.5.1**: Todos encontrados
   * Entrada: `{1,2,3,4,5}, [1,3,5]`
   * Espera: `([1,3,5], 3, 100.0)` ✅

2. **s10.5.2**: Algunos encontrados
   * Entrada: `{1,2,3}, [1,4,5]`
   * Espera: `([1], 1, 33.33)` ✅

3. **s10.5.3**: Ninguno encontrado
   * Entrada: `{1,2,3}, [4,5,6]`
   * Espera: `([], 0, 0.0)` ✅

4. **s10.5.4**: Verificación de tipos
   * Entrada: `{1,2}, [1]`
   * Verificar: primer elemento es lista ✅

5. **s10.5.5**: Lista vacía
   * Entrada: `{1,2,3}, []`
   * Espera: `([], 0, 0.0)` ✅

---

#### 💻 Código Base 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def validate_membership(set_datos, lista_buscar):
    """✅ Validate which elements from list are in the set.
    Returns (found_elements, count_found, percentage_found)"""
    # Your solution here 🛠️
    pass

def test_s10_5():
    # s10.5.1: Todos encontrados
    result = validate_membership({1,2,3,4,5}, [1,3,5])
    record_test("s10.5.1 todos encontrados", result == ([1,3,5], 3, 100.0))
    
    # s10.5.2: Algunos encontrados
    result = validate_membership({1,2,3}, [1,4,5])
    record_test("s10.5.2 algunos encontrados", result == ([1], 1, 33.33))
    
    # s10.5.3: Ninguno encontrado
    result = validate_membership({1,2,3}, [4,5,6])
    record_test("s10.5.3 ninguno encontrado", result == ([], 0, 0.0))
    
    # s10.5.4: Verificación de tipos
    encontrados, total, porcentaje = validate_membership({1,2}, [1])
    types_ok = isinstance(encontrados, list) and isinstance(total, int) and isinstance(porcentaje, float)
    record_test("s10.5.4 tipos correctos", types_ok)
    
    # s10.5.5: Lista vacía
    result = validate_membership({1,2,3}, [])
    record_test("s10.5.5 lista vacía", result == ([], 0, 0.0))

# 🚀 Run tests
test_s10_5()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Usa `elemento in set_datos` para verificar membresía (muy rápido) ✅
* Itera sobre `lista_buscar` y verifica cada elemento 📝
* Calcula porcentaje: `(encontrados / total_buscar) * 100` si total_buscar > 0 📊
* Maneja casos especiales como listas vacías ⚠️

---

#### 🧠 Motivación 💭

* **Validación de datos**: verificar presencia de elementos 🔐
* **Filtros eficientes**: los sets son muy rápidos para búsquedas ⚡
* **Sistemas de seguridad**: validar permisos y accesos ✅

---

## 🎯 **¡Felicitaciones!**

Has completado todos los retos de sets en Python. Ahora dominas:

✅ **Eliminar duplicados** automáticamente con sets  
✅ **Encontrar intersecciones** entre conjuntos de datos  
✅ **Combinar información** con operaciones de unión  
✅ **Detectar diferencias** y elementos únicos  
✅ **Validar membresías** de manera eficiente  

🚀 **Próximo paso**: ¡Usa estos conocimientos de sets con diccionarios para crear estructuras de datos más poderosas!

💪 ¡Sigue practicando y construyendo proyectos increíbles! 🐍✨