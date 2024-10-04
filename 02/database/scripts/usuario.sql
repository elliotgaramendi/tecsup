alter session set "_ORACLE_SCRIPT" = true;

drop user user01 cascade;

create user user01 identified by tecsup
  default tablespace users
  temporary tablespace temp;

grant
  create session
to user01;
grant connect to user01;
grant resource to user01;
grant
  unlimited tablespace
to user01;
