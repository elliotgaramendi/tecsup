"""
🐍 PYTHON NIVEL 4 - COMPLETE SOLUTIONS
======================================
Instructions: Uncomment the challenge you want to run
"""

# ============================================================================
# o4.1: DATE & TIME - WORKING WITH DATES
# ============================================================================


def o4_1_1_birthday_countdown():
    """🎂 Birthday Countdown"""
    print("=" * 50)
    print("🎂 Contador de Cumpleaños")
    print("=" * 50)

    from datetime import datetime

    # Solution
    current_date = datetime.now()
    birthday_month = 8
    birthday_day = 15
    birth_year = 2008

    # Create next birthday
    current_year = current_date.year
    next_birthday = datetime(current_year, birthday_month, birthday_day)

    # If birthday already passed this year, use next year
    if next_birthday < current_date:
        next_birthday = datetime(
            current_year + 1, birthday_month, birthday_day)

    # Calculate days until birthday
    days_until = (next_birthday - current_date).days

    # Calculate age turning
    age_turning = next_birthday.year - birth_year

    print(f"Hoy es: {current_date.strftime('%d/%m/%Y')}")
    print(f"Próximo cumpleaños: {next_birthday.strftime('%d/%m/%Y')}")
    print(f"Faltan {days_until} días para tu cumpleaños!")
    print(f"Cumplirás {age_turning} años")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (birthday_month): {birthday_month == 8}")
    print(f"Test 2 (birthday_day): {birthday_day == 15}")
    print(f"Test 3 (age_turning): {age_turning == 18}")
    print(f"Test 4 (days_until > 0): {days_until > 0}")
    print(f"Test 5 (type check): {type(current_date).__name__ == 'datetime'}")


def o4_1_2_adventure_timer():
    """⏰ Adventure Timer"""
    print("=" * 50)
    print("⏰ Registro de Aventura")
    print("=" * 50)

    from datetime import datetime, time, timedelta

    # Solution
    start_hour = 14
    start_minute = 30
    allowed_hours = 2

    # Create time object
    start_time = time(start_hour, start_minute)

    # Combine with current date
    current_date = datetime.now().date()
    start_datetime = datetime.combine(current_date, start_time)

    # Create duration
    duration = timedelta(hours=allowed_hours)

    # Calculate end time
    end_datetime = start_datetime + duration
    end_hour = end_datetime.hour

    print(f"Inicio de juego: {start_time.strftime('%I:%M %p')}")
    print(f"Duración permitida: {allowed_hours} horas")
    print(f"Debe terminar a las: {end_datetime.strftime('%I:%M %p')}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (start_hour): {start_hour == 14}")
    print(f"Test 2 (start_minute): {start_minute == 30}")
    print(f"Test 3 (allowed_hours): {allowed_hours == 2}")
    print(f"Test 4 (end_hour): {end_hour == 16}")
    print(f"Test 5 (type check): {type(duration).__name__ == 'timedelta'}")


# ============================================================================
# o4.2: MODULES - ORGANIZING CODE
# ============================================================================

def o4_2_1_lucky_number_generator():
    """🎲 Lucky Number Generator"""
    print("=" * 50)
    print("🎲 Generador de Números de Suerte")
    print("=" * 50)

    import random
    import math

    # Solution
    lucky_numbers = []
    for i in range(5):
        lucky_numbers.append(random.randint(1, 50))

    average = sum(lucky_numbers) / len(lucky_numbers)
    rounded_avg = math.ceil(average)
    max_number = max(lucky_numbers)
    min_number = min(lucky_numbers)

    print(f"Números de suerte: {lucky_numbers}")
    print(f"Promedio: {average:.2f}")
    print(f"Promedio redondeado: {rounded_avg}")
    print(f"Mayor: {max_number}, Menor: {min_number}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (length): {len(lucky_numbers) == 5}")
    print(f"Test 2 (range check): {all(1 <= n <= 50 for n in lucky_numbers)}")
    print(f"Test 3 (average > 0): {average > 0}")
    print(f"Test 4 (rounded >= avg): {rounded_avg >= average}")
    print(f"Test 5 (type check): {type(lucky_numbers) == list}")


def o4_2_2_scientific_calculator():
    """🧮 Scientific Calculator"""
    print("=" * 50)
    print("🧮 Calculadora Científica")
    print("=" * 50)

    from math import sqrt, factorial, pow, pi

    # Solution
    number = 144
    square_root = sqrt(number)

    base = 2
    exponent = 10
    power_result = pow(base, exponent)

    n = 5
    factorial_result = factorial(n)

    pi_value = pi
    pi_rounded = round(pi, 2)

    print(f"√{number} = {square_root}")
    print(f"{base}^{exponent} = {power_result}")
    print(f"{n}! = {factorial_result}")
    print(f"π ≈ {pi_rounded}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (square_root): {square_root == 12.0}")
    print(f"Test 2 (power_result): {power_result == 1024.0}")
    print(f"Test 3 (factorial_result): {factorial_result == 120}")
    print(f"Test 4 (pi_value range): {3.14 < pi_value < 3.15}")
    print(f"Test 5 (type check): {type(square_root) == float}")


# ============================================================================
# o4.3: FILES - SAVING INFORMATION
# ============================================================================

def o4_3_1_amorosa_diary():
    """📝 Amorosa's Diary"""
    print("=" * 50)
    print("📝 Diario de Amorosa")
    print("=" * 50)

    # Solution
    file_name = 'diary.txt'
    entry = "Hoy fue un día increíble, aprendí Python y me siento feliz"

    # Write to file
    file = open(file_name, 'w')
    file.write(entry)
    file.close()

    # Read from file
    file = open(file_name, 'r')
    content = file.read()
    file.close()

    # Process content
    word_count = len(content.split())
    has_python = 'Python' in content

    print(f"Contenido del diario:")
    print(content)
    print(f"\nTotal de palabras: {word_count}")
    print(f"Menciona Python: {has_python}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (file_name): {file_name == 'diary.txt'}")
    print(f"Test 2 (content length): {len(content) > 0}")
    print(f"Test 3 (contains Python): {'Python' in content}")
    print(f"Test 4 (contains feliz): {'feliz' in content}")
    print(f"Test 5 (type check): {type(content) == str}")


def o4_3_2_game_scores():
    """🎮 Game Scores"""
    print("=" * 50)
    print("🎮 Puntuaciones de Juego")
    print("=" * 50)

    # Solution
    file_name = 'scores.txt'
    players_scores = [
        "Elliot: 1500",
        "Fe: 1200",
        "Chocolate: 1800"
    ]

    # Write all scores to file
    file = open(file_name, 'w')
    for score_line in players_scores:
        file.write(score_line + '\n')
    file.close()

    # Read file and process
    file = open(file_name, 'r')
    scores = file.readlines()
    file.close()

    num_lines = len(scores)

    # Process to find max score and winner
    max_score = 0
    winner = ''
    total_score = 0

    for line in scores:
        parts = line.strip().split(': ')
        player_name = parts[0]
        player_score = int(parts[1])
        total_score += player_score

        if player_score > max_score:
            max_score = player_score
            winner = player_name

    print(f"Puntuaciones guardadas:")
    for score in scores:
        print(score.strip())

    print(f"\n🏆 Ganador: {winner} con {max_score} puntos")
    print(f"Total de jugadores: {num_lines}")
    print(f"Puntuación total: {total_score}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (num_lines): {num_lines == 3}")
    print(f"Test 2 (max_score): {max_score == 1800}")
    print(f"Test 3 (winner): {winner == 'Chocolate'}")
    print(f"Test 4 (contains Elliot): {'Elliot' in scores[0]}")
    print(f"Test 5 (type check): {type(scores) == list}")


# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main menu to run individual challenges"""

    challenges = {
        # o4.1: Date & Time
        '4.1.1': ('🎂 Contador de Cumpleaños', o4_1_1_birthday_countdown),
        '4.1.2': ('⏰ Registro de Aventura', o4_1_2_adventure_timer),

        # o4.2: Modules
        '4.2.1': ('🎲 Generador de Números de Suerte', o4_2_1_lucky_number_generator),
        '4.2.2': ('🧮 Calculadora Científica', o4_2_2_scientific_calculator),

        # o4.3: Files
        '4.3.1': ('📝 Diario de Amorosa', o4_3_1_amorosa_diary),
        '4.3.2': ('🎮 Puntuaciones de Juego', o4_3_2_game_scores),
    }

    print("\n" + "=" * 60)
    print("🐍 PYTHON NIVEL 4 - SOLUCIONES")
    print("=" * 60)
    print("\nRetos disponibles:\n")

    # Show by topics
    print("📅 o4.1: Date & Time")
    for key in ['4.1.1', '4.1.2']:
        print(f"  {key} - {challenges[key][0]}")

    print("\n📦 o4.2: Modules")
    for key in ['4.2.1', '4.2.2']:
        print(f"  {key} - {challenges[key][0]}")

    print("\n💾 o4.3: Files")
    for key in ['4.3.1', '4.3.2']:
        print(f"  {key} - {challenges[key][0]}")

    print("\n" + "=" * 60)

    while True:
        option = input(
            "\n🎯 Ingresa el número del reto (ej: 4.1.1) o 'q' para salir: ").strip()

        if option.lower() == 'q':
            print("\n👋 ¡Hasta luego! Sigue practicando 🐍✨")
            break

        if option in challenges:
            print("\n")
            challenges[option][1]()  # Execute challenge function
            print("\n" + "=" * 60)
            input("Presiona ENTER para continuar...")
        else:
            print("❌ Reto no encontrado. Intenta de nuevo.")


# ============================================================================
# DIRECT EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Uncomment ONE of these lines to run a specific challenge:

    # --- o4.1: Date & Time ---
    # o4_1_1_birthday_countdown()
    # o4_1_2_adventure_timer()

    # --- o4.2: Modules ---
    # o4_2_1_lucky_number_generator()
    # o4_2_2_scientific_calculator()

    # --- o4.3: Files ---
    # o4_3_1_amorosa_diary()
    # o4_3_2_game_scores()

    # --- Interactive Menu (recommended) ---
    main()
