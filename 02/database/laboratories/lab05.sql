-- 1. Mostrar los nombres y fecha_ing de todos los empleados del mismo departamento.
--    Si se ingresa el empleado 'MENDOZA', se deben mostrar todos los empleados que trabajan con 'MENDOZA'.
--    Usar un PROMPT para pedir el nombre (usar & y &&).
select nombre_emp,
       fecha_ing
  from empleados
 where cod_dept = (
   select cod_dept
     from empleados
    where nombre_emp = '&nombre'
);

-- 2. Mostrar el código de empleado, nombres y salario de todos los empleados que ganan más que el promedio de salario.
--    Mostrar los resultados en forma ascendente por salario.
select cod_emp,
       nombre_emp,
       salario
  from empleados
 where salario > (
   select avg(salario)
     from empleados
)
 order by salario asc;

-- 3. Escribir una consulta que muestre el número de empleado y nombres de todos los empleados
--    que trabajan con un empleado cuyo nombre contiene la vocal “u”.
select cod_emp,
       nombre_emp
  from empleados
 where cod_dept in (
   select cod_dept
     from empleados
    where nombre_emp like '%L%'
);

-- 4. Mostrar los nombres, cod_dept y puesto de todos los empleados cuya ubicación sea 'SAN MIGUEL'.
select nombre_emp,
       cod_dept,
       puesto
  from empleados
 where cod_dept = (
   select cod_dept
     from depart
    where ubicacion = 'SAN MIGUEL'
);

-- 5. Mostrar los nombres y salario de cada empleado que reporte a “PRESIDENTE”.
select nombre_emp,
       salario
  from empleados
 where jefe in (
   select cod_emp
     from empleados
    where puesto = 'PRESIDENTE'
);

-- 6. Mostrar el número de departamento, nombres y puesto para cada empleado que pertenezca al departamento: “VENTAS”.
select cod_dept,
       nombre_emp,
       puesto
  from empleados
 where cod_dept = (
   select cod_dept
     from depart
    where nombre_dept = 'VENTAS'
);