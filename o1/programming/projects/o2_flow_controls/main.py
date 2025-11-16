# ====================================================================
# 📝 o2.1: Strings y Condicionales Avanzadas
# ====================================================================


# --------------------------------------------------------------------
# # o2.1.1 Text Case Converter 🔤
# --------------------------------------------------------------------

# print("🔤 Conversor de Mayúsculas/Minúsculas")
# print("=" * 40)

# # Your code here 👇
# text = input("Ingresa un texto: ")
# upper_text = text.upper()
# lower_text = text.lower()
# title_text = text.title()

# # Example output:
# print(upper_text)
# print(lower_text)
# print(title_text)

# # Test cases:
# print("=" * 40)
# print(upper_text == "HOLA MUNDO" and lower_text ==
#       "hola mundo" and title_text == "Hola Mundo")
# print(upper_text == "PYTHON" and lower_text ==
#       "python" and title_text == "Python")
# print(upper_text == "APRENDER PYTHON" and lower_text ==
#       "aprender python" and title_text == "Aprender Python")


# --------------------------------------------------------------------
# # o2.1.2 Word Extractor ✂️
# --------------------------------------------------------------------

# print("✂️ Extractor de Palabras")
# print("=" * 30)

# # Your code here 👇
# text = input("Ingresa una oración: ")
# words = text.split(' ')

# print(words)

# word_count = len(words)
# first_word = words[0]
# last_word = words[-1]

# # Example output:
# print(f"Total de palabras: {word_count}")
# print(f"Primera palabra: {first_word}")
# print(f"Última palabra: {last_word}")

# # Test cases:
# print("=" * 30)
# print(word_count == 3 and first_word == "Python" and last_word == "genial")
# print(word_count == 1 and first_word ==
#       "Programar" and last_word == "Programar")
# print(word_count == 7 and first_word == "Me" and last_word == "días")


# --------------------------------------------------------------------
# # o2.1.3 Word Finder and Replacer 🔍
# --------------------------------------------------------------------

# print("🔍 Buscador y Reemplazador")
# print("=" * 35)

# # Your code here 👇
# text = input("Ingresa un texto: ")
# search = input("Ingresa una palabra a buscar: ")
# replace = input("Ingresa una palabra a reemplazar: ")
# result = text.replace(search, replace)

# # Example output:
# print(result)

# # Test cases:
# print("=" * 35)
# print(result == "Python es increíble")
# print(result == "Aprender programación")
# print(result == "Hola mundo")


# --------------------------------------------------------------------
# # o2.1.4Credential Validator 🎫
# --------------------------------------------------------------------

# print("🎫 Validador de Credenciales")
# print("=" * 35)

# # Your code here 👇
# user = input("Ingrese su usuario: ")
# password = input("Ingresa su contraseña: ")
# status = ""

# print(len(user))
# print(len(password))

# if len(user) >= 5 and len(password) >= 8:
#     status = "válido"
# elif len(user) < 5:
#     status = "usuario inválido"
# elif len(password) < 8:
#     status = "contraseña inválida"

# # Example output:
# print(status)

# # Test cases:
# print("=" * 35)
# print(status == "válido")
# print(status == "usuario inválido")
# print(status == "contraseña inválida")


# --------------------------------------------------------------------
# # o2.1.P 📋 User Registration System
# --------------------------------------------------------------------

# print("📋 SISTEMA DE REGISTRO DE USUARIO")
# print("=" * 40)

# # Your code here 👇
# name = input("Ingresa su nombre: ")
# email = input("Ingresa su email: ")
# age = int(input("Ingresa su edad: "))
# username = input("Ingresa su usuario: ")

# valid = False
# user_code = ""
# error = ""

# name_words = name.split(' ')

# if len(name_words) < 3:
#     valid = False
#     error = "nombre incompleto"
# elif "@" not in email or "." not in email:
#     valid = False
#     error = "email inválido"
# elif age < 18 or age > 100:
#     valid = False
#     error = "edad inválida"
# elif len(username) < 5 or " " in username:
#     valid = False
#     error = "usuario inválido"
# else:
#     valid = True

# name = name.title()
# username = username.lower()
# user_code = username[:3] + str(age)

# # Example output:
# if valid:
#     print("✅ REGISTRO EXITOSO")
#     print(f"Nombre: {name}")
#     print(f"Email: {email}")
#     print(f"Edad: {age} años")
#     print(f"Usuario: {username}")
#     print(f"Código: {user_code}")
# else:
#     print("❌ REGISTRO NO EXITOSO")
#     print(f"Error: {error}")

# # Test cases:
# print("=" * 40)
# print(valid == True and user_code == "jua25")
# print(valid == False and error == "edad menor")
# print(valid == True and user_code == "car30")


# ====================================================================
# 🔄 o2.2: Bucles II - Control de Flujo Avanzado
# ====================================================================


# # --------------------------------------------------------------------
# # 💻 o2.2.1: 🛑 Buscador con Break
# # --------------------------------------------------------------------
# # Number Finder with Break 🛑
# print("🛑 Buscador de Números")
# print("=" * 30)

# # Your code here 👇
# found = False
# iterations = 0

# target = int(input("🎮 Ingrese un número a buscar: "))

# for i in range(1, 21):
#   if i == target:
#     found = True
#     iterations = i
#     break

# print(f"✨ Número {target} {"encontrado" if found else "no encontrado"} en la iteración {iterations} 🎯")

# # Test cases:
# print("=" * 30)
# print(found == True and iterations == 5)
# print(found == True and iterations == 1)
# print(found == True and iterations == 15)


# # --------------------------------------------------------------------
# # 💻 o2.2.2: ⏭️ Contador de Pares con Continue
# # --------------------------------------------------------------------
# # Even Counter with Continue ⏭️
# print("⏭️ Contador de Pares (sin múltiplos de 10)")
# print("=" * 45)

# # Your code here 👇
# even_count = 0

# for i in range(1, 21):
#     if i % 10 == 0:
#         continue
#     if i % 2 == 0:
#         even_count += 1

# print(f"✨ Números pares: {even_count} 🎉")

# # Test cases:
# print("=" * 45)
# print(even_count == 8)


# # --------------------------------------------------------------------
# # 💻 o2.2.3: 🎨 Generador de Triángulo
# # --------------------------------------------------------------------
# # Triangle Generator 🎨
# print("🎨 Generador de Triángulo")
# print("=" * 30)

# # Your code here 👇
# pattern = ""

# height = int(input("🎮 Ingrese la altura del triángulo: "))

# for i in range(height):
#   for j in range(i + 1):
#     pattern += "*"
#   if i == height - 1:
#     break
#   pattern += "\n"

# print(pattern)

# # Test cases:
# print("=" * 30)
# print(pattern == "*\n**\n***")
# print(pattern == "*\n**\n***\n****")
# print(pattern == "*\n**\n***\n****\n*****")


# # --------------------------------------------------------------------
# # 💻 o2.2.4: 🔢 Tabla de Multiplicar Completa
# # --------------------------------------------------------------------
# # Complete Multiplication Tables 🔢
# print("🔢 Tablas de Multiplicar del 1 al 5")
# print("=" * 40)

# # Your code here 👇
# total_operations = 0
# table_5_sum = 0

# for number in range(5):
#     print(f"Tabla del {number + 1}:")
#     for multi in range(10):
#         multiplicand = number + 1
#         multiplier = multi + 1
#         product = multiplicand * multiplier
#         print(f"{multiplicand} x {multiplier} = {multiplicand * multiplier}")
#         total_operations += 1

#         if multiplicand == 5:
#             table_5_sum += multiplicand * multiplier

# # Test cases:
# print("=" * 40)
# print(total_operations == 50)
# print(table_5_sum == 275)


# # --------------------------------------------------------------------
# # 🎯 o2.2.P: 🎯 Proyecto Integrador - Juego de Adivina el Número Mejorado
# # --------------------------------------------------------------------
# import random

# # 🎯 Advanced Number Guessing Game
# print("🎯 JUEGO: ADIVINA EL NÚMERO")
# print("=" * 35)
# print("Adivina un número entre 1 y 50")
# print("Tienes 7 intentos máximo")
# print("=" * 35)

# # Your code here 👇
# secret_number = random.randint(1, 50)
# max_attempts = 7
# won = False
# attempts = 0
# score = 0

# while attempts < max_attempts:
#   attempts += 1
#   guess = int(input(f"🎲 Intento {attempts}/{max_attempts}: "))

#   if guess == secret_number:
#     won = True
#     score += 100 - (attempts * 10)
#     if attempts <= 3:
#       score += 50
#     break

#   if guess < secret_number:
#     print("Muy bajo")
#   elif guess > secret_number:
#     print("Muy alto")

# # Example output:
# if won:
#   print(f"🎉 ¡CORRECTO! Adivinaste en {attempts} intento el número {secret_number}")
# else:
#   print(f"💔 Game over! El número era {secret_number}")

# print(f"🏆 Puntuación: {score} puntos")

# # Test cases:
# print("=" * 35)
# print(won == True and attempts == 1 and score == 140)
# print(won == True and attempts == 5 and score == 50)
# print(won == False and attempts == 7 and score == 0)
