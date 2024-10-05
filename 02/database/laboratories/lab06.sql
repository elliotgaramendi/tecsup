-- 1. Mostrar todas las posibles combinaciones existentes entre nombre de empleados y ubicación de departamentos.
--    Usar sintaxis ANSI SQL.
select empleados.nombre_emp,
       depart.ubicacion
  from empleados
 cross join depart;

-- 2. Mostrar los empleados (nombres) acompañada de la ubicación del departamento para el cual laboran.
select empleados.nombre_emp,
       depart.ubicacion
  from empleados
 inner join depart
on empleados.cod_dept = depart.cod_dept;

-- 3. Repetir el ejercicio anterior mostrando adicionalmente los códigos de departamento. Usar sintaxis ANSI SQL.
select empleados.nombre_emp,
       depart.ubicacion,
       depart.cod_dept
  from empleados
 inner join depart
on empleados.cod_dept = depart.cod_dept;

-- 4. Repetir nuevamente el ejercicio anterior, pero esta vez haciendo uso de alias en tablas.
select e.nombre_emp,
       d.ubicacion,
       d.cod_dept
  from empleados e
 inner join depart d
on e.cod_dept = d.cod_dept;

-- 5. Se requiere mostrar una lista de todos los inventores acompañada de su país de origen (nombres).
select invention.inventor,
       nation.nation
  from invention
 inner join nation
on invention.nation_code = nation.code;

-- 6. Mostrar los nombres y salarios de todo empleado cuyo salario pertenezca a la categoría o grado 3.
--    Usar sintaxis ANSI SQL.
select empleados.nombre_emp,
       empleados.salario
  from empleados
 inner join salgrade
on empleados.salario between salgrade.losal and salgrade.hisal
 where salgrade.grade = 3;

-- 7. Mostrar los nombres y salarios de todo empleado cuyo salario iguale o supere el límite máximo de la categoría 4.
select empleados.nombre_emp,
       empleados.salario
  from empleados
 inner join salgrade
on empleados.salario >= salgrade.hisal
 where salgrade.grade = 4;

-- 8. Mostrar la relación de empleados (nombres) acompañada de la ubicación del departamento para el cual laboran.
--    Adicionalmente mostrar las ubicaciones del resto de departamentos.
select empleados.nombre_emp,
       depart.ubicacion
  from empleados
  left join depart
on empleados.cod_dept = depart.cod_dept;

-- 9. Mostrar la relación de empleados (nombres) acompañada de la ubicación del departamento para el cual laboran.
--    Adicionalmente mostrar los nombres de empleados que no tengan asignado algún departamento. Usar sintaxis ANSI SQL.
select empleados.nombre_emp,
       depart.ubicacion
  from empleados
  left join depart
on empleados.cod_dept = depart.cod_dept
union
select empleados.nombre_emp,
       null
  from empleados
 where empleados.cod_dept is null;

-- 10. Mostrar la relación de nombres, tanto de empleados como de sus respectivos jefes, bajo el siguiente formato:
--     EMPLEADO trabaja para JEFE.
select e.nombre_emp
       || ' trabaja para '
       || j.nombre_emp as relacion
  from empleados e
  join empleados j
on e.jefe = j.cod_emp;

-- 11. Mostrar los nombres de empleados acompañados de sus respectivos salarios, del salario de sus jefes y de la diferencia entre estos últimos.
select e.nombre_emp,
       e.salario as salario_empleado,
       j.salario as salario_jefe,
       ( j.salario - e.salario ) as diferencia_salario
  from empleados e
  join empleados j
on e.jefe = j.cod_emp;