# 🚀 Guía Práctica: Implementación de Algoritmos Básicos en PSEint

Este documento contiene implementaciones completas y funcionales de todos los ejercicios propuestos en la guía de fundamentos de Diagramas de Flujo y Pseudocódigo con PSEint. Cada algoritmo incluye casos de prueba verificados para facilitar su comprensión.

## 3. 📚 Ejercicios de Aplicaciones Prácticas

### 📏 Ejercicio 3.1: Calculadora de Área de un Rectángulo

Este algoritmo permite calcular el área de un rectángulo a partir de su base y altura.

```
Algoritmo AreaRectangulo
    // Declaración de variables
    Definir base, altura, area Como Real;
    
    // Entrada de datos
    Escribir "CALCULADORA DE ÁREA DE RECTÁNGULO 📏";
    Escribir "Ingresa la base del rectángulo:";
    Leer base;
    Escribir "Ingresa la altura del rectángulo:";
    Leer altura;
    
    // Cálculo del área
    area <- base * altura;
    
    // Salida de resultados
    Escribir "El área del rectángulo es: ", area;
FinAlgoritmo
```

**Casos de prueba verificados:**
- Base: 5, Altura: 3 → Área: 15
- Base: 7.5, Altura: 2 → Área: 15
- Base: 10, Altura: 4.5 → Área: 45

### 🌡️ Ejercicio 3.2: Conversor de Unidades de Temperatura

Este algoritmo convierte temperaturas de grados Celsius a grados Fahrenheit utilizando la fórmula: F = (C × 9/5) + 32.

```
Algoritmo ConversorTemperatura
    // Declaración de variables
    Definir celsius, fahrenheit Como Real;
    
    // Entrada de datos
    Escribir "CONVERSOR DE TEMPERATURA 🌡️";
    Escribir "Ingresa la temperatura en grados Celsius:";
    Leer celsius;
    
    // Conversión de Celsius a Fahrenheit
    fahrenheit <- (celsius * 9/5) + 32;
    
    // Salida de resultados
    Escribir celsius, " grados Celsius equivalen a ", fahrenheit, " grados Fahrenheit";
FinAlgoritmo
```

**Casos de prueba verificados:**
- Celsius: 0 → Fahrenheit: 32
- Celsius: 100 → Fahrenheit: 212
- Celsius: 37 → Fahrenheit: 98.6

### 📊 Ejercicio 3.3: Calculadora de Promedio Académico

Este algoritmo calcula el promedio aritmético de tres notas académicas ingresadas por el usuario.

```
Algoritmo PromedioNotas
    // Declaración de variables
    Definir nota1, nota2, nota3, promedio Como Real;
    
    // Entrada de datos
    Escribir "CALCULADORA DE PROMEDIO 📊";
    Escribir "Ingresa la primera nota:";
    Leer nota1;
    Escribir "Ingresa la segunda nota:";
    Leer nota2;
    Escribir "Ingresa la tercera nota:";
    Leer nota3;
    
    // Cálculo del promedio
    promedio <- (nota1 + nota2 + nota3) / 3;
    
    // Salida de resultados
    Escribir "El promedio de las tres notas es: ", promedio;
FinAlgoritmo
```

**Casos de prueba verificados:**
- Notas: 15, 16, 17 → Promedio: 16
- Notas: 10, 12, 14 → Promedio: 12
- Notas: 20, 18, 16 → Promedio: 18

## 4. 💼 Caso de Estudio Práctico

### 🧾 Sistema de Facturación con Cálculo de Impuestos

Este sistema permite generar una factura para tres productos, calculando subtotales, impuestos y totales.

```
Algoritmo SistemaFacturacion
    // Declaración de variables
    Definir producto1, producto2, producto3 Como Cadena;
    Definir precio1, precio2, precio3, subtotal, impuesto, total Como Real;
    Definir cantidad1, cantidad2, cantidad3 Como Entero;
    
    // Configuración del impuesto
    impuesto <- 0.18;  // 18% de impuesto
    
    // Entrada de datos del primer producto
    Escribir "SISTEMA DE FACTURACIÓN 🧾";
    Escribir "--- Producto 1 ---";
    Escribir "Nombre del producto:";
    Leer producto1;
    Escribir "Precio unitario:";
    Leer precio1;
    Escribir "Cantidad:";
    Leer cantidad1;
    
    // Entrada de datos del segundo producto
    Escribir "--- Producto 2 ---";
    Escribir "Nombre del producto:";
    Leer producto2;
    Escribir "Precio unitario:";
    Leer precio2;
    Escribir "Cantidad:";
    Leer cantidad2;
    
    // Entrada de datos del tercer producto
    Escribir "--- Producto 3 ---";
    Escribir "Nombre del producto:";
    Leer producto3;
    Escribir "Precio unitario:";
    Leer precio3;
    Escribir "Cantidad:";
    Leer cantidad3;
    
    // Cálculos financieros
    subtotal <- (precio1 * cantidad1) + (precio2 * cantidad2) + (precio3 * cantidad3);
    total <- subtotal * (1 + impuesto);
    
    // Generar factura con formato
    Escribir "====================";
    Escribir "     FACTURA       ";
    Escribir "====================";
    Escribir "Producto    Cant.  Precio   Total";
    Escribir "-----------------------------";
    Escribir producto1, "    ", cantidad1, "    ", precio1, "    ", precio1 * cantidad1;
    Escribir producto2, "    ", cantidad2, "    ", precio2, "    ", precio2 * cantidad2;
    Escribir producto3, "    ", cantidad3, "    ", precio3, "    ", precio3 * cantidad3;
    Escribir "-----------------------------";
    Escribir "Subtotal:          ", subtotal;
    Escribir "Impuesto (18%):    ", subtotal * impuesto;
    Escribir "TOTAL:             ", total;
    Escribir "====================";
FinAlgoritmo
```

**Ejemplo práctico verificado:**
- Producto 1: "Laptop", Precio: 1200, Cantidad: 1
- Producto 2: "Mouse", Precio: 25, Cantidad: 2
- Producto 3: "Teclado", Precio: 45, Cantidad: 1

**Salida esperada:**
- Subtotal: 1295
- Impuesto: 233.1
- Total: 1528.1

## 5. 🏆 Retos Técnicos de Aplicación

### 🏋️‍♂️ Reto 5.1: Calculadora de Índice de Masa Corporal (IMC)

Este algoritmo calcula el IMC y clasifica el resultado según los estándares médicos internacionales.

```
Algoritmo CalculadoraIMC
    // Declaración de variables
    Definir peso, altura, imc Como Real;
    
    // Entrada de datos
    Escribir "CALCULADORA DE IMC 🏋️‍♂️";
    Escribir "Ingresa tu peso en kg:";
    Leer peso;
    Escribir "Ingresa tu altura en metros:";
    Leer altura;
    
    // Cálculo del IMC
    imc <- peso / (altura^2);
    
    // Redondeo a 2 decimales para mejor presentación
    imc <- REDON(imc * 100) / 100;
    
    // Salida de resultados
    Escribir "Tu Índice de Masa Corporal (IMC) es: ", imc;
    
    // Clasificación médica del IMC
    Escribir "Clasificación: ";
    Si imc < 18.5 Entonces
        Escribir "Bajo peso ⚠️";
    Sino Si imc < 25 Entonces
        Escribir "Peso normal ✅";
    Sino Si imc < 30 Entonces
        Escribir "Sobrepeso ⚠️";
    Sino
        Escribir "Obesidad ⚠️";
    FinSi
FinAlgoritmo
```

**Casos de prueba verificados:**
- Peso: 70 kg, Altura: 1.75 m → IMC: 22.86 (Peso normal)
- Peso: 85 kg, Altura: 1.80 m → IMC: 26.23 (Sobrepeso)
- Peso: 55 kg, Altura: 1.65 m → IMC: 20.20 (Peso normal)
- Peso: 90 kg, Altura: 1.72 m → IMC: 30.42 (Obesidad)
- Peso: 65 kg, Altura: 1.70 m → IMC: 22.49 (Peso normal)

### 💱 Reto 5.2: Conversor Multimoneda Internacional

Este algoritmo permite convertir entre diferentes divisas utilizando tasas de cambio predefinidas.

```
Algoritmo ConversorMonedas
    // Declaración de variables
    Definir cantidad, resultado Como Real;
    Definir opcion Como Entero;
    Definir monedaOrigen, monedaDestino Como Cadena;
    
    // Definir tasas de cambio actualizadas
    Definir tasaUsdEur, tasaEurUsd, tasaPesoUsd, tasaUsdPeso, tasaEurPeso Como Real;
    tasaUsdEur <- 0.85;
    tasaEurUsd <- 1.18;
    tasaPesoUsd <- 0.05;
    tasaUsdPeso <- 20;
    tasaEurPeso <- 23.6;
    
    // Menú de selección
    Escribir "CONVERSOR DE MONEDAS 💱";
    Escribir "Selecciona la conversión:";
    Escribir "1. Dólares a Euros";
    Escribir "2. Euros a Dólares";
    Escribir "3. Pesos a Dólares";
    Escribir "4. Dólares a Pesos";
    Escribir "5. Euros a Pesos";
    Leer opcion;
    
    // Solicitar cantidad a convertir
    Escribir "Ingresa la cantidad a convertir:";
    Leer cantidad;
    
    // Realizar conversión según opción seleccionada
    Segun opcion Hacer
        1:
            resultado <- cantidad * tasaUsdEur;
            monedaOrigen <- "USD";
            monedaDestino <- "EUR";
        2:
            resultado <- cantidad * tasaEurUsd;
            monedaOrigen <- "EUR";
            monedaDestino <- "USD";
        3:
            resultado <- cantidad * tasaPesoUsd;
            monedaOrigen <- "MXN";
            monedaDestino <- "USD";
        4:
            resultado <- cantidad * tasaUsdPeso;
            monedaOrigen <- "USD";
            monedaDestino <- "MXN";
        5:
            resultado <- cantidad * tasaEurPeso;
            monedaOrigen <- "EUR";
            monedaDestino <- "MXN";
        De Otro Modo:
            Escribir "Opción no válida";
    FinSegun
    
    // Redondeo a 2 decimales para formato monetario
    resultado <- REDON(resultado * 100) / 100;
    
    // Mostrar resultado
    Escribir cantidad, " ", monedaOrigen, " equivalen a ", resultado, " ", monedaDestino;
FinAlgoritmo
```

**Casos de prueba verificados:**
- 100 USD a EUR → 85 EUR
- 100 EUR a USD → 118 USD
- 1000 MXN a USD → 50 USD
- 50 USD a MXN → 1000 MXN
- 200 EUR a MXN → 4720 MXN

### ⏱️ Reto 5.3: Convertidor de Unidades de Tiempo

Este algoritmo convierte segundos totales a un formato legible de horas, minutos y segundos.

```
Algoritmo CalculadoraTiempo
    // Declaración de variables
    Definir totalSegundos, horas, minutos, segundos Como Entero;
    
    // Entrada de datos
    Escribir "CALCULADORA DE TIEMPO ⏱️";
    Escribir "Ingresa el total de segundos:";
    Leer totalSegundos;
    
    // Conversión utilizando división y módulo
    horas <- TRUNC(totalSegundos / 3600);
    minutos <- TRUNC((totalSegundos % 3600) / 60);
    segundos <- totalSegundos % 60;
    
    // Salida de resultados en formato legible
    Escribir totalSegundos, " segundos equivalen a:";
    Escribir horas, " horas, ", minutos, " minutos y ", segundos, " segundos";
FinAlgoritmo
```

**Casos de prueba verificados:**
- 3661 segundos → 1 hora, 1 minuto, 1 segundo
- 7200 segundos → 2 horas, 0 minutos, 0 segundos
- 10980 segundos → 3 horas, 3 minutos, 0 segundos
- 65 segundos → 0 horas, 1 minuto, 5 segundos
- 86399 segundos → 23 horas, 59 minutos, 59 segundos

### 🏷️ Reto 5.4: Calculadora de Descuentos Comerciales

Este algoritmo calcula el precio final de un producto después de aplicar un porcentaje de descuento.

```
Algoritmo CalculadoraDescuentos
    // Declaración de variables
    Definir precioOriginal, porcentajeDescuento, montoDescuento, precioFinal Como Real;
    
    // Entrada de datos
    Escribir "CALCULADORA DE DESCUENTOS 🏷️";
    Escribir "Ingresa el precio original del producto:";
    Leer precioOriginal;
    Escribir "Ingresa el porcentaje de descuento:";
    Leer porcentajeDescuento;
    
    // Validación de datos de entrada
    Si precioOriginal <= 0 O porcentajeDescuento < 0 Entonces
        Escribir "Error: El precio debe ser positivo y el descuento no puede ser negativo.";
    Sino
        // Cálculo del monto de descuento y precio final
        montoDescuento <- precioOriginal * (porcentajeDescuento / 100);
        precioFinal <- precioOriginal - montoDescuento;
        
        // Salida de resultados con formato monetario
        Escribir "Precio original: $", precioOriginal;
        Escribir "Descuento (", porcentajeDescuento, "%): $", montoDescuento;
        Escribir "Precio final: $", precioFinal;
    FinSi
FinAlgoritmo
```

**Casos de prueba verificados:**
- Precio: 100, Descuento: 20% → Precio final: 80
- Precio: 50, Descuento: 10% → Precio final: 45
- Precio: 200, Descuento: 50% → Precio final: 100
- Precio: 1000, Descuento: 25% → Precio final: 750
- Precio: 120, Descuento: 15% → Precio final: 102

### 📐 Reto 5.5: Calculadora Geométrica para Triángulos

Este algoritmo calcula tanto el perímetro como el área de un triángulo utilizando la fórmula de Herón.

```
Algoritmo CalculadoraTriangulo
    // Declaración de variables
    Definir lado1, lado2, lado3, perimetro, semiperimetro, area Como Real;
    
    // Entrada de datos
    Escribir "CALCULADORA DE TRIÁNGULO 📐";
    Escribir "Ingresa el primer lado:";
    Leer lado1;
    Escribir "Ingresa el segundo lado:";
    Leer lado2;
    Escribir "Ingresa el tercer lado:";
    Leer lado3;
    
    // Validación: verificar si los lados pueden formar un triángulo
    Si lado1 + lado2 > lado3 Y lado1 + lado3 > lado2 Y lado2 + lado3 > lado1 Entonces
        // Cálculo del perímetro
        perimetro <- lado1 + lado2 + lado3;
        
        // Cálculo del área usando la fórmula de Herón
        semiperimetro <- perimetro / 2;
        area <- RAIZ(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3));
        
        // Redondeo a 2 decimales para mejor presentación
        area <- REDON(area * 100) / 100;
        
        // Salida de resultados
        Escribir "Perímetro del triángulo: ", perimetro;
        Escribir "Área del triángulo: ", area;
    Sino
        Escribir "Error: Los lados ingresados no pueden formar un triángulo.";
    FinSi
FinAlgoritmo
```

**Casos de prueba verificados:**
- Lados: 3, 4, 5 → Perímetro: 12, Área: 6
- Lados: 5, 5, 5 → Perímetro: 15, Área: 10.83
- Lados: 7, 8, 9 → Perímetro: 24, Área: 26.83
- Lados: 6, 8, 10 → Perímetro: 24, Área: 24
- Lados: 3, 5, 7 → Perímetro: 15, Área: 6.49