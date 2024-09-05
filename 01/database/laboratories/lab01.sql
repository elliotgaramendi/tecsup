-- 1. Mostrar el nombre, salario y cod_dept con el alias "departamento", de los empleados de los departamentos 10 y 30, además ordenados por el máximo salario.
select nombre_emp,
       salario,
       cod_dept as "departamento"
  from empleados
 where cod_dept in ( 10,
                     30 )
 order by salario desc;

-- 2. Mostrar a los empleados que tienen el tercer carácter del nombre la letra “R” y terminan con “Z” o con “S”.
select nombre_emp
  from empleados
 where substr(
	  nombre_emp,
	  3,
	  1
  ) = 'R'
   and ( nombre_emp like '%Z'
    or nombre_emp like '%S' );

-- 3. Mostrar los empleados que ingresaron el año 81 u 82 en los meses de enero o diciembre. No deben ser gerentes y deben tener un salario entre 1000 y 3500.
select nombre_emp,
       puesto,
       salario,
       fecha_ing
  from empleados
 where ( extract(year from fecha_ing) = 1981
    or extract(year from fecha_ing) = 1982 )
   and ( extract(month from fecha_ing) = 1
    or extract(month from fecha_ing) = 12 )
   and puesto <> 'GERENTE'
   and salario between 1000 and 3500;

-- 4. Mostrar los empleados de los departamentos 10 y 30 que tengan derecho a comisión y que su puesto sea ANALISTA, VENDEDOR o ADMINISTRATIVO.
select nombre_emp,
       puesto,
       comision,
       cod_dept
  from empleados
 where cod_dept in ( 10,
                     30 )
   and comision is not null
   and puesto in ( 'ANALISTA',
                   'VENDEDOR',
                   'ADMINISTRATIVO' );

-- 5. Mostrar los inventos de EDISON, LAND, LOUD y PASCAL que hayan realizado en la década de los 40, 70 y 80; ordenados por año y por inventor.
select invention,
       inventor,
       year
  from invention
 where inventor in ( 'Edison',
                     'Land',
                     'Loud',
                     'Pascal' )
   and ( year between 1940 and 1949
    or year between 1970 and 1979
    or year between 1980 and 1989 )
 order by year,
          inventor;

-- 6. Mostrar el Código de nación, Nombre de nación, Capital, Área y Población (usar estos alias) de las naciones que inicien con I o G y que tengan un área mayor a 100,000.
select code as "Código de nación",
       nation as "Nombre de nación",
       capital as "Capital",
       area as "Área",
       population as "Población"
  from nation
 where ( nation like 'I%'
    or nation like 'G%' )
   and area > 100000;

-- 7. Escribir la siguiente consulta y analizar el resultado:
-- i. SELECT NOMBRE_EMP, PUESTO, SALARIO FROM EMPLEADOS
-- ii. WHERE SALARIO >= 1500
-- iii. AND PUESTO = 'GERENTE' OR PUESTO = 'VENDEDOR';

-- Análisis: La consulta selecciona el nombre, puesto y salario de los empleados que cumplen cualquiera de las siguientes condiciones:
--   Tienen un salario mayor o igual a 1500 y su puesto es 'GERENTE'.
--   Su puesto es 'VENDEDOR', sin importar el salario.
-- Esto se debe a que el operador OR tiene menor precedencia que el AND, por lo que la consulta evalúa primero la condición AND y luego la condición OR se aplica a todos los resultados.
select nombre_emp,
       puesto,
       salario
  from empleados
 where salario >= 1500
   and puesto = 'GERENTE'
    or puesto = 'VENDEDOR';

-- 8. Escribir la siguiente consulta y compararla con la anterior.
-- i. SELECT NOMBRE_EMP, PUESTO, SALARIO FROM EMPLEADOS
-- ii. WHERE SALARIO >= 1500
-- iii. AND (PUESTO = 'GERENTE' OR PUESTO = 'VENDEDOR');

-- Análisis: La consulta selecciona el nombre, puesto y salario de los empleados cuyo salario es mayor o igual a 1500 y cuyo puesto es 'GERENTE' o 'VENDEDOR'. Los paréntesis aseguran que ambos puestos se evalúen con el salario >= 1500, aplicando AND después de OR.
select nombre_emp,
       puesto,
       salario
  from empleados
 where salario >= 1500
   and ( puesto = 'GERENTE'
    or puesto = 'VENDEDOR' );

-- 9. Mostrar los nombres, puestos y salarios de aquellos empleados que laboren en el departamento 30. Ordenarlos en función al puesto que ocupen, al salario (de mayor a menor) y finalmente por nombre alfabéticamente.
select nombre_emp,
       puesto,
       salario
  from empleados
 where cod_dept = 30
 order by puesto,
          salario desc,
          nombre_emp;

-- 10. Mostrar a todos los departamentos almacenados en la tabla DEPART ordenados en forma descendente por ubicación y por código. Emplear posiciones para el ordenamiento.
select cod_dept,
       nombre_dept,
       ubicacion
  from depart
 order by 3 desc,
          1 desc;