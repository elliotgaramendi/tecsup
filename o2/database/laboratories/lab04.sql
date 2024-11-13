-- 1. ¿Las funciones de grupo incluyen los NULOS en sus cálculos?.- Respondan sí o no y la razón.
-- No, las funciones de grupo como SUM, AVG, MIN y MAX ignoran los valores NULL. 
-- Esto significa que los valores NULL no son considerados en los cálculos, lo que permite obtener resultados precisos
-- en caso de que existan campos nulos.

-- 2. Encontrar el salario más alto, el más bajo, la suma y el promedio de todos los empleados.
select max(salario) as salario_maximo,
       min(salario) as salario_minimo,
       sum(salario) as suma_salarios,
       avg(salario) as promedio_salario
  from empleados;

-- 3. Modificar la consulta anterior y mostrar los resultados por cada puesto.
select puesto,
       to_char(
          max(salario),
          'L999,999.00'
       ) as salario_maximo,
       min(salario) as salario_minimo,
       sum(salario) as suma_salarios,
       avg(salario) as promedio_salario
  from empleados
 group by puesto
 order by salario_maximo desc;

-- 4. Mostrar el número de empleados que tienen el mismo puesto.
select puesto,
       count(*) as numero_empleados
  from empleados
 group by puesto;

-- 5. Mostrar la diferencia entre el máximo salario y el mínimo salario.
select max(salario) - min(salario) as diferencia_salarios
  from empleados;

-- 6. Mostrar los puestos que tienen más de 3 empleados.
select puesto,
       count(*) as numero_empleados
  from empleados
 group by puesto
having count(*) > 3;

-- 7. Mostrar los departamentos que tengan al menos 3 empleados y que su salario sea menos de 3000.
select cod_dept,
       count(*) as numero_empleados,
       min(salario) as salario_minimo
  from empleados
 group by cod_dept
having count(*) > 3
   and min(salario) < 3000;