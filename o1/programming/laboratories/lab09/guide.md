# **📝 Guía de Retos - Listas en Python 🐍✨**

Esta guía está diseñada para que practiques y domines el uso de listas en Python. Las listas son colecciones ordenadas de elementos que puedes modificar, agregar y eliminar. Son fundamentales para organizar y manipular datos de manera eficiente. ¡Cada reto te ayudará a fortalecer tus habilidades paso a paso! 💪📊

## 🎯 Objetivos

* 📝 **Crear y manipular listas** usando métodos básicos como append(), remove() y len()
* 🔍 **Acceder a elementos** por índice y usar slicing para obtener porciones específicas
* 📊 **Analizar datos en listas** calculando máximos, mínimos y promedios con funciones integradas
* 🔎 **Buscar y contar elementos** usando métodos como count(), index() y el operador in
* 🗂️ **Modificar listas dinámicamente** agregando y eliminando elementos según necesidades
* 📈 **Procesar información** de manera eficiente para resolver problemas cotidianos

---

## 🔍 Visualizando el Concepto con ASCII Art

```
📝 ESTRUCTURA DE UNA LISTA

    mi_lista = [🍎, 🍌, 🍊, 🍇]
                 ↑   ↑   ↑   ↑
               [0] [1] [2] [3]  ← índices

🔧 OPERACIONES BÁSICAS:
┌─────────────────────┐
│ append() → Agregar  │
│ remove() → Eliminar │  
│ len()    → Longitud │
│ [index]  → Acceder  │
└─────────────────────┘
```

---

### **Reto 1: Creador de Lista de Compras 🛒📝**

**Problema**: Crea y manipula una lista de compras agregando productos y mostrando información básica 🎯🛍️

**Descripción**: Las listas son perfectas para almacenar elementos que pueden cambiar. En este ejercicio crearás una lista de compras, agregarás productos y obtendrás información sobre ella como la cantidad total de productos.

🛒 **Operaciones a realizar**:

```plaintext
- Crear lista vacía
- Agregar productos con append()
- Mostrar primer y último producto  
- Calcular total de productos
```

Tu programa debe:

* 📝 Crear una lista vacía para las compras
* ➕ Agregar 4 productos diferentes
* 🔍 Mostrar el primer y último producto
* 📊 Calcular el total de productos en la lista

**Casos de prueba**:

1. Entrada ➡️ productos=["pan","leche","huevos","queso"] → primer="pan", ultimo="queso", total=4
2. Entrada ➡️ productos=["manzanas","arroz","pollo","agua"] → primer="manzanas", ultimo="agua", total=4
3. Entrada ➡️ productos=["pasta","tomate","cebolla","ajo"] → primer="pasta", ultimo="ajo", total=4
4. Entrada ➡️ productos=["yogur","cereales","bananas","miel"] → primer="yogur", ultimo="miel", total=4
5. Entrada ➡️ productos=["salmón","limón","papa","aceite"] → primer="salmón", ultimo="aceite", total=4

**Código base**:

```python
# Reto 1: Creador de Lista de Compras 🛒📝
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

first_product = ""      # Esta variable debe calcularse en base a la lógica del problema
last_product = ""       # Esta variable debe calcularse en base a la lógica del problema
total_products = 0      # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", first_product == "pan" and last_product == "queso" and total_products == 4)
print("🧪 ", first_product == "manzanas" and last_product == "agua" and total_products == 4)
print("🧪 ", first_product == "pasta" and last_product == "ajo" and total_products == 4)
print("🧪 ", first_product == "yogur" and last_product == "miel" and total_products == 4)
print("🧪 ", first_product == "salmón" and last_product == "aceite" and total_products == 4)
```

🧠 **Tips útiles**:

* 📝 Crea la lista con `compras = []`
* ➕ Usa `compras.append("producto")` para agregar
* 🔍 Accede con `compras[0]` (primero) y `compras[-1]` (último)
* 📊 Usa `len(compras)` para obtener el total

🛒 ¡Organiza tus compras como un experto! 🎯✨

---

### **Reto 2: Analizador de Números 🔢📊**

**Problema**: Analiza una lista de números para encontrar el mayor, menor y calcular el promedio 📈🔍

**Descripción**: Una de las tareas más comunes con listas es analizar datos numéricos. Este ejercicio te enseñará a extraer información importante de una colección de números usando métodos integrados de Python.

🔢 **Análisis a realizar**:

```plaintext
- Encontrar el número mayor
- Encontrar el número menor  
- Calcular el promedio
- Contar total de números
```

Tu programa debe:

* 🔍 Encontrar el número más grande de la lista
* 🔍 Encontrar el número más pequeño de la lista
* 🧮 Calcular el promedio de todos los números
* 📊 Mostrar cuántos números hay en total

**Casos de prueba**:

1. Entrada ➡️ números=[5,2,8,1,9] → mayor=9, menor=1, promedio=5.0
2. Entrada ➡️ números=[10,15,3,7,12] → mayor=15, menor=3, promedio=9.4
3. Entrada ➡️ números=[4,4,4,4] → mayor=4, menor=4, promedio=4.0
4. Entrada ➡️ números=[20,30,10] → mayor=30, menor=10, promedio=20.0
5. Entrada ➡️ números=[6,8,2,9,5] → mayor=9, menor=2, promedio=6.0

**Código base**:

```python
# Reto 2: Analizador de Números 🔢📊
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

max_number = 0          # Esta variable debe calcularse en base a la lógica del problema
min_number = 0          # Esta variable debe calcularse en base a la lógica del problema
average = 0.0           # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", max_number == 9 and min_number == 1 and average == 5.0)
print("🧪 ", max_number == 15 and min_number == 3 and average == 9.4)
print("🧪 ", max_number == 4 and min_number == 4 and average == 4.0)
print("🧪 ", max_number == 30 and min_number == 10 and average == 20.0)
print("🧪 ", max_number == 9 and min_number == 2 and average == 6.0)
```

🧠 **Tips útiles**:

* 🔍 Usa `max(lista)` para encontrar el mayor
* 🔍 Usa `min(lista)` para encontrar el menor
* 🧮 Calcula promedio con `sum(lista) / len(lista)`
* 📊 Redondea si es necesario con `round(resultado, 1)`

📊 ¡Analiza datos como un científico! 📈🔬

---

### **Reto 3: Explorador de Slicing 🍰✂️**

**Problema**: Practica el slicing (rebanado) de listas para extraer diferentes porciones de datos 🎯📏

**Descripción**: El slicing es una técnica poderosa que te permite extraer partes específicas de una lista. Es como cortar rebanadas de un pastel - puedes obtener exactamente la porción que necesitas usando índices de inicio y fin.

🍰 **Operaciones de slicing**:

```plaintext
- Primeros elementos: lista[:n]
- Últimos elementos: lista[-n:]
- Elementos del medio: lista[start:end]
- Elementos con saltos: lista[::step]
```

Tu programa debe:

* ✂️ Extraer los primeros 3 elementos
* ✂️ Extraer los últimos 2 elementos  
* ✂️ Extraer elementos del índice 2 al 5
* ✂️ Extraer elementos de posiciones pares

**Casos de prueba**:

1. Entrada ➡️ lista=[1,2,3,4,5,6,7,8] → primeros3=[1,2,3], ultimos2=[7,8], medio=[3,4,5,6], pares=[1,3,5,7]
2. Entrada ➡️ lista=[10,20,30,40,50,60,70,80] → primeros3=[10,20,30], ultimos2=[70,80], medio=[30,40,50,60], pares=[10,30,50,70]
3. Entrada ➡️ lista=['a','b','c','d','e','f','g','h'] → primeros3=['a','b','c'], ultimos2=['g','h'], medio=['c','d','e','f'], pares=['a','c','e','g']
4. Entrada ➡️ lista=[5,15,25,35,45,55,65,75] → primeros3=[5,15,25], ultimos2=[65,75], medio=[25,35,45,55], pares=[5,25,45,65]
5. Entrada ➡️ lista=[2,4,6,8,10,12,14,16] → primeros3=[2,4,6], ultimos2=[14,16], medio=[6,8,10,12], pares=[2,6,10,14]

**Código base**:

```python
# Reto 3: Explorador de Slicing 🍰✂️
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

first_three = []        # Esta variable debe calcularse en base a la lógica del problema
last_two = []           # Esta variable debe calcularse en base a la lógica del problema
middle_slice = []       # Esta variable debe calcularse en base a la lógica del problema
even_positions = []     # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", first_three == [1,2,3] and last_two == [7,8] and middle_slice == [3,4,5,6] and even_positions == [1,3,5,7])
print("🧪 ", first_three == [10,20,30] and last_two == [70,80] and middle_slice == [30,40,50,60] and even_positions == [10,30,50,70])
print("🧪 ", first_three == ['a','b','c'] and last_two == ['g','h'] and middle_slice == ['c','d','e','f'] and even_positions == ['a','c','e','g'])
print("🧪 ", first_three == [5,15,25] and last_two == [65,75] and middle_slice == [25,35,45,55] and even_positions == [5,25,45,65])
print("🧪 ", first_three == [2,4,6] and last_two == [14,16] and middle_slice == [6,8,10,12] and even_positions == [2,6,10,14])
```

🧠 **Tips útiles**:

* ✂️ Usa `lista[:3]` para los primeros 3
* ✂️ Usa `lista[-2:]` para los últimos 2
* ✂️ Usa `lista[2:6]` para índices 2 al 5
* ✂️ Usa `lista[::2]` para posiciones pares

🍰 ¡Corta listas con precisión quirúrgica! ✂️🎯

---

### **Reto 4: Buscador y Contador 🔍📊**

**Problema**: Busca elementos específicos en listas y cuenta cuántas veces aparecen usando métodos de búsqueda 🎯🔢

**Descripción**: Buscar y contar elementos es una tarea fundamental cuando trabajas con datos. Python ofrece métodos integrados como `count()`, `index()` y el operador `in` para hacer estas operaciones de manera eficiente.

🔍 **Operaciones de búsqueda**:

```plaintext
- Verificar existencia: elemento in lista
- Contar apariciones: lista.count(elemento)
- Encontrar posición: lista.index(elemento)
- Buscar múltiples elementos
```

Tu programa debe:

* 🔍 Verificar si un elemento existe en la lista
* 📊 Contar cuántas veces aparece un elemento
* 📍 Encontrar la primera posición de un elemento
* 📈 Verificar si existe otro elemento diferente

**Casos de prueba**:

1. Entrada ➡️ lista=[1,2,3,2,4,2], buscar1=2, buscar2=5 → existe1=True, count1=3, index1=1, existe2=False
2. Entrada ➡️ lista=['a','b','c','b','d'], buscar1='b', buscar2='e' → existe1=True, count1=2, index1=1, existe2=False
3. Entrada ➡️ lista=[10,20,10,30,10], buscar1=10, buscar2=40 → existe1=True, count1=3, index1=0, existe2=False
4. Entrada ➡️ lista=[5,7,5,8,9], buscar1=5, buscar2=8 → existe1=True, count1=2, index1=0, existe2=True
5. Entrada ➡️ lista=[1,1,1,1], buscar1=1, buscar2=2 → existe1=True, count1=4, index1=0, existe2=False

**Código base**:

```python
# Reto 4: Buscador y Contador 🔍📊
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

element1_exists = False # Esta variable debe calcularse en base a la lógica del problema
element1_count = 0      # Esta variable debe calcularse en base a la lógica del problema
element1_index = 0      # Esta variable debe calcularse en base a la lógica del problema
element2_exists = False # Esta variable debe calcularse en base a la lógica del problema

print("🧪 ", element1_exists == True and element1_count == 3 and element1_index == 1 and element2_exists == False)
print("🧪 ", element1_exists == True and element1_count == 2 and element1_index == 1 and element2_exists == False)
print("🧪 ", element1_exists == True and element1_count == 3 and element1_index == 0 and element2_exists == False)
print("🧪 ", element1_exists == True and element1_count == 2 and element1_index == 0 and element2_exists == True)
print("🧪 ", element1_exists == True and element1_count == 4 and element1_index == 0 and element2_exists == False)
```

🧠 **Tips útiles**:

* 🔍 Usa `elemento in lista` para verificar existencia
* 📊 Usa `lista.count(elemento)` para contar
* 📍 Usa `lista.index(elemento)` para encontrar posición
* ⚠️ Verifica existencia antes de usar `index()` para evitar errores

🔍 ¡Busca elementos como un detective experto! 🕵️‍♂️🔎

---

### **Reto 5: Organizador de Datos 🗂️📋**

**Problema**: Modifica listas agregando y eliminando elementos, y reorganiza la información de manera eficiente 🔄✨

**Descripción**: Las listas son mutables, lo que significa que puedes cambiar su contenido después de crearlas. Este ejercicio te enseñará a agregar elementos al final, eliminar elementos específicos y reorganizar datos dinámicamente.

🗂️ **Operaciones de modificación**:

```plaintext
- Agregar elemento: lista.append(elemento)
- Eliminar elemento: lista.remove(elemento)
- Eliminar por posición: lista.pop(índice)
- Reorganizar y contar elementos finales
```

Tu programa debe:

* ➕ Agregar dos elementos nuevos a una lista existente
* ➖ Eliminar un elemento específico de la lista
* 📊 Contar cuántos elementos quedan
* 🔍 Verificar que un elemento específico ya no esté

**Casos de prueba**:

1. Entrada ➡️ inicial=["a","b","c"], agregar=["d","e"], eliminar="b" → final=["a","c","d","e"], total=4, no_esta="b"
2. Entrada ➡️ inicial=[1,2,3], agregar=[4,5], eliminar=2 → final=[1,3,4,5], total=4, no_esta=2
3. Entrada ➡️ inicial=["x","y"], agregar=["z","w"], eliminar="x" → final=["y","z","w"], total=3, no_esta="x"
4. Entrada ➡️ inicial=[10,20], agregar=[30,40], eliminar=10 → final=[20,30,40], total=3, no_esta=10
5. Entrada ➡️ inicial=["red","blue"], agregar=["green","yellow"], eliminar="red" → final=["blue","green","yellow"], total=3, no_esta="red"

**Código base**:

```python
# Reto 5: Organizador de Datos 🗂️📋
# 👇 Inserta tu código aquí y verifica que pase los casos de prueba ✅

final_list = []         # Esta variable debe calcularse en base a la lógica del problema
total_elements = 0      # Esta variable debe calcularse en base a la lógica del problema
element_removed = ""    # Esta variable debe calcularse en base a la lógica del problema (elemento que ya no está)

print("🧪 ", final_list == ["a","c","d","e"] and total_elements == 4 and element_removed not in final_list)
print("🧪 ", final_list == [1,3,4,5] and total_elements == 4 and element_removed not in final_list)
print("🧪 ", final_list == ["y","z","w"] and total_elements == 3 and element_removed not in final_list)
print("🧪 ", final_list == [20,30,40] and total_elements == 3 and element_removed not in final_list)
print("🧪 ", final_list == ["blue","green","yellow"] and total_elements == 3 and element_removed not in final_list)
```

🧠 **Tips útiles**:

* ➕ Usa `lista.append(elemento)` para agregar al final
* ➖ Usa `lista.remove(elemento)` para eliminar por valor
* 📊 Usa `len(lista)` para contar elementos
* 🔍 Verifica con `elemento not in lista`

🗂️ ¡Organiza datos como un profesional! 📋✨

---

## 🎯 **¡Felicitaciones!**

Has completado todos los retos de listas en Python. Ahora dominas:

✅ **Crear y manipular listas** con append() y remove()  
✅ **Analizar datos** encontrando máximos, mínimos y promedios  
✅ **Usar slicing** para extraer porciones específicas  
✅ **Buscar y contar elementos** con métodos integrados  
✅ **Modificar listas dinámicamente** agregando y eliminando datos  

🚀 **Próximo paso**: ¡Combina listas con bucles for para procesar datos de manera más eficiente!

💪 ¡Sigue practicando y construyendo proyectos increíbles! 🐍✨