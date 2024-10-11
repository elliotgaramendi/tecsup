-- 1. Crear una tabla ALUMNO con la estructura especificada
-- COLUMNA  TIPO          RESTRICCION
-- idalumno Char(4)       Primary Key pk_alumno
-- paterno  (20)          Not Null nn_paterno
-- materno  (20)
-- Nombre   Varchar2(20)
-- Fec_nac  Date          default sysdate
create table alumno (
   idalumno char(4) primary key,
   paterno  varchar2(20) not null,
   materno  varchar2(20),
   nombre   varchar2(20),
   fec_nac  date default sysdate
);

-- 2. Crear una tabla CURSO2 con la estructura especificada
-- COLUMNA    TIPO DATO     RESTRICCION
-- idcurso    Char(2)       Primary Key pk_curso
-- Nombre     Varchar2(30)  Not Null nn_nom_curso
-- ciclo      Number        Check ch_ciclo
-- Ciclo únicamente podrá aceptar valores enteros comprendidos entre 1 y 6.
create table curso2 (
   idcurso char(2) primary key,
   nombre  varchar2(30) not null,
   ciclo   number check ( ciclo between 1 and 6 )
);

-- 3. Crear la tabla MATRICULA con la estructura especificada
-- COLUMNA    TIPO DATO   RESTRICCION
-- idcurso    Char(2)     Primary Key, references CURSO2(idcurso)
-- idalumno   Char(4)     Primary Key, references ALUMNO(idalumno)
-- seccion    Char        Check ch_seccion, Not Null nn_seccion
-- Sección únicamente podrá aceptar como valores A o B.
create table matricula (
   idcurso  char(2)
      references curso2 ( idcurso ),
   idalumno char(4)
      references alumno ( idalumno ),
   seccion  char check ( seccion in ( 'A',
                                     'B' ) ) not null,
   primary key ( idcurso,
                 idalumno )
);

-- 4. Mostrar los constraints de la tabla MATRICULA
select constraint_name,
       constraint_type
  from user_constraints
 where table_name = 'MATRICULA';

-- 5. Añadir la columna DNI a la tabla ALUMNO
alter table alumno add dni varchar2(8);

-- 6. Crear un constraint de tipo UNIQUE al campo DNI
alter table alumno add constraint uq_dni unique ( dni );

-- 7. Mostrar todos los constraints de la tabla ALUMNO
select constraint_name,
       constraint_type
  from user_constraints
 where table_name = 'ALUMNO';

-- 8. Crear la tabla FECHA_A a partir de la tabla EMPLEADOS, incluyendo empleados del departamento 10
create table fecha_a
   as
      select cod_emp,
             nombre_emp,
             fecha_ing
        from empleados
       where cod_dept = 10;

-- 9. Mostrar los constraints de la tabla FECHA_A
select constraint_name,
       constraint_type
  from user_constraints
 where table_name = 'FECHA_A';

-- 10. Añadir la columna Jefe a la tabla FECHA_A
-- COLUMNA  TIPO DATO   RESTRICCION
-- Jefe     Number(4)
alter table fecha_a add jefe number(4);

-- 11. Establecer una llave primaria a partir de FECHA_A.cod_emp
alter table fecha_a add constraint pk_fecha_a primary key ( cod_emp );

-- 12. Reemplazar el tipo de dato de CURSO2.nombre para que sea CHAR(25)
alter table curso2 modify
   nombre char(25);

-- 13. Eliminar la columna Jefe de la tabla FECHA_A
alter table fecha_a drop column jefe;

-- 14. Eliminar la llave primaria de la tabla FECHA_A
alter table fecha_a drop constraint pk_fecha_a;

-- 15. Eliminar la tabla FECHA_A
drop table fecha_a;