# ✨ Examen de Estructuras de Datos y Algoritmos 💻📊

Este examen está diseñado para evaluar tus competencias en estructuras de datos y algoritmos utilizando Python 🐍. A través de 4 grupos de ejercicios, pondrás en práctica tus habilidades en diseño algorítmico, recursividad, listas enlazadas y pilas, abordando problemas reales con enfoques eficientes y escalables. Cada ejercicio incluye pruebas automatizadas con `print(True)` para verificar resultados, fomentando buenas prácticas de programación, claridad en el código y análisis computacional. ¡Demuestra todo tu potencial! 🚀🎯

## 🧠 Grupo 1: Diseño de Algoritmos y Análisis de Complejidad 🚀
En esta sección, demostrarás tu capacidad para diseñar algoritmos eficientes, analizar su complejidad temporal y codificar funciones claras y mantenibles en Python 🐍.  
Cada ejercicio debe resolverse en una función con el nombre especificado. No debes modificar la firma de la función.  
⚠️ Debes retornar el tiempo de ejecución junto con el resultado como una tupla.  
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### 🧮 Algoritmo Logarítmico (O(log n))  
Crea una función `logarithmic_complexity(n)` que calcule cuántas veces se debe duplicar un valor inicial de 1 para superar `n`.  
Debe retornar una tupla `(cantidad, tiempo)`.

```python
import time

def logarithmic_complexity(n):
    """Return number of doublings to exceed n."""
    # Your code here
    pass

# ✅ Test cases
print(logarithmic_complexity(10)[0] == 4)
print(logarithmic_complexity(100)[0] == 7)
print(logarithmic_complexity(1000)[0] == 10)
print(isinstance(logarithmic_complexity(100)[0], int))
print(isinstance(logarithmic_complexity(100)[1], float))
```

---

### ➕ Suma de N Números Naturales (O(1))  
Implementa `linear_sum_with_time(n)` que devuelva la suma de los `n` primeros números naturales usando fórmula matemática.  
Debe retornar una tupla `(suma, tiempo)`.

```python
def linear_sum_with_time(n):
    """Return sum of first n natural numbers."""
    # Your code here
    pass

# ✅ Test cases
print(linear_sum_with_time(100)[0] == 5050)
print(linear_sum_with_time(0)[0] == 0)
print(linear_sum_with_time(10)[0] == 55)
print(isinstance(linear_sum_with_time(10)[0], int))
print(isinstance(linear_sum_with_time(10)[1], float))
```

---

### 🔢 Conteo de Números Pares (O(n))  
Define la función `count_even_numbers_with_time(n)` que cuente los números pares desde 0 hasta `n`.  
Debe retornar `(cantidad_de_pares, tiempo)`.

```python
def count_even_numbers_with_time(n):
    """Return count of even numbers from 0 to n."""
    # Your code here
    pass

# ✅ Test cases
print(count_even_numbers_with_time(10)[0] == 6)
print(count_even_numbers_with_time(1)[0] == 1)
print(count_even_numbers_with_time(20)[0] == 11)
print(isinstance(count_even_numbers_with_time(5)[0], int))
print(isinstance(count_even_numbers_with_time(5)[1], float))
```

---

### 🧩 Verificar Números Perfectos (O(n))  
Crea `is_perfect_number_with_time(n)` que devuelva si un número es perfecto (suma de divisores propios = número).  
Debe retornar `(es_perfecto, tiempo)`.

```python
def is_perfect_number_with_time(n):
    """Return True if number is perfect."""
    # Your code here
    pass

# ✅ Test cases
print(is_perfect_number_with_time(6)[0] == True)
print(is_perfect_number_with_time(12)[0] == False)
print(is_perfect_number_with_time(28)[0] == True)
print(isinstance(is_perfect_number_with_time(28)[0], bool))
print(isinstance(is_perfect_number_with_time(28)[1], float))
```

---

### ♻️ Verificación de Duplicados (O(n²))  
Define `has_duplicates_with_time(arr)` que retorne si un arreglo tiene duplicados.  
Debe retornar `(tiene_duplicados, tiempo)`.  
Se permite usar listas unidimensionales, pero puedes proponer mejora futura con matrices.

```python
def has_duplicates_with_time(arr):
    """Return True if array contains duplicates."""
    # Your code here
    pass

# ✅ Test cases
print(has_duplicates_with_time([1, 2, 3, 4])[0] == False)
print(has_duplicates_with_time([1, 2, 2, 3])[0] == True)
print(has_duplicates_with_time([5, 5, 5])[0] == True)
print(isinstance(has_duplicates_with_time([1, 2])[0], bool))
print(isinstance(has_duplicates_with_time([1, 2])[1], float))
```

## 🧪 Grupo 2: Recursividad y Backtracking 🌀
En esta sección, demostrarás tu dominio de la recursividad y la técnica de backtracking aplicadas a la resolución de problemas algorítmicos.  
Cada ejercicio debe ser resuelto con una función recursiva o basada en backtracking según corresponda.  
⚠️ Debes respetar las firmas de funciones y realizar exactamente 5 pruebas por ejercicio (3 funcionales + 2 de tipo).  
🎯 Cada `print(True)` representa 1 punto. ¡Mucha suerte! 🍀

---

### 🔁 Factorial Recursivo  
Implementa `factorial(n)` para calcular el factorial de `n` usando recursividad.

```python
def factorial(n):
    """Return factorial of n recursively."""
    # Your code here
    pass

# ✅ Test cases
print(factorial(0) == 1)
print(factorial(1) == 1)
print(factorial(5) == 120)
print(isinstance(factorial(3), int))
print(isinstance(factorial(6), int))
```

---

### ➕ Suma de Dígitos Recursiva  
Crea la función `sum_of_digits(n)` para retornar la suma de los dígitos de `n` usando recursividad.

```python
def sum_of_digits(n):
    """Return sum of digits of n recursively."""
    # Your code here
    pass

# ✅ Test cases
print(sum_of_digits(123) == 6)
print(sum_of_digits(9) == 9)
print(sum_of_digits(9876) == 30)
print(isinstance(sum_of_digits(10), int))
print(isinstance(sum_of_digits(1), int))
```

---

### 🧠 Secuencia de Fibonacci recursivo
Implementa `fibonacci(n)` para calcular el n-ésimo número de Fibonacci usando memoización con recursión.

```python
def fibonacci(n):
    """Return nth Fibonacci number using recursion."""
    # Your code here
    pass

# ✅ Test cases
print(fibonacci(0) == 0)
print(fibonacci(1) == 1)
print(fibonacci(10) == 55)
print(isinstance(fibonacci(5), int))
print(isinstance(fibonacci(20), int))
```

---

### 🔤 Backtracking - Binarios de Longitud N  
Define `generate_binary_strings(n)` que genere todos los strings binarios posibles de longitud `n`.

```python
def generate_binary_strings(n):
    """Return list of all binary strings of length n."""
    # Your code here
    pass

# ✅ Test cases
print(generate_binary_strings(2) == ['00', '01', '10', '11'])
print(len(generate_binary_strings(3)) == 8)
print('101' in generate_binary_strings(3))
print(isinstance(generate_binary_strings(2), list))
print(isinstance(generate_binary_strings(1)[0], str))
```

---

### 🔀 Backtracking - Combinaciones de T/F de longitud n  
Define `generate_tf_combinations(n)` que devuelva todas las combinaciones posibles de T y F de longitud `n`.

```python
def generate_tf_combinations(n):
    """Return list of all T/F combinations of length n."""
    # Your code here
    pass

# ✅ Test cases
print(generate_tf_combinations(2) == ['TT', 'TF', 'FT', 'FF'])
print(len(generate_tf_combinations(3)) == 8)
print('TF' in generate_tf_combinations(2))
print(isinstance(generate_tf_combinations(2), list))
print(isinstance(generate_tf_combinations(1)[0], str))
```

## 🔗 Grupo 3: Listas Enlazadas (Linked Lists) 📎
En esta sección, demostrarás tu habilidad para construir, manipular y recorrer listas enlazadas en Python 🐍.  
🎯 Cada `print(True)` representa 1 punto. Los ejercicios son graduales: para resolver los más avanzados, necesitas haber construido funcionalidades anteriores como `insert_at_beginning()` y `display()` correctamente.  
En cada ejercicio se te da una versión base de la clase `LinkedList` y `Node`, para que puedas probar como objetos reales (`ll.display()`, `ll.insert_at_beginning(…)`, etc.).  
💡 ¡Usa tu ingenio para mejorar tu implementación, pero no cambies los nombres de los métodos! 😄

---

### 📥 Inserción al Inicio de Lista Enlazada  
Implementa los métodos insert_at_beginning y display.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        """Insert new node at beginning."""
        # Your code here
        pass

    def display(self):
        """Return string representation of the list."""
        # Your code here
        pass

# ✅ Test cases
ll = LinkedList()
ll.insert_at_beginning(3)
print(ll.display() == '3')
ll.insert_at_beginning(2)
print(ll.display() == '2 -> 3')
ll.insert_at_beginning(1)
print(ll.display() == '1 -> 2 -> 3')
ll.insert_at_beginning(0)
print(ll.display() == '0 -> 1 -> 2 -> 3')
print(isinstance(ll.head.data, int))
```

---

### 📌 Inserción al final de la lista  
Agrega el método `insert_at_end(data)` a la clase `LinkedList` que inserte un nodo al final de la lista.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node with data at the end of the list."""
        # Your code here
        pass

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty list"

# ✅ Test cases
ll = LinkedList()
ll.insert_at_end(1)
print(ll.display() == '1')
ll.insert_at_end(2)
print(ll.display() == '1 -> 2')
ll.insert_at_end(3)
print(ll.display() == '1 -> 2 -> 3')
ll.insert_at_beginning(0)
print(ll.display() == '0 -> 1 -> 2 -> 3')
print(isinstance(ll.head.data, int))
```
---

### 📏 Longitud de la lista  
Agrega el método `length()` a la clase `LinkedList` que retorne el número total de nodos.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def length(self):
        """Return number of nodes in the list."""
        # Your code here
        pass

# ✅ Test cases
ll = LinkedList()
print(ll.length() == 0)
ll.insert_at_beginning(3)
print(ll.length() == 1)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
print(ll.length() == 3)
ll.insert_at_beginning(0)
print(ll.length() == 4)
ll = LinkedList()
for i in range(10):
    ll.insert_at_beginning(i)
print(ll.length() == 10)
```

---

### 🔍 Búsqueda de un valor  
Agrega el método `search(self, target)` a la clase `LinkedList`, que retorne `True` si el valor existe en la lista.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        """Insert new node at beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """Return string representation of the list."""
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty list"
    
    def search(self, target):
        """Return True if target is in the list."""
        # Your code here
        pass

# ✅ Test cases
ll = LinkedList()
for value in [3, 2, 1, 0]:
    ll.insert_at_beginning(value)

print(ll.search(2) == True)
print(ll.search(0) == True)
print(ll.search(3) == True)
print(ll.search(4) == False)
print(isinstance(ll.search(1), bool))
```

---

### 🗑️ Eliminar un nodo específico  
Agrega el método `delete(self, target)` que elimine el primer nodo cuyo valor sea igual a `target`.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty list"

    def delete(self, target):
        """Delete first node with target value."""
        # Your code here
        pass

# ✅ Test cases
ll = LinkedList()
for value in [3, 2, 1, 0]:
    ll.insert_at_beginning(value)

ll.delete(2)
print(ll.display() == '0 -> 1 -> 3')
ll.delete(0)
print(ll.display() == '1 -> 3')
ll.delete(3)
print(ll.display() == '1')
ll.delete(1)
print(ll.display() == 'Empty list')
ll.delete(4)
print(ll.display() == 'Empty list')
```

---

### 🔁 Invertir la lista  
Agrega el método `reverse()` a `LinkedList` que invierta el orden de los nodos.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty list"

    def reverse(self):
        """Reverse the linked list."""
        # Your code here
        pass

# ✅ Test cases
ll = LinkedList()
for value in [3, 2, 1, 0]:
    ll.insert_at_beginning(value)

ll.reverse()
print(ll.display() == '3 -> 2 -> 1 -> 0')

ll = LinkedList()
ll.insert_at_beginning(1)
ll.reverse()
print(ll.display() == '1')

ll = LinkedList()
ll.reverse()
print(ll.display() == 'Empty list')

ll = LinkedList()
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.reverse()
print(ll.display() == '2 -> 1')

print(isinstance(ll.display(), str))
```

## 🥞 Grupo 4: Pilas (Stacks) 📚
En esta sección, implementarás una estructura de datos tipo Pila (Stack) usando listas en Python 🐍.  
🎯 Cada `print(True)` representa 1 punto. Los ejercicios están organizados del más simple al más complejo.  
💡 ¡Apóyate en los métodos típicos de pilas: `push`, `pop`, `peek`, etc.!

---

### 🚦 Verificar si la pila está vacía  
Agrega el método `is_empty()` que retorne `True` si la pila está vacía, `False` en caso contrario.

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if stack is empty."""
        # Your code here
        pass

# ✅ Test cases
stack = Stack()
print(stack.is_empty() == True)
stack.items.append(1)
print(stack.is_empty() == False)
stack.items.pop()
print(stack.is_empty() == True)
stack.items.append(0)
print(stack.is_empty() == False)
print(isinstance(stack.is_empty(), bool))
```

---

### ➕ Agregar elementos a la pila  
Implementa el método `push(data)` que inserta un elemento al tope de la pila.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        """Push data onto the stack."""
        # Your code here
        pass

# ✅ Test cases
stack = Stack()
stack.push(1)
print(stack.items == [1])
stack.push(2)
print(stack.items == [1, 2])
stack.push(3)
print(stack.items == [1, 2, 3])
stack.push(0)
print(stack.items == [1, 2, 3, 0])
print(isinstance(stack.items, list))
```

---

### ➖ Quitar el elemento del tope  
Agrega el método `pop()` que elimine y retorne el último elemento insertado (el tope).

```python
class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        """Pop and return top item of the stack."""
        # Your code here
        pass

# ✅ Test cases
stack = Stack()
stack.items = [1, 2, 3]
print(stack.pop() == 3)
print(stack.pop() == 2)
print(stack.pop() == 1)
stack.items = []
print(stack.pop() == None)
print(isinstance(stack.items, list))
```

---

### 👁️ Ver el elemento en el tope sin eliminarlo  
Agrega el método `peek()` que retorne el valor en el tope de la pila sin eliminarlo.

```python
class Stack:
    def __init__(self):
        self.items = []

    def peek(self):
        """Return top item without removing it."""
        # Your code here
        pass

# ✅ Test cases
stack = Stack()
stack.items = [10, 20, 30]
print(stack.peek() == 30)
stack.items.pop()
print(stack.peek() == 20)
stack.items.clear()
print(stack.peek() == None)
stack.items.append(99)
print(stack.peek() == 99)
print(isinstance(stack.peek(), int) or stack.peek() == None)
```

---

### 📦 Tamaño de la pila  
Implementa el método `size()` que retorne cuántos elementos hay en la pila.

```python
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        """Return number of elements in the stack."""
        # Your code here
        pass

# ✅ Test cases
stack = Stack()
print(stack.size() == 0)
stack.items = [1]
print(stack.size() == 1)
stack.items = [1, 2, 3, 4]
print(stack.size() == 4)
stack.items.pop()
print(stack.size() == 3)
print(isinstance(stack.size(), int))
```

---

### 🧱 Implementar Stack con nodos enlazados  
Crea una clase `Node` y `LinkedStack` que funcione como una pila. Implementa `push(data)`.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """Push element using linked nodes."""
        # Your code here
        pass

    def display(self):
        current = self.top
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty"

# ✅ Test cases
s = LinkedStack()
s.push(1)
print(s.display() == "1")
s.push(2)
print(s.display() == "2 -> 1")
s.push(3)
print(s.display() == "3 -> 2 -> 1")
s.push(4)
print(s.display() == "4 -> 3 -> 2 -> 1")
print(isinstance(s.top.data, int))
```

---

### 🧽 Eliminar elemento (pop) en Stack enlazado  
Agrega el método `pop()` a `LinkedStack` para eliminar el tope de la pila.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Pop top element from linked stack."""
        # Your code here
        pass

    def display(self):
        current = self.top
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty"

# ✅ Test cases
s = LinkedStack()
for val in [1, 2, 3]:
    s.push(val)
print(s.pop() == 3)
print(s.pop() == 2)
print(s.display() == "1")
print(s.pop() == 1)
print(s.pop() == None)
```

---

### 🧼 Ver el tope en Stack enlazado  
Agrega `peek()` a `LinkedStack` para retornar el valor sin eliminarlo.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        """Return top value of linked stack."""
        # Your code here
        pass

# ✅ Test cases
s = LinkedStack()
print(s.peek() == None)
s.push(10)
print(s.peek() == 10)
s.push(20)
print(s.peek() == 20)
s.push(30)
print(s.peek() == 30)
s.pop = lambda: setattr(s, 'top', s.top.next)
s.pop()
print(s.peek() == 20)
```
