"""
✨ Gestión de Fechas y Hora Lab Solutions o12 by @elliotgaramendi 👨‍💻
📚 o12 Gestión de Fechas y Hora en Python 🐍✨
"""

from datetime import datetime, timedelta

test_results = []


def record_test(test_name, condition):
    """Run a test and record the result. ✅/❌"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")


# ====================================================================
# o12 Gestión de Fechas y Hora Lab 📚✨
# ====================================================================


# --------------------------------------------------------------------
# o12.1 🎂 Calculadora de Edad 📊✨
# --------------------------------------------------------------------
def calculate_age(birth_date, current_date):
    """🎂 Calculate exact age in years from birth date.
    Returns age as integer."""
    # Convert string dates to datetime objects
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    current = datetime.strptime(current_date, "%Y-%m-%d")

    # Calculate basic age difference in years
    age = current.year - birth.year

    # Check if birthday hasn't occurred yet this year
    # If current month/day is before birth month/day, subtract 1 year
    if (current.month, current.day) < (birth.month, birth.day):
        age -= 1

    return age


def test_o12_1():
    # o12.1.1: Cumpleaños ya pasado
    result = calculate_age("2020-03-15", "2024-08-10")
    record_test("o12.1.1 cumpleaños pasado", result == 4)

    # o12.1.2: Cumpleaños aún no llega
    result = calculate_age("2020-11-25", "2024-08-10")
    record_test("o12.1.2 cumpleaños no llega", result == 3)

    # o12.1.3: Exactamente en cumpleaños
    result = calculate_age("2021-12-31", "2024-12-31")
    record_test("o12.1.3 en cumpleaños", result == 3)

    # o12.1.4: Verificación de tipos
    result = calculate_age("2022-01-01", "2024-01-01")
    record_test("o12.1.4 retorna int", isinstance(result, int))

    # o12.1.5: Ratita bebé
    result = calculate_age("2024-05-01", "2024-08-15")
    record_test("o12.1.5 bebé menor 1 año", result == 0)


# Run tests for o12.1 🚀
test_o12_1()


# --------------------------------------------------------------------
# o12.2 📊 Contador de días hábiles 🗓️🎯
# --------------------------------------------------------------------
def count_business_days(start_date, end_date):
    """📊 Count business days (Mon-Fri) between two dates.
    Returns count as integer."""
    # Convert string dates to datetime objects
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    # Initialize counter and current date
    business_days = 0
    current_date = start

    # Iterate through each day from start to end (excluding end)
    while current_date < end:
        # Check if current day is a weekday (Monday=0 to Friday=4)
        if current_date.weekday() < 5:
            business_days += 1

        # Move to next day
        current_date += timedelta(days=1)

    return business_days


def test_o12_2():
    # o12.2.1: Semana completa
    result = count_business_days("2024-01-01", "2024-01-08")
    record_test("o12.2.1 semana completa", result == 5)

    # o12.2.2: Solo fin de semana
    result = count_business_days("2024-01-06", "2024-01-08")
    record_test("o12.2.2 solo fin semana", result == 0)

    # o12.2.3: Misma fecha hábil
    result = count_business_days("2024-01-01", "2024-01-01")
    record_test("o12.2.3 misma fecha", result == 0)

    # o12.2.4: Verificación de tipos
    result = count_business_days("2024-01-01", "2024-01-05")
    record_test("o12.2.4 retorna int", isinstance(result, int))

    # o12.2.5: Período con fines de semana
    result = count_business_days("2024-01-01", "2024-01-15")
    record_test("o12.2.5 dos semanas", result == 10)


# Run tests for o12.2 🚀
test_o12_2()


# --------------------------------------------------------------------
# o12.3 🔍 Formateador de fechas 🎨📋
# --------------------------------------------------------------------
def format_date_display(date_string, format_type):
    """🔍 Format date string into different display formats.
    Returns formatted string."""
    try:
        # Convert string to datetime object
        dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

        # Spanish month names
        meses = [
            "enero",
            "febrero",
            "marzo",
            "abril",
            "mayo",
            "junio",
            "julio",
            "agosto",
            "septiembre",
            "octubre",
            "noviembre",
            "diciembre",
        ]

        # Format according to type
        if format_type == "short":
            return dt.strftime("%d/%m/%Y")
        elif format_type == "long":
            mes_nombre = meses[dt.month - 1]
            return f"{dt.day} de {mes_nombre} de {dt.year}"
        elif format_type == "time":
            return dt.strftime("%H:%M")
        else:
            # Invalid format type, return original
            return date_string

    except ValueError:
        # Invalid date format, return original
        return date_string


def test_o12_3():
    # o12.3.1: Formato corto
    result = format_date_display("2024-03-15 14:30:45", "short")
    record_test("o12.3.1 formato corto", result == "15/03/2024")

    # o12.3.2: Formato largo
    result = format_date_display("2024-12-25 09:15:30", "long")
    record_test("o12.3.2 formato largo", result == "25 de diciembre de 2024")

    # o12.3.3: Solo tiempo
    result = format_date_display("2024-06-10 16:45:20", "time")
    record_test("o12.3.3 solo tiempo", result == "16:45")

    # o12.3.4: Verificación de tipos
    result = format_date_display("2024-01-01 12:00:00", "short")
    record_test("o12.3.4 retorna str", isinstance(result, str))

    # o12.3.5: Formato inválido
    result = format_date_display("2024-08-20 11:30:15", "invalid")
    record_test("o12.3.5 formato inválido", result == "2024-08-20 11:30:15")


# Run tests for o12.3 🚀
test_o12_3()


# --------------------------------------------------------------------
# o12.4 🔄 Calculadora de diferencias ⏰📊
# --------------------------------------------------------------------
def calculate_time_difference(datetime1, datetime2, unit):
    """🔄 Calculate time difference between two datetimes.
    Returns difference in specified unit as float."""
    try:
        # Convert string datetimes to datetime objects
        dt1 = datetime.strptime(datetime1, "%Y-%m-%d %H:%M:%S")
        dt2 = datetime.strptime(datetime2, "%Y-%m-%d %H:%M:%S")

        # Calculate difference as timedelta
        diff = dt2 - dt1

        # Convert to requested unit
        if unit == "days":
            return float(diff.total_seconds() / (24 * 3600))
        elif unit == "hours":
            return float(diff.total_seconds() / 3600)
        elif unit == "minutes":
            return float(diff.total_seconds() / 60)
        else:
            # Invalid unit
            return 0.0

    except ValueError:
        # Invalid datetime format
        return 0.0


def test_o12_4():
    # o12.4.1: Diferencia en días
    result = calculate_time_difference(
        "2024-01-01 00:00:00", "2024-01-05 00:00:00", "days"
    )
    record_test("o12.4.1 diferencia días", result == 4.0)

    # o12.4.2: Diferencia en horas
    result = calculate_time_difference(
        "2024-01-01 10:00:00", "2024-01-01 15:30:00", "hours"
    )
    record_test("o12.4.2 diferencia horas", result == 5.5)

    # o12.4.3: Diferencia en minutos
    result = calculate_time_difference(
        "2024-01-01 10:00:00", "2024-01-01 10:45:00", "minutes"
    )
    record_test("o12.4.3 diferencia minutos", result == 45.0)

    # o12.4.4: Verificación de tipos
    result = calculate_time_difference(
        "2024-01-01 10:00:00", "2024-01-01 12:00:00", "days"
    )
    record_test("o12.4.4 retorna float", isinstance(result, float))

    # o12.4.5: Unidad inválida
    result = calculate_time_difference(
        "2024-01-01 10:00:00", "2024-01-01 11:00:00", "invalid"
    )
    record_test("o12.4.5 unidad inválida", result == 0.0)


# Run tests for o12.4 🚀
test_o12_4()


# --------------------------------------------------------------------
# o12.5 🤝 Generador de cronograma 📅✨
# --------------------------------------------------------------------
def generate_schedule(start_date, num_weeks, meeting_day):
    """🤝 Generate weekly meeting schedule starting from date.
    Returns list of meeting dates as strings."""
    # Handle zero weeks case
    if num_weeks == 0:
        return []

    # Convert start date to datetime object
    start = datetime.strptime(start_date, "%Y-%m-%d")

    # Find the first meeting date
    # Calculate days until the desired meeting day
    days_until_meeting = (meeting_day - start.weekday()) % 7

    # If start_date is already the meeting day, use it
    if start.weekday() == meeting_day:
        first_meeting = start
    else:
        first_meeting = start + timedelta(days=days_until_meeting)

    # Generate the schedule
    schedule = []
    current_meeting = first_meeting

    for week in range(num_weeks):
        # Add current meeting date to schedule
        schedule.append(current_meeting.strftime("%Y-%m-%d"))
        # Move to next week (add 7 days)
        current_meeting += timedelta(days=7)

    return schedule


def test_o12_5():
    # o12.5.1: Cronograma básico
    result = generate_schedule("2024-01-01", 3, 1)
    expected = ["2024-01-02", "2024-01-09", "2024-01-16"]
    record_test("o12.5.1 cronograma básico", result == expected)

    # o12.5.2: Empezar día correcto
    result = generate_schedule("2024-01-02", 2, 1)
    expected = ["2024-01-02", "2024-01-09"]
    record_test("o12.5.2 día correcto", result == expected)

    # o12.5.3: Reuniones de viernes
    result = generate_schedule("2024-01-01", 2, 4)
    expected = ["2024-01-05", "2024-01-12"]
    record_test("o12.5.3 viernes", result == expected)

    # o12.5.4: Verificación de tipos
    result = generate_schedule("2024-01-01", 1, 0)
    record_test("o12.5.4 retorna list", isinstance(result, list))

    # o12.5.5: Cero semanas
    result = generate_schedule("2024-01-01", 0, 1)
    record_test("o12.5.5 cero semanas", result == [])


# Run tests for o12.5 🚀
test_o12_5()

# ====================================================================
# Final Summary 📋
# ====================================================================
print("\n# 📚 Gestión de Fechas y Hora Lab o12 - Final Test Summary 📋")
for r in test_results:
    print(r)
print(f"\nTotal Approved: {sum('✅' in r for r in test_results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in test_results)} ❌")

print(
    "\n🎯 ¡Felicitaciones! Has completado todos los retos de Gestión de Fechas y Hora en Python 🐍✨"
)