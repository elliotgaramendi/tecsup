"""
🐍 PYTHON FUNDAMENTALS - COMPLETE GUIDE 🐍
==========================================
A comprehensive collection of 20 exercises + 1 final project ✨

HOW TO USE:
-----------
1. Uncomment the exercise you want to run at the bottom of the file
2. Run the file: python this_file.py
3. Follow the prompts and enjoy coding! 🚀
"""

# ====================================================================
# 📚 TOPIC 1: Algorithms and Code Representation
# ====================================================================

def exercise_01():
    """🧮 Simple Addition Calculator ➕"""
    print("\n" + "="*60)
    print("Exercise 1.1 - Simple Addition Calculator ➕")
    print("="*60)

    num1 = float(input("💡 Enter first number: "))
    num2 = float(input("💡 Enter second number: "))
    result = num1 + num2

    print(f"✨ The result is: {result} 🎉")
    print("="*60)
    return result


def exercise_02():
    """📐 Rectangle Area Calculator"""
    print("\n" + "="*60)
    print("Exercise 1.2 - Rectangle Area Calculator 📐")
    print("="*60)

    base = float(input("📏 Enter the base: "))
    height = float(input("📏 Enter the height: "))
    area = base * height

    print(f"✨ The rectangle area is: {area} square meters 📐✅")
    print("="*60)
    return area


def exercise_03():
    """🌡️ Temperature Converter (Celsius to Fahrenheit)"""
    print("\n" + "="*60)
    print("Exercise 1.3 - Temperature Converter 🌡️")
    print("="*60)

    celsius = float(input("🌡️ Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32

    print(f"🔥 Fahrenheit is: {fahrenheit:.1f} °F 🌡️✨")
    print("="*60)
    return fahrenheit


def exercise_04():
    """📊 Average Calculator"""
    print("\n" + "="*60)
    print("Exercise 1.4 - Average Calculator 📊")
    print("="*60)

    num1 = float(input("📝 Enter first number: "))
    num2 = float(input("📝 Enter second number: "))
    num3 = float(input("📝 Enter third number: "))
    average = (num1 + num2 + num3) / 3

    print(f"✨ The average is: {average:.2f} 📊✅")
    print("="*60)
    return average


def exercise_05():
    """📏 Rectangle Perimeter Calculator"""
    print("\n" + "="*60)
    print("Exercise 1.5 - Rectangle Perimeter Calculator 📏")
    print("="*60)

    base = float(input("📐 Enter the base: "))
    height = float(input("📐 Enter the height: "))
    perimeter = 2 * (base + height)

    print(f"✨ The perimeter is: {perimeter} 📏✅")
    print("="*60)
    return perimeter


# ====================================================================
# 🔀 TOPIC 2: Basic Conditional Structures
# ====================================================================

def exercise_06():
    """🔢 Even or Odd Detector"""
    print("\n" + "="*60)
    print("Exercise 2.2 - Even/Odd Detector 🔢")
    print("="*60)

    number = int(input("🔢 Enter an integer: "))

    if number % 2 == 0:
        result = "even"
        emoji = "2️⃣"
    else:
        result = "odd"
        emoji = "1️⃣"

    print(f"{emoji} The number is: {result} ✨")
    print("="*60)
    return result


def exercise_07():
    """➕➖ Positive, Negative or Zero Detector"""
    print("\n" + "="*60)
    print("Exercise 2.1 - Number Classifier ➕➖")
    print("="*60)

    number = float(input("🔢 Enter a number: "))

    if number > 0:
        result = "positive"
        emoji = "✅"
    elif number < 0:
        result = "negative"
        emoji = "⚠️"
    else:
        result = "zero"
        emoji = "⭕"

    print(f"{emoji} The number is: {result} 🎯")
    print("="*60)
    return result


def exercise_08():
    """⚖️ Number Comparator"""
    print("\n" + "="*60)
    print("Exercise 2.3 - Number Comparator ⚖️")
    print("="*60)

    num1 = float(input("📝 Enter first number: "))
    num2 = float(input("📝 Enter second number: "))

    if num1 > num2:
        result = "greater"
        emoji = "📈"
    elif num1 < num2:
        result = "less"
        emoji = "📉"
    else:
        result = "equal"
        emoji = "⚖️"

    print(f"{emoji} First number is {result} than second 🎯")
    print("="*60)
    return result


def exercise_09():
    """👥 Age Classifier"""
    print("\n" + "="*60)
    print("Exercise 2.4 - Age Classifier 👥")
    print("="*60)

    age = int(input("🎂 Enter your age: "))

    if age < 18:
        result = "child"
        emoji = "👶"
    elif age <= 64:
        result = "adult"
        emoji = "👨"
    else:
        result = "senior"
        emoji = "👴"

    print(f"{emoji} You are classified as: {result} ✨")
    print("="*60)
    return result


def exercise_10():
    """➕➖ Simple Calculator"""
    print("\n" + "="*60)
    print("Exercise 2.5 - Simple Calculator ➕➖")
    print("="*60)

    num1 = float(input("🔢 Enter first number: "))
    num2 = float(input("🔢 Enter second number: "))
    operation = input("⚙️ Enter operation (+ or -): ")

    if operation == "+":
        result = num1 + num2
        emoji = "➕"
    elif operation == "-":
        result = num1 - num2
        emoji = "➖"
    else:
        result = 0
        emoji = "❌"

    print(f"{emoji} Result: {result} 🎉")
    print("="*60)
    return result


# ====================================================================
# 🔁 TOPIC 3: Basic Loop Structures
# ====================================================================

def exercise_11():
    """🔢 Number Counter (1 to 10)"""
    print("\n" + "="*60)
    print("Exercise 3.1 - Number Counter 🔢")
    print("="*60)

    count = 0
    print("📊 Counting from 1 to 10:")

    for i in range(1, 11):
        print(f"  {i} {'🌟' if i == 10 else '⭐'}")
        count += 1

    print(f"✨ Total numbers counted: {count} 🎯")
    print("="*60)
    return count


def exercise_12():
    """🧮 Sum of Numbers (1 to 5)"""
    print("\n" + "="*60)
    print("Exercise 3.2 - Sum Calculator 🧮")
    print("="*60)

    total = 0
    print("📊 Adding numbers from 1 to 5:")

    for i in range(1, 6):
        total += i
        print(f"  + {i} = {total}")

    print(f"✨ Final sum: {total} 🎉")
    print("="*60)
    return total


def exercise_13():
    """✖️ Multiplication Table of 2"""
    print("\n" + "="*60)
    print("Exercise 3.3 - Multiplication Table ✖️")
    print("="*60)

    print("📊 Multiplication table of 2:")
    last_result = 0

    for i in range(1, 11):
        result = 2 * i
        last_result = result
        print(f"  2 × {i:2d} = {result:3d} {'🌟' if i == 10 else '⭐'}")

    print(f"✨ Last result: {last_result} 🎯")
    print("="*60)
    return last_result


def exercise_14():
    """🔢 Even Number Counter"""
    print("\n" + "="*60)
    print("Exercise 3.4 - Even Counter 🔢")
    print("="*60)

    even_count = 0
    print("📊 Finding even numbers from 1 to 10:")

    for i in range(1, 11):
        if i % 2 == 0:
            even_count += 1
            print(f"  {i} is even! ✅")

    print(f"✨ Total even numbers: {even_count} 🎉")
    print("="*60)
    return even_count


def exercise_15():
    """🧮 Sum of Odd Numbers (1 to 9)"""
    print("\n" + "="*60)
    print("Exercise 3.5 - Odd Sum Calculator 🧮")
    print("="*60)

    odd_sum = 0
    print("📊 Adding odd numbers from 1 to 9:")

    for i in range(1, 10):
        if i % 2 != 0:
            odd_sum += i
            print(f"  + {i} = {odd_sum}")

    print(f"✨ Final sum of odds: {odd_sum} 🎉")
    print("="*60)
    return odd_sum


# ====================================================================
# 🚀 TOPIC 4: Knowledge Integration
# ====================================================================

def exercise_16():
    """📊 Grade Average Calculator"""
    print("\n" + "="*60)
    print("Exercise 4.1 - Grade Average Calculator 📊")
    print("="*60)

    total = 0
    print("📝 Enter 5 grades:")

    for i in range(1, 6):
        grade = float(input(f"  Grade {i}: "))
        total += grade

    average = total / 5
    status = "passed" if average >= 70 else "failed"
    emoji = "✅" if average >= 70 else "❌"

    print(f"\n{emoji} Average: {average:.1f}")
    print(f"{emoji} Status: {status.upper()} 🎯")
    print("="*60)
    return average, status


def exercise_17():
    """➕➖ Positive/Negative Counter"""
    print("\n" + "="*60)
    print("Exercise 4.2 - Positive/Negative Counter ➕➖")
    print("="*60)

    positive_count = 0
    negative_count = 0

    print("📝 Enter 5 numbers:")
    for i in range(1, 6):
        number = float(input(f"  Number {i}: "))
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    print(f"\n✨ Positive numbers: {positive_count} ➕")
    print(f"✨ Negative numbers: {negative_count} ➖")
    print("="*60)
    return positive_count, negative_count


def exercise_18():
    """✖️ Custom Multiplication Table"""
    print("\n" + "="*60)
    print("Exercise 4.3 - Custom Multiplication Table ✖️")
    print("="*60)

    number = int(input("🔢 Enter a number (1-5): "))

    if 1 <= number <= 5:
        print(f"\n📊 Multiplication table of {number}:")
        last_result = 0

        for i in range(1, 6):
            result = number * i
            last_result = result
            print(f"  {number} × {i} = {result:2d} {'🌟' if i == 5 else '⭐'}")

        print(f"✨ Last result: {last_result} 🎯")
    else:
        print("❌ Invalid number! Please enter 1-5")
        last_result = 0

    print("="*60)
    return last_result


def exercise_19():
    """🧮 Simple Factorial Calculator"""
    print("\n" + "="*60)
    print("Exercise 4.4 - Factorial Calculator 🧮")
    print("="*60)

    number = int(input("🔢 Enter a number (1-5): "))

    if 1 <= number <= 5:
        factorial = 1
        print(f"\n📊 Calculating {number}!:")

        for i in range(1, number + 1):
            factorial *= i
            print(f"  Step {i}: {factorial}")

        print(f"✨ {number}! = {factorial} 🎉")
    else:
        print("❌ Invalid number! Please enter 1-5")
        factorial = 0

    print("="*60)
    return factorial


def exercise_20():
    """🎯 Number Guessing Game"""
    print("\n" + "="*60)
    print("Exercise 4.5 - Guessing Game 🎯")
    print("="*60)

    secret_number = 7
    attempts = 3
    result = ""

    print("🎮 Guess the secret number between 1 and 10!")
    print(f"⚡ You have {attempts} attempts\n")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"🎲 Attempt {attempt}/{attempts}: "))

        if guess == secret_number:
            result = "won"
            print(f"🎉 CONGRATULATIONS! You won! 🏆")
            break
        elif guess < secret_number:
            result = "higher"
            print("📈 Try HIGHER! ⬆️")
        else:
            result = "lower"
            print("📉 Try LOWER! ⬇️")
    else:
        result = "lost"
        print(f"💔 Game over! The number was {secret_number}")

    print("="*60)
    return result


# ====================================================================
# 🏫 FINAL PROJECT: Basic Grade Management System
# ====================================================================

def final_project():
    """🏫 Student Grade Management System"""
    print("\n" + "="*70)
    print("🏫 FINAL PROJECT - GRADE MANAGEMENT SYSTEM 🏫")
    print("="*70)

    # 1. Register students
    print("\n📝 STUDENT REGISTRATION:")
    student1_name = input("  Student 1 name: ")
    student2_name = input("  Student 2 name: ")
    student3_name = input("  Student 3 name: ")

    # 2. Enter grades
    print("\n📊 GRADE ENTRY (0-100):")
    student1_grade = float(input(f"  {student1_name}'s grade: "))
    student2_grade = float(input(f"  {student2_name}'s grade: "))
    student3_grade = float(input(f"  {student3_name}'s grade: "))

    # 3. Calculate statistics
    average = (student1_grade + student2_grade + student3_grade) / 3
    highest_grade = max(student1_grade, student2_grade, student3_grade)

    passed_count = 0
    if student1_grade >= 70: passed_count += 1
    if student2_grade >= 70: passed_count += 1
    if student3_grade >= 70: passed_count += 1

    # 4. Generate report
    print("\n" + "="*70)
    print("📋 FINAL REPORT:")
    print("="*70)

    print(f"\n👨‍🎓 {student1_name}: {student1_grade} {'✅' if student1_grade >= 70 else '❌'}")
    print(f"👨‍🎓 {student2_name}: {student2_grade} {'✅' if student2_grade >= 70 else '❌'}")
    print(f"👨‍🎓 {student3_name}: {student3_grade} {'✅' if student3_grade >= 70 else '❌'}")

    print(f"\n📊 GROUP STATISTICS:")
    print(f"  ✨ Class average: {average:.1f}")
    print(f"  🏆 Highest grade: {highest_grade}")
    print(f"  ✅ Students passed: {passed_count}/3")

    print("="*70)
    print("🎉 REPORT COMPLETED SUCCESSFULLY! 🎉")
    print("="*70)

    return average, highest_grade, passed_count


# ====================================================================
# 🎮 MAIN MENU - Exercise Selector
# ====================================================================

def main_menu():
    """Interactive menu to select exercises"""
    print("\n" + "🐍"*30)
    print("🌟 PYTHON FUNDAMENTALS - COMPLETE GUIDE 🌟")
    print("🐍"*30)

    exercises = {
        "1.1": ("Simple Addition Calculator ➕", exercise_01),
        "1.2": ("Rectangle Area Calculator 📐", exercise_02),
        "1.3": ("Temperature Converter 🌡️", exercise_03),
        "1.4": ("Average Calculator 📊", exercise_04),
        "1.5": ("Rectangle Perimeter 📏", exercise_05),
        "2.1": ("Even/Odd Detector 🔢", exercise_06),
        "2.2": ("Number Classifier ➕➖", exercise_07),
        "2.3": ("Number Comparator ⚖️", exercise_08),
        "2.4": ("Age Classifier 👥", exercise_09),
        "2.5": ("Simple Calculator ➕➖", exercise_10),
        "3.1": ("Number Counter 🔢", exercise_11),
        "3.2": ("Sum Calculator 🧮", exercise_12),
        "3.3": ("Multiplication Table ✖️", exercise_13),
        "3.4": ("Even Counter 🔢", exercise_14),
        "3.5": ("Odd Sum Calculator 🧮", exercise_15),
        "4.1": ("Grade Average 📊", exercise_16),
        "4.2": ("Positive/Negative Counter ➕➖", exercise_17),
        "4.3": ("Custom Multiplication ✖️", exercise_18),
        "4.4": ("Factorial Calculator 🧮", exercise_19),
        "4.5": ("Guessing Game 🎯", exercise_20),
        "FP": ("🏫 FINAL PROJECT 🏫", final_project),
    }

    print("\n📚 TOPIC 1: Algorithms and Code")
    for key in ["1.1", "1.2", "1.3", "1.4", "1.5"]:
        print(f"  {key} - {exercises[key][0]}")

    print("\n🔀 TOPIC 2: Conditional Structures")
    for key in ["2.1", "2.2", "2.3", "2.4", "2.5"]:
        print(f"  {key} - {exercises[key][0]}")

    print("\n🔁 TOPIC 3: Loop Structures")
    for key in ["3.1", "3.2", "3.3", "3.4", "3.5"]:
        print(f"  {key} - {exercises[key][0]}")

    print("\n🚀 TOPIC 4: Knowledge Integration")
    for key in ["4.1", "4.2", "4.3", "4.4", "4.5"]:
        print(f"  {key} - {exercises[key][0]}")

    print("\n🎯 FINAL PROJECT")
    print(f"  FP - {exercises['FP'][0]}")

    print("\n" + "="*60)
    choice = input("🎮 Select exercise (e.g., 1.1, 2.3, FP) or 'Q' to quit: ").upper()

    if choice == 'Q':
        print("👋 Thanks for coding! See you soon! 🚀")
        return

    if choice in exercises:
        exercises[choice][1]()
        input("\n⏸️  Press ENTER to continue...")
        main_menu()
    else:
        print("❌ Invalid selection! Try again.")
        input("\n⏸️  Press ENTER to continue...")
        main_menu()


# ====================================================================
# 🚀 PROGRAM ENTRY POINT
# ====================================================================

if __name__ == "__main__":
    """
    🎯 HOW TO USE THIS FILE:

    METHOD 1 - Interactive Menu (Recommended):
    ------------------------------------------
    Uncomment the line below to use the interactive menu
    """
    main_menu()

    """
    METHOD 2 - Run Specific Exercise:
    ---------------------------------
    Uncomment ONE of the lines below to run a specific exercise:
    """
    # exercise_01()  # Simple Addition
    # exercise_02()  # Rectangle Area
    # exercise_03()  # Temperature Converter
    # exercise_04()  # Average Calculator
    # exercise_05()  # Rectangle Perimeter
    # exercise_06()  # Even/Odd Detector
    # exercise_07()  # Number Classifier
    # exercise_08()  # Number Comparator
    # exercise_09()  # Age Classifier
    # exercise_10()  # Simple Calculator
    # exercise_11()  # Number Counter
    # exercise_12()  # Sum Calculator
    # exercise_13()  # Multiplication Table
    # exercise_14()  # Even Counter
    # exercise_15()  # Odd Sum Calculator
    # exercise_16()  # Grade Average
    # exercise_17()  # Positive/Negative Counter
    # exercise_18()  # Custom Multiplication
    # exercise_19()  # Factorial Calculator
    # exercise_20()  # Guessing Game
    # final_project()  # Final Project

    """
    🎉 CONGRATULATIONS! 🎉
    You have access to all 20 exercises + 1 final project!

    ✨ Choose your preferred method above and start coding!
    💡 Tip: Use the interactive menu for the best experience!
    """

    print("\n" + "🌟"*30)
    print("🐍 Python Fundamentals Guide Loaded Successfully! 🐍")
    print("🌟"*30)
    print("\n💡 QUICK START:")
    print("  1. Scroll up to 'PROGRAM ENTRY POINT' section")
    print("  2. Uncomment 'main_menu()' for interactive mode")
    print("  3. Or uncomment any specific exercise to run it")
    print("  4. Save and run the file!")
    print("\n🚀 Happy Coding! ✨")
    print("="*70)
