# **📅 o12 Gestión de Fechas y Hora ⏰✨**

La gestión de fechas y hora es fundamental en programación, permitiendo trabajar con información temporal de manera precisa y eficiente. Python ofrece el módulo `datetime` que nos permite crear, manipular, formatear y realizar cálculos con fechas y horas. ¡Es esencial para aplicaciones que manejan eventos, registros, programación de tareas y análisis temporal! 🕐📊

## 🎯 Objetivos

* 📅 **Crear y manipular fechas** usando datetime para representar momentos específicos
* ⏰ **Trabajar con tiempo** manejando horas, minutos y segundos con precisión
* 🔄 **Realizar cálculos temporales** sumando, restando y comparando fechas
* 📝 **Formatear fechas** convirtiendo entre strings y objetos datetime
* 🌍 **Manejar zonas horarias** trabajando con tiempo local y UTC

---

## 🔍 Visualizando el Concepto

```
📅 ESTRUCTURA DE DATETIME

    from datetime import datetime, date, time, timedelta
    
    fecha = datetime(2024, 12, 25, 14, 30, 0)
                     ↑    ↑   ↑   ↑   ↑   ↑
                   año  mes día hora min seg

🗓️ COMPONENTES PRINCIPALES:
┌─────────────────────────────────┐
│ date(año, mes, día)             │ ← Solo fecha
│ time(hora, min, seg)            │ ← Solo tiempo  
│ datetime(año,mes,día,h,m,s)     │ ← Fecha + tiempo
│ timedelta(días=X, horas=Y)      │ ← Diferencias
└─────────────────────────────────┘

⚡ OPERACIONES ÚTILES:
┌─────────────────────────────────┐
│ datetime.now()      → Ahora     │
│ datetime.today()    → Hoy       │
│ fecha.strftime()    → String    │
│ datetime.strptime() → De string │
│ fecha1 - fecha2     → Diferencia│
│ fecha + timedelta   → Nueva     │
│ fecha.year/month    → Atributos │
└─────────────────────────────────┘

🚀 CASOS DE USO COMUNES:
┌──────────────────────────────────┐
│ • Registro de eventos/logs       │
│ • Cálculo de edades              │
│ • Programación de tareas         │
│ • Análisis temporal              │
│ • Sistemas de recordatorios      │
└──────────────────────────────────┘
```

---

### o12.1 🎂 **Calculadora de Edad** 📊✨

---

#### ❓ Problema 🤔

Implementa una función `calculate_age(birth_date, current_date)` que calcule la edad exacta en años de una ratita basándose en su fecha de nacimiento. 🐭🎯

---

#### 📜 Descripción 📖

* **Función**: `calculate_age(birth_date, current_date) → int` 🛠️
* **Entradas**:
  * `birth_date`: string en formato "YYYY-MM-DD" (fecha de nacimiento) 🎯
  * `current_date`: string en formato "YYYY-MM-DD" (fecha actual) 🎯  
* **Salidas**:
  * **entero**: edad en años completos 📊
* **Casos especiales**:
  * Fecha actual antes del cumpleaños → edad se reduce en 1 ⚠️
  * Mismo día de cumpleaños → cuenta como año completo 🔍
* **Restricciones**:
  * Fechas deben estar en formato válido "YYYY-MM-DD" 🔗
  * `current_date` debe ser posterior a `birth_date` ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o12.1.1**: Cumpleaños ya pasado
   * Entrada: `("2020-03-15", "2024-08-10")`
   * Espera: `4` años ✅

2. **o12.1.2**: Cumpleaños aún no llega
   * Entrada: `("2020-11-25", "2024-08-10")`
   * Espera: `3` años ✅

3. **o12.1.3**: Exactamente en cumpleaños
   * Entrada: `("2021-12-31", "2024-12-31")`
   * Espera: `3` años ✅

4. **o12.1.4**: Verificación de tipos
   * Entrada: `("2022-01-01", "2024-01-01")`
   * Verificar: resultado es entero ✅

5. **o12.1.5**: Ratita bebé (menos de 1 año)
   * Entrada: `("2024-05-01", "2024-08-15")`
   * Espera: `0` años ✅

---

#### 💻 Código Base 🖥️

```python
from datetime import datetime

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def calculate_age(birth_date, current_date):
    """🎂 Calculate exact age in years from birth date.
    Returns age as integer."""
    # Your solution here 🛠️
    pass

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

# 🚀 Run tests
test_o12_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Usa `datetime.strptime(fecha, "%Y-%m-%d")` para convertir strings a datetime 🔍
* Calcula la diferencia básica de años: `current.year - birth.year` 📝
* Verifica si el cumpleaños ya pasó comparando mes y día ✉️
* Si no ha pasado, resta 1 año al resultado 👍

---

#### 🧠 Motivación 💭

* **Sistemas de usuarios**: calcular edades automáticamente 🔒
* **Validaciones de edad**: verificar mayoría de edad en aplicaciones 👥
* **Análisis demográfico**: estadísticas por grupos etarios ⚡

---

### o12.2 📊 **Contador de días hábiles** 🗓️🎯

---

#### ❓ Problema 🤔

Implementa una función `count_business_days(start_date, end_date)` que cuente cuántos días hábiles (lunes a viernes) hay entre dos fechas, excluyendo fines de semana. 📈🔍

---

#### 📜 Descripción 📖

* **Función**: `count_business_days(start_date, end_date) → int` 🛠️
* **Entradas**:
  * `start_date`: string en formato "YYYY-MM-DD" (fecha inicio) 🎯
  * `end_date`: string en formato "YYYY-MM-DD" (fecha fin) 🎯
* **Salidas**:
  * **entero**: número de días hábiles entre las fechas 📊
* **Casos especiales**:
  * Misma fecha → 1 día si es hábil, 0 si es fin de semana ⚠️
  * Incluye la fecha de inicio, excluye la de fin 🔍
* **Restricciones**:
  * `end_date` debe ser posterior o igual a `start_date` 🔗
  * Solo considerar lunes=0 a viernes=4 como días hábiles ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o12.2.1**: Semana completa
   * Entrada: `("2024-01-01", "2024-01-08")`  (lunes a lunes)
   * Espera: `5` días hábiles ✅

2. **o12.2.2**: Solo fin de semana
   * Entrada: `("2024-01-06", "2024-01-08")`  (sábado a lunes)
   * Espera: `0` días hábiles ✅

3. **o12.2.3**: Misma fecha hábil
   * Entrada: `("2024-01-01", "2024-01-01")`  (lunes)
   * Espera: `0` días (no se incluye el final) ✅

4. **o12.2.4**: Verificación de tipos
   * Entrada: `("2024-01-01", "2024-01-05")`
   * Verificar: resultado es entero ✅

5. **o12.2.5**: Período con fines de semana
   * Entrada: `("2024-01-01", "2024-01-15")`  (2 semanas)
   * Espera: `10` días hábiles ✅

---

#### 💻 Código Base 🖥️

```python
from datetime import datetime, timedelta

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def count_business_days(start_date, end_date):
    """📊 Count business days (Mon-Fri) between two dates.
    Returns count as integer."""
    # Your solution here 🛠️
    pass

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

# 🚀 Run tests
test_o12_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Convierte las fechas string a objetos datetime 🔍
* Usa un bucle while para iterar día por día desde start hasta end ➕
* Verifica `current_date.weekday() < 5` (lunes=0 a viernes=4) 🆕
* Incrementa contador solo para días hábiles y usa `timedelta(days=1)` 📊

---

#### 🧠 Motivación 💭

* **Planificación de proyectos**: calcular días laborales disponibles 📊
* **Sistemas de nómina**: calcular días trabajados 📝
* **Estimación de tiempos**: excluir fines de semana en cálculos 🚀

---

### o12.3 🔍 **Formateador de fechas** 🎨📋

---

#### ❓ Problema 🤔

Implementa una función `format_date_display(date_string, format_type)` que tome una fecha en formato ISO y la convierta a diferentes formatos legibles para mostrar al chanchito usuario. 🐷🎯

---

#### 📜 Descripción 📖

* **Función**: `format_date_display(date_string, format_type) → str` 🛠️
* **Entradas**:
  * `date_string`: string en formato "YYYY-MM-DD HH:MM:SS" 🎯
  * `format_type`: string con tipo de formato deseado 🔍
* **Salidas**:
  * **string**: fecha formateada según el tipo solicitado 📊
* **Casos especiales**:
  * format_type="short" → "DD/MM/YYYY" ⚠️
  * format_type="long" → "DD de Mes de YYYY" 🔍
  * format_type="time" → "HH:MM" ⚠️
* **Restricciones**:
  * Usar nombres de meses en español 🔗
  * format_type inválido → retornar string original ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o12.3.1**: Formato corto
   * Entrada: `("2024-03-15 14:30:45", "short")`
   * Espera: `"15/03/2024"` ✅

2. **o12.3.2**: Formato largo
   * Entrada: `("2024-12-25 09:15:30", "long")`
   * Espera: `"25 de diciembre de 2024"` ✅

3. **o12.3.3**: Solo tiempo
   * Entrada: `("2024-06-10 16:45:20", "time")`
   * Espera: `"16:45"` ✅

4. **o12.3.4**: Verificación de tipos
   * Entrada: `("2024-01-01 12:00:00", "short")`
   * Verificar: resultado es string ✅

5. **o12.3.5**: Formato inválido
   * Entrada: `("2024-08-20 11:30:15", "invalid")`
   * Espera: `"2024-08-20 11:30:15"` (original) ✅

---

#### 💻 Código Base 🖥️

```python
from datetime import datetime

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def format_date_display(date_string, format_type):
    """🔍 Format date string into different display formats.
    Returns formatted string."""
    # Your solution here 🛠️
    pass

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

# 🚀 Run tests
test_o12_3()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Convierte el string a datetime con `strptime(date_string, "%Y-%m-%d %H:%M:%S")` 🔍
* Crea una lista de meses: `["enero", "febrero", "marzo", ...]` 🔄
* Para formato corto usa `strftime("%d/%m/%Y")` 📊
* Para formato largo construye manualmente: `f"{día} de {mes_nombre} de {año}"` ❌

---

#### 🧠 Motivación 💭

* **Interfaces de usuario**: mostrar fechas amigables al usuario 🔍
* **Reportes y documentos**: formatear fechas para presentación 👤
* **Localización**: adaptar formatos a culturas específicas 🎯

---

### o12.4 🔄 **Calculadora de diferencias** ⏰📊

---

#### ❓ Problema 🤔

Implementa una función `calculate_time_difference(datetime1, datetime2, unit)` que calcule la diferencia entre dos fechas/horas y la retorne en la unidad especificada. 🎯📦

---

#### 📜 Descripción 📖

* **Función**: `calculate_time_difference(datetime1, datetime2, unit) → float` 🛠️
* **Entradas**:
  * `datetime1`: string "YYYY-MM-DD HH:MM:SS" (fecha inicial) 🎯
  * `datetime2`: string "YYYY-MM-DD HH:MM:SS" (fecha final) 📦
  * `unit`: string con unidad ("days", "hours", "minutes") ➕➖
* **Salidas**:
  * **float**: diferencia en la unidad especificada 📊
* **Casos especiales**:
  * datetime2 > datetime1 → resultado positivo ⚠️
  * datetime1 > datetime2 → resultado negativo 🔍
* **Restricciones**:
  * Soportar solo "days", "hours", "minutes" como unidades 🔗
  * Unidad inválida → retornar 0.0 ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o12.4.1**: Diferencia en días
   * Entrada: `("2024-01-01 00:00:00", "2024-01-05 00:00:00", "days")`
   * Espera: `4.0` días ✅

2. **o12.4.2**: Diferencia en horas
   * Entrada: `("2024-01-01 10:00:00", "2024-01-01 15:30:00", "hours")`
   * Espera: `5.5` horas ✅

3. **o12.4.3**: Diferencia en minutos
   * Entrada: `("2024-01-01 10:00:00", "2024-01-01 10:45:00", "minutes")`
   * Espera: `45.0` minutos ✅

4. **o12.4.4**: Verificación de tipos
   * Entrada: fechas válidas con unidad "days"
   * Verificar: resultado es float ✅

5. **o12.4.5**: Unidad inválida
   * Entrada: `("2024-01-01 10:00:00", "2024-01-01 11:00:00", "invalid")`
   * Espera: `0.0` ✅

---

#### 💻 Código Base 🖥️

```python
from datetime import datetime

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def calculate_time_difference(datetime1, datetime2, unit):
    """🔄 Calculate time difference between two datetimes.
    Returns difference in specified unit as float."""
    # Your solution here 🛠️
    pass

def test_o12_4():
    # o12.4.1: Diferencia en días
    result = calculate_time_difference("2024-01-01 00:00:00", "2024-01-05 00:00:00", "days")
    record_test("o12.4.1 diferencia días", result == 4.0)
    
    # o12.4.2: Diferencia en horas
    result = calculate_time_difference("2024-01-01 10:00:00", "2024-01-01 15:30:00", "hours")
    record_test("o12.4.2 diferencia horas", result == 5.5)
    
    # o12.4.3: Diferencia en minutos
    result = calculate_time_difference("2024-01-01 10:00:00", "2024-01-01 10:45:00", "minutes")
    record_test("o12.4.3 diferencia minutos", result == 45.0)
    
    # o12.4.4: Verificación de tipos
    result = calculate_time_difference("2024-01-01 10:00:00", "2024-01-01 12:00:00", "days")
    record_test("o12.4.4 retorna float", isinstance(result, float))
    
    # o12.4.5: Unidad inválida
    result = calculate_time_difference("2024-01-01 10:00:00", "2024-01-01 11:00:00", "invalid")
    record_test("o12.4.5 unidad inválida", result == 0.0)

# 🚀 Run tests
test_o12_4()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Convierte ambos strings a datetime objects 🔍
* Calcula `diff = datetime2 - datetime1` para obtener timedelta 🆕
* Para días: `diff.total_seconds() / (24 * 3600)` ➕
* Para horas: `diff.total_seconds() / 3600`, para minutos: `diff.total_seconds() / 60` 📊

---

#### 🧠 Motivación 💭

* **Medición de duración**: calcular tiempo transcurrido en eventos 📦
* **Análisis de rendimiento**: medir eficiencia temporal 🔄
* **Sistemas de facturación**: calcular horas trabajadas 📋

---

### o12.5 🤝 **Generador de cronograma** 📅✨

---

#### ❓ Problema 🤔

Implementa una función `generate_schedule(start_date, num_weeks, meeting_day)` que genere un cronograma de reuniones semanales para los chanchitos, comenzando en una fecha específica. 🎯🔗

---

#### 📜 Descripción 📖

* **Función**: `generate_schedule(start_date, num_weeks, meeting_day) → list` 🛠️
* **Entradas**:
  * `start_date`: string "YYYY-MM-DD" (fecha de inicio) 🎯
  * `num_weeks`: int (número de semanas) 🎯
  * `meeting_day`: int (día de la semana 0=lunes, 6=domingo) 🎯
* **Salidas**:
  * **lista**: fechas de reuniones en formato "YYYY-MM-DD" 📊
* **Casos especiales**:
  * Si start_date no es el día correcto → encuentra el próximo 🔍
  * num_weeks = 0 → lista vacía ⚠️
* **Restricciones**:
  * meeting_day debe estar entre 0-6 🔗
  * Generar exactamente num_weeks fechas ❌⚙️

---

#### 🧪 Tests que Pasar ✅

1. **o12.5.1**: Cronograma básico
   * Entrada: `("2024-01-01", 3, 1)`  (3 martes desde lunes)
   * Espera: `["2024-01-02", "2024-01-09", "2024-01-16"]` ✅

2. **o12.5.2**: Empezar día correcto
   * Entrada: `("2024-01-02", 2, 1)`  (2 martes desde martes)
   * Espera: `["2024-01-02", "2024-01-09"]` ✅

3. **o12.5.3**: Reuniones de viernes
   * Entrada: `("2024-01-01", 2, 4)`  (2 viernes desde lunes)
   * Espera: `["2024-01-05", "2024-01-12"]` ✅

4. **o12.5.4**: Verificación de tipos
   * Entrada: `("2024-01-01", 1, 0)`
   * Verificar: resultado es lista ✅

5. **o12.5.5**: Cero semanas
   * Entrada: `("2024-01-01", 0, 1)`
   * Espera: `[]` ✅

---

#### 💻 Código Base 🖥️

```python
from datetime import datetime, timedelta

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def generate_schedule(start_date, num_weeks, meeting_day):
    """🤝 Generate weekly meeting schedule starting from date.
    Returns list of meeting dates as strings."""
    # Your solution here 🛠️
    pass

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

# 🚀 Run tests
test_o12_5()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Si `num_weeks == 0`, retorna lista vacía inmediatamente 🔍
* Encuentra la primera fecha: si `start.weekday() == meeting_day` úsala, sino calcula días hasta el próximo 🔄
* Usa un bucle para generar `num_weeks` fechas, incrementando 7 días cada vez 📊
* Convierte cada fecha a string con `strftime("%Y-%m-%d")` 🎯

---

#### 🧠 Motivación 💭

* **Programación de eventos**: automatizar calendarios de reuniones 🔧
* **Sistemas de reservas**: generar slots regulares disponibles 🎯
* **Planificación académica**: crear cronogramas de clases automáticamente 🏗️

---

## 🎯 **¡Felicitaciones, maestro del tiempo!** ⏰🎉

Has completado exitosamente todos los retos de gestión de fechas y hora en Python. Ahora eres capaz de manipular el tiempo como un verdadero chanchito programador! 🐷✨ 

Dominas habilidades temporales esenciales como calcular edades exactas, contar días hábiles para proyectos, formatear fechas de manera elegante, calcular diferencias precisas entre momentos, y generar cronogramas automáticos. Estas son herramientas fundamentales que todo desarrollador necesita en el mundo real. 🚀📊

## 🚀 **Siguientes Pasos en tu Aventura Temporal**

Ahora que controlas el tiempo, estás listo para crear aplicaciones más sofisticadas que requieren manejo temporal preciso. En el próximo tema exploraremos **Funciones**, donde aprenderás a organizar tu código en bloques reutilizables y modulares, permitiéndote crear programas más elegantes y mantenibles.

### 🌟 **El poder temporal te llevará a:**

- **🎯 Aplicaciones web dinámicas**: Sistemas de reservas, calendarios interactivos y programadores de tareas que manejan fechas en tiempo real
- **📊 Análisis de datos temporales**: Dashboards que muestran tendencias, métricas de rendimiento por períodos y reportes automatizados con rangos de fechas
- **🔔 Sistemas de notificaciones**: Recordatorios inteligentes, alertas programadas y sistemas de seguimiento que funcionan con precisión temporal
- **🏢 Aplicaciones empresariales**: Sistemas de nómina que calculan días trabajados, planificadores de proyectos y herramientas de gestión del tiempo
- **🎮 Juegos y simulaciones**: Mecánicas basadas en tiempo real, eventos programados y sistemas de progresión temporal

Con las **Funciones** que viene a continuación, podrás encapsular toda esta lógica temporal en bloques reutilizables, crear bibliotecas de utilidades de fecha/hora personalizadas, y construir sistemas más complejos que combinen el manejo del tiempo con otras funcionalidades. ¡El futuro de la programación te espera! 💪🐍✨