alter session set nls_language = spanish;
alter session set nls_territory = spain;

drop table empleados;
drop table depart;
drop table salgrade;
drop table invention;
drop table nation;


--Tabla Depart
create table depart (
	cod_dept    number(2) not null
		constraint pk_dept primary key,
	nombre_dept varchar2(14),
	ubicacion   varchar2(13)
);

insert into depart values ( 10,
                            'CONTABILIDAD',
                            'COMAS' );
insert into depart values ( 20,
                            'INVESTIGACION',
                            'SAN MIGUEL' );
insert into depart values ( 30,
                            'VENTAS',
                            'MIRAFLORES' );
insert into depart values ( 40,
                            'OPERACIONES',
                            'LIMA' );

--Tabla Empleados
create table empleados (
	cod_emp    number(4) not null
		constraint pk_emp primary key,
	nombre_emp varchar2(10)
		constraint nn_nombemp not null,
	puesto     varchar2(15),
	jefe       number(4)
		constraint fk_jefe
			references empleados ( cod_emp ),
	fecha_ing  date default sysdate,
	salario    number(7,2)
		constraint ch_sal check ( salario > 500 ),
	comision   number(7,2) default null,
	cod_dept   number(2)
		constraint fk_coddept
			references depart ( cod_dept )
);

insert into empleados values ( 7839,
                               'LOPEZ',
                               'PRESIDENTE',
                               null,
                               '17-NOV-81',
                               5000,
                               null,
                               10 );
insert into empleados values ( 7698,
                               'BENAVIDES',
                               'GERENTE',
                               7839,
                               '1-MAY-81',
                               2850,
                               null,
                               30 );
insert into empleados values ( 7844,
                               'TORRES',
                               'VENDEDOR',
                               7698,
                               '8-SEP-81',
                               1500,
                               0,
                               30 );
insert into empleados values ( 7566,
                               'JARA',
                               'GERENTE',
                               7839,
                               '2-ABR-81',
                               2975,
                               null,
                               20 );
insert into empleados values ( 7654,
                               'MARTINEZ',
                               'VENDEDOR',
                               7698,
                               '28-SEP-81',
                               1250,
                               1400,
                               30 );
insert into empleados values ( 7902,
                               'FARFAN',
                               'ANALISTA',
                               7566,
                               '3-DIC-81',
                               3000,
                               null,
                               20 );
insert into empleados values ( 7499,
                               'ALVAREZ',
                               'VENDEDOR',
                               7698,
                               '20-FEB-81',
                               1600,
                               300,
                               30 );
insert into empleados values ( 7782,
                               'CASTRO',
                               'GERENTE',
                               7839,
                               '9-JUN-81',
                               2450,
                               null,
                               10 );
insert into empleados values ( 7369,
                               'PEREZ',
                               'ADMINISTRATIVO',
                               7902,
                               '17-DIC-80',
                               800,
                               null,
                               20 );
insert into empleados values ( 7788,
                               'SANCHEZ',
                               'ANALISTA',
                               7566,
                               '09-DIC-82',
                               3000,
                               null,
                               20 );
insert into empleados values ( 7934,
                               'MENDOZA',
                               'ADMINISTRATIVO',
                               7782,
                               '23-ENE-82',
                               1300,
                               null,
                               10 );
insert into empleados values ( 7521,
                               'WONG',
                               'VENDEDOR',
                               7698,
                               '22-FEB-81',
                               1250,
                               500,
                               30 );
insert into empleados values ( 7900,
                               'JIMENEZ',
                               'ADMINISTRATIVO',
                               7698,
                               '3-DIC-81',
                               950,
                               null,
                               30 );
insert into empleados values ( 7876,
                               'AMPUERO',
                               'ADMINISTRATIVO',
                               7788,
                               '12-ENE-83',
                               1100,
                               null,
                               20 );

--Tabla Salgrade
create table salgrade (
	grade number,
	losal number,
	hisal number
);

insert into salgrade values ( 1,
                              700,
                              1200 );
insert into salgrade values ( 2,
                              1201,
                              1400 );
insert into salgrade values ( 3,
                              1401,
                              2000 );
insert into salgrade values ( 4,
                              2001,
                              3000 );
insert into salgrade values ( 5,
                              3001,
                              9999 );


--Tabla Nation
create table nation (
	code       number(4)
		constraint nn_code not null
		constraint pk_code primary key,
	nation     varchar2(28)
		constraint nn_nation not null,
	capital    varchar2(20),
	area       number(22),
	population number(22)
);

insert into nation values ( 56,
                            'West Germany',
                            'Bonn',
                            96011,
                            6.1E+07 );
insert into nation values ( 57,
                            'Ghana',
                            'Accra',
                            92098,
                            1.3E+07 );
insert into nation values ( 60,
                            'Guatemala',
                            'Guatemala City',
                            42042,
                            7714000 );
insert into nation values ( 61,
                            'Guinea',
                            'Conakry',
                            94925,
                            5430000 );
insert into nation values ( 66,
                            'Hungary',
                            'Budapest',
                            35919,
                            1.1E+07 );
insert into nation values ( 68,
                            'India',
                            'New Delhi',
                            1259420,
                            7.3E+08 );
insert into nation values ( 69,
                            'Indonesia',
                            'Jakarta',
                            741101,
                            1.7E+08 );
insert into nation values ( 70,
                            'Iran',
                            'Teheran',
                            636363,
                            4.2E+07 );
insert into nation values ( 71,
                            'Iraq',
                            'Bagdad',
                            163923,
                            1.5E+07 );
insert into nation values ( 73,
                            'Israel',
                            'Jerusalen',
                            8219,
                            3958000 );
insert into nation values ( 74,
                            'Italy',
                            'Rome',
                            116303,
                            5.7E+07 );
insert into nation values ( 63,
                            'Guyana',
                            'Georgetown',
                            83000,
                            833000 );
insert into nation values ( 107,
                            'New Zealand',
                            'Wellington',
                            103833,
                            3203000 );
insert into nation values ( 28,
                            'Cape Verde',
                            'Praia',
                            1557,
                            297000 );
insert into nation values ( 11,
                            'Bahrain',
                            'Manama',
                            258,
                            393000 );
insert into nation values ( 135,
                            'Somalia',
                            'Mogadishu',
                            246300,
                            6248000 );
insert into nation values ( 141,
                            'Swaziland',
                            'Mbabane',
                            6704,
                            632000 );
insert into nation values ( 77,
                            'Japan',
                            'Tokyo',
                            147470,
                            1.2E+07 );
insert into nation values ( 157,
                            'United States of America',
                            'Washington',
                            3717813,
                            278000000 );
insert into nation values ( 156,
                            'United Kingdom',
                            'London',
                            94526,
                            59000000 );
insert into nation values ( 52,
                            'France',
                            'Paris',
                            211209,
                            61100000 );

--Tabla Invention
create table invention (
	invention   varchar2(30)
		constraint nn_inv not null
		constraint pk_inv primary key,
	inventor    varchar2(30),
	year        number(4),
	nation_code number(4)
		constraint fk_nat_code
			references nation ( code )
);

insert into invention values ( 'Record Wax.Cylinder',
                               'Edison',
                               1888,
                               157 );
insert into invention values ( 'Stock Ticker',
                               'Edison',
                               1870,
                               157 );
insert into invention values ( 'Camera Polaroid Land',
                               'Land',
                               1943,
                               157 );
insert into invention values ( 'Antiseptic Surgery',
                               'Lister',
                               1867,
                               156 );
insert into invention values ( 'Pen.Ballpoint',
                               'Loud',
                               1888,
                               157 );
insert into invention values ( 'Cotton Gin',
                               'Whitney',
                               1793,
                               157 );
insert into invention values ( 'Machine Gun',
                               'Gatting',
                               1851,
                               157 );
insert into invention values ( 'Bottle Machine',
                               'Owens',
                               1903,
                               157 );
insert into invention values ( 'Calculating Machine',
                               'Babbage',
                               1823,
                               156 );
insert into invention values ( 'Sewing Machine',
                               'Howe',
                               1846,
                               157 );
insert into invention values ( 'Ice-Making Machine',
                               'Gorrie',
                               1851,
                               157 );
insert into invention values ( 'Adding Machine',
                               'Pascal',
                               1642,
                               52 );

commit;
/