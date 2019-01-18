use [practic];


--1
create table customers(
holder int primary key identity,
C_Name varchar(50),
C_Date time
);

create table cards(
nr_Card int primary key,
CVV int
);

create table bank(
IBAN int primary key,
balance int,
holder int,
FOREIGN KEY (holder) REFERENCES customers(holder),
nr_Card INT UNIQUE FOREIGN KEY REFERENCES cards(nr_Card)
);

create table ATM(
AID int primary key identity,
Addressa char(25)
);

create table trasactions(
nr_Card INT NOT NULL,
AID INT NOT NULL,
T_Date time,
T_Sume int,
PRIMARY KEY (nr_Card,AID),
FOREIGN KEY (nr_Card) REFERENCES cards(nr_Card),
FOREIGN KEY (AID) REFERENCES ATM(AID)
);

delete from customers
delete from ATM
delete from cards
delete from bank
delete from trasactions

insert into customers values ('Tudor','02.02.2000'),('Dani','01.01.1999'),('Robert','03.03.1990'),('Roberta','04.04.1990')
insert into ATM ([Addressa]) values ('Str Unirii 6'),('Str Pt. Unirii 6'),('Str Cealalta Strada 7')
insert into cards values (1,123),(2,234),(3,345)
insert into bank values (1,9999,1,1),(2,9999,2,2),(3,9999,3,3)
insert into trasactions values (1,1,'3:00',99),(2,2,'5:00',102),(3,3,'2:00',2001)

--2
go
create or alter procedure deleteP @nr_Card int
as
begin
	delete from trasactions where nr_Card=@nr_Card
end

select * from trasactions
exec deleteP '1'

--3


--4
go
create or alter procedure selectJoin
as
begin
	select * from cards c where c.nr_Card in(select T.nr_Card from trasactions T where SUM(T_Sume)>2000)

end

