# Estructuras de Control Repetitivas en PSeInt

## 1. Comprendiendo el Concepto Fundamental

### Implementación Básica del Bucle FOR

```
Algoritmo BucleForDemostracion
    // Mostrar los números del 1 al 5 🔢
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir i; // Muestra el valor del contador i en cada iteración 🖨️
    FinPara
    
    Escribir "¡Bucle completado! 🏁";
FinAlgoritmo
```

### Visualización del Flujo de Control

```
Algoritmo VisualizacionFlujoFor
    // Mostrar el valor y la dirección del flujo 🔄
    Escribir "🔄 Iniciando bucle FOR...";
    
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir "⭐ Iteración ", i, ":";
        Escribir "   Valor actual: ", i;
        
        Si i < 5 Entonces
            Escribir "   Siguiente iteración: ", i+1;
        Sino
            Escribir "   Esta es la última iteración 🏁";
        FinSi
    FinPara
    
    Escribir "🔄 Bucle FOR finalizado";
FinAlgoritmo
```

## 2. Implementaciones Progresivas

### 2.1 Bucle FOR Básico

```
Algoritmo BucleForBasico
    // Imprimimos los números del 1 al 5 🔢
    Escribir "Números del 1 al 5:";
    
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir i; // Muestra cada número 🖨️
    FinPara
    
    Escribir "Fin del bucle 🏁";
FinAlgoritmo
```

### 2.2 Bucle FOR con Paso Diferente

```
Algoritmo BucleForPaso
    // Contar de 2 en 2 desde 0 hasta 10 🔄
    Escribir "Números pares del 0 al 10:";
    
    Para i <- 0 Hasta 10 Con Paso 2 Hacer
        Escribir i; // Muestra: 0, 2, 4, 6, 8, 10 🖨️
    FinPara
    
    // Contar de 3 en 3 desde 0 hasta 15
    Escribir "Números múltiplos de 3 del 0 al 15:";
    
    Para i <- 0 Hasta 15 Con Paso 3 Hacer
        Escribir i; // Muestra: 0, 3, 6, 9, 12, 15 🖨️
    FinPara
    
    Escribir "Fin del bucle 🏁";
FinAlgoritmo
```

### 2.3 Bucle FOR Descendente

```
Algoritmo CuentaRegresiva
    // Simulamos el lanzamiento de un cohete 🚀
    Escribir "¡Preparados para el despegue! 🔥";
    
    // Cuenta regresiva de 10 a 1
    Para i <- 10 Hasta 1 Con Paso -1 Hacer
        Escribir i, "..."; // Muestra: 10, 9, 8... ⏱️
        
        // Añadimos efectos visuales para los últimos segundos
        Si i <= 3 Entonces
            Escribir "  🔥🔥🔥";
        FinSi
    FinPara
    
    Escribir "¡DESPEGUE! 🚀";
FinAlgoritmo
```

### 2.4 Bucle FOR con Cálculos Internos

```
Algoritmo TablaMultiplicar
    // Generamos la tabla de multiplicar de un número 🧮
    Definir numero Como Entero;
    
    // Solicitamos el número al usuario
    Escribir "Ingrese un número para ver su tabla de multiplicar: 🔢";
    Leer numero;
    
    // Creamos encabezado de la tabla
    Escribir "=================================";
    Escribir " 📊 Tabla de multiplicar del ", numero, " 📊";
    Escribir "=================================";
    
    // Generamos las multiplicaciones del 1 al 10
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        Escribir " ", numero, " x ", i, " = ", (numero * i); // Multiplicación en cada iteración ✖️
    FinPara
    
    Escribir "=================================";
FinAlgoritmo
```

### 2.5 Bucle FOR con Suma Acumulativa

```
Algoritmo SumaAcumulativa
    // Sumamos los números del 1 al 100 ➕
    Definir suma Como Entero;
    suma <- 0; // Inicializamos el acumulador 🧮
    
    Para i <- 1 Hasta 100 Con Paso 1 Hacer
        suma <- suma + i; // Sumamos cada número al acumulador ➕
        
        // Mostramos actualizaciones en ciertos puntos para visualizar el progreso
        Si i % 25 = 0 Entonces
            Escribir "Sumando hasta ", i, ": ", suma;
        FinSi
    FinPara
    
    Escribir "La suma total de los números del 1 al 100 es: ", suma, " 🎯";
    Escribir "Verificación: fórmula n*(n+1)/2 = 100*101/2 = ", 100*101/2;
FinAlgoritmo
```

### 2.6 Bucle WHILE Básico

```
Algoritmo BucleWhileBasico
    // Declaramos e inicializamos una variable contador 🔢
    Definir contador Como Entero;
    contador <- 1;
    
    // Bucle que se ejecuta mientras el contador sea menor o igual a 5 🔄
    Mientras contador <= 5 Hacer
        Escribir "Contador: ", contador, " 🔄"; // Mostramos el valor actual
        contador <- contador + 1; // Incrementamos el contador ➕
    FinMientras
    
    Escribir "¡Bucle completado! 🏁";
FinAlgoritmo
```

## 3. Aplicaciones Prácticas

### 3.1 Calculadora de Factorial con FOR

```
Algoritmo CalculadoraFactorial
    // Calculamos el factorial de un número 🧮
    Definir num, factorial Como Entero;
    
    // Solicitamos el número al usuario
    Escribir "🧮 CALCULADORA DE FACTORIAL 🧮";
    Escribir "============================";
    Escribir "Ingrese un número para calcular su factorial: 🔢";
    Leer num;
    
    // Validamos que el número sea positivo
    Si num < 0 Entonces
        Escribir "⚠️ ¡Error! No se puede calcular el factorial de números negativos ❌";
    Sino
        factorial <- 1; // Inicializamos en 1 (elemento neutro de la multiplicación) 🔄
        
        // Calculamos el factorial mediante iteraciones
        Para i <- 1 Hasta num Con Paso 1 Hacer
            factorial <- factorial * i; // Multiplicación acumulativa ✖️
            Escribir "Paso ", i, ": ", factorial;
        FinPara
        
        // Mostramos el resultado final
        Escribir "El factorial de ", num, "! = ", factorial, " 🎯";
    FinSi
FinAlgoritmo
```

### 3.2 Verificador de Números Primos con FOR

```
Algoritmo VerificarPrimo
    // Verificamos si un número es primo 🔍
    Definir num Como Entero;
    Definir esPrimo Como Logico;
    Definir divisores Como Entero;
    
    // Solicitamos el número a verificar
    Escribir "🔍 VERIFICADOR DE NÚMEROS PRIMOS 🔍";
    Escribir "================================";
    Escribir "Ingrese un número para verificar si es primo: 🔢";
    Leer num;
    
    // Inicializamos variables
    esPrimo <- Verdadero;
    divisores <- 0;
    
    // Los números menores o iguales a 1 no son primos por definición
    Si num <= 1 Entonces
        esPrimo <- Falso;
    Sino
        // Buscamos divisores entre 2 y la raíz cuadrada del número (optimización)
        Para i <- 2 Hasta RC(num) Con Paso 1 Hacer
            // Si encontramos un divisor exacto
            Si num % i = 0 Entonces
                esPrimo <- Falso;
                divisores <- divisores + 1;
                Escribir "El número ", num, " es divisible por ", i, " ✂️";
            FinSi
        FinPara
    FinSi
    
    // Mostramos el resultado
    Si esPrimo Entonces
        Escribir "✅ El número ", num, " ES PRIMO 🎯";
        Escribir "Solo es divisible por 1 y por sí mismo";
    Sino
        Escribir "❌ El número ", num, " NO ES PRIMO ❌";
        
        Si num <= 1 Entonces
            Escribir "Los números menores o iguales a 1 no son considerados primos por definición";
        Sino
            Escribir "Se encontraron ", divisores, " divisores entre 2 y ", RC(num);
        FinSi
    FinSi
FinAlgoritmo
```

### 3.3 Dibujar Patrones con Asteriscos

```
Algoritmo PiramideAsteriscos
    // Dibujamos una pirámide de asteriscos 🌟
    Definir altura, espacios, asteriscos Como Entero;
    
    // Pedimos la altura de la pirámide
    Escribir "🏗️ GENERADOR DE PIRÁMIDES 🏗️";
    Escribir "Ingrese la altura de la pirámide: 📏";
    Leer altura;
    
    // Construimos la pirámide fila por fila
    Para fila <- 1 Hasta altura Con Paso 1 Hacer
        // Primero los espacios (disminuyen con cada fila)
        Para espacios <- 1 Hasta altura-fila Con Paso 1 Hacer
            Escribir Sin Saltar " ";
        FinPara
        
        // Luego los asteriscos (aumentan en 2 con cada fila)
        Para asteriscos <- 1 Hasta 2*fila-1 Con Paso 1 Hacer
            Escribir Sin Saltar "*";
        FinPara
        
        Escribir ""; // Salto de línea al final de cada fila
    FinPara
    
    Escribir "¡Pirámide completada! 🏁";
FinAlgoritmo
```

### 3.4 Cálculo de Promedio de Notas

```
Algoritmo CalcularPromedio
    // Calculamos el promedio de un conjunto de notas 📊
    Definir n, i Como Entero;
    Definir nota, suma, promedio, notaMaxima, notaMinima Como Real;
    
    // Solicitamos la cantidad de notas
    Escribir "📊 CALCULADORA DE PROMEDIO 📊";
    Escribir "Ingrese la cantidad de notas a promediar: 🔢";
    Leer n;
    
    // Validamos que la cantidad sea positiva
    Si n <= 0 Entonces
        Escribir "⚠️ Debe ingresar al menos una nota ❌";
    Sino
        // Inicializamos las variables
        suma <- 0;
        notaMaxima <- 0;
        notaMinima <- 20; // Asumiendo escala de 0 a 20
        
        // Procesamos cada nota
        Para i <- 1 Hasta n Con Paso 1 Hacer
            Escribir "Ingrese la nota ", i, " (0-20): 📝";
            Leer nota;
            
            // Validamos que la nota esté en el rango correcto
            Mientras nota < 0 O nota > 20 Hacer
                Escribir "⚠️ Nota fuera de rango. Ingrese un valor entre 0 y 20: ⚠️";
                Leer nota;
            FinMientras
            
            // Actualizamos suma y valores extremos
            suma <- suma + nota;
            
            Si nota > notaMaxima Entonces
                notaMaxima <- nota;
            FinSi
            
            Si nota < notaMinima Entonces
                notaMinima <- nota;
            FinSi
        FinPara
        
        // Calculamos y mostramos el promedio
        promedio <- suma / n;
        
        Escribir "Resultados del análisis: 📊";
        Escribir "========================";
        Escribir "Cantidad de notas: ", n;
        Escribir "Nota promedio: ", promedio;
        Escribir "Nota más alta: ", notaMaxima, " 🏆";
        Escribir "Nota más baja: ", notaMinima, " 📉";
        
        // Evaluación del promedio
        Si promedio >= 14 Entonces
            Escribir "¡Excelente rendimiento! 🌟";
        Sino
            Si promedio >= 11 Entonces
                Escribir "Rendimiento satisfactorio ✅";
            Sino
                Escribir "Necesita mejorar ⚠️";
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

## 4. Caso de Estudio del Mundo Real

### Sistema de Análisis de Calificaciones Escolares

```
Algoritmo SistemaCalificacionesEscolares
    // Sistema completo para análisis de calificaciones escolares 🏫
    Definir numEstudiantes, i, aprobados, reprobados Como Entero;
    Definir calificacion, sumaTotal, promedio, calificacionMaxima, calificacionMinima Como Real;
    Definir nombreEstudiante Como Cadena;
    
    // Encabezado del sistema
    Escribir "🏫 SISTEMA DE ANÁLISIS DE CALIFICACIONES 🏫";
    Escribir "=========================================";
    
    // Solicitamos la cantidad de estudiantes
    Escribir "Ingrese la cantidad de estudiantes: 👨‍🎓";
    Leer numEstudiantes;
    
    // Validamos la entrada
    Si numEstudiantes <= 0 Entonces
        Escribir "⚠️ La cantidad debe ser un número positivo ❌";
    Sino
        // Inicializamos variables
        sumaTotal <- 0;
        aprobados <- 0;
        reprobados <- 0;
        calificacionMaxima <- 0;
        calificacionMinima <- 20; // Asumimos escala de 0 a 20
        
        // Procesamos los datos de cada estudiante
        Para i <- 1 Hasta numEstudiantes Con Paso 1 Hacer
            Escribir "📝 ESTUDIANTE ", i, " DE ", numEstudiantes, " 📝";
            
            // Solicitamos nombre del estudiante
            Escribir "Nombre del estudiante:";
            Leer nombreEstudiante;
            
            // Solicitamos la calificación
            Escribir "Calificación de ", nombreEstudiante, " (0-20): 🔢";
            Leer calificacion;
            
            // Validamos que la calificación esté en rango
            Mientras calificacion < 0 O calificacion > 20 Hacer
                Escribir "⚠️ Calificación fuera de rango. Ingrese un valor entre 0 y 20: ⚠️";
                Leer calificacion;
            FinMientras
            
            // Actualizamos estadísticas generales
            sumaTotal <- sumaTotal + calificacion;
            
            // Actualizamos máximo y mínimo
            Si calificacion > calificacionMaxima Entonces
                calificacionMaxima <- calificacion;
            FinSi
            
            Si calificacion < calificacionMinima Entonces
                calificacionMinima <- calificacion;
            FinSi
            
            // Verificamos si el estudiante aprobó (11 o más)
            Si calificacion >= 11 Entonces
                aprobados <- aprobados + 1;
                Escribir nombreEstudiante, " ha APROBADO con ", calificacion, " ✅";
            Sino
                reprobados <- reprobados + 1;
                Escribir nombreEstudiante, " ha REPROBADO con ", calificacion, " ❌";
            FinSi
        FinPara
        
        // Calculamos estadísticas finales
        promedio <- sumaTotal / numEstudiantes;
        
        // Mostramos el informe final
        Escribir "";
        Escribir "📊 INFORME FINAL DE CALIFICACIONES 📊";
        Escribir "===================================";
        Escribir "Total de estudiantes: ", numEstudiantes, " 👨‍🎓";
        Escribir "Calificación promedio: ", promedio, " 📈";
        Escribir "Calificación más alta: ", calificacionMaxima, " 🏆";
        Escribir "Calificación más baja: ", calificacionMinima, " 📉";
        Escribir "Estudiantes aprobados: ", aprobados, " (", (aprobados*100)/numEstudiantes, "%) ✅";
        Escribir "Estudiantes reprobados: ", reprobados, " (", (reprobados*100)/numEstudiantes, "%) ❌";
        
        // Representación visual de aprobados vs reprobados
        Escribir "";
        Escribir "Aprobados: [", Sin Saltar;
        Para i <- 1 Hasta 20 Hacer
            Si i <= (aprobados*20)/numEstudiantes Entonces
                Escribir "█", Sin Saltar;
            Sino
                Escribir " ", Sin Saltar;
            FinSi
        FinPara
        Escribir "] ", (aprobados*100)/numEstudiantes, "% ✅";
        
        Escribir "Reprobados: [", Sin Saltar;
        Para i <- 1 Hasta 20 Hacer
            Si i <= (reprobados*20)/numEstudiantes Entonces
                Escribir "█", Sin Saltar;
            Sino
                Escribir " ", Sin Saltar;
            FinSi
        FinPara
        Escribir "] ", (reprobados*100)/numEstudiantes, "% ❌";
    FinSi
FinAlgoritmo
```

## 5. Retos Técnicos

### 5.1 Generador de Secuencia Fibonacci

```
Algoritmo SerieFibonacci
    // Generamos los primeros N términos de la serie Fibonacci 🌀
    Definir n, a, b, c, i Como Entero;
    
    // Solicitamos la cantidad de términos
    Escribir "🌀 GENERADOR DE SERIE FIBONACCI 🌀";
    Escribir "=================================";
    Escribir "¿Cuántos términos de la serie Fibonacci desea generar? 🔢";
    Leer n;
    
    // Validamos la entrada
    Si n <= 0 Entonces
        Escribir "⚠️ El número de términos debe ser positivo ❌";
    Sino
        // Inicializamos los primeros dos términos
        a <- 0;
        b <- 1;
        
        Escribir "Serie Fibonacci de ", n, " términos:";
        
        // Generamos y mostramos los términos según el caso
        Si n >= 1 Entonces
            Escribir "Término 1: ", a; // Primer término (0)
        FinSi
        
        Si n >= 2 Entonces
            Escribir "Término 2: ", b; // Segundo término (1)
        FinSi
        
        // Generamos el resto de términos
        Para i <- 3 Hasta n Con Paso 1 Hacer
            c <- a + b; // El siguiente término es la suma de los dos anteriores
            Escribir "Término ", i, ": ", c;
            
            // Actualizamos para la próxima iteración
            a <- b;
            b <- c;
        FinPara
        
        Escribir "¡Serie Fibonacci generada con éxito! 🏁";
    FinSi
FinAlgoritmo
```

### 5.2 Detector de Números Perfectos

```
Algoritmo VerificarNumeroPerfecto
    // Verificamos si un número es perfecto (igual a la suma de sus divisores propios) 💯
    Definir num, sumaDivisores, i Como Entero;
    
    // Solicitamos el número a verificar
    Escribir "💯 DETECTOR DE NÚMEROS PERFECTOS 💯";
    Escribir "=================================";
    Escribir "Ingrese un número para verificar si es perfecto: 🔢";
    Leer num;
    
    // Validamos que el número sea positivo
    Si num <= 0 Entonces
        Escribir "⚠️ Solo se pueden verificar números positivos ❌";
    Sino
        sumaDivisores <- 0; // Inicializamos la suma
        
        Escribir "Divisores propios de ", num, ":";
        
        // Buscamos los divisores propios y los sumamos
        Para i <- 1 Hasta num-1 Con Paso 1 Hacer
            Si num % i = 0 Entonces // Si i es divisor de num
                sumaDivisores <- sumaDivisores + i; // Lo sumamos
                Escribir "- ", i;
            FinSi
        FinPara
        
        Escribir "Suma de divisores propios: ", sumaDivisores;
        
        // Verificamos si es perfecto (igual a sus divisores propios)
        Si sumaDivisores = num Entonces
            Escribir "✅ El número ", num, " ES PERFECTO ✅";
            Escribir "La suma de sus divisores propios es igual al número.";
        Sino
            Escribir "❌ El número ", num, " NO ES PERFECTO ❌";
            Si sumaDivisores < num Entonces
                Escribir "Es un número deficiente (la suma de sus divisores es menor).";
            Sino
                Escribir "Es un número abundante (la suma de sus divisores es mayor).";
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

### 5.3 Simulador de Interés Compuesto

```
Algoritmo InteresCompuesto
    // Simulamos el crecimiento de una inversión con interés compuesto 💰
    Definir capital, tasa, capitalFinal Como Real;
    Definir anos, i Como Entero;
    
    // Solicitamos los datos de la inversión
    Escribir "💰 SIMULADOR DE INTERÉS COMPUESTO 💰";
    Escribir "==================================";
    Escribir "Ingrese el capital inicial ($): 💵";
    Leer capital;
    Escribir "Ingrese la tasa de interés anual (%): 📈";
    Leer tasa;
    Escribir "Ingrese el número de años: ⏱️";
    Leer anos;
    
    // Validamos los datos
    Si capital <= 0 O tasa <= 0 O anos <= 0 Entonces
        Escribir "⚠️ Todos los valores deben ser positivos ❌";
    Sino
        // Convertimos la tasa a decimal
        tasa <- tasa / 100;
        
        // Mostramos encabezado de la tabla
        Escribir "=================================================";
        Escribir " Año |   Capital   | Intereses |  Capital Final  ";
        Escribir "=================================================";
        
        // Simulamos año por año
        capitalFinal <- capital;
        
        Para i <- 1 Hasta anos Con Paso 1 Hacer
            // Calculamos el interés del año actual
            capitalFinal <- capital * (1 + tasa) ^ i;
            
            // Mostramos los resultados de este año
            Escribir "  ", i, "  | $", capital, " | $", capitalFinal - capital, " | $", capitalFinal;
            
            // Si no es el último año, añadimos separador
            Si i < anos Entonces
                Escribir "-------------------------------------------------";
            FinSi
        FinPara
        
        Escribir "=================================================";
        Escribir "Capital inicial: $", capital;
        Escribir "Capital final después de ", anos, " años: $", capitalFinal, " 💰";
        Escribir "Ganancia total: $", capitalFinal - capital, " 📈";
    FinSi
FinAlgoritmo
```

### 5.4 Conversor de Números Decimales a Binarios

```
Algoritmo DecimalABinario
    // Convertimos un número decimal a su representación binaria 🔢
    Definir numDecimal, i, potencia Como Entero;
    Definir binario Como Cadena;
    Definir residuos Como Entero;
    Dimension residuos[50]; // Arreglo para almacenar los restos
    
    // Solicitamos el número decimal
    Escribir "🔢 CONVERSOR DECIMAL A BINARIO 🔢";
    Escribir "==============================";
    Escribir "Ingrese un número decimal positivo: 🔢";
    Leer numDecimal;
    
    // Validamos que sea positivo
    Si numDecimal < 0 Entonces
        Escribir "⚠️ Solo se pueden convertir números positivos ❌";
    Sino
        // Caso especial: si el número es 0
        Si numDecimal = 0 Entonces
            Escribir "El número 0 en binario es: 0";
        Sino
            // Inicializaciones
            binario <- "";
            i <- 0;
            
            // Proceso de conversión mediante divisiones sucesivas
            Mientras numDecimal > 0 Hacer
                residuos[i] <- numDecimal % 2; // Guardamos el resto
                numDecimal <- trunc(numDecimal / 2); // División entera
                i <- i + 1;
            FinMientras
            
            // Construimos el número binario (de atrás hacia adelante)
            Escribir "El número en binario es: ", Sin Saltar;
            
            Para j <- i-1 Hasta 0 Con Paso -1 Hacer
                Escribir residuos[j], Sin Saltar;
                binario <- binario + ConvertirATexto(residuos[j]);
            FinPara
            
            Escribir "";
            Escribir "Representación binaria: ", binario;
            
            // Verificamos la conversión mostrando potencias de 2
            Escribir "Verificación por potencias de 2:";
            
            Para j <- 0 Hasta i-1 Con Paso 1 Hacer
                potencia <- 2 ^ (i-1-j);
                Si residuos[j] = 1 Entonces
                    Escribir "2^", (i-1-j), " = ", potencia;
                FinSi
            FinPara
        FinSi
    FinSi
FinAlgoritmo
```

### 5.5 Verificador de Palíndromos Numéricos

```
Algoritmo VerificarPalindromoNumerico
    // Verificamos si un número es palíndromo (se lee igual al derecho y al revés) 🔄
    Definir num, numOriginal, numInvertido, resto Como Entero;
    
    // Solicitamos el número a verificar
    Escribir "🔄 VERIFICADOR DE PALÍNDROMOS NUMÉRICOS 🔄";
    Escribir "=======================================";
    Escribir "Ingrese un número para verificar si es palíndromo: 🔢";
    Leer num;
    
    // Validamos que sea positivo
    Si num < 0 Entonces
        Escribir "⚠️ Solo se pueden verificar números positivos ❌";
    Sino
        // Guardamos el número original para comparar después
        numOriginal <- num;
        numInvertido <- 0;
        
        // Proceso para invertir el número usando operaciones matemáticas
        Escribir "Proceso de inversión del número:";
        Escribir "Número original: ", num;
        
        Mientras num > 0 Hacer
            resto <- num % 10; // Obtenemos el último dígito
            numInvertido <- numInvertido * 10 + resto; // Construimos el número invertido
            num <- trunc(num / 10); // Eliminamos el último dígito
            
            Escribir "Último dígito: ", resto, " → Número invertido parcial: ", numInvertido;
        FinMientras
        
        // Verificamos si es palíndromo comparando original e invertido
        Si numOriginal = numInvertido Entonces
            Escribir "✅ El número ", numOriginal, " ES PALÍNDROMO ✅";
            Escribir "Se lee igual de izquierda a derecha y de derecha a izquierda.";
        Sino
            Escribir "❌ El número ", numOriginal, " NO ES PALÍNDROMO ❌";
```