"""
✨ Funciones Lab Solutions o13 by @elliotgaramendi 👨‍💻
📚 o13 Funciones en Python 🐍✨
"""

import math

test_results = []


def record_test(test_name, condition):
    """Run a test and record the result. ✅/❌"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")


# ====================================================================
# o13 Funciones Lab 📚✨
# ====================================================================


# --------------------------------------------------------------------
# o13.1 🧮 Calculadora de Área 📐✨
# --------------------------------------------------------------------
def calculate_area(shape, **dimensions):
    """🧮 Calculate area of geometric shapes.
    Returns area as float."""
    # Validate that shape is supported and dimensions are valid
    if shape == "rectangle":
        # Check required dimensions
        if "width" not in dimensions or "height" not in dimensions:
            return 0.0
        width = dimensions["width"]
        height = dimensions["height"]
        # Check for negative dimensions
        if width < 0 or height < 0:
            return 0.0
        return float(width * height)

    elif shape == "circle":
        # Check required dimensions
        if "radius" not in dimensions:
            return 0.0
        radius = dimensions["radius"]
        # Check for negative radius
        if radius < 0:
            return 0.0
        return float(math.pi * radius * radius)

    elif shape == "triangle":
        # Check required dimensions
        if "base" not in dimensions or "height" not in dimensions:
            return 0.0
        base = dimensions["base"]
        height = dimensions["height"]
        # Check for negative dimensions
        if base < 0 or height < 0:
            return 0.0
        return float((base * height) / 2)

    else:
        # Unsupported shape
        return 0.0


def test_o13_1():
    # o13.1.1: Área de rectángulo
    result = calculate_area("rectangle", width=5, height=3)
    record_test("o13.1.1 rectángulo", result == 15.0)

    # o13.1.2: Área de círculo
    result = calculate_area("circle", radius=2)
    expected = math.pi * 4  # π × 2²
    record_test("o13.1.2 círculo", abs(result - expected) < 0.001)

    # o13.1.3: Área de triángulo
    result = calculate_area("triangle", base=4, height=6)
    record_test("o13.1.3 triángulo", result == 12.0)

    # o13.1.4: Verificación de tipos
    result = calculate_area("rectangle", width=2, height=3)
    record_test("o13.1.4 retorna float", isinstance(result, float))

    # o13.1.5: Figura no soportada
    result = calculate_area("pentagon", side=5)
    record_test("o13.1.5 no soportada", result == 0.0)


# Run tests for o13.1 🚀
test_o13_1()


# --------------------------------------------------------------------
# o13.2 🔒 Validador de contraseñas 🛡️🎯
# --------------------------------------------------------------------
def validate_password(password, min_length=8, require_special=True):
    """🔒 Validate password strength and security requirements.
    Returns dict with validation result and errors."""
    # Handle None or empty password
    if not password or password == "":
        return {"is_valid": False, "errors": ["Password cannot be empty"]}

    # Handle invalid min_length
    if min_length <= 0:
        return {"is_valid": False, "errors": ["Invalid minimum length"]}

    errors = []

    # Check minimum length
    if len(password) < min_length:
        errors.append("Too short")

    # Check for uppercase letter
    if not any(c.isupper() for c in password):
        errors.append("Missing uppercase letter")

    # Check for lowercase letter
    if not any(c.islower() for c in password):
        errors.append("Missing lowercase letter")

    # Check for digit
    if not any(c.isdigit() for c in password):
        errors.append("Missing digit")

    # Check for special character if required
    if require_special:
        special_chars = "!@#$%^&*"
        if not any(c in special_chars for c in password):
            errors.append("Missing special character")

    return {"is_valid": len(errors) == 0, "errors": errors}


def test_o13_2():
    # o13.2.1: Contraseña válida completa
    result = validate_password("Password123!", 8, True)
    expected = {"is_valid": True, "errors": []}
    record_test("o13.2.1 válida completa", result == expected)

    # o13.2.2: Muy corta
    result = validate_password("Pass1!", 8, True)
    record_test(
        "o13.2.2 muy corta", not result["is_valid"] and "Too short" in result["errors"]
    )

    # o13.2.3: Sin caracteres especiales
    result = validate_password("Password123", 8, True)
    record_test(
        "o13.2.3 sin especiales",
        not result["is_valid"] and "Missing special character" in result["errors"],
    )

    # o13.2.4: Verificación de tipos
    result = validate_password("ValidPass1!", 8, True)
    record_test("o13.2.4 retorna dict", isinstance(result, dict))

    # o13.2.5: Sin requerir especiales
    result = validate_password("Password123", 8, False)
    record_test("o13.2.5 sin requerir especiales", result["is_valid"])


# Run tests for o13.2 🚀
test_o13_2()


# --------------------------------------------------------------------
# o13.3 📊 Analizador de estadísticas 📈🔍
# --------------------------------------------------------------------
def analyze_numbers(numbers, operations=["mean", "median", "mode"]):
    """📊 Analyze list of numbers with statistical operations.
    Returns dict with calculated statistics."""
    # Handle empty list
    if not numbers:
        return {}

    results = {}

    for operation in operations:
        if operation == "mean":
            # Calculate arithmetic mean
            results["mean"] = sum(numbers) / len(numbers)

        elif operation == "median":
            # Calculate median (middle value when sorted)
            sorted_nums = sorted(numbers)
            n = len(sorted_nums)
            if n % 2 == 0:
                # Even number of elements - average of two middle values
                results["median"] = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
            else:
                # Odd number of elements - middle value
                results["median"] = sorted_nums[n // 2]

        elif operation == "mode":
            # Calculate mode (most frequent value)
            frequency = {}
            for num in numbers:
                frequency[num] = frequency.get(num, 0) + 1

            # Find the value with highest frequency
            max_count = max(frequency.values())
            # Get first value with max frequency (in case of tie)
            for num in numbers:
                if frequency[num] == max_count:
                    results["mode"] = num
                    break

    return results


def test_o13_3():
    # o13.3.1: Análisis completo
    result = analyze_numbers([1, 2, 2, 3, 4], ["mean", "median", "mode"])
    expected = {"mean": 2.4, "median": 2, "mode": 2}
    record_test("o13.3.1 análisis completo", result == expected)

    # o13.3.2: Solo promedio
    result = analyze_numbers([5, 10, 15], ["mean"])
    expected = {"mean": 10.0}
    record_test("o13.3.2 solo promedio", result == expected)

    # o13.3.3: Números decimales
    result = analyze_numbers([1.5, 2.5, 3.5], ["mean", "median"])
    expected = {"mean": 2.5, "median": 2.5}
    record_test("o13.3.3 decimales", result == expected)

    # o13.3.4: Verificación de tipos
    result = analyze_numbers([1, 2, 3], ["mean"])
    record_test("o13.3.4 retorna dict", isinstance(result, dict))

    # o13.3.5: Lista vacía
    result = analyze_numbers([], ["mean", "median"])
    record_test("o13.3.5 lista vacía", result == {})


# Run tests for o13.3 🚀
test_o13_3()


# --------------------------------------------------------------------
# o13.4 🎨 Generador de patrones 🌈📝
# --------------------------------------------------------------------
def generate_pattern(pattern_type, size, char="*"):
    """🎨 Generate visual patterns with specified character.
    Returns pattern as string with newlines."""
    # Validate size
    if size <= 0:
        return ""

    if pattern_type == "triangle":
        # Generate triangle pattern (growing)
        lines = []
        for i in range(1, size + 1):
            lines.append(char * i)
        return "\n".join(lines)

    elif pattern_type == "diamond":
        # Generate diamond pattern
        lines = []

        # Upper part (including middle)
        for i in range(1, size + 1):
            spaces = " " * (size - i)
            chars = char * (2 * i - 1)
            lines.append(spaces + chars)

        # Lower part
        for i in range(size - 1, 0, -1):
            spaces = " " * (size - i)
            chars = char * (2 * i - 1)
            lines.append(spaces + chars)

        return "\n".join(lines)

    elif pattern_type == "square":
        # Generate hollow square pattern
        lines = []

        for i in range(size):
            if i == 0 or i == size - 1:
                # Top or bottom border - all characters
                lines.append(char * size)
            else:
                # Middle rows - only borders
                lines.append(char + " " * (size - 2) + char)

        return "\n".join(lines)

    else:
        # Unsupported pattern type
        return ""


def test_o13_4():
    # o13.4.1: Triángulo tamaño 3
    result = generate_pattern("triangle", 3, "*")
    expected = "*\n**\n***"
    record_test("o13.4.1 triángulo", result == expected)

    # o13.4.2: Rombo tamaño 3
    result = generate_pattern("diamond", 3, "#")
    expected = "  #\n ###\n#####\n ###\n  #"
    record_test("o13.4.2 rombo", result == expected)

    # o13.4.3: Cuadrado hueco tamaño 3
    result = generate_pattern("square", 3, "+")
    expected = "+++\n+ +\n+++"
    record_test("o13.4.3 cuadrado hueco", result == expected)

    # o13.4.4: Verificación de tipos
    result = generate_pattern("triangle", 2, "*")
    record_test("o13.4.4 retorna str", isinstance(result, str))

    # o13.4.5: Patrón no soportado
    result = generate_pattern("circle", 3, "*")
    record_test("o13.4.5 no soportado", result == "")


# Run tests for o13.4 🚀
test_o13_4()


# --------------------------------------------------------------------
# o13.5 🔄 Procesador de texto avanzado 📝⚡
# --------------------------------------------------------------------
def process_text(text, transformations=["clean", "count"]):
    """🔄 Process text with multiple transformation operations.
    Returns dict with transformation results."""
    results = {}

    for transformation in transformations:
        if transformation == "clean":
            # Clean text: remove extra spaces and convert to lowercase
            cleaned = " ".join(text.split()).lower()
            results["clean"] = cleaned

        elif transformation == "count":
            # Count characters, words, and sentences
            char_count = len(text)
            word_count = len(text.split())

            # Count sentences by looking for sentence-ending punctuation
            sentence_count = text.count(".") + text.count("!") + text.count("?")

            results["count"] = {
                "chars": char_count,
                "words": word_count,
                "sentences": sentence_count,
            }

        elif transformation == "reverse":
            # Reverse the text
            results["reverse"] = text[::-1]

    return results


def test_o13_5():
    # o13.5.1: Limpieza básica
    result = process_text("  Hello   World!  ", ["clean"])
    expected = {"clean": "hello world!"}
    record_test("o13.5.1 limpieza", result == expected)

    # o13.5.2: Conteo de elementos
    result = process_text("Hello world. How are you?", ["count"])
    expected = {"count": {"chars": 25, "words": 5, "sentences": 2}}
    record_test("o13.5.2 conteo", result == expected)

    # o13.5.3: Texto invertido
    result = process_text("Python", ["reverse"])
    expected = {"reverse": "nohtyP"}
    record_test("o13.5.3 invertido", result == expected)

    # o13.5.4: Verificación de tipos
    result = process_text("test", ["clean"])
    record_test("o13.5.4 retorna dict", isinstance(result, dict))

    # o13.5.5: Múltiples transformaciones
    result = process_text("Hello!", ["clean", "reverse"])
    expected = {"clean": "hello!", "reverse": "!olleH"}
    record_test("o13.5.5 múltiples", result == expected)


# Run tests for o13.5 🚀
test_o13_5()

# ====================================================================
# Final Summary 📋
# ====================================================================
print("\n# 📚 Funciones Lab o13 - Final Test Summary 📋")
for r in test_results:
    print(r)
print(f"\nTotal Approved: {sum('✅' in r for r in test_results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in test_results)} ❌")

print(
    "\n🎯 ¡Felicitaciones! Has completado todos los retos de Funciones en Python 🐍✨"
)
