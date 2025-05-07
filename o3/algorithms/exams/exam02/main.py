"""Soluciones para el examen de Árboles, Colas y Pilas en Estructuras de Datos."""

# Lista para guardar resultados de pruebas
results = []


def test(title, condition):
    """Ejecuta un test y guarda el resultado."""
    emoji = "✅" if condition else "❌"
    results.append(f"{emoji} {title}")

# =====================================================================
# 🚶 Colas (Queues) 🚶‍♀️
# =====================================================================

# 🔁 dequeue() en Cola Simple 🔄
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        """Elimina y retorna el elemento al frente de la cola."""
        # Si la cola está vacía, retornamos None
        if not self.items:
            return None
        # Removemos y retornamos el primer elemento (FIFO)
        return self.items.pop(0)


# ✅ Test cases
q = Queue()
test("1.1 dequeue cola vacía", q.dequeue() == None)  # 📭 Cola vacía
q.enqueue(1)
q.enqueue(2)
test("1.2 dequeue primer elemento", q.dequeue() == 1)  # 🥇 Primer elemento
test("1.3 dequeue segundo elemento", q.dequeue() == 2)  # 🥈 Segundo elemento
test("1.4 dequeue cola vacía de nuevo",
     q.dequeue() == None)  # 📭 Cola vacía de nuevo
q.enqueue(3)
test("1.5 dequeue tipo correcto", isinstance(
    q.dequeue(), int))  # 🔢 Tipo correcto


# 👀 peek() en Cola Simple 🔍
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def peek(self):
        """Retorna el elemento al frente sin eliminarlo."""
        # Si la cola está vacía, retornamos None
        if not self.items:
            return None
        # Retornamos el primer elemento sin eliminarlo
        return self.items[0]


# ✅ Test cases
q = Queue()
test("2.1 peek cola vacía", q.peek() == None)  # 📭 Cola vacía
q.enqueue("primero")
test("2.2 peek muestra primer elemento", q.peek()
     == "primero")  # 👁️ Ver sin eliminar
q.enqueue("segundo")
test("2.3 peek sigue mostrando primer elemento",
     q.peek() == "primero")  # 🥇 Sigue siendo el primero
q.items = []
test("2.4 peek cola vacía de nuevo", q.peek() == None)  # 📭 Cola vacía de nuevo
test("2.5 peek tipo correcto", isinstance(q.peek(), str)
     or q.peek() == None)  # 📝 Tipo correcto


# 📊 is_empty() en Cola con Listas Enlazadas 📋
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
        """Verifica si la cola está vacía."""
        # La cola está vacía si front es None
        return self.front is None


# ✅ Test cases
q = LinkedQueue()
test("3.1 is_empty cola vacía inicial",
     q.is_empty() == True)  # ✅ Cola vacía inicial
q.enqueue(1)
test("3.2 is_empty cola con elementos",
     q.is_empty() == False)  # ❌ No está vacía
q.front = None
q.rear = None
test("3.3 is_empty cola vaciada manualmente",
     q.is_empty() == True)  # ✅ Vaciada manualmente
q.enqueue("test")
test("3.4 is_empty cola con elementos de nuevo",
     q.is_empty() == False)  # ❌ Ya no está vacía
test("3.5 is_empty tipo correcto", isinstance(
    q.is_empty(), bool))  # 🔍 Tipo booleano


# 🔢 size() en Cola Circular ⭕
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
        """Retorna el número de elementos en la cola circular."""
        # Retornamos el contador de elementos
        return self.count


# ✅ Test cases
cq = CircularQueue(3)
test("4.1 size cola vacía", cq.size() == 0)  # 📭 Cola vacía
cq.enqueue("A")
test("4.2 size cola con un elemento", cq.size() == 1)  # 🥇 Un elemento
cq.enqueue("B")
cq.enqueue("C")
test("4.3 size cola con tres elementos", cq.size() == 3)  # 🧮 Tres elementos
cq.count = 0
test("4.4 size después de reiniciar contador",
     cq.size() == 0)  # 📭 Contador en cero
test("4.5 size tipo correcto", isinstance(cq.size(), int))  # 🔢 Tipo numérico


# 📝 display() en Cola Simple 📋
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
        """Retorna una representación en cadena de la cola."""
        # Convertimos la lista a string para mostrarla
        return str(self.items)


# ✅ Test cases
q = Queue()
test("5.1 display cola vacía", q.display() == "[]")  # 📭 Cola vacía
q.enqueue(1)
test("5.2 display cola con un elemento", q.display() == "[1]")  # 🥇 Un elemento
q.enqueue(2)
q.enqueue(3)
test("5.3 display cola con tres elementos",
     q.display() == "[1, 2, 3]")  # 📊 Tres elementos
q.dequeue()
test("5.4 display después de dequeue", q.display()
     == "[2, 3]")  # 🔄 Después de dequeue
test("5.5 display tipo correcto", isinstance(q.display(), str))  # 📝 Tipo cadena


# =====================================================================
# 🔄 Colas Avanzadas 📊
# =====================================================================

# 📋 add_front() en Cola Doble (Deque) 📝
class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Añade un elemento al frente de la cola doble."""
        # Insertamos al inicio de la lista
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)


# ✅ Test cases
dq = Deque()
dq.add_front(1)
test("6.1 add_front en deque vacío", dq.items == [1])  # 🥇 Un elemento
dq.add_front(2)
test("6.2 add_front orden correcto", dq.items == [2, 1])  # 🔄 Orden correcto
dq.add_rear(3)
test("6.3 combinación add_front y add_rear",
     dq.items == [2, 1, 3])  # 📊 Tres elementos en orden
dq.add_front(4)
test("6.4 add_front elemento adicional", dq.items ==
     [4, 2, 1, 3])  # 🎯 Insertado al frente
test("6.5 add_front tipo correcto", isinstance(dq.items, list))  # 📋 Tipo lista


# ⭕ enqueue() en Cola Circular 🔄
class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        """Añade un elemento a la cola circular."""
        # Si la cola está llena
        if (self.rear + 1) % self.capacity == self.front:
            return False

        # Si la cola está vacía
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            # Avanzamos el puntero rear de forma circular
            self.rear = (self.rear + 1) % self.capacity

        # Insertamos el elemento y retornamos éxito
        self.queue[self.rear] = item
        return True


# ✅ Test cases
cq = CircularQueue(2)
test("7.1 enqueue primer elemento", cq.enqueue("A") == True)  # ✅ Primer elemento
test("7.2 enqueue posiciones correctas", cq.front ==
     0 and cq.rear == 0)  # 🎯 Posiciones correctas
test("7.3 enqueue segundo elemento", cq.enqueue(
    "B") == True)  # ✅ Segundo elemento
test("7.4 enqueue tercer elemento", cq.enqueue("C") == False)  # ❌ Cola llena
test("7.5 enqueue tipo correcto", isinstance(
    cq.enqueue("X"), bool))  # 🔍 Tipo booleano


# 🔄 dequeue() en Cola Circular Simple ⭕
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
        """Elimina y retorna el elemento al frente de la cola circular."""
        # Si la cola está vacía
        if self.count == 0:
            return None

        # Guardamos el elemento a retornar
        item = self.queue[self.front]

        # Marcamos la posición como vacía
        self.queue[self.front] = None

        # Si es el único elemento
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # Avanzamos el puntero front circularmente
            self.front = (self.front + 1) % self.capacity

        # Decrementamos el contador y retornamos
        self.count -= 1
        return item


# ✅ Test cases
cq = CircularQueue(3)
test("8.1 dequeue cola circular vacía", cq.dequeue() == None)  # 📭 Cola vacía
cq.enqueue("A")
cq.enqueue("B")
test("8.2 dequeue primer elemento", cq.dequeue() == "A")  # 🥇 Primer elemento
test("8.3 dequeue segundo elemento", cq.dequeue() == "B")  # 🥈 Segundo elemento
test("8.4 dequeue cola vacía de nuevo",
     cq.dequeue() == None)  # 📭 Cola vacía de nuevo
cq.enqueue("C")
test("8.5 dequeue tipo correcto", isinstance(cq.dequeue(), str)
     or cq.dequeue() == None)  # 📝 Tipo correcto


# 🔄 enqueue() en Cola Circular con Listas Enlazadas 🔗
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedQueue:
    def __init__(self):
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        """Añade un elemento a la cola circular con listas enlazadas."""
        # Creamos el nuevo nodo
        new_node = Node(data)

        # Si la cola está vacía
        if not self.rear:
            # El nodo apunta a sí mismo (circular)
            new_node.next = new_node
            self.rear = new_node
        else:
            # Insertamos después del último y actualizamos referencias
            new_node.next = self.rear.next
            self.rear.next = new_node
            # El nuevo nodo es ahora el último
            self.rear = new_node

        self.size += 1

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
test("9.1 enqueue primer elemento", clq.rear.data == "A")  # 🥇 Primer elemento
test("9.2 enqueue referencia circular",
     clq.rear.next == clq.rear)  # 🔄 Apunta a sí mismo
clq.enqueue("B")
test("9.3 enqueue segundo elemento", clq.display()
     == ["A", "B"])  # 📊 Cola tiene A y B
clq.enqueue("C")
test("9.4 enqueue tercer elemento", clq.display()
     == ["A", "B", "C"])  # 📊 Cola tiene A, B y C
test("9.5 enqueue tipo correcto", isinstance(clq.rear, Node))  # 🔍 Tipo nodo


# 🔄 remove_rear() en Cola Doble (Deque) 📤
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
        """Elimina y retorna el elemento al final de la cola doble."""
        # Si la cola está vacía
        if not self.items:
            return None
        # Eliminamos y retornamos el último elemento
        return self.items.pop()


# ✅ Test cases
dq = Deque()
test("10.1 remove_rear deque vacío", dq.remove_rear() == None)  # 📭 Deque vacío
dq.add_rear(1)
test("10.2 remove_rear un elemento", dq.remove_rear() == 1)  # 🥇 Un elemento
dq.add_rear(2)
dq.add_rear(3)
test("10.3 remove_rear último elemento",
     dq.remove_rear() == 3)  # 🔄 Último elemento
dq.add_front(4)
test("10.4 remove_rear después de add_front",
     dq.remove_rear() == 2)  # 📊 Elemento al final
test("10.5 remove_rear tipo correcto", isinstance(dq.remove_rear(), int)
     or dq.remove_rear() == None)  # 📝 Tipo correcto


# =====================================================================
# 🌳 Árboles Binarios 🌿
# =====================================================================

# 🌱 insert_left() en Nodo de Árbol 🌿
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        """Inserta un nodo como hijo izquierdo del nodo actual."""
        # Creamos el nuevo nodo
        new_node = TreeNode(value)

        # Si ya existe un hijo izquierdo
        if self.left:
            # El nuevo nodo toma al hijo existente como su hijo izquierdo
            new_node.left = self.left

        # El nuevo nodo se convierte en el hijo izquierdo
        self.left = new_node

        # Retornamos el nuevo nodo
        return new_node


# ✅ Test cases
root = TreeNode(1)
left = root.insert_left(2)
# 🌿 Hijo izquierdo creado
test("11.1 insert_left hijo creado", root.left.value == 2)
test("11.2 insert_left retorna nodo", left.value == 2)  # 🎯 Retorna el nuevo nodo
left_child = left.insert_left(3)
test("11.3 insert_left estructura correcta",
     root.left.left.value == 3)  # 🌳 Estructura correcta
old_left = TreeNode(4)
root.left = old_left
new_left = root.insert_left(5)
test("11.4 insert_left preserva nodo anterior",
     new_left.left.value == 4)  # 🔄 Nodo anterior como hijo
test("11.5 insert_left tipo correcto", isinstance(
    new_left, TreeNode))  # 🔍 Tipo TreeNode


# 🚶‍♂️ inorder_traversal() en Árbol Binario 🔍
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def inorder_traversal(self, node=None, result=None):
        """Realiza un recorrido inorden (izquierda-raíz-derecha) del árbol."""
        # Inicializamos result si es None
        if result is None:
            result = []

        # Usamos root por defecto si node es None
        if node is None:
            node = self.root

        # Si no hay nodo, retornamos la lista vacía
        if node is None:
            return result

        # Recorrido inorden: izquierda, nodo, derecha
        # Usamos recorrido iterativo para evitar recursión excesiva
        stack = []
        current = node

        while current or stack:
            # Llegamos al nodo más a la izquierda
            while current:
                stack.append(current)
                current = current.left

            # Procesamos el nodo actual
            current = stack.pop()
            result.append(current.value)

            # Vamos al subárbol derecho
            current = current.right

        return result


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
test("12.1 inorder_traversal básico", tree.inorder_traversal()
     == [4, 2, 5, 1, 3, 6])  # 🔍 Recorrido inorden correcto
single_node_tree = BinaryTree(TreeNode(42))
test("12.2 inorder_traversal un solo nodo",
     single_node_tree.inorder_traversal() == [42])  # 🌱 Árbol de un solo nodo
empty_tree = BinaryTree()
test("12.3 inorder_traversal árbol vacío",
     empty_tree.inorder_traversal() == [])  # 📭 Árbol vacío
tree.root = TreeNode(10)
test("12.4 inorder_traversal otro árbol",
     tree.inorder_traversal() == [10])  # 🎯 Otro árbol simple
test("12.5 inorder_traversal tipo correcto", isinstance(
    tree.inorder_traversal(), list))  # 📋 Tipo lista


# 🔄 preorder_traversal() en Árbol Binario 🌲
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preorder_traversal(self, node=None, result=None):
        """Realiza un recorrido preorden (raíz-izquierda-derecha) del árbol."""
        # Inicializamos result si es None
        if result is None:
            result = []

        # Usamos root por defecto si node es None
        if node is None:
            node = self.root

        # Si no hay nodo, retornamos la lista vacía
        if node is None:
            return result

        # Usamos enfoque iterativo para evitar recursión excesiva
        stack = [node]

        while stack:
            # Procesamos el nodo actual
            current = stack.pop()
            result.append(current.value)

            # Primero agregamos el derecho (para que el izquierdo salga primero)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result


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
test("13.1 preorder_traversal básico", tree.preorder_traversal()
     == [1, 2, 4, 5, 3, 6])  # 🔍 Recorrido preorden correcto
single_node_tree = BinaryTree(TreeNode(42))
test("13.2 preorder_traversal un solo nodo",
     single_node_tree.preorder_traversal() == [42])  # 🌱 Árbol de un solo nodo
empty_tree = BinaryTree()
test("13.3 preorder_traversal árbol vacío",
     empty_tree.preorder_traversal() == [])  # 📭 Árbol vacío
tree.root = TreeNode(10)
test("13.4 preorder_traversal otro árbol",
     tree.preorder_traversal() == [10])  # 🎯 Otro árbol simple
test("13.5 preorder_traversal tipo correcto", isinstance(
    tree.preorder_traversal(), list))  # 📋 Tipo lista


# 🚶‍♀️ postorder_traversal() en Árbol Binario 🌴
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def postorder_traversal(self, node=None, result=None):
        """Realiza un recorrido postorden (izquierda-derecha-raíz) del árbol."""
        # Inicializamos result si es None
        if result is None:
            result = []

        # Usamos root por defecto si node es None
        if node is None:
            node = self.root

        # Si no hay nodo, retornamos la lista vacía
        if node is None:
            return result

        # Enfoque iterativo con dos pilas
        stack1 = [node]
        stack2 = []

        # Primera fase: construir stack2 en orden invertido (raíz-derecha-izquierda)
        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        # Segunda fase: extraer de stack2 para obtener (izquierda-derecha-raíz)
        while stack2:
            result.append(stack2.pop().value)

        return result


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
test("14.1 postorder_traversal básico", tree.postorder_traversal()
     == [4, 5, 2, 6, 3, 1])  # 🔍 Recorrido postorden correcto
single_node_tree = BinaryTree(TreeNode(42))
test("14.2 postorder_traversal un solo nodo",
     single_node_tree.postorder_traversal() == [42])  # 🌱 Árbol de un solo nodo
empty_tree = BinaryTree()
test("14.3 postorder_traversal árbol vacío",
     empty_tree.postorder_traversal() == [])  # 📭 Árbol vacío
tree.root = TreeNode(10)
test("14.4 postorder_traversal otro árbol",
     tree.postorder_traversal() == [10])  # 🎯 Otro árbol simple
test("14.5 postorder_traversal tipo correcto", isinstance(
    tree.postorder_traversal(), list))  # 📋 Tipo lista


# 🌿 insert_right() en Nodo de Árbol 🌲
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_right(self, value):
        """Inserta un nodo como hijo derecho del nodo actual."""
        # Creamos el nuevo nodo
        new_node = TreeNode(value)

        # Si ya existe un hijo derecho
        if self.right:
            # El nuevo nodo toma al hijo existente como su hijo derecho
            new_node.right = self.right

        # El nuevo nodo se convierte en el hijo derecho
        self.right = new_node

        # Retornamos el nuevo nodo
        return new_node


# ✅ Test cases
root = TreeNode(1)
right = root.insert_right(2)
test("15.1 insert_right hijo creado",
     root.right.value == 2)  # 🌲 Hijo derecho creado
# 🎯 Retorna el nuevo nodo
test("15.2 insert_right retorna nodo", right.value == 2)
right_child = right.insert_right(3)
test("15.3 insert_right estructura correcta",
     root.right.right.value == 3)  # 🌳 Estructura correcta
old_right = TreeNode(4)
root.right = old_right
new_right = root.insert_right(5)
test("15.4 insert_right preserva nodo anterior",
     new_right.right.value == 4)  # 🔄 Nodo anterior como hijo
test("15.5 insert_right tipo correcto", isinstance(
    new_right, TreeNode))  # 🔍 Tipo TreeNode


# =====================================================================
# 🔍 Árboles Binarios Avanzados 🔎
# =====================================================================

# 📏 height() en Árbol Binario 📐
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def height(self, node=None):
        """Calcula la altura del árbol binario."""
        # Usamos root por defecto si node es None
        if node is None:
            node = self.root

        # Altura de árbol vacío es -1
        if node is None:
            return -1

        # Usamos un enfoque iterativo con BFS
        queue = [(node, 0)]  # (nodo, nivel)
        max_height = 0

        while queue:
            current, level = queue.pop(0)
            max_height = max(max_height, level)

            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))

        return max_height


# ✅ Test cases
empty_tree = BinaryTree()
test("16.1 height árbol vacío", empty_tree.height() == -1)  # 📭 Árbol vacío
single_node_tree = BinaryTree(TreeNode(1))
# 🌱 Árbol de un solo nodo
test("16.2 height un solo nodo", single_node_tree.height() == 0)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
tree = BinaryTree(root)
test("16.3 height árbol normal", tree.height() == 2)  # 📏 Altura 2

deep_root = TreeNode(1)
deep_root.left = TreeNode(2)
deep_root.left.left = TreeNode(3)
deep_root.left.left.left = TreeNode(4)
deep_tree = BinaryTree(deep_root)
test("16.4 height árbol profundo", deep_tree.height() == 3)  # 📐 Altura 3

test("16.5 height tipo correcto", isinstance(
    deep_tree.height(), int))  # 🔢 Tipo numérico


# 🍂 size() en Árbol Binario 📏
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def size(self, node=None):
        """Calcula el número total de nodos en el árbol."""
        # Usamos root por defecto si node es None
        if node is None:
            node = self.root

        # Tamaño de árbol vacío es 0
        if node is None:
            return 0

        # Enfoque iterativo para evitar recursión excesiva
        count = 0
        queue = [node]

        while queue:
            current = queue.pop(0)
            count += 1

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return count


# ✅ Test cases
empty_tree = BinaryTree()
test("17.1 size árbol vacío", empty_tree.size() == 0)  # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(42))
# 🌱 Árbol de un solo nodo
test("17.2 size un solo nodo", single_node_tree.size() == 1)

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
test("17.3 size árbol completo", tree.size() == 6)  # 📊 Árbol con 6 nodos

tree.root = TreeNode(10)
tree.root.left = TreeNode(20)
test("17.4 size árbol pequeño", tree.size() == 2)  # 🎯 Árbol con 2 nodos

test("17.5 size tipo correcto", isinstance(
    tree.size(), int))  # 🔢 Tipo numérico


# 🌲 get_root() en Árbol Binario 🌱
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        """Obtiene el valor de la raíz del árbol."""
        # Si no hay raíz, retornamos None
        if not self.root:
            return None
        # Retornamos el valor de la raíz
        return self.root.value


# ✅ Test cases
empty_tree = BinaryTree()
test("18.1 get_root árbol vacío", empty_tree.get_root() == None)  # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(42))
# 🌱 Árbol de un solo nodo
test("18.2 get_root un solo nodo", single_node_tree.get_root() == 42)

# Árbol:      1
#           /   \
#          2     3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
tree = BinaryTree(root)
test("18.3 get_root árbol normal", tree.get_root() == 1)  # 🌲 Raíz es 1

# Cambiar la raíz
tree.root = TreeNode(10)
test("18.4 get_root después de cambio",
     tree.get_root() == 10)  # 🔄 Raíz cambiada

test("18.5 get_root tipo correcto", isinstance(tree.get_root(), int)
     or tree.get_root() == None)  # 🔢 Tipo correcto


# 🔍 search() en Árbol Binario de Búsqueda 🔎
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
        """Busca un valor en el árbol binario de búsqueda."""
        # Enfoque iterativo para evitar recursión excesiva
        current = self.root

        while current:
            # Si encontramos el valor
            if current.value == value:
                return True

            # Decidimos si buscar a la izquierda o derecha
            if value < current.value:
                current = current.left
            else:
                current = current.right

        # Si llegamos aquí, no se encontró el valor
        return False


# ✅ Test cases
bst = BinarySearchTree()
test("19.1 search árbol vacío", bst.search(10) == False)  # 📭 Árbol vacío

bst.insert(10)
test("19.2 search valor existente", bst.search(10) == True)  # ✅ Valor encontrado
test("19.3 search valor inexistente", bst.search(
    20) == False)  # ❌ Valor no encontrado

bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
test("19.4 search valor en subárbol", bst.search(
    7) == True)  # 🎯 Valor en subárbol

test("19.5 search tipo correcto", isinstance(
    bst.search(5), bool))  # 🔍 Tipo booleano


# 🍃 count_leaves() en Árbol Binario 🍂
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def count_leaves(self, node=None):
        """Cuenta los nodos hoja (sin hijos) en el árbol."""
        # Usamos root por defecto si node es None
        if node is None:
            node = self.root

        # Si no hay nodo, no hay hojas
        if node is None:
            return 0

        # Enfoque iterativo para evitar recursión excesiva
        count = 0
        queue = [node]

        while queue:
            current = queue.pop(0)

            # Si es un nodo hoja (sin hijos)
            if not current.left and not current.right:
                count += 1
            else:
                # Agregamos los hijos a la cola
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return count


# ✅ Test cases
empty_tree = BinaryTree()
test("20.1 count_leaves árbol vacío",
     empty_tree.count_leaves() == 0)  # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(1))
test("20.2 count_leaves un solo nodo",
     single_node_tree.count_leaves() == 1)  # 🌱 Un solo nodo es hoja

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
test("20.3 count_leaves múltiples hojas",
     tree.count_leaves() == 3)  # 🍃 Hojas: 4, 5, 6

balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_tree = BinaryTree(balanced_root)
test("20.4 count_leaves hojas en nivel 1",
     balanced_tree.count_leaves() == 2)  # 🍂 Hojas: 2, 3

test("20.5 count_leaves tipo correcto", isinstance(
    tree.count_leaves(), int))  # 🔢 Tipo numérico


# ---------------------------
# 🧾 Final Summary
# ---------------------------
print("\n# Final Test Summary")
for result in results:
    print(result)

print(f"\nTotal Approved: {sum('✅' in r for r in results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in results)} ❌")
