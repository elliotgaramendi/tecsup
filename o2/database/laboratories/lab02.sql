-- 1. Mostrar los nombres, salarios, salarios diarios, 
--    salarios diarios redondeados (un decimal, 2 decimales) 
--    y salarios diarios truncados (un decimal, 2 decimales) de todo empleado.
select nombre_emp,
       salario,
       salario / 30 as salario_diario,
       round(
          salario / 30,
          1
       ) as salario_redondeado_1_decimal,
       round(
          salario / 30,
          2
       ) as salario_redondeado_2_decimales,
       trunc(
          salario / 30,
          1
       ) as salario_truncado_1_decimal,
       trunc(
          salario / 30,
          2
       ) as salario_truncado_2_decimales
  from empleados;

-- 2. Mostrar los nombres y las fechas de contratación de todos los empleados 
--    cuya permanencia actual en la empresa sea de entre 15000 y 16000 días.
select nombre_emp,
       fecha_ing
  from empleados
 where sysdate - fecha_ing between 15000 and 16000;

-- 3. Mostrar las ubicaciones de todos los departamentos así: Iniciales en mayúscula y en minúsculas. 
--    Además, mostrar las longitudes de las cadenas y la posición de la primera letra S de la cadena.
select ubicacion,
       initcap(ubicacion) as ubicacion_iniciales_mayuscula,
       lower(ubicacion) as ubicacion_minusculas,
       length(ubicacion) as longitud_cadena,
       instr(
          ubicacion,
          'S'
       ) as posicion_primer_s
  from depart;

-- 4. Mostrar las naciones (en mayúscula), 
--    así como las 2 primeras letras y las 2 últimas.
select upper(nation) as nacion_mayuscula,
       substr(
          nation,
          1,
          2
       ) as primeras_2_letras,
       substr(
          nation,
          -2,
          2
       ) as ultimas_2_letras
  from nation;

-- 5. Mostrar el nombre y el cod_departamento multiplicado por 100.
select nombre_emp,
       cod_dept * 100 as cod_dept_multiplicado
  from empleados;

-- 6. Mostrar los departamentos bajo el siguiente formato: 
--    COD_DEPT y sus ubicaciones, utilizando alias.
select cod_dept as "Código de Departamento",
       ubicacion as "Ubicación"
  from depart;