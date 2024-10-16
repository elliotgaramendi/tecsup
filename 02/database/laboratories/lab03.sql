-- 1. Mostrar los nombres, salarios, comisiones y sueldos (salario + comisión) de todo empleado.
-- Ordenar el resultado del menor al mayor salario. No usar función NVL.
select nombre_emp,
       salario,
       comision,
       ( salario + comision ) as sueldo_total
  from empleados
 order by salario;

-- 2. Repetir la consulta anterior mostrando los sueldos como números reales, que recibiría cada empleado.
select nombre_emp,
       salario,
       comision,
       ( salario + nvl(
          comision,
          0
       ) ) as sueldo_real
  from empleados
 order by sueldo_real;

-- 3. Mostrar los salarios en formato monetario para todos los empleados.
select nombre_emp,
       to_char(
          salario,
          'L999G999D99'
       ) as salario_formateado
  from empleados;

-- 4. Mostrar la fecha actual bajo el siguiente formato:
-- Martes, 10 de MAYO del 2013 - 10:10:00
select to_char(
   sysdate,
   'Day, DD "de" MONTH "del" YYYY - HH24:MI:SS'
) as fecha_actual
  from dual;

-- 5. Crear un reporte que muestre:
-- [Empleado] gana [SALARIO], pero su salario anual es [SALARIO_ANUAL]
select nombre_emp
       || ' gana '
       || salario
       || ', pero su salario anual es '
       || ( salario * 12 ) as reporte_salario
  from empleados;

-- 6. Mostrar un reporte con los siguientes campos:
-- [NOMBRE EMPLEADO] [HIRE_DATE] [DIA] [MES] [AÑO]
select nombre_emp,
       to_char(
          fecha_ing,
          'DD'
       ) as dia,
       to_char(
          fecha_ing,
          'MM'
       ) as mes,
       to_char(
          fecha_ing,
          'YYYY'
       ) as año
  from empleados;

-- 7. Crear un reporte que muestre:
-- [NOMBRE EMPLEADO] [COMISION]
-- Si tiene comisión debe mostrarla, en caso de que no tenga comisión mostrar el mensaje “SIN COMISION”.
select nombre_emp,
       nvl(
          to_char(comision),
          'SIN COMISION'
       ) as comision
  from empleados;

-- 8. Crear un reporte que muestre:
-- [NOMBRE EMPLEADO] [SALARIO]  [RANGO DE SALARIO]
-- El rango se calcula de la siguiente manera:
-- Mayor a 4000 nivel 1
-- [3000-4000] nivel 2
-- [2000-3000] nivel 3
-- Menor a 2000 nivel 4
select nombre_emp,
       salario,
       case
          when salario > 4000                then
             'Nivel 1'
          when salario between 3000 and 4000 then
             'Nivel 2'
          when salario between 2000 and 3000 then
             'Nivel 3'
          else
             'Nivel 4'
       end as rango_salario
  from empleados;