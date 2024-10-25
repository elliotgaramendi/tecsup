-- 1.Crear la tabla ALUMNOS indicando un índice y llave primaria, según lo siguiente: ✅
-- ALUMNOS
-- NOMBRE       TIPO DE DATO  TAMAÑO  PRIMARY KEY  INDEX
-- CODIGO       NUMBER        6       ALU_COD_PK   ALU_COD_IDX
-- NOMBRE       VARCHAR2      20
-- APP_PATERNO  VARCHAR2      20
-- EMAIL        VARCHAR2      40
-- DNI2         VARCHAR2      8
-- EDAD         NUMBER        2

drop table alumnos;
create table alumnos (
   codigo      number(6),
   nombre      varchar2(20),
   app_paterno varchar2(20),
   email       varchar2(40),
   dni2        varchar2(8),
   edad        number(2),
   constraint alu_cod_pk primary key ( codigo )
);

DESCRIBE alumnos;

select constraint_name,
       constraint_type
  from user_constraints
 where table_name = 'ALUMNOS';

select index_name,
       column_name
  from user_ind_columns
 where table_name = 'ALUMNOS';

-- 2. Modificar el nombre del campo DNI2 a DNI
alter table alumnos rename column dni2 to dni;

-- 3. Modificar el tipo de dato del campo DNI a NUMBER(8)
alter table alumnos modify (
   dni number(8)
);

-- 4. Insertar un registro y hacer COMMIT
insert into alumnos (
   codigo,
   nombre,
   app_paterno,
   email,
   dni,
   edad
) values ( 1,
           'Alberto',
           'Gonzales',
           'agonzales@gmail.com',
           12345678,
           22 );

commit;

-- 5. Modificar el tipo de dato del campo DNI a VARCHAR2(8)
alter table alumnos modify (
   dni varchar2(8)
);

-- 6. Agregar el campo F_CREACION (date)
alter table alumnos add (
   f_creacion date
);

-- 7. Insertar un registro sin F_CREACION y hacer COMMIT
insert into alumnos (
   codigo,
   nombre,
   app_paterno,
   email,
   dni,
   edad
) values ( 2,
           'Juan',
           'Márquez',
           'jmarquez@gmail.com',
           '87654321',
           20 );

commit;

-- 8. Modificar F_CREACION para que tenga un valor por defecto
alter table alumnos modify (
   f_creacion date default sysdate
);

-- 9. Insertar un registro sin F_CREACION y hacer COMMIT
insert into alumnos (
   codigo,
   nombre,
   app_paterno,
   email,
   dni,
   edad
) values ( 3,
           'José',
           'Montero',
           'jmontero@gmail.com',
           '89898989',
           21 );

commit;

-- 10. Borrar el campo F_CREACION con el comando UNUSED
alter table alumnos set unused ( f_creacion );

-- 11. Borrar los campos UNUSED
alter table alumnos drop unused columns;

-- 12. Crear un índice para las búsquedas de nombres en mayúsculas
create index upper_alu_nom_idx on
   alumnos ( upper(nombre) );

-- 13. Usar el índice UPPER_ALU_NOM_IDX
select *
  from alumnos
 where upper(nombre) = 'ALBERTO';

-- 14. Borrar el índice UPPER_ALU_NOM_IDX
drop index upper_alu_nom_idx;

-- 15. Crear un constraint para que las edades sean mayores a 5
alter table alumnos add constraint alu_edad_ck check ( edad > 5 );

-- 16. Insertar un registro con edad menor a 5 (esto dará error debido al constraint)
insert into alumnos (
   codigo,
   nombre,
   app_paterno,
   email,
   dni,
   edad
) values ( 4,
           'Carlos',
           'Sánchez',
           'csanchez@gmail.com',
           '11223344',
           3 );

-- 17. Deshabilitar el constraint ALU_EDAD_CK
alter table alumnos disable constraint alu_edad_ck;

-- 18. Habilitar el constraint ALU_EDAD_CK
alter table alumnos enable constraint alu_edad_ck;

-- 19. Borrar el constraint ALU_EDAD_CK
alter table alumnos drop constraint alu_edad_ck;