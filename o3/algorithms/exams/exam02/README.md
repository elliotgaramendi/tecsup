# 📘 Examen de Árboles, Colas y Pilas en Estructuras de Datos 🌳🔄📚

Este proyecto contiene la resolución completa del **examen de estructuras de datos avanzadas**, enfocado en implementaciones prácticas en Python. Cada sección evalúa competencias específicas relacionadas con la implementación de estructuras de datos fundamentales mediante ejercicios graduales y pruebas automatizadas.

---

## 📂 Contenido del Proyecto

| Grupo | Tema Principal             | Descripción                                                          |
| ----- | -------------------------- | -------------------------------------------------------------------- |
| 1     | Colas (Queues)             | Implementaciones básicas con arreglos y listas enlazadas             |
| 2     | Colas Avanzadas            | Colas circulares, colas dobles (deque) y sus operaciones             |
| 3     | Árboles Binarios           | Operaciones de inserción y recorridos (inorden, preorden, postorden) |
| 4     | Árboles Binarios Avanzados | Cálculo de altura, tamaño, búsqueda y operaciones específicas        |

---

## 🚀 Tecnologías Usadas
- Lenguaje: **Python 3.8+**
- No se utilizan librerías externas
- Pruebas automatizadas con verificación directa `print(condición == True)`
- Funciones `test()` para registro y contabilización de resultados

---

## 🧪 Estructura de Evaluación
Cada ejercicio contiene **5 pruebas automatizadas** que validan:
- Funcionalidad en casos normales
- Comportamiento en casos límite (estructuras vacías)
- Validación de tipos de datos retornados
- Operaciones combinadas
- Estados inconsistentes o errores esperados

---

## 🧾 Archivos Clave

| Archivo     | Propósito                                                  |
| ----------- | ---------------------------------------------------------- |
| `main.py`   | Implementación completa con todas las soluciones y pruebas |
| `README.md` | Documentación del proyecto y guía técnica                  |

---

## 📚 Estructuras Implementadas

### 🚶 Colas (Queues)
- Cola Simple (basada en lista)
- Cola con Listas Enlazadas
- Cola Circular

### 🔄 Colas Avanzadas
- Cola Doble (Deque)
- Cola Circular con arreglos
- Cola Circular con Listas Enlazadas

### 🌳 Árboles Binarios
- Inserción de nodos (izquierda/derecha)
- Recorridos básicos (inorden, preorden, postorden)

### 🔍 Árboles Binarios Avanzados
- Cálculo de altura y tamaño
- Búsqueda en Árboles Binarios de Búsqueda (BST)
- Conteo de hojas

---

## 📈 Métodos Implementados

| Grupo | Método                  | Descripción                                         |
| ----- | ----------------------- | --------------------------------------------------- |
| 1     | `dequeue()`             | Extrae elemento al frente de la cola                |
| 1     | `peek()`                | Visualiza elemento al frente sin eliminarlo         |
| 1     | `is_empty()`            | Verifica si la cola está vacía                      |
| 1     | `size()`                | Calcula número de elementos en la cola              |
| 1     | `display()`             | Muestra representación visual de la cola            |
| 2     | `add_front()`           | Añade elemento al frente de una cola doble          |
| 2     | `enqueue()`             | Añade elemento a una cola circular                  |
| 2     | `dequeue()`             | Extrae elemento de una cola circular                |
| 2     | `enqueue()`             | Añade elemento a cola circular con listas enlazadas |
| 2     | `remove_rear()`         | Elimina elemento del final de una cola doble        |
| 3     | `insert_left()`         | Inserta nodo como hijo izquierdo                    |
| 3     | `inorder_traversal()`   | Recorre el árbol en orden (izq-raíz-der)            |
| 3     | `preorder_traversal()`  | Recorre el árbol en preorden (raíz-izq-der)         |
| 3     | `postorder_traversal()` | Recorre el árbol en postorden (izq-der-raíz)        |
| 3     | `insert_right()`        | Inserta nodo como hijo derecho                      |
| 4     | `height()`              | Calcula altura del árbol                            |
| 4     | `size()`                | Cuenta número total de nodos                        |
| 4     | `get_root()`            | Obtiene valor de la raíz                            |
| 4     | `search()`              | Busca valor en árbol binario de búsqueda            |
| 4     | `count_leaves()`        | Cuenta número de nodos hoja                         |

---

## 📚 Estilo del Código
- Docstrings informativos en todas las funciones
- Comentarios explicativos con emojis para mejor visualización
- Implementaciones iterativas para evitar problemas de recursión
- Verificación adecuada de casos límite

---

## ✅ Ejecución
Para ejecutar todas las implementaciones y pruebas:
```bash
python main.py
```

---

## 🎉 Resultado Final
Al finalizar la ejecución, el programa muestra:
- Resumen de todos los tests ejecutados
- Conteo de pruebas aprobadas ✅ y fallidas ❌

---

## 🌟 Consideraciones Pedagógicas
- Las implementaciones priorizan claridad sobre optimización extrema
- Se incluyen versiones iterativas para evitar errores de recursión
- Las pruebas abarcan casos comunes y casos límite
- Cada estructura parte de conceptos fundamentales y avanza en complejidad

---

Este examen está diseñado para evaluar comprensión profunda de estructuras de datos fundamentales, con énfasis en implementaciones prácticas que reflejan situaciones reales. ¡Buena suerte! 🍀