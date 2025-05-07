# ✨ Examen de Árboles, Colas y Pilas en Estructuras de Datos 🌳🔄📚

Este segundo examen está diseñado para evaluar tus competencias en estructuras de datos avanzadas utilizando Python 🐍. A través de 4 grupos de ejercicios, pondrás en práctica tus habilidades en colas 🔄, colas avanzadas 📊, árboles 🌳 y árboles avanzados 🔎. Cada ejercicio incluye pruebas automatizadas con `print(True)` para verificar resultados. ¡Demuestra todo tu potencial! 🚀🎯

## 🚶 Colas (Queues) 🚶‍♀️
En esta sección, demostrarás tu dominio de las colas (estructuras FIFO), implementando operaciones fundamentales en distintos tipos de colas 🔄.  
Cada ejercicio debe resolverse completando el método especificado sin modificar su firma.  
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### 🔁 dequeue() en Cola Simple 🔄
Implementa el método `dequeue()` para una cola básica que elimine y retorne el elemento al frente.

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        # Tu código aquí 🚀
        pass

# ✅ Test cases
q = Queue()
print(q.dequeue() == None) # 📭 Cola vacía
q.enqueue(1)
q.enqueue(2)
print(q.dequeue() == 1) # 🥇 Primer elemento
print(q.dequeue() == 2) # 🥈 Segundo elemento
print(q.dequeue() == None) # 📭 Cola vacía de nuevo
q.enqueue(3)
print(isinstance(q.dequeue(), int)) # 🔢 Tipo correcto
```

---

### 👀 peek() en Cola Simple 🔍
Implementa el método `peek()` para una cola que permita ver el elemento al frente sin eliminarlo.

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def peek(self):
        # Tu código aquí 👁️
        pass

# ✅ Test cases
q = Queue()
print(q.peek() == None) # 📭 Cola vacía
q.enqueue("primero")
print(q.peek() == "primero") # 👁️ Ver sin eliminar
q.enqueue("segundo")
print(q.peek() == "primero") # 🥇 Sigue siendo el primero
q.items = []
print(q.peek() == None) # 📭 Cola vacía de nuevo
print(isinstance(q.peek(), str) or q.peek() == None) # 📝 Tipo correcto
```

---

### 📊 is_empty() en Cola con Listas Enlazadas 📋
Implementa el método `is_empty()` para una cola implementada con listas enlazadas.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node
    
    def is_empty(self):
        # Tu código aquí 🧠
        pass

# ✅ Test cases
q = LinkedQueue()
print(q.is_empty() == True) # ✅ Cola vacía inicial
q.enqueue(1)
print(q.is_empty() == False) # ❌ No está vacía
q.front = None
q.rear = None
print(q.is_empty() == True) # ✅ Vaciada manualmente
q.enqueue("test")
print(q.is_empty() == False) # ❌ Ya no está vacía
print(isinstance(q.is_empty(), bool)) # 🔍 Tipo booleano
```

---

### 🔢 size() en Cola Circular ⭕
Implementa el método `size()` para una cola circular que retorne la cantidad de elementos.

```python
class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0
    
    def enqueue(self, item):
        if self.count < self.capacity:
            if self.rear == -1:
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.count += 1
            return True
        return False
    
    def size(self):
        # Tu código aquí 📏
        pass

# ✅ Test cases
cq = CircularQueue(3)
print(cq.size() == 0) # 📭 Cola vacía
cq.enqueue("A")
print(cq.size() == 1) # 🥇 Un elemento
cq.enqueue("B")
cq.enqueue("C")
print(cq.size() == 3) # 🧮 Tres elementos
cq.count = 0
print(cq.size() == 0) # 📭 Contador en cero
print(isinstance(cq.size(), int)) # 🔢 Tipo numérico
```

---

### 📝 display() en Cola Simple 📋
Implementa el método `display()` que devuelva una representación en cadena de la cola.

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)
    
    def display(self):
        # Tu código aquí 📝
        pass

# ✅ Test cases
q = Queue()
print(q.display() == "[]") # 📭 Cola vacía
q.enqueue(1)
print(q.display() == "[1]") # 🥇 Un elemento
q.enqueue(2)
q.enqueue(3)
print(q.display() == "[1, 2, 3]") # 📊 Tres elementos
q.dequeue()
print(q.display() == "[2, 3]") # 🔄 Después de dequeue
print(isinstance(q.display(), str)) # 📝 Tipo cadena
```

## 🔄 Colas Avanzadas 📊
En esta sección, demostrarás tu comprensión de las colas con comportamientos avanzados como colas circulares, de prioridad y colas dobles (deque) 🧩.  
Cada ejercicio debe resolverse completando el método especificado sin modificar su firma.  
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### 📋 add_front() en Cola Doble (Deque) 📝
Implementa el método `add_front()` para una cola doble (deque) que permita añadir elementos al frente.

```python
class Deque:
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        # Tu código aquí 🎯
        pass
    
    def add_rear(self, item):
        self.items.append(item)

# ✅ Test cases
dq = Deque()
dq.add_front(1)
print(dq.items == [1]) # 🥇 Un elemento
dq.add_front(2)
print(dq.items == [2, 1]) # 🔄 Orden correcto
dq.add_rear(3)
print(dq.items == [2, 1, 3]) # 📊 Tres elementos en orden
dq.add_front(4)
print(dq.items == [4, 2, 1, 3]) # 🎯 Insertado al frente
print(isinstance(dq.items, list)) # 📋 Tipo lista
```

---

### ⭕ enqueue() en Cola Circular 🔄
Implementa el método `enqueue()` para una cola circular que añada elementos circulando cuando llega al final.

```python
class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        # Tu código aquí 🔄
        pass

# ✅ Test cases
cq = CircularQueue(2)
print(cq.enqueue("A") == True) # ✅ Primer elemento
print(cq.front == 0 and cq.rear == 0) # 🎯 Posiciones correctas
print(cq.enqueue("B") == True) # ✅ Segundo elemento
print(cq.enqueue("C") == False) # ❌ Tercer elemento
print(isinstance(cq.enqueue("X"), bool)) # 🔍 Tipo booleano
```

---

### 🔄 dequeue() en Cola Circular Simple ⭕
Implementa el método `dequeue()` para una cola circular que extraiga elementos del frente.

```python
class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0
    
    def enqueue(self, item):
        if self.count < self.capacity:
            if self.rear == -1:
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.count += 1
            return True
        return False
    
    def dequeue(self):
        # Tu código aquí 🔄
        pass

# ✅ Test cases
cq = CircularQueue(3)
print(cq.dequeue() == None) # 📭 Cola vacía
cq.enqueue("A")
cq.enqueue("B")
print(cq.dequeue() == "A") # 🥇 Primer elemento
print(cq.dequeue() == "B") # 🥈 Segundo elemento
print(cq.dequeue() == None) # 📭 Cola vacía de nuevo
cq.enqueue("C")
print(isinstance(cq.dequeue(), str)) # 📝 Tipo correcto
```

---

### 🔄 enqueue() en Cola Circular con Listas Enlazadas 🔗
Implementa el método `enqueue()` para una cola circular basada en listas enlazadas.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedQueue:
    def __init__(self):
        self.rear = None
        self.size = 0
    
    def enqueue(self, data):
        # Tu código aquí 🔗
        pass
    
    def display(self):
        if not self.rear:
            return []
        
        result = []
        current = self.rear.next  # Comenzar desde el frente
        while True:
            result.append(current.data)
            current = current.next
            if current == self.rear.next:  # Vuelta completa
                break
        return result

# ✅ Test cases
clq = CircularLinkedQueue()
clq.enqueue("A")
print(clq.rear.data == "A") # 🥇 Primer elemento
print(clq.rear.next == clq.rear) # 🔄 Apunta a sí mismo
clq.enqueue("B")
print(clq.display() == ["A", "B"]) # 📊 Cola tiene A y B
clq.enqueue("C")
print(clq.display() == ["A", "B", "C"]) # 📊 Cola tiene A, B y C
print(isinstance(clq.rear, Node)) # 🔍 Tipo nodo
```

---

### 🔄 remove_rear() en Cola Doble (Deque) 📤
Implementa el método `remove_rear()` para una cola doble que elimine y retorne el elemento al final.

```python
class Deque:
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        self.items.insert(0, item)
    
    def add_rear(self, item):
        self.items.append(item)
    
    def remove_front(self):
        if not self.items:
            return None
        return self.items.pop(0)
    
    def remove_rear(self):
        # Tu código aquí 📤
        pass

# ✅ Test cases
dq = Deque()
print(dq.remove_rear() == None) # 📭 Deque vacío
dq.add_rear(1)
print(dq.remove_rear() == 1) # 🥇 Un elemento
dq.add_rear(2)
dq.add_rear(3)
print(dq.remove_rear() == 3) # 🔄 Último elemento
dq.add_front(4)
print(dq.remove_rear() == 2) # 📊 Elemento al final
print(isinstance(dq.remove_rear(), int) or dq.remove_rear() == None) # 📝 Tipo correcto
```

## 🌳 Árboles Binarios 🌿
En esta sección, demostrarás tu comprensión de los árboles binarios, su estructura y las operaciones de recorrido 🌱.  
Cada ejercicio debe resolverse completando el método especificado sin modificar su firma.  
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### 🌱 insert_left() en Nodo de Árbol 🌿
Implementa el método `insert_left()` para insertar un nodo como hijo izquierdo en un árbol binario.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        # Tu código aquí 🌿
        pass

# ✅ Test cases
root = TreeNode(1)
left = root.insert_left(2)
print(root.left.value == 2) # 🌿 Hijo izquierdo creado
print(left.value == 2) # 🎯 Retorna el nuevo nodo
left_child = left.insert_left(3)
print(root.left.left.value == 3) # 🌳 Estructura correcta
old_left = TreeNode(4)
root.left = old_left
new_left = root.insert_left(5)
print(new_left.left.value == 4) # 🔄 Nodo anterior como hijo
print(isinstance(new_left, TreeNode)) # 🔍 Tipo TreeNode
```

---

### 🚶‍♂️ inorder_traversal() en Árbol Binario 🔍
Implementa el método `inorder_traversal()` para realizar un recorrido inorden (izquierda-raíz-derecha) en un árbol binario.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def inorder_traversal(self, node=None, result=None):
        # Tu código aquí 🔄
        pass

# ✅ Test cases
# Árbol:      1
#           /   \
#          2     3
#         / \     \
#        4   5     6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

tree = BinaryTree(root)
print(tree.inorder_traversal() == [4, 2, 5, 1, 3, 6]) # 🔍 Recorrido inorden correcto
single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.inorder_traversal() == [42]) # 🌱 Árbol de un solo nodo
empty_tree = BinaryTree()
print(empty_tree.inorder_traversal() == []) # 📭 Árbol vacío
tree.root = TreeNode(10)
print(tree.inorder_traversal() == [10]) # 🎯 Otro árbol simple
print(isinstance(tree.inorder_traversal(), list)) # 📋 Tipo lista
```

---

### 🔄 preorder_traversal() en Árbol Binario 🌲
Implementa el método `preorder_traversal()` para realizar un recorrido preorden (raíz-izquierda-derecha) en un árbol binario.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def preorder_traversal(self, node=None, result=None):
        # Tu código aquí 🌲
        pass

# ✅ Test cases
# Árbol:      1
#           /   \
#          2     3
#         / \     \
#        4   5     6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

tree = BinaryTree(root)
print(tree.preorder_traversal() == [1, 2, 4, 5, 3, 6]) # 🔍 Recorrido preorden correcto
single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.preorder_traversal() == [42]) # 🌱 Árbol de un solo nodo
empty_tree = BinaryTree()
print(empty_tree.preorder_traversal() == []) # 📭 Árbol vacío
tree.root = TreeNode(10)
print(tree.preorder_traversal() == [10]) # 🎯 Otro árbol simple
print(isinstance(tree.preorder_traversal(), list)) # 📋 Tipo lista
```

---

### 🚶‍♀️ postorder_traversal() en Árbol Binario 🌴
Implementa el método `postorder_traversal()` para realizar un recorrido postorden (izquierda-derecha-raíz) en un árbol binario.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def postorder_traversal(self, node=None, result=None):
        # Tu código aquí 🌴
        pass

# ✅ Test cases
# Árbol:      1
#           /   \
#          2     3
#         / \     \
#        4   5     6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

tree = BinaryTree(root)
print(tree.postorder_traversal() == [4, 5, 2, 6, 3, 1]) # 🔍 Recorrido postorden correcto
single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.postorder_traversal() == [42]) # 🌱 Árbol de un solo nodo
empty_tree = BinaryTree()
print(empty_tree.postorder_traversal() == []) # 📭 Árbol vacío
tree.root = TreeNode(10)
print(tree.postorder_traversal() == [10]) # 🎯 Otro árbol simple
print(isinstance(tree.postorder_traversal(), list)) # 📋 Tipo lista
```

---

### 🌿 insert_right() en Nodo de Árbol 🌲
Implementa el método `insert_right()` para insertar un nodo como hijo derecho en un árbol binario.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_right(self, value):
        # Tu código aquí 🌲
        pass

# ✅ Test cases
root = TreeNode(1)
right = root.insert_right(2)
print(root.right.value == 2) # 🌲 Hijo derecho creado
print(right.value == 2) # 🎯 Retorna el nuevo nodo
right_child = right.insert_right(3)
print(root.right.right.value == 3) # 🌳 Estructura correcta
old_right = TreeNode(4)
root.right = old_right
new_right = root.insert_right(5)
print(new_right.right.value == 4) # 🔄 Nodo anterior como hijo
print(isinstance(new_right, TreeNode)) # 🔍 Tipo TreeNode
```

## 🔍 Árboles Binarios Avanzados 🔎
En esta sección, demostrarás tu comprensión de operaciones más complejas en árboles binarios, como el cálculo de altura, búsqueda por niveles y árboles de búsqueda binaria 🧠.  
Cada ejercicio debe resolverse completando el método especificado sin modificar su firma.  
Cada `print(True)` equivale a ✅ 1 punto. Solo se evaluarán los 5 casos especificados.

---

### 📏 height() en Árbol Binario 📐
Implementa el método `height()` que calcule la altura de un árbol binario (la longitud del camino más largo desde la raíz hasta una hoja).

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def height(self, node=None):
        # Tu código aquí 📏
        pass

# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.height() == -1) # 📭 Árbol vacío
single_node_tree = BinaryTree(TreeNode(1))
print(single_node_tree.height() == 0) # 🌱 Árbol de un solo nodo

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
tree = BinaryTree(root)
print(tree.height() == 2) # 📏 Altura 2

deep_root = TreeNode(1)
deep_root.left = TreeNode(2)
deep_root.left.left = TreeNode(3)
deep_root.left.left.left = TreeNode(4)
deep_tree = BinaryTree(deep_root)
print(deep_tree.height() == 3) # 📐 Altura 3

print(isinstance(deep_tree.height(), int)) # 🔢 Tipo numérico
```

---

### 🍂 size() en Árbol Binario 📏
Implementa el método `size()` que calcule el número total de nodos en un árbol binario.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def size(self, node=None):
        # Tu código aquí 📏
        pass

# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.size() == 0) # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.size() == 1) # 🌱 Árbol de un solo nodo

# Árbol:      1
#           /   \
#          2     3
#         / \     \
#        4   5     6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

tree = BinaryTree(root)
print(tree.size() == 6) # 📊 Árbol con 6 nodos

tree.root = TreeNode(10)
tree.root.left = TreeNode(20)
print(tree.size() == 2) # 🎯 Árbol con 2 nodos

print(isinstance(tree.size(), int)) # 🔢 Tipo numérico
```

---

### 🔍 search() en Árbol Binario de Búsqueda 🔎
Implementa el método `search()` para buscar un valor en un Árbol Binario de Búsqueda (BST).

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        
        def _insert(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    _insert(node.left, value)
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    _insert(node.right, value)
        
        _insert(self.root, value)
    
    def search(self, value):
        # Tu código aquí 🔎
        pass

# ✅ Test cases
bst = BinarySearchTree()
print(bst.search(10) == False) # 📭 Árbol vacío

bst.insert(10)
print(bst.search(10) == True) # ✅ Valor encontrado
print(bst.search(20) == False) # ❌ Valor no encontrado

bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
print(bst.search(7) == True) # 🎯 Valor en subárbol

print(isinstance(bst.search(5), bool)) # 🔍 Tipo booleano
```

---

### 🌲 get_root() en Árbol Binario 🌱
Implementa el método `get_root()` para obtener el valor de la raíz del árbol binario.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def get_root(self):
        # Tu código aquí 🌱
        pass

# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.get_root() == None) # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.get_root() == 42) # 🌱 Árbol de un solo nodo

# Árbol:      1
#           /   \
#          2     3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
tree = BinaryTree(root)
print(tree.get_root() == 1) # 🌲 Raíz es 1

# Cambiar la raíz
tree.root = TreeNode(10)
print(tree.get_root() == 10) # 🔄 Raíz cambiada

print(isinstance(tree.get_root(), int) or tree.get_root() == None) # 🔢 Tipo correcto
```

---

### 🍃 count_leaves() en Árbol Binario 🍂
Implementa el método `count_leaves()` para contar el número de nodos hoja (sin hijos) en un árbol binario.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def count_leaves(self, node=None):
        # Tu código aquí 🍃
        pass

# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.count_leaves() == 0) # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(1))
print(single_node_tree.count_leaves() == 1) # 🌱 Un solo nodo es hoja

# Árbol:      1
#           /   \
#          2     3
#         / \     \
#        4   5     6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
tree = BinaryTree(root)
print(tree.count_leaves() == 3) # 🍃 Hojas: 4, 5, 6

balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_tree = BinaryTree(balanced_root)
print(balanced_tree.count_leaves() == 2) # 🍂 Hojas: 2, 3

print(isinstance(tree.count_leaves(), int)) # 🔢 Tipo numérico
```