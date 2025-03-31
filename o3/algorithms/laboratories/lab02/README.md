# Recursion and Backtracking Algorithms

Este documento contiene explicaciones detalladas, diagramas de ejecución y casos de prueba para varios algoritmos de recursión y backtracking.

## Índice

### Algoritmos de Recursión
1. [Factorial](#1-factorial)
2. [Potencia (x^n)](#2-potencia-xn)
3. [Suma de dígitos](#3-suma-de-dígitos)
4. [Verificar si una cadena es palíndromo](#4-verificar-si-una-cadena-es-palíndromo)
5. [Invertir una cadena](#5-invertir-una-cadena)
6. [Suma de elementos en una lista](#6-suma-de-elementos-en-una-lista)
7. [Fibonacci](#7-fibonacci)
8. [Torre de Hanoi](#8-torre-de-hanoi)

### Algoritmos de Backtracking
1. [Generar strings de dígitos binarios de longitud N](#1-generar-strings-de-dígitos-binarios-de-longitud-n)
2. [Combinaciones de strings de T/F de longitud n](#2-combinaciones-de-strings-de-tf-de-longitud-n)
3. [Generar números con los valores 1, 2 y 3 de N dígitos](#3-generar-números-con-los-valores-1-2-y-3-de-n-dígitos)
4. [Suma de subconjuntos dando el valor de n](#4-suma-de-subconjuntos-dando-el-valor-de-n)

---

## Algoritmos de Recursión

### 1. Factorial

#### Explicación del algoritmo
El factorial de un número entero positivo n (escrito como n!) es el producto de todos los enteros positivos menores o iguales a n.

La definición recursiva se basa en:
- Caso base: 0! = 1! = 1
- Caso recursivo: n! = n × (n-1)!

#### Código
```python
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n-1)
```

#### Diagrama de ejecución
Para factorial(4):

```
factorial(4)
├─> 4 * factorial(3)
│   ├─> 3 * factorial(2)
│   │   ├─> 2 * factorial(1)
│   │   │   └─> 1 (caso base)
│   │   └─> 2 * 1 = 2
│   └─> 3 * 2 = 6
└─> 4 * 6 = 24
```

#### Comentarios del problema
- La función es una traducción directa de la definición matemática
- Cada llamada recursiva reduce n en 1, acercándose al caso base
- La pila de llamadas crece linealmente con n (profundidad O(n))
- En Python, el límite práctico es alrededor de n ≈ 1000 debido al límite de recursión

#### Casos de prueba
1. **Caso base:** `factorial(0)` = 1
2. **Caso simple:** `factorial(5)` = 120
3. **Caso límite:** `factorial(10)` = 3628800

---

### 2. Potencia (x^n)

#### Explicación del algoritmo
Este algoritmo calcula x elevado a la potencia n utilizando recursividad:
- x^0 = 1 (caso base)
- x^n = x * x^(n-1) para n > 0 (caso recursivo)

#### Código
```python
def power(x, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return x * power(x, n-1)
```

#### Diagrama de ejecución
Para power(2, 3):

```
power(2, 3)
├─> 2 * power(2, 2)
│   ├─> 2 * power(2, 1)
│   │   ├─> 2 * power(2, 0)
│   │   │   └─> 1 (caso base)
│   │   └─> 2 * 1 = 2
│   └─> 2 * 2 = 4
└─> 2 * 4 = 8
```

#### Comentarios del problema
- Esta implementación es sencilla pero no óptima para valores grandes de n
- Se podría mejorar utilizando la propiedad de que x^n = (x^(n/2))^2 para n par
- La complejidad en tiempo es O(n) y la complejidad espacial también es O(n)

#### Casos de prueba
1. **Caso base:** `power(2, 0)` = 1
2. **Caso simple:** `power(2, 10)` = 1024
3. **Caso con base negativa:** `power(-2, 3)` = -8

---

### 3. Suma de dígitos

#### Explicación del algoritmo
Este algoritmo calcula la suma de los dígitos de un número entero no negativo:
- Si el número tiene un solo dígito, ese es el resultado (caso base)
- De lo contrario, la suma es el último dígito más la suma de los dígitos restantes (caso recursivo)

#### Código
```python
def sum_digits(n):
    # Base case: single digit
    if n < 10:
        return n
    # Recursive case: last digit + sum of remaining digits
    return n % 10 + sum_digits(n // 10)
```

#### Diagrama de ejecución
Para sum_digits(123):

```
sum_digits(123)
├─> 3 + sum_digits(12)
│   ├─> 2 + sum_digits(1)
│   │   └─> 1 (caso base)
│   └─> 2 + 1 = 3
└─> 3 + 3 = 6
```

#### Comentarios del problema
- En cada paso, extraemos el último dígito con n % 10
- Reducimos el problema con n // 10 (división entera)
- La profundidad de la recursión es igual al número de dígitos en n
- La complejidad en tiempo y espacio es O(log n), donde log es en base 10

#### Casos de prueba
1. **Caso de un dígito:** `sum_digits(7)` = 7
2. **Caso de varios dígitos:** `sum_digits(123)` = 6
3. **Caso con dígitos repetidos:** `sum_digits(9999)` = 36

---

### 4. Verificar si una cadena es palíndromo

#### Explicación del algoritmo
Un palíndromo es una palabra, frase o número que se lee igual hacia adelante que hacia atrás:
- Una cadena vacía o de un solo carácter es un palíndromo (caso base)
- Una cadena es un palíndromo si el primer y último carácter son iguales, y la subcadena interna es un palíndromo (caso recursivo)

#### Código
```python
def is_palindrome(text):
    # Convert to lowercase and remove spaces
    text = text.lower().replace(" ", "")

    # Base case: empty string or single character
    if len(text) <= 1:
        return True

    # Recursive case: check first and last character, then check substring
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False
```

#### Diagrama de ejecución
Para is_palindrome("radar"):

```
is_palindrome("radar")
├─> 'r' == 'r' ? Yes
│   └─> is_palindrome("ada")
│       ├─> 'a' == 'a' ? Yes
│       │   └─> is_palindrome("d")
│       │       └─> True (caso base - un solo carácter)
│       └─> True
└─> True
```

#### Comentarios del problema
- La función primero normaliza el texto (minúsculas, sin espacios)
- Compara los caracteres de los extremos y si coinciden, continúa con la subcadena interior
- La profundidad de la recursión es la mitad de la longitud de la cadena
- La complejidad en tiempo es O(n) y la complejidad espacial es O(n)

#### Casos de prueba
1. **Caso simple:** `is_palindrome("radar")` = True
2. **Caso con espacios y mayúsculas:** `is_palindrome("A man a plan a canal Panama")` = True
3. **Caso no palíndromo:** `is_palindrome("hello")` = False

---

### 5. Invertir una cadena

#### Explicación del algoritmo
Este algoritmo invierte una cadena utilizando recursividad:
- Una cadena vacía o de un solo carácter ya está invertida (caso base)
- Para cadenas más largas, la inversión es el último carácter seguido de la inversión del resto de la cadena (caso recursivo)

#### Código
```python
def reverse_string(s):
    # Base case: empty string or single character
    if len(s) <= 1:
        return s

    # Recursive case: last character + reverse of the rest
    return s[-1] + reverse_string(s[:-1])
```

#### Diagrama de ejecución
Para reverse_string("hello"):

```
reverse_string("hello")
├─> 'o' + reverse_string("hell")
│   ├─> 'o' + ('l' + reverse_string("hel"))
│   │   ├─> 'o' + ('l' + ('l' + reverse_string("he")))
│   │   │   ├─> 'o' + ('l' + ('l' + ('e' + reverse_string("h"))))
│   │   │   │   ├─> 'o' + ('l' + ('l' + ('e' + 'h')))
│   │   │   │   └─> 'o' + ('l' + ('l' + 'eh'))
│   │   │   └─> 'o' + ('l' + 'lleh')
│   │   └─> 'o' + 'llleh'
│   └─> 'olleh'
└─> 'olleh'
```

#### Comentarios del problema
- En cada paso, tomamos el último carácter y lo concatenamos al principio del resultado
- Esta implementación es sencilla pero no óptima para cadenas muy largas debido a la creación de nuevas cadenas en cada paso
- La complejidad en tiempo es O(n²) debido a las concatenaciones de cadenas, y la complejidad espacial es O(n)

#### Casos de prueba
1. **Caso simple:** `reverse_string("hello")` = "olleh"
2. **Caso con mayúsculas:** `reverse_string("Python")` = "nohtyP"
3. **Caso de un carácter:** `reverse_string("a")` = "a"

---

### 6. Suma de elementos en una lista

#### Explicación del algoritmo
Este algoritmo calcula la suma de todos los elementos en una lista:
- Si la lista está vacía, la suma es 0 (caso base)
- De lo contrario, la suma es el primer elemento más la suma del resto de la lista (caso recursivo)

#### Código
```python
def sum_list(arr):
    # Base case: empty list
    if not arr:
        return 0

    # Recursive case: first element + sum of the rest
    return arr[0] + sum_list(arr[1:])
```

#### Diagrama de ejecución
Para sum_list([1, 2, 3]):

```
sum_list([1, 2, 3])
├─> 1 + sum_list([2, 3])
│   ├─> 1 + (2 + sum_list([3]))
│   │   ├─> 1 + (2 + (3 + sum_list([])))
│   │   │   ├─> 1 + (2 + (3 + 0))
│   │   │   └─> 1 + (2 + 3)
│   │   └─> 1 + 5
│   └─> 6
└─> 6
```

#### Comentarios del problema
- En cada paso, tomamos el primer elemento y lo sumamos al resultado de la recursión con el resto de la lista
- La profundidad de la recursión es igual al número de elementos en la lista
- La complejidad en tiempo es O(n) y la complejidad espacial es O(n)

#### Casos de prueba
1. **Caso vacío:** `sum_list([])` = 0
2. **Caso normal:** `sum_list([1, 2, 3, 4, 5])` = 15
3. **Caso con negativos:** `sum_list([-1, 10, -5, 6])` = 10

---

### 7. Fibonacci

#### Explicación del algoritmo
La secuencia de Fibonacci es una serie donde cada número es la suma de los dos anteriores:
- F(0) = 0, F(1) = 1 (casos base)
- F(n) = F(n-1) + F(n-2) para n > 1 (caso recursivo)

#### Código
```python
def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: sum of the two previous Fibonacci numbers
    return fibonacci(n-1) + fibonacci(n-2)
```

#### Diagrama de ejecución
Para fibonacci(4):

```
                      fibonacci(4)
                     /           \
            fibonacci(3)        fibonacci(2)
           /        \           /        \
    fibonacci(2)  fibonacci(1) fibonacci(1) fibonacci(0)
    /        \       |             |           |
fibonacci(1) fibonacci(0)     1           1           0
    |           |
    1           0
```

El resultado final sería: 1 + 0 + 1 + 1 + 0 = 3

#### Comentarios del problema
- Esta implementación es sencilla pero muy ineficiente para valores grandes de n debido a cálculos repetidos
- La complejidad en tiempo es O(2^n) lo que la hace impráctica para n > 40
- Se podría mejorar dramáticamente con técnicas como memoización o una solución iterativa
- La implementación recursiva sirve principalmente como ejemplo didáctico

#### Casos de prueba
1. **Caso base 0:** `fibonacci(0)` = 0
2. **Caso base 1:** `fibonacci(1)` = 1
3. **Caso normal:** `fibonacci(7)` = 13

---

### 8. Torre de Hanoi

#### Explicación del algoritmo
El problema de la Torre de Hanoi consiste en mover n discos desde una torre origen a una torre destino, usando una torre auxiliar, siguiendo estas reglas:
1. Solo se puede mover un disco a la vez
2. Un disco más grande nunca puede estar sobre uno más pequeño

La solución recursiva es:
- Para n=1: mover el disco directamente de origen a destino (caso base)
- Para n>1:
  1. Mover n-1 discos de origen a auxiliar (usando destino como auxiliar)
  2. Mover el disco n de origen a destino
  3. Mover n-1 discos de auxiliar a destino (usando origen como auxiliar)

#### Código
```python
def towers_of_hanoi(n, source="A", auxiliary="B", target="C"):
    # Base case: only one disk
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Recursive case:
    # 1. Move n-1 disks from source to auxiliary using target as auxiliary
    towers_of_hanoi(n-1, source, target, auxiliary)

    # 2. Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # 3. Move n-1 disks from auxiliary to target using source as auxiliary
    towers_of_hanoi(n-1, auxiliary, source, target)
```

#### Diagrama de ejecución
Para towers_of_hanoi(3):

```
towers_of_hanoi(3, A, B, C)
├─> towers_of_hanoi(2, A, C, B)
│   ├─> towers_of_hanoi(1, A, B, C)
│   │   └─> "Move disk 1 from A to C"
│   ├─> "Move disk 2 from A to B"
│   └─> towers_of_hanoi(1, C, A, B)
│       └─> "Move disk 1 from C to B"
├─> "Move disk 3 from A to C"
└─> towers_of_hanoi(2, B, A, C)
    ├─> towers_of_hanoi(1, B, C, A)
    │   └─> "Move disk 1 from B to A"
    ├─> "Move disk 2 from B to C"
    └─> towers_of_hanoi(1, A, B, C)
        └─> "Move disk 1 from A to C"
```

El resultado serían los movimientos:
1. Move disk 1 from A to C
2. Move disk 2 from A to B
3. Move disk 1 from C to B
4. Move disk 3 from A to C
5. Move disk 1 from B to A
6. Move disk 2 from B to C
7. Move disk 1 from A to C

#### Comentarios del problema
- Este es un problema clásico que demuestra la elegancia de la recursividad
- El número de movimientos para n discos es 2^n - 1
- La complejidad en tiempo es O(2^n) y la complejidad espacial es O(n)
- El problema tiene aplicaciones en campos como planificación y robótica

#### Casos de prueba
1. **Caso simple:** `towers_of_hanoi(1)` = 1 movimiento
2. **Caso medio:** `towers_of_hanoi(3)` = 7 movimientos
3. **Caso más grande:** `towers_of_hanoi(4)` = 15 movimientos

---

## Algoritmos de Backtracking

### 1. Generar strings de dígitos binarios de longitud N

#### Explicación del algoritmo
Este algoritmo genera todas las posibles cadenas binarias (compuestas de 0s y 1s) de longitud N:
- Si ya tenemos una cadena de longitud N, la imprimimos (caso base)
- De lo contrario, exploramos dos opciones: añadir un 0 o añadir un 1 a la cadena actual

#### Código
```python
def generate_binary_strings(n, current=""):
    # Base case: we have a binary string of length n
    if len(current) == n:
        print(current)
        return

    # Recursive case 1: append '0'
    generate_binary_strings(n, current + "0")

    # Recursive case 2: append '1'
    generate_binary_strings(n, current + "1")
```

#### Diagrama de ejecución
Para generate_binary_strings(2):

```
                     ""
                    /  \
                   /    \
                  /      \
                 /        \
                0          1
               / \        / \
              /   \      /   \
             00   01    10   11
```

#### Comentarios del problema
- Este es un caso simple de backtracking donde exploramos todas las posibilidades
- Para n=3, generaríamos 2^3=8 combinaciones
- La profundidad máxima de recursión es n
- La complejidad en tiempo es O(2^n) y la complejidad espacial es O(n)

#### Casos de prueba
1. **Caso simple:** `generate_binary_strings(1)` genera "0" y "1"
2. **Caso normal:** `generate_binary_strings(2)` genera "00", "01", "10", "11"
3. **Caso más grande:** `generate_binary_strings(3)` genera "000", "001", "010", "011", "100", "101", "110", "111"

---

### 2. Combinaciones de strings de T/F de longitud n

#### Explicación del algoritmo
Similar al problema anterior, este algoritmo genera todas las posibles combinaciones de "T" (true) y "F" (false) de longitud n:
- Si ya tenemos una cadena de longitud n, la imprimimos (caso base)
- De lo contrario, exploramos dos opciones: añadir "T" o añadir "F" a la cadena actual

#### Código
```python
def generate_tf_combinations(n, current=""):
    # Base case: we have a combination of length n
    if len(current) == n:
        print(current)
        return

    # Recursive case 1: append 'T'
    generate_tf_combinations(n, current + "T")

    # Recursive case 2: append 'F'
    generate_tf_combinations(n, current + "F")
```

#### Diagrama de ejecución
Para generate_tf_combinations(2):

```
                   ""
                  /  \
                 /    \
                /      \
               /        \
              /          \
             /            \
            T              F
           /\              /\
          /  \            /  \
         /    \          /    \
        /      \        /      \
       TT       TF      FT       FF
```

#### Comentarios del problema
- La estructura y complejidad son idénticas al problema de generar cadenas binarias
- Solo cambia la representación de los valores: "T"/"F" en lugar de "0"/"1"
- La complejidad en tiempo es O(2^n) y la complejidad espacial es O(n)

#### Casos de prueba
1. **Caso simple:** `generate_tf_combinations(1)` genera "T" y "F"
2. **Caso normal:** `generate_tf_combinations(2)` genera "TT", "TF", "FT", "FF"
3. **Caso más grande:** `generate_tf_combinations(3)` genera "TTT", "TTF", "TFT", "TFF", "FTT", "FTF", "FFT", "FFF"

---

### 3. Generar números con los valores 1, 2 y 3 de N dígitos

#### Explicación del algoritmo
Este algoritmo genera todos los posibles números de longitud N utilizando solo los dígitos 1, 2 y 3:
- Si ya tenemos un número de longitud N, lo imprimimos (caso base)
- De lo contrario, exploramos tres opciones: añadir "1", "2" o "3" al número actual

#### Código
```python
def generate_123_numbers(n, current=""):
    # Base case: we have a number of length n
    if len(current) == n:
        print(current)
        return

    # Recursive case 1: append '1'
    generate_123_numbers(n, current + "1")

    # Recursive case 2: append '2'
    generate_123_numbers(n, current + "2")

    # Recursive case 3: append '3'
    generate_123_numbers(n, current + "3")
```

#### Diagrama de ejecución
Para generate_123_numbers(2):

```
                       ""
                   /    |    \
                  /     |     \
                 /      |      \
                1       2       3
              / | \   / | \   / | \
             /  |  \ /  |  \ /  |  \
            11  12 13 21 22 23 31 32 33
```

#### Comentarios del problema
- A diferencia de los problemas anteriores, aquí exploramos tres opciones en cada nivel
- Para n=2, generamos 3^2=9 combinaciones
- La profundidad máxima de recursión sigue siendo n
- La complejidad en tiempo es O(3^n) y la complejidad espacial es O(n)

#### Casos de prueba
1. **Caso simple:** `generate_123_numbers(1)` genera "1", "2", "3"
2. **Caso normal:** `generate_123_numbers(2)` genera "11", "12", "13", "21", "22", "23", "31", "32", "33"
3. **Caso más grande:** `generate_123_numbers(3)` genera 27 combinaciones diferentes

---

### 4. Suma de subconjuntos dando el valor de n

#### Explicación del algoritmo
Este algoritmo encuentra todos los subconjuntos de un conjunto de números que suman exactamente un valor objetivo:
- Si el subconjunto actual suma exactamente el valor objetivo, lo imprimimos
- Si nos pasamos del valor objetivo o ya no hay más elementos para considerar, retornamos
- De lo contrario, exploramos dos opciones: incluir o no incluir el elemento actual en el subconjunto

#### Código
```python
def find_subsets_with_sum(numbers, target_sum, current=None, index=0):
    if current is None:
        current = []

    # Case: we found a subset with the target sum
    if sum(current) == target_sum:
        print(current)

    # Base case: we've considered all numbers or exceeded the target
    if index >= len(numbers) or sum(current) > target_sum:
        return

    # Include the current number
    current.append(numbers[index])
    find_subsets_with_sum(numbers, target_sum, current, index + 1)

    # Exclude the current number (backtrack)
    current.pop()
    find_subsets_with_sum(numbers, target_sum, current, index + 1)
```

#### Diagrama de ejecución
Para find_subsets_with_sum([1, 2, 3], 3):

```
                   [] (1)
                   /\
                  /  \
                 /    \
                /      \
               /        \
              /          \
             /            \
      [1] (2)              [] (8) ← BACKTRACK desde [1]
         /\                  /\
        /  \                /  \
       /    \              /    \
      /      \            /      \
     /        \          /        \
    /          \        /          \
   /            \      /            \
[1,2] (3)      [1] (5) ← BT    [2] (9)       [] (13) ← BT
 /\              /\              /\             /\
/  \            /  \            /  \           /  \
/    \          /    \          /    \         /    \
/      \        /      \        /      \       /      \
[1,2,3](4)  [1,2] ✓(5)  [1,3](6)  [1](7)  [2,3](10)  [2](11)  [3] ✓(14)  [](15)
    ×                       ×        ×        ×         ×                    ×
    BT                      BT       BT       BT        BT                   BT
```

#### Comentarios del problema
- Este es un ejemplo clásico de backtracking con poda (pruning)
- La poda ocurre cuando la suma actual excede el objetivo
- A diferencia de los problemas anteriores, aquí debemos mantener un estado (la suma actual) y deshacerlo (backtrack)
- La complejidad en tiempo es O(2^n) en el peor caso, pero la poda puede mejorar el rendimiento en la práctica
- La complejidad espacial es O(n) para la pila de recursión y el subconjunto actual

#### Casos de prueba
1. **Caso simple:** `find_subsets_with_sum([1, 2, 3], 3)` encuentra [1, 2] y [3]
2. **Caso sin solución:** `find_subsets_with_sum([5, 10, 15], 7)` no encuentra ningún subconjunto
3. **Caso con múltiples soluciones:** `find_subsets_with_sum([1, 2, 3, 4, 5], 5)` encuentra [1, 4], [2, 3], [5]