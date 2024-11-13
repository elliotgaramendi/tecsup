-- 1. Crear la vista V_EMPLEADOS10 a partir de la tabla EMPLEADOS para que muestre los códigos, nombres, puestos y departamentos de aquellos empleados que laboren en el departamento 10.
create or replace view v_empleados10 as
   select cod_emp as codigo,
          nombre_emp as empleado,
          puesto as cargo,
          cod_dept as departamento
     from empleados
    where cod_dept = 10;

-- 2. La vista V_EMPLEADOS10 debe mostrar los encabezados: Codigo, Empleado, Cargo y Departamento, para aquellos donde el salario sea mayor a 2000.
create or replace view v_empleados10 as
   select cod_emp as codigo,
          nombre_emp as empleado,
          puesto as cargo,
          cod_dept as departamento
     from empleados
    where cod_dept = 10
      and salario > 2000;

-- 3. Crear la vista V_EMPLEADOS20 a partir de la tabla EMPLEADOS, mostrando los empleados del departamento 20. Usar WITH CHECK OPTION.
create or replace view v_empleados20 as
   select cod_emp as codigo,
          nombre_emp as empleado,
          puesto as cargo,
          cod_dept as departamento
     from empleados
    where cod_dept = 20
with check option;

-- 4. Insertar un registro en la vista V_EMPLEADOS20 con el código de departamento 20.
insert into empleados (
   cod_emp,
   nombre_emp,
   puesto,
   cod_dept,
   salario
) values ( 8001,
           'GONZALEZ',
           'ANALISTA',
           20,
           3100 );

-- 5. Crear la tabla cliente2 con los campos código, nombre, dni, y email.
create table cliente2 (
   codigo char(4) primary key,
   nombre varchar2(50) not null,
   dni    varchar2(8),
   email  varchar2(100)
);

-- 6. Agregar un índice único al campo dni en la tabla cliente2.
create unique index idx_cliente_dni on
   cliente2 (
      dni
   );

-- 7. Agregar una clave primaria a la tabla cliente2.
-- Ya se ha definido la clave primaria en el paso 5.
-- alter table cliente2 add constraint pk_cliente primary key ( codigo );

-- 8. Mostrar los índices de la tabla cliente2.
select index_name,
       column_name
  from user_ind_columns
 where table_name = 'CLIENTE2';

-- 9. Agregar un índice al campo nombre en la tabla cliente2.
create index idx_cliente_nombre on
   cliente2 (
      nombre
   );

-- 10. Eliminar el índice del campo dni en cliente2.
drop index idx_cliente_dni;

-- 11. Crear la secuencia básica S_UNO.
create sequence s_uno;

-- 12. Crear una secuencia S_DOS que muestre los números pares del 10 al 20.
create sequence s_dos start with 10 increment by 2 maxvalue 20 nocycle;


-- 13. Utilizar la secuencia S_DOS.
select s_dos.nextval
  from dual;

-- 14. Eliminar la secuencia S_DOS.
drop sequence s_dos;