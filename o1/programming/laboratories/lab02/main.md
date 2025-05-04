# 🔀 Estructuras de Control Condicional en PSeInt

## 1. Comprendiendo el Concepto Fundamental

En esta sección exploramos qué son las estructuras condicionales, sus elementos fundamentales y los diferentes tipos que existen. Las estructuras condicionales son puntos de decisión en los algoritmos que permiten evaluar condiciones y ejecutar diferentes bloques de código según el resultado de esa evaluación.

Para implementar estructuras condicionales efectivas, necesitamos familiarizarnos con los operadores relacionales (`>`, `<`, `>=`, `<=`, `==`, `!=`) y lógicos (`Y`, `O`, `NO`), que nos permiten construir condiciones simples y complejas.

Esta sección es principalmente teórica y sienta las bases para las implementaciones prácticas que se desarrollan a continuación.

## 2. Implementaciones Progresivas

### 2.1 Bifurcación Simple (Si-Entonces)

```
Algoritmo BifurcacionSimple
    // Declaramos una variable para almacenar el número 🔢
    Definir numero Como Entero;
    
    // Solicitamos un número al usuario 🙋‍♂️
    Escribir "Ingrese un número entero: 🔢";
    Leer numero;
    
    // Verificamos si el número es positivo usando condicional simple 🧐
    Si numero > 0 Entonces
        Escribir "El número ", numero, " es positivo 📈✅";
        Escribir "Los números positivos son mayores que cero 📊";
    FinSi
    
    Escribir "Fin del programa 🏁✨";
FinAlgoritmo
```

**Casos de prueba**: 
- Entrada: 5 → Salida: "El número 5 es positivo" + mensaje adicional
- Entrada: -3 → Salida: Solo "Fin del programa" (no muestra mensaje sobre positivo)
- Entrada: 0 → Salida: Solo "Fin del programa" (no muestra mensaje sobre positivo)

### 2.2 Bifurcación Completa (Si-Entonces-Sino)

```
Algoritmo BifurcacionCompleta
    // Declaramos una variable para almacenar el número 🔢
    Definir numero Como Entero;
    
    // Solicitamos un número al usuario 🙋‍♂️
    Escribir "Ingrese un número entero: 🔢";
    Leer numero;
    
    // Verificamos si el número es positivo o no usando condicional completa 🧐
    Si numero > 0 Entonces
        Escribir "El número ", numero, " es positivo 📈✅";
    Sino
        Escribir "El número ", numero, " es cero o negativo 📉❌";
    FinSi
    
    Escribir "Fin del programa 🏁✨";
FinAlgoritmo
```

**Casos de prueba**:
- Entrada: 8 → Salida: "El número 8 es positivo"
- Entrada: -4 → Salida: "El número -4 es cero o negativo"
- Entrada: 0 → Salida: "El número 0 es cero o negativo"

### 2.3 Bifurcación Múltiple (Si-Entonces-Sino Si-Entonces-Sino)

```
Algoritmo BifurcacionMultiple
    // Declaramos una variable para almacenar el número 🔢
    Definir numero Como Entero;
    
    // Solicitamos un número al usuario 🙋‍♂️
    Escribir "Ingrese un número entero: 🔢";
    Leer numero;
    
    // Verificamos si el número es positivo, negativo o cero usando condicional múltiple 🧐
    Si numero > 0 Entonces
        Escribir "El número ", numero, " es positivo 📈✅";
    Sino
        Si numero < 0 Entonces
            Escribir "El número ", numero, " es negativo 📉❌";
        Sino
            Escribir "El número es cero 0️⃣";
        FinSi
    FinSi
    
    Escribir "Fin del programa 🏁✨";
FinAlgoritmo
```

**Casos de prueba**:
- Entrada: 10 → Salida: "El número 10 es positivo"
- Entrada: -7 → Salida: "El número -7 es negativo"
- Entrada: 0 → Salida: "El número es cero"

### 2.4 Operador Lógico AND (Y)

```
Algoritmo OperadorAND
    // Declaramos variables 📋
    Definir edad Como Entero;
    Definir tieneCarnet Como Logico;
    
    // Solicitamos los datos 🙋‍♂️
    Escribir "Verificador de permisos de conducir 🚗";
    Escribir "Ingrese su edad: 🔢";
    Leer edad;
    Escribir "¿Tiene carnet de conducir? (Verdadero/Falso): 📜";
    Leer tieneCarnet;
    
    // Verificamos ambas condiciones con AND 🧐
    Si edad >= 18 Y tieneCarnet = Verdadero Entonces
        Escribir "¡Puede conducir! ✅🚗";
        Escribir "Recuerde respetar las normas de tránsito 🚦";
    Sino
        Escribir "No puede conducir ⛔🚫";
        Si edad < 18 Entonces
            Escribir "Debe ser mayor de edad para conducir 📏";
        FinSi
        Si tieneCarnet = Falso Entonces
            Escribir "Debe obtener un carnet de conducir 📜";
        FinSi
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Edad: 20, Tiene Carnet: Verdadero → Puede conducir
- Edad: 16, Tiene Carnet: Verdadero → No puede conducir (menor de edad)
- Edad: 25, Tiene Carnet: Falso → No puede conducir (sin carnet)
- Edad: 15, Tiene Carnet: Falso → No puede conducir (menor de edad y sin carnet)

### 2.5 Operador Lógico OR (O)

```
Algoritmo OperadorOR
    // Declaramos variables 📋
    Definir esFeriado, esDomingo Como Logico;
    
    // Solicitamos los datos 🙋‍♂️
    Escribir "Verificador de días de descanso 📅";
    Escribir "¿Es feriado? (Verdadero/Falso): 🎊";
    Leer esFeriado;
    Escribir "¿Es domingo? (Verdadero/Falso): 🗓️";
    Leer esDomingo;
    
    // Verificamos las condiciones con OR 🧐
    Si esFeriado = Verdadero O esDomingo = Verdadero Entonces
        Escribir "¡Hoy es día de descanso! 🏖️😎";
        Si esFeriado = Verdadero Y esDomingo = Verdadero Entonces
            Escribir "¡Doble celebración! Es domingo y feriado 🎉🎊";
        FinSi
    Sino
        Escribir "Hoy es día laboral 🧰💼";
        Escribir "¡A trabajar! 💪";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Es Feriado: Verdadero, Es Domingo: Falso → Día de descanso
- Es Feriado: Falso, Es Domingo: Verdadero → Día de descanso
- Es Feriado: Verdadero, Es Domingo: Verdadero → Día de descanso (muestra mensaje adicional)
- Es Feriado: Falso, Es Domingo: Falso → Día laboral

### 2.6 Operador Lógico NOT (NO)

```
Algoritmo OperadorNOT
    // Declaramos variables 📋
    Definir estaLloviendo Como Logico;
    
    // Solicitamos el dato 🙋‍♂️
    Escribir "Planificador de actividades al aire libre ☀️";
    Escribir "¿Está lloviendo? (Verdadero/Falso): 🌧️";
    Leer estaLloviendo;
    
    // Verificamos la condición invertida con NOT 🧐
    Si NO estaLloviendo Entonces
        Escribir "¡El clima es perfecto para salir al parque! 🏞️🌳";
        Escribir "No olvides llevar agua y protector solar ☀️💧";
    Sino
        Escribir "Mejor quedarse en casa hoy 🏠🛋️";
        Escribir "Es un buen día para ver películas o leer un libro 📚🎬";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Está Lloviendo: Falso → Perfecto para salir al parque
- Está Lloviendo: Verdadero → Mejor quedarse en casa

## 3. Aplicaciones Prácticas

### 3.1 Determinar si un Número es Par o Impar

```
Algoritmo ParImpar
    // Declaramos variables 📋
    Definir numero Como Entero;
    
    // Solicitamos un número 🙋‍♂️
    Escribir "VERIFICADOR DE NÚMEROS PARES E IMPARES 🔢";
    Escribir "Ingrese un número entero: 🔢";
    Leer numero;
    
    // Verificamos si es par o impar usando el operador módulo (%) 🧐
    Si numero % 2 = 0 Entonces
        Escribir "El número ", numero, " es PAR ✅";
        Escribir "Los números pares son divisibles por 2 sin dejar residuo 📏";
    Sino
        Escribir "El número ", numero, " es IMPAR ❌";
        Escribir "Los números impares dejan residuo 1 al dividirlos por 2 📏";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Entrada: 4 → Salida: "El número 4 es PAR"
- Entrada: 7 → Salida: "El número 7 es IMPAR"
- Entrada: 0 → Salida: "El número 0 es PAR"
- Entrada: -3 → Salida: "El número -3 es IMPAR"

### 3.2 Calculadora de Descuentos

```
Algoritmo CalculadoraDescuentos
    // Declaramos variables 📋
    Definir precio, descuento, precioFinal Como Real;
    Definir esMiembro Como Logico;
    
    // Solicitamos datos 🙋‍♂️
    Escribir "CALCULADORA DE DESCUENTOS 🏷️";
    Escribir "Ingrese el precio del producto: $";
    Leer precio;
    Escribir "¿El cliente es miembro del club? (Verdadero/Falso): 💳";
    Leer esMiembro;
    
    // Aplicamos descuento según condición 🧮
    Si esMiembro = Verdadero Entonces
        descuento <- precio * 0.15; // 15% de descuento para miembros 🎯
        Escribir "¡Descuento para miembros aplicado! 🌟";
    Sino
        descuento <- precio * 0.05; // 5% de descuento para no miembros 📉
        Escribir "Descuento estándar aplicado 📝";
    FinSi
    
    // Calculamos precio final 🧮
    precioFinal <- precio - descuento;
    
    // Mostramos resultados 📊
    Escribir "Resumen de la compra: 🧾";
    Escribir "Precio original: $", precio, " 💰";
    Escribir "Descuento aplicado: $", descuento, " 🏷️";
    Escribir "Precio final: $", precioFinal, " 💵";
    Si esMiembro = Verdadero Entonces
        Escribir "Gracias por ser miembro de nuestro club de fidelidad 🌟";
    Sino
        Escribir "Considere unirse a nuestro club para mayores beneficios 💡";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Precio: 100, Es Miembro: Verdadero → Precio final: 85 (15% descuento)
- Precio: 100, Es Miembro: Falso → Precio final: 95 (5% descuento)
- Precio: 50, Es Miembro: Verdadero → Precio final: 42.5 (15% descuento)
- Precio: 200, Es Miembro: Falso → Precio final: 190 (5% descuento)

### 3.3 Sistema de Calificación Escolar

```
Algoritmo SistemaCalificacion
    // Declaramos variables 📋
    Definir nota Como Real;
    Definir calificacion Como Cadena;
    
    // Solicitamos la nota 🙋‍♂️
    Escribir "SISTEMA DE CALIFICACIÓN ESCOLAR 📊";
    Escribir "Ingrese la nota del estudiante (0-20): 📝";
    Leer nota;
    
    // Validamos que la nota esté en el rango correcto 🧐
    Si nota >= 0 Y nota <= 20 Entonces
        // Asignamos calificación según nota usando condicionales anidadas 🧮
        Si nota >= 18 Entonces
            calificacion <- "A (Excelente)"; // 🌟🏆
        Sino
            Si nota >= 14 Entonces
                calificacion <- "B (Bueno)"; // ✨👍
            Sino
                Si nota >= 11 Entonces
                    calificacion <- "C (Aprobado)"; // ✅😊
                Sino
                    calificacion <- "D (Reprobado)"; // ❌😔
                FinSi
            FinSi
        FinSi
        
        // Mostramos la calificación y retroalimentación 📊
        Escribir "La calificación del estudiante es: ", calificacion;
        
        // Proporcionamos retroalimentación adicional según la calificación 💭
        Si nota >= 11 Entonces
            Escribir "¡Felicidades! El estudiante ha aprobado el curso ✅";
            Si nota >= 18 Entonces
                Escribir "¡Desempeño sobresaliente! 🌟";
            FinSi
        Sino
            Escribir "El estudiante necesita mejorar su desempeño ⚠️";
            Escribir "Se recomienda brindar apoyo adicional 📚";
        FinSi
    Sino
        Escribir "Error: Nota fuera de rango. Debe estar entre 0 y 20. ⚠️";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Nota: 19 → Calificación: "A (Excelente)" con mensajes positivos adicionales
- Nota: 16 → Calificación: "B (Bueno)" con mensaje de aprobación
- Nota: 12 → Calificación: "C (Aprobado)" con mensaje de aprobación
- Nota: 8 → Calificación: "D (Reprobado)" con mensajes de recomendación
- Nota: 25 → Mensaje de error: "Nota fuera de rango"

### 3.4 Validador de Edad para Sitios Web

```
Algoritmo ValidadorEdad
    // Declaramos variables 📋
    Definir edad Como Entero;
    Definir fechaNacimiento Como Cadena;
    
    // Solicitamos datos 🙋‍♂️
    Escribir "VERIFICADOR DE ACCESO POR EDAD 🔞";
    Escribir "Ingrese su fecha de nacimiento (DD/MM/AAAA): 📅";
    Leer fechaNacimiento;
    
    // En un caso real, calcularíamos la edad desde la fecha
    // Para simplificar este ejemplo, pedimos la edad directamente
    Escribir "Ingrese su edad: 🔢";
    Leer edad;
    
    // Verificamos acceso según edad 🧐
    Si edad >= 18 Entonces
        Escribir "✅ ACCESO PERMITIDO ✅";
        Escribir "Bienvenido/a al contenido para adultos 🔓";
        Escribir "Recuerde que este contenido es solo para mayores de edad 👨‍💼";
        
        // Verificación adicional para contenido restringido especial
        Si edad >= 21 Entonces
            Escribir "También tiene acceso a secciones especiales del sitio 🌟";
        FinSi
    Sino
        Escribir "❌ ACCESO DENEGADO ❌";
        Escribir "Lo sentimos, debe ser mayor de 18 años para acceder a este contenido 🔒";
        
        // Ofrecemos alternativas según la edad
        Si edad >= 13 Entonces
            Escribir "Te invitamos a visitar nuestro contenido para adolescentes 👦👧";
        Sino
            Escribir "Te invitamos a visitar nuestro contenido infantil 👶";
        FinSi
        
        Escribir "Redirigiendo a contenido apropiado para tu edad... 🔄";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Edad: 25 → Acceso permitido con mensaje de acceso a secciones especiales
- Edad: 19 → Acceso permitido
- Edad: 16 → Acceso denegado con redirección a contenido para adolescentes
- Edad: 10 → Acceso denegado con redirección a contenido infantil

## 4. Caso de Estudio del Mundo Real

### Sistema de Recomendación de Películas

```
Algoritmo RecomendadorPeliculas
    // Declaramos variables 📋
    Definir edad Como Entero;
    Definir generoPreferido Como Cadena;
    Definir opcion Como Entero;
    
    // Mostramos una pantalla de bienvenida atractiva 🎭
    Escribir "═════════════════════════════════";
    Escribir "   🎬 CINEMANÍA: TU RECOMENDADOR PERSONAL 🍿   ";
    Escribir "═════════════════════════════════";
    
    // Solicitamos datos al usuario 🙋‍♂️
    Escribir "¿Cuál es tu edad? 🔢";
    Leer edad;
    
    // Mostramos menú de géneros con formato mejorado 📋
    Escribir "╔═══════════════════════════╗";
    Escribir "║  SELECCIONA TU GÉNERO FAVORITO  ║";
    Escribir "╠═══════════════════════════╣";
    Escribir "║  1. Acción 💥                ║";
    Escribir "║  2. Comedia 😂               ║";
    Escribir "║  3. Drama 😢                 ║";
    Escribir "║  4. Terror 👻                ║";
    Escribir "╚═══════════════════════════╝";
    Leer opcion;
    
    // Convertimos la opción numérica a letra para facilitar el procesamiento
    Segun opcion Hacer
        1:
            generoPreferido <- "A";
        2:
            generoPreferido <- "C";
        3:
            generoPreferido <- "D";
        4:
            generoPreferido <- "T";
        De Otro Modo:
            generoPreferido <- "X"; // Género no reconocido
    FinSegun
    
    // Verificamos que el género sea válido 🧐
    Si generoPreferido = "X" Entonces
        Escribir "Lo siento, la opción seleccionada no es válida ❌";
    Sino
        Escribir "╔═══════════════════════════╗";
        Escribir "║    TU RECOMENDACIÓN PERSONAL    ║";
        Escribir "╚═══════════════════════════╝";
        
        // Recomendamos según edad y género usando condicionales anidadas 🎯
        Si edad < 13 Entonces
            // Películas para niños 👶
            Escribir "CATEGORÍA: PELÍCULAS INFANTILES 👦👧";
            
            Si generoPreferido = "A" Entonces
                Escribir "Te recomendamos: 'Kung Fu Panda 3' 🐼🥋";
                Escribir "Un panda convertido en maestro de kung fu deberá entrenar a sus compañeros para enfrentar una nueva amenaza 🌟";
            Sino
                Si generoPreferido = "C" Entonces
                    Escribir "Te recomendamos: 'Mi Villano Favorito 3' 🤪😈";
                    Escribir "Gru regresa con nuevas aventuras junto a sus minions y su hermano gemelo 🍌";
                Sino
                    Si generoPreferido = "D" Entonces
                        Escribir "Te recomendamos: 'Up: Una Aventura de Altura' 🎈🏠";
                        Escribir "Un anciano y un niño explorador viven una emocionante aventura en una casa voladora ❤️";
                    Sino
                        Escribir "Lo sentimos, no tenemos recomendaciones de terror para niños 👻❌";
                        Escribir "Te sugerimos: 'Coco' - Una emotiva historia sobre la familia y las tradiciones 💀🎸";
                    FinSi
                FinSi
            FinSi
        Sino
            Si edad < 18 Entonces
                // Películas para adolescentes 👦🎬
                Escribir "CATEGORÍA: PELÍCULAS JUVENILES 🎒🎬";
                
                Si generoPreferido = "A" Entonces
                    Escribir "Te recomendamos: 'Los Juegos del Hambre: Sinsajo' 🏹🔥";
                    Escribir "Katniss Everdeen lidera la rebelión contra el Capitolio en esta emocionante aventura distópica 🦅";
                Sino
                    Si generoPreferido = "C" Entonces
                        Escribir "Te recomendamos: 'Espía por Accidente' 🕵️😂";
                        Escribir "Un vendedor común se ve envuelto en una red de espionaje internacional con resultados hilarantes 🌍";
                    Sino
                        Si generoPreferido = "D" Entonces
                            Escribir "Te recomendamos: 'Bajo la Misma Estrella' ⭐💔";
                            Escribir "Una emotiva historia de amor entre dos adolescentes que se conocen en un grupo de apoyo para cáncer 📚";
                        Sino
                            Escribir "Te recomendamos: 'Actividad Paranormal' 👻🎥";
                            Escribir "Una pareja comienza a experimentar eventos sobrenaturales en su nueva casa 🏚️";
                        FinSi
                    FinSi
                FinSi
            Sino
                // Películas para adultos 👨🎬
                Escribir "CATEGORÍA: PELÍCULAS PARA ADULTOS 🎭🎬";
                
                Si generoPreferido = "A" Entonces
                    Escribir "Te recomendamos: 'Matrix Resurrections' 🤖💊";
                    Escribir "Neo regresa a la Matrix para enfrentar nuevas amenazas y descubrir más sobre su pasado 🕶️";
                Sino
                    Si generoPreferido = "C" Entonces
                        Escribir "Te recomendamos: 'Qué Pasó Ayer 3' 🎭🎲";
                        Escribir "El grupo de amigos vive una nueva aventura llena de situaciones cómicas e inesperadas 🌃";
                    Sino
                        Si generoPreferido = "D" Entonces
                            Escribir "Te recomendamos: 'El Padrino' 🎭🔫";
                            Escribir "La obra maestra de Francis Ford Coppola sobre la familia Corleone y su imperio criminal 🇮🇹";
                        Sino
                            Escribir "Te recomendamos: 'El Resplandor' 🪓👨";
                            Escribir "La obra maestra de Stanley Kubrick basada en la novela de Stephen King 🏨";
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Mensaje de cierre con sugerencias adicionales 🎁
        Escribir "═════════════════════════════════";
        Escribir "¡Disfruta tu película recomendada! 🍿";
        Escribir "Si necesitas más sugerencias, vuelve a consultar nuestro recomendador 🔄";
        Escribir "═════════════════════════════════";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Edad: 10, Género: Acción → Recomienda "Kung Fu Panda 3"
- Edad: 10, Género: Terror → Mensaje de no disponibilidad y sugerencia alternativa
- Edad: 16, Género: Drama → Recomienda "Bajo la Misma Estrella"
- Edad: 30, Género: Comedia → Recomienda "Qué Pasó Ayer 3"
- Opción inválida → Mensaje de error

## 5. Retos Técnicos

### 5.1 Calculadora de Año Bisiesto

```
Algoritmo AnoBisiesto
    // Declaramos variables 📋
    Definir ano Como Entero;
    Definir esBisiesto Como Logico;
    
    // Mostramos título y explicación 📚
    Escribir "╔═══════════════════════════╗";
    Escribir "║   CALCULADORA DE AÑO BISIESTO   ║";
    Escribir "╚═══════════════════════════╝";
    Escribir "Un año bisiesto tiene 366 días, con un 29 de febrero adicional 📅";
    
    // Solicitamos el año a verificar 🙋‍♂️
    Escribir "Ingrese un año (ej. 2024): 🗓️";
    Leer ano;
    
    // Aplicamos las reglas para determinar si es bisiesto 🧮
    // Regla 1: Es divisible por 4
    // Regla 2: No es divisible por 100, a menos que también sea divisible por 400
    Si ((ano % 4 = 0) Y (ano % 100 <> 0)) O (ano % 400 = 0) Entonces
        esBisiesto <- Verdadero;
    Sino
        esBisiesto <- Falso;
    FinSi
    
    // Mostramos el resultado con explicación detallada 📊
    Si esBisiesto Entonces
        Escribir "✅ El año ", ano, " ES BISIESTO ✅";
        Escribir "Tiene 366 días incluyendo el 29 de febrero 📅";
        
        // Información adicional sobre por qué es bisiesto
        Si ano % 400 = 0 Entonces
            Escribir "Es bisiesto porque es divisible por 400 🧮";
        Sino
            Escribir "Es bisiesto porque es divisible por 4 pero no por 100 🧮";
        FinSi
    Sino
        Escribir "❌ El año ", ano, " NO ES BISIESTO ❌";
        Escribir "Tiene 365 días y febrero termina el día 28 📅";
        
        // Información adicional sobre por qué no es bisiesto
        Si ano % 4 <> 0 Entonces
            Escribir "No es bisiesto porque no es divisible por 4 🧮";
        Sino
            Escribir "No es bisiesto porque es divisible por 100 pero no por 400 🧮";
        FinSi
    FinSi
    
    // Dato curioso sobre años bisiestos 💡
    Escribir "¿Sabías que? Los años bisiestos se añaden para mantener";
    Escribir "nuestro calendario sincronizado con las estaciones 🌞🍂❄️🌷";
FinAlgoritmo
```

**Casos de prueba**:
- Año: 2000 → Es bisiesto (divisible por 400)
- Año: 2020 → Es bisiesto (divisible por 4 pero no por 100)
- Año: 1900 → No es bisiesto (divisible por 100 pero no por 400)
- Año: 2023 → No es bisiesto (no es divisible por 4)
- Año: 2024 → Es bisiesto (divisible por 4 pero no por 100)

### 5.2 Calculadora de IMC con Clasificación

```
Algoritmo CalculadoraIMC
    // Declaramos variables 📋
    Definir peso, altura, imc Como Real;
    Definir categoria Como Cadena;
    
    // Mostramos título y explicación 📚
    Escribir "╔═══════════════════════════╗";
    Escribir "║   CALCULADORA DE IMC   ║";
    Escribir "╚═══════════════════════════╝";
    Escribir "El IMC es un indicador que relaciona el peso y la altura 📊";
    Escribir "Utilizado por médicos para evaluar riesgos de salud 🩺";
    
    // Solicitamos datos al usuario 🙋‍♂️
    Escribir "Ingrese su peso en kilogramos: ⚖️";
    Leer peso;
    Escribir "Ingrese su altura en metros: 📏";
    Leer altura;
    
    // Validamos datos de entrada 🧐
    Si peso <= 0 O altura <= 0 Entonces
        Escribir "Error: Los valores de peso y altura deben ser positivos ⚠️";
    Sino
        // Calculamos el IMC 🧮
        imc <- peso / (altura * altura);
        
        // Redondeamos a 2 decimales para mejor visualización
        imc <- TRUNC(imc * 100) / 100;
        
        // Determinamos la categoría según los rangos estándar 📊
        Si imc < 18.5 Entonces
            categoria <- "Bajo peso";
        Sino
            Si imc < 25 Entonces
                categoria <- "Peso normal";
            Sino
                Si imc < 30 Entonces
                    categoria <- "Sobrepeso";
                Sino
                    Si imc < 35 Entonces
                        categoria <- "Obesidad grado I";
                    Sino
                        Si imc < 40 Entonces
                            categoria <- "Obesidad grado II";
                        Sino
                            categoria <- "Obesidad grado III";
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Mostramos resultados con formato y emojis según categoría 📋
        Escribir "╔═══════════════════════════╗";
        Escribir "║      RESULTADO DEL IMC      ║";
        Escribir "╚═══════════════════════════╝";
        Escribir "Su IMC es: ", imc;
        Escribir "Categoría: ", categoria;
        
        // Añadimos recomendaciones específicas según la categoría 💡
        Escribir "Recomendación:";
        Si imc < 18.5 Entonces
            Escribir "- Considere aumentar su ingesta calórica de manera saludable 🍎";
            Escribir "- Consulte a un nutricionista para un plan personalizado 👨‍⚕️";
        Sino
            Si imc < 25 Entonces
                Escribir "- ¡Felicidades! Mantiene un peso saludable 🎉";
                Escribir "- Continúe con buenos hábitos alimenticios y ejercicio regular 🏃‍♂️";
            Sino
                Si imc < 30 Entonces
                    Escribir "- Considere incrementar su actividad física 🚶‍♀️";
                    Escribir "- Vigile su ingesta calórica y elija alimentos saludables 🥗";
                Sino
                    Escribir "- Consulte con un profesional de la salud para un plan integral 👨‍⚕️";
                    Escribir "- Es importante abordar los riesgos asociados a la obesidad ❤️";
                FinSi
            FinSi
        FinSi
        
        // Nota importante sobre el IMC 📝
        Escribir "Recuerde: El IMC es solo un indicador general y no considera";
        Escribir "otros factores como la composición corporal o condiciones médicas 🔬";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Peso: 70 kg, Altura: 1.75 m → IMC: 22.86 (Peso normal)
- Peso: 85 kg, Altura: 1.80 m → IMC: 26.23 (Sobrepeso)
- Peso: 55 kg, Altura: 1.65 m → IMC: 20.20 (Peso normal)
- Peso: 90 kg, Altura: 1.72 m → IMC: 30.42 (Obesidad grado I)
- Peso: 65 kg, Altura: 1.70 m → IMC: 22.49 (Peso normal)
- Peso: -5 kg, Altura: 1.70 m → Mensaje de error por datos inválidos

### 5.3 Conversor de Monedas

```
Algoritmo ConversorMonedas
    // Declaramos variables 📋
    Definir monto, resultado Como Real;
    Definir monedaOrigen, monedaDestino Como Entero;
    Definir nombreOrigen, nombreDestino Como Cadena;
    
    // Definimos tasas de cambio (valores de ejemplo) 💹
    Definir tasaDolarEuro, tasaDolarPeso, tasaEuroPeso Como Real;
    tasaDolarEuro <- 0.85;  // 1 USD = 0.85 EUR
    tasaDolarPeso <- 20.0;  // 1 USD = 20 MXN
    tasaEuroPeso <- 23.6;   // 1 EUR = 23.6 MXN
    
    // Mostramos título y explicación 📚
    Escribir "╔═══════════════════════════╗";
    Escribir "║   CONVERSOR DE MONEDAS INTERNACIONAL   ║";
    Escribir "╚═══════════════════════════╝";
    Escribir "Convierte entre dólares (USD), euros (EUR) y pesos mexicanos (MXN) 💵💶💴";
    
    // Solicitamos la moneda de origen 🙋‍♂️
    Escribir "Seleccione la moneda de origen:";
    Escribir "1. Dólar estadounidense (USD) 💵";
    Escribir "2. Euro (EUR) 💶";
    Escribir "3. Peso mexicano (MXN) 💴";
    Leer monedaOrigen;
    
    // Solicitamos la moneda de destino 🙋‍♂️
    Escribir "Seleccione la moneda de destino:";
    Escribir "1. Dólar estadounidense (USD) 💵";
    Escribir "2. Euro (EUR) 💶";
    Escribir "3. Peso mexicano (MXN) 💴";
    Leer monedaDestino;
    
    // Verificamos que las monedas sean válidas 🧐
    Si (monedaOrigen < 1 O monedaOrigen > 3) O (monedaDestino < 1 O monedaDestino > 3) Entonces
        Escribir "Error: Selección de moneda inválida ⚠️";
    Sino
        // Verificamos que las monedas sean diferentes
        Si monedaOrigen = monedaDestino Entonces
            Escribir "Las monedas de origen y destino son iguales. La conversión es 1:1 🔄";
        Sino
            // Solicitamos el monto a convertir 🙋‍♂️
            Escribir "Ingrese el monto a convertir:";
            Leer monto;
            
            // Validamos que el monto sea positivo
            Si monto <= 0 Entonces
                Escribir "Error: El monto debe ser un valor positivo ⚠️";
            Sino
                // Asignamos nombres a las monedas para mejor presentación
                Segun monedaOrigen Hacer
                    1: nombreOrigen <- "USD";
                    2: nombreOrigen <- "EUR";
                    3: nombreOrigen <- "MXN";
                FinSegun
                
                Segun monedaDestino Hacer
                    1: nombreDestino <- "USD";
                    2: nombreDestino <- "EUR";
                    3: nombreDestino <- "MXN";
                FinSegun
                
                // Realizamos la conversión según las monedas seleccionadas 🧮
                // De USD a otras monedas
                Si monedaOrigen = 1 Y monedaDestino = 2 Entonces
                    resultado <- monto * tasaDolarEuro;  // USD a EUR
                Sino
                    Si monedaOrigen = 1 Y monedaDestino = 3 Entonces
                        resultado <- monto * tasaDolarPeso;  // USD a MXN
                    // De EUR a otras monedas
                    Sino
                        Si monedaOrigen = 2 Y monedaDestino = 1 Entonces
                            resultado <- monto / tasaDolarEuro;  // EUR a USD
                        Sino
                            Si monedaOrigen = 2 Y monedaDestino = 3 Entonces
                                resultado <- monto * tasaEuroPeso;  // EUR a MXN
                            // De MXN a otras monedas
                            Sino
                                Si monedaOrigen = 3 Y monedaDestino = 1 Entonces
                                    resultado <- monto / tasaDolarPeso;  // MXN a USD
                                Sino
                                    resultado <- monto / tasaEuroPeso;  // MXN a EUR
                                FinSi
                            FinSi
                        FinSi
                    FinSi
                FinSi
                
                // Redondeamos a 2 decimales para formato monetario
                resultado <- TRUNC(resultado * 100) / 100;
                
                // Mostramos el resultado con formato 📊
                Escribir "╔═══════════════════════════╗";
                Escribir "║      RESULTADO DE CONVERSIÓN      ║";
                Escribir "╚═══════════════════════════╝";
                Escribir monto, " ", nombreOrigen, " = ", resultado, " ", nombreDestino;
                
                // Mostramos la tasa de cambio utilizada 📈
                Escribir "Tasa de cambio aplicada:";
                Si monedaOrigen = 1 Y monedaDestino = 2 Entonces
                    Escribir "1 USD = ", tasaDolarEuro, " EUR";
                Sino
                    Si monedaOrigen = 1 Y monedaDestino = 3 Entonces
                        Escribir "1 USD = ", tasaDolarPeso, " MXN";
                    Sino
                        Si monedaOrigen = 2 Y monedaDestino = 1 Entonces
                            Escribir "1 EUR = ", 1/tasaDolarEuro, " USD";
                        Sino
                            Si monedaOrigen = 2 Y monedaDestino = 3 Entonces
                                Escribir "1 EUR = ", tasaEuroPeso, " MXN";
                            Sino
                                Si monedaOrigen = 3 Y monedaDestino = 1 Entonces
                                    Escribir "1 MXN = ", 1/tasaDolarPeso, " USD";
                                Sino
                                    Escribir "1 MXN = ", 1/tasaEuroPeso, " EUR";
                                FinSi
                            FinSi
                        FinSi
                    FinSi
                FinSi
                
                // Nota informativa sobre tasas de cambio 💡
                Escribir "Nota: Las tasas de cambio fluctúan diariamente.";
                Escribir "Esta conversión es solo una aproximación 📊";
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- 100 USD a EUR → 85.00 EUR (tasa: 0.85)
- 100 EUR a USD → 117.65 USD (tasa: 0.85)
- 1000 MXN a USD → 50.00 USD (tasa: 20)
- 50 USD a MXN → 1000.00 MXN (tasa: 20)
- 200 EUR a MXN → 4720.00 MXN (tasa: 23.6)
- Moneda inválida → Mensaje de error
- Monedas iguales → Mensaje indicando que la conversión es 1:1
- Monto negativo → Mensaje de error

### 5.4 Validador de Triángulos

```
Algoritmo ValidadorTriangulos
    // Declaramos variables 📋
    Definir lado1, lado2, lado3 Como Real;
    Definir esTriangulo Como Logico;
    Definir tipoTriangulo Como Cadena;
    
    // Mostramos título y explicación 📚
    Escribir "╔═══════════════════════════╗";
    Escribir "║   VALIDADOR DE TRIÁNGULOS   ║";
    Escribir "╚═══════════════════════════╝";
    Escribir "Verifica si tres longitudes pueden formar un triángulo";
    Escribir "y determina su tipo (equilátero, isósceles o escaleno) 📐";
    
    // Solicitamos las longitudes de los lados 🙋‍♂️
    Escribir "Ingrese la longitud del primer lado:";
    Leer lado1;
    Escribir "Ingrese la longitud del segundo lado:";
    Leer lado2;
    Escribir "Ingrese la longitud del tercer lado:";
    Leer lado3;
    
    // Verificamos que los valores sean positivos 🧐
    Si lado1 <= 0 O lado2 <= 0 O lado3 <= 0 Entonces
        Escribir "Error: Las longitudes deben ser valores positivos ⚠️";
    Sino
        // Verificamos si pueden formar un triángulo (desigualdad triangular) 📏
        // La suma de las longitudes de dos lados debe ser mayor que la longitud del tercer lado
        Si (lado1 + lado2 > lado3) Y (lado1 + lado3 > lado2) Y (lado2 + lado3 > lado1) Entonces
            esTriangulo <- Verdadero;
            
            // Determinamos el tipo de triángulo 🧮
            Si lado1 = lado2 Y lado2 = lado3 Entonces
                tipoTriangulo <- "equilátero"; // Tres lados iguales
            Sino
                Si lado1 = lado2 O lado1 = lado3 O lado2 = lado3 Entonces
                    tipoTriangulo <- "isósceles"; // Dos lados iguales
                Sino
                    tipoTriangulo <- "escaleno"; // Todos los lados diferentes
                FinSi
            FinSi
        Sino
            esTriangulo <- Falso;
        FinSi
        
        // Mostramos los resultados con visualización mejorada 📊
        Si esTriangulo Entonces
            Escribir "✅ ¡Las longitudes SI forman un triángulo! ✅";
            
            // Visualizamos el tipo de triángulo con emojis
            Escribir "Tipo de triángulo: ", tipoTriangulo;
            
            Si tipoTriangulo = "equilátero" Entonces
                Escribir "  🟩🟩🟩  ";
                Escribir "Todos los lados son iguales y todos los ángulos miden 60° 📐";
            Sino
                Si tipoTriangulo = "isósceles" Entonces
                    Escribir "  🟦🟦🟨  ";
                    Escribir "Dos lados son iguales y dos ángulos son iguales 📐";
                Sino
                    Escribir "  🟥🟨🟩  ";
                    Escribir "Todos los lados y ángulos son diferentes 📐";
                FinSi
            FinSi
            
            // Calculamos el perímetro como dato adicional
            Escribir "Perímetro del triángulo: ", lado1 + lado2 + lado3;
        Sino
            Escribir "❌ Las longitudes NO forman un triángulo ❌";
            Escribir "Para formar un triángulo, la suma de dos lados";
            Escribir "debe ser mayor que el tercer lado 📏";
            
            // Identificamos qué condición falla
            Si lado1 + lado2 <= lado3 Entonces
                Escribir "Problema: ", lado1, " + ", lado2, " ≤ ", lado3;
            FinSi
            Si lado1 + lado3 <= lado2 Entonces
                Escribir "Problema: ", lado1, " + ", lado3, " ≤ ", lado2;
            FinSi
            Si lado2 + lado3 <= lado1 Entonces
                Escribir "Problema: ", lado2, " + ", lado3, " ≤ ", lado1;
            FinSi
        FinSi
        
        // Dato interesante sobre triángulos 💡
        Escribir "¿Sabías que? Un triángulo tiene exactamente 180° internos,";
        Escribir "sin importar sus dimensiones o su tipo 🎓";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Lados: 5, 5, 5 → Triángulo equilátero
- Lados: 5, 5, 8 → Triángulo isósceles
- Lados: 3, 4, 5 → Triángulo escaleno
- Lados: 1, 1, 10 → No forma un triángulo (viola la desigualdad triangular)
- Lados: 7, 10, 5 → Triángulo escaleno
- Lados: 0, 5, 5 → Error: longitudes deben ser positivas

### 5.5 Calculadora de Día de la Semana

```
Algoritmo DiaSemana
    // Declaramos variables 📋
    Definir numeroDia Como Entero;
    Definir nombreDia Como Cadena;
    Definir esFinDeSemana Como Logico;
    
    // Mostramos título y explicación 📚
    Escribir "╔═══════════════════════════╗";
    Escribir "║   CALCULADORA DE DÍAS DE LA SEMANA   ║";
    Escribir "╚═══════════════════════════╝";
    Escribir "Convierte un número del 1 al 7 en el día correspondiente 📆";
    Escribir "Donde 1 = Lunes, 2 = Martes, ..., 7 = Domingo";
    
    // Solicitamos el número del día 🙋‍♂️
    Escribir "Ingrese un número del 1 al 7:";
    Leer numeroDia;
    
    // Verificamos que el número esté en el rango válido 🧐
    Si numeroDia >= 1 Y numeroDia <= 7 Entonces
        // Asignamos el nombre del día y determinamos si es fin de semana
        Segun numeroDia Hacer
            1:
                nombreDia <- "Lunes";
                esFinDeSemana <- Falso;
            2:
                nombreDia <- "Martes";
                esFinDeSemana <- Falso;
            3:
                nombreDia <- "Miércoles";
                esFinDeSemana <- Falso;
            4:
                nombreDia <- "Jueves";
                esFinDeSemana <- Falso;
            5:
                nombreDia <- "Viernes";
                esFinDeSemana <- Falso;
            6:
                nombreDia <- "Sábado";
                esFinDeSemana <- Verdadero;
            7:
                nombreDia <- "Domingo";
                esFinDeSemana <- Verdadero;
        FinSegun
        
        // Mostramos el resultado con formato y emojis según el día 📊
        Escribir "╔═══════════════════════════╗";
        Escribir "║      RESULTADO      ║";
        Escribir "╚═══════════════════════════╝";
        
        // Emoji personalizado según el día
        Segun numeroDia Hacer
            1: Escribir "Día: ", nombreDia, " 🏢";  // Lunes - oficina
            2: Escribir "Día: ", nombreDia, " 📚";  // Martes - libros
            3: Escribir "Día: ", nombreDia, " 📊";  // Miércoles - gráficos
            4: Escribir "Día: ", nombreDia, " 🖥️";  // Jueves - computadora
            5: Escribir "Día: ", nombreDia, " 🎉";  // Viernes - celebración
            6: Escribir "Día: ", nombreDia, " 🎮";  // Sábado - videojuegos
            7: Escribir "Día: ", nombreDia, " 🛌";  // Domingo - descanso
        FinSegun
        
        // Indicamos si es día laborable o fin de semana
        Si esFinDeSemana Entonces
            Escribir "¡Es fin de semana! 🎉 Tiempo de descanso y diversión";
        Sino
            Escribir "Es día laborable 💼 Ánimo con tus actividades";
        FinSi
        
        // Características adicionales según el día
        Segun numeroDia Hacer
            1: Escribir "Inicio de semana. Buen momento para planificar 📝";
            2, 3, 4: Escribir "Mitad de semana. ¡Mantén el ritmo! 💪";
            5: Escribir "¡Viernes! La puerta al fin de semana 🚪";
            6: Escribir "Día perfecto para actividades recreativas 🏞️";
            7: Escribir "Último día del fin de semana. Prepárate para el lunes 🧘‍♂️";
        FinSegun
    Sino
        // Mensaje de error para número fuera de rango
        Escribir "❌ Error: El número debe estar entre 1 y 7 ❌";
        Escribir "Donde:";
        Escribir "1 = Lunes";
        Escribir "2 = Martes";
        Escribir "3 = Miércoles";
        Escribir "4 = Jueves";
        Escribir "5 = Viernes";
        Escribir "6 = Sábado";
        Escribir "7 = Domingo";
    FinSi
FinAlgoritmo
```

**Casos de prueba**:
- Entrada: 1 → Día: Lunes (Día laborable)
- Entrada: 5 → Día: Viernes (Día laborable)
- Entrada: 6 → Día: Sábado (Fin de semana)
- Entrada: 7 → Día: Domingo (Fin de semana)
- Entrada: 9 → Error: Número fuera de rango
- Entrada: 0 → Error: Número fuera de rango

## Conclusiones

Las estructuras condicionales son herramientas esenciales en programación que permiten crear algoritmos dinámicos capaces de responder a diferentes situaciones. A través de este material, hemos explorado desde los conceptos básicos hasta implementaciones complejas, demostrando su versatilidad y aplicación en problemas reales.

Aspectos clave a recordar:

1. Las estructuras condicionales (Si-Entonces, Si-Entonces-Sino, anidadas) permiten que los programas tomen decisiones basadas en condiciones específicas 🧠🔀

2. Los operadores lógicos (Y, O, NO) son fundamentales para crear condiciones más sofisticadas que combinen múltiples criterios 🧩🔄

3. Las validaciones de datos de entrada mejoran la robustez de los algoritmos, previniendo errores y comportamientos inesperados ⚠️🛡️

4. La presentación clara de resultados y retroalimentación específica mejora la experiencia del usuario 📊👍

5. Estructurar el código en secciones lógicas (entrada de datos, validación, procesamiento, salida) facilita su comprensión, mantenimiento y depuración 🏗️📝

Con los fundamentos aprendidos en estas estructuras condicionales, estamos preparados para avanzar hacia conceptos más complejos, como las estructuras repetitivas (bucles), que nos permitirán automatizar tareas repetitivas y procesar conjuntos de datos de manera eficiente.

¡Feliz programación! 🚀💻