use [Auto Parking Management];

--Create table for version

create table DB_version
(
	version_id int identity(1,1) not null,
	currentVersion int,
	constraint pk_version_id primary key clustered (version_id)
);
insert into DB_version values(0);




--Create Procedure

--a. modify the type of a column;

go
create procedure do1 as
begin

alter table Vehicles 
alter column type_Vehicle varchar(25);

end;
go

--reverse
go
create procedure undo1 as
begin

alter table Vehicles
alter column type_Vehicle char(25);

end;
go

--b. add / remove a column;

go
create procedure do2 as
begin

alter table Vehicles
add an_fabricatie int

end;
go

--reverse

go
create procedure undo2 as
begin

alter table Vehicles
drop column an_fabricatie

end;
go

--c. add / remove a DEFAULT constraint;

GO
create procedure do3 as
begin
alter table Vehicles
add an_accidente char(50)
alter table Vehicles
add constraint an_accidente_default
default '0' for an_accidente
end;
go

--reverse

go
create procedure undo3 as
begin
alter table Vehicles
drop constraint an_accidente_default
alter table Vehicles
drop column an_accidente
end;
go

--d. add / remove a primary key;

go
create procedure do4 as
begin
create table soldcars
(
	SCID int not null,
);
	alter table soldcars
	add constraint pk_soldcars_SCID primary key clustered (SCID);

end;
go

--reverse

go
create procedure undo4 as
begin
alter table soldcars
drop constraint pk_soldcars_SCID;
drop table soldcars;
end;
go

--e. add / remove a candidate key;

go
create procedure do5 as
begin
create table owners2(
O2ID int,
description varchar(15) not null,
constraint pk_1 primary key (O2ID)
);

alter table owners2
drop constraint pk_1;
alter table owners2
add constraint pk_2 primary key clustered (description)
end
go

--reverse
go
create procedure undo5 as
begin
alter table owners2
drop constraint pk_2;

alter table owners2
add constraint pk_1 primary key clustered (O2ID)
drop table owners2
end
go

--f. add / remove a foreign key;
go
create procedure do6
as
begin
create table tableA(
Aid int not null,
A2id int,
primary key (Aid)
);

create table tableB(
Bid int,
primary key(Bid)
);
alter table tableB
add Aid int
alter table tableB
add constraint FK_AID foreign key(Aid) references tableA(Aid)
end;
go

go
create procedure undo6
as
begin
alter table tableB
drop constraint FK_AID
alter table tableB
drop column Aid
drop table tableB
drop table tableA
end;
go

--g. create / remove a table.

create procedure do7
as
begin
create table c(
cid int not null,
primary key(cid)
);
end
go

--reverse

create procedure undo7
as
begin
drop table c
end
go

