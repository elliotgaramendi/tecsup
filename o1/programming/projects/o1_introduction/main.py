# # ====================================================================
# # 📚 o1: Algorithms and Code Representation
# # ====================================================================

# # --------------------------------------------------------------------
# # o1.1 🧮 Simple Addition Calculator ➕
# # --------------------------------------------------------------------

# # Simple Addition Calculator ➕
# print("➕ Calculadora de Suma Simple")
# print("=" * 30)

# # Your code here 👇
# number1 = float(input("Número 1: "))
# number2 = float(input("Número 2: "))
# result = number1 + number2
# print(f"El resultado es: {result}")

# # Example output:
# El resultado es: 15.0

# # Test cases:
# print("=" * 30)
# print(result == 15)
# print(result == 10.0)
# print(result == 300.0)


# # --------------------------------------------------------------------
# # o1.2 📐 Rectangle Area Calculator
# # --------------------------------------------------------------------

# # Rectangle Area Calculator 📐
# print("🏗️ Rectangle Area Calculator")
# print("=" * 40)

# # Your code here 👇
# base = float(input('Base: '))
# height = float(input('Altura: '))
# area = base * height
# result = f'El área del rectángulo es: {area} metros cuadrados'
# print(result)

# # Example output:
# # El área del rectángulo es: 15 metros cuadrados

# print("=" * 40)
# # Test cases:
# print(result == 'El área del rectángulo es: 15.0 metros cuadrados')
# print(result == 'El área del rectángulo es: 24.15 metros cuadrados')
# print(result == 'El área del rectángulo es: 49.0 metros cuadrados')


# # --------------------------------------------------------------------
# # o1.3 🌡️ Temperature Converter (Celsius to Fahrenheit)
# # --------------------------------------------------------------------

# # Temperature Converter 🌡️
# print("🌡️ Conversor de Temperatura")
# print("=" * 30)

# # Your code here 👇
# celsius = float(input("¿Cuál es la temperatura en grados Celsius? "))
# fahrenheit = (celsius * 9 / 5) + 32
# print(f"Fahrenheit es: {fahrenheit:.1f} °F 🌡️🔥")

# # Test cases:
# print("=" * 30)
# print(fahrenheit == 32.0)
# print(fahrenheit == 77.0)
# print(fahrenheit == 212.0)


# # --------------------------------------------------------------------
# # o1.4 📊 Average Calculator
# # --------------------------------------------------------------------

# # Average Calculator 📊
# print("📊 Calculadora de Promedio")
# print("=" * 30)

# # Your code here 👇
# number1 = float(input("Número 1: "))
# number2 = float(input("Número 2: "))
# number3 = float(input("Número 3: "))

# average = (number1 + number2 + number3) / 3

# print(f"El promedio es: {average:.2f}")

# # Test cases:
# print("=" * 30)
# print(average == 20.0)
# print(average == 10.0)
# print(average == 9.0)


# # --------------------------------------------------------------------
# # o1.5 📏 Rectangle Perimeter Calculator
# # --------------------------------------------------------------------

# # Rectangle Perimeter Calculator 📏
# print("📏 Calculadora de Perímetro")
# print("=" * 30)

# # Your code here 👇
# base = float(input('Base: '))
# height = float(input('Altura: '))

# perimeter = 2 * (base + height)

# print(f"El perímetro es: {perimeter}")

# # Test cases:
# print("=" * 30)
# print(perimeter == 16)
# print(perimeter == 34)
# print(perimeter == 16)



# # ====================================================================
# # 🔀 o2: Basic Conditional Structures
# # ====================================================================


# # --------------------------------------------------------------------
# # o2.1 ➕➖ Positive, Negative or Zero Detector
# # --------------------------------------------------------------------
# # Even/Odd Detector 🔢
# print("🔢 Detector Par/Impar")
# print("=" * 25)

# # Your code here 👇
# number = int(input("Número: "))

# if number % 2 == 0:
#     result = "par"
# else:
#     result = "impar"

# print(f"El resultado es: {result}")

# # Test cases:
# print("=" * 25)
# print(result == "par")
# print(result == "impar")
# print(result == "par")


# # --------------------------------------------------------------------
# # o2.2 ➕➖ Positive, Negative or Zero Detector
# # --------------------------------------------------------------------

# # Number Classifier ➕➖
# print("➕➖ Clasificador de Números")
# print("=" * 30)

# # Your code here 👇
# number = float(input("Número: "))

# if number > 0:
#     result = "positivo"
# elif number < 0:
#     result = "negativo"
# else:
#     result = "cero"

# print(f"El resultado es: {result}")

# # Test cases:
# print("=" * 30)
# print(result == "positivo")
# print(result == "negativo")
# print(result == "cero")


# # --------------------------------------------------------------------
# # o2.3 ⚖️ Number Comparator
# # --------------------------------------------------------------------

# # Number Comparator ⚖️
# print("⚖️ Comparador de Números")
# print("=" * 28)

# # Your code here 👇
# number1 = float(input("Número 1: "))
# number2 = float(input("Número 2: "))

# if number1 > number2:
#     result = "mayor"
# elif number1 < number2:
#     result = "menor"
# else:
#     result = "igual"

# print(f"El resultado es: {result}")

# # Test cases:
# print("=" * 28)
# print(result == "mayor")
# print(result == "menor")
# print(result == "igual")


# # --------------------------------------------------------------------
# # o2.4 👥 Age Classifier
# # --------------------------------------------------------------------

# # Age Classifier 👥
# print("👥 Clasificador de Edades")
# print("=" * 28)

# # Your code here 👇
# age = int(input("Edad: "))

# if age < 18:
#     result = "niño"
# elif age <= 64:
#     result = "adulto"
# else:
#     result = "adulto mayor"

# print(f"El resultado es: {result}")

# # Test cases:
# print("=" * 28)
# print(result == "niño")
# print(result == "adulto")
# print(result == "adulto mayor")


# # --------------------------------------------------------------------
# # o2.5 ➕➖ Simple Calculator
# # --------------------------------------------------------------------

# # Simple Calculator ➕➖✖️➗
# print("➕➖✖️➗ Calculadora Simple")
# print("=" * 25)

# # Your code here 👇
# number1 = float(input("Número 1: "))
# operation = input("Operación (+, -, *, /): ")
# number2 = float(input("Número 2: "))

# if operation == "+":
#     result = number1 + number2
# elif operation == "-":
#     result = number1 - number2
# elif operation == "*":
#     result = number1 * number2
# elif operation == "/":
#     result = number1 / number2

# print(f"El resultado es: {result}")

# # Test cases:
# print("=" * 25)
# print(result == 15.0)
# print(result == 7.0)
# print(result == 16.0)
# print(result == 3.0)
