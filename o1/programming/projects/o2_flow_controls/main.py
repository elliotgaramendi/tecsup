# # o2.1.1 Text Case Converter 🔤
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

# ========

# # o2.1.2 Word Extractor ✂️
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

# ========

# # o2.1.3 Word Finder and Replacer 🔍
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

# ========

# # o2.1.4Credential Validator 🎫
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

# ========

# # o2.1.P 📋 User Registration System
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
