-- Eliminar la tabla PRODUCTO si existe
drop table producto;

-- Crear la tabla PRODUCTO con las columnas especificadas
-- -	Idproducto 	number(5) primary key
-- -	Nombre 	varchar(20)
-- -	Estado		char(1) 
-- -	Precio		number(7,2)
-- -	Categoría	char

create table producto (
   idproducto number(5) primary key,
   nombre     varchar2(20),
   estado     char(1),
   precio     number(7,2),
   categoría  char(1)
);

-- Agregar la columna Marca varchar(40) a la tabla PRODUCTO 
alter table producto add marca varchar2(40);

-- Insertar 2 productos con el estado 1 (Activo)
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( 1,
           'Laptop Dell',
           '1',
           1800.00,
           'A',
           'Dell' );
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( 2,
           'HP Monitor',
           '1',
           500.00,
           'B',
           'HP' );

-- Insertar 2 productos con el estado 0 (Inactivo)
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( 3,
           'Teclado Logitech',
           '0',
           50.00,
           'C',
           'Logitech' );
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( 4,
           'Mouse Genius',
           '0',
           30.00,
           'D',
           'Genius' );

-- Insertar 1 producto para cada categoría (A, B, C y D)
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( 5,
           'MacBook Pro',
           '1',
           2500.00,
           'A',
           'Apple' );
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( 6,
           'Samsung Monitor',
           '1',
           300.00,
           'B',
           'Samsung' );
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( 7,
           'Auriculares Sony',
           '1',
           150.00,
           'C',
           'Sony' );
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( 8,
           'Impresora Epson',
           '1',
           120.00,
           'D',
           'Epson' );

-- Insertar 2 productos usando el carácter de sustitución "&"
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( &product_id,
           '&product_name',
           '&estado',
           &precio,
           '&categoria',
           '&marca' );
insert into producto (
   idproducto,
   nombre,
   estado,
   precio,
   categoría,
   marca
) values ( &product_id,
           '&product_name',
           '&estado',
           &precio,
           '&categoria',
           '&marca' );

-- Crear la tabla MisProductos con la misma estructura de PRODUCTO, considerando aquellos con precio mayor a 1500 y estado 1
create table misproductos
   as
      select *
        from producto
       where precio > 1500
         and estado = '1';

-- Insertar en la tabla MisProductos aquellos productos que sean de la categoría A o B
insert into misproductos
   select *
     from producto
    where categoría in ( 'A',
                         'B' );

-- Confirmar todas las transacciones
commit;