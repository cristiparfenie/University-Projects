use [Auto Parking Management]

delete from Park;
insert into Park values (1,'Raven Mobile','Piata Unirii');
insert into Park values (2,'Mobile.de','Libertatii');

delete from Place_for_sale;
insert into Place_for_sale values (1,10,1);
insert into Place_for_sale values (2,10,1);
insert into Place_for_sale values (3,11,1);
insert into Place_for_sale values (4,11,1);
insert into Place_for_sale values (5,20,1);
insert into Place_for_sale values (6,9,2);
insert into Place_for_sale values (7,11,2);
insert into Place_for_sale values (8,9,2);
insert into Place_for_sale values (9,10,2);
insert into Place_for_sale values (10,15,2);


delete from Maintenance_Team;
insert into Maintenance_Team values (1,'Sobarilor',1);
insert into Maintenance_Team values (2,'Libertatii',2);

delete from Employees;
insert into Employees values (1,'Dorel',2400,1);
insert into Employees values (2,'Mirel',2450,1);
insert into Employees values (1,'Marcel',2470,1);
insert into Employees values (3,'Daniel',2370,1);
insert into Employees values (4,'Dorian',2400,2);
insert into Employees values (5,'Mirela',2450,2);
insert into Employees values (6,'Marcela',2470,2);
insert into Employees values (7,'Daniela',2370,2);

Update Employees
Set EName = 'Damiam'
Where EID = 3;
Update Employees
Set EName = 'Marcel'
Where EID = 2;
Update Employees
Set EName = 'Mirel'
Where EID = 1;
Update Employees
Set EName = 'Daniel'
Where EID = 7;

--a. 2 queries with the union operation; use UNION [ALL] and OR;
--Afisiaza numele cumparatorilor si al vanzatorilor
select B_Name from Buyer 
union all
select O_Name from Owners

--Afisiaza numele cumparatorilor care incepe cu D sau G
select B_Name from Buyer
where B_Name like 'D%' or B_Name like 'G%'

--b. 2 queries with the intersection operation; use INTERSECT and IN;
--Afisiaza numele cumparatorilor si vanzatorilor
select B_Name from Buyer 
intersect 
select O_Name from Owners

--Afiseaza vehiculele cu pretul 6500, 6000, 8000
select * from Vehicles
where Price in (6500,6000,8000);

--c. 2 queries with the difference operation; use EXCEPT and NOT IN;
--Afiseaza vehiculele cu pret diferit de 6500, 6000, 8000
select * from Vehicles
where Price not in (6500,6000,8000);

--Afiseaza numele celor care sunt doar cumparatori sau sunt doar vanzatori
select B_Name from Buyer 
except
select O_Name from Owners

--d. 4 queries with INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN; one query will join at least 3 tables, while another one will join at least two many-to-many relationships;
--Afiseaza masinile care au avut si test drive
SELECT distinct *
FROM ((Vehicles V
INNER JOIN Vehicle_Test_Drive VT ON VT.VID = V.VID)
INNER JOIN Test_Drive_Order  TDO ON TDO.TOID = VT.TOID);

--Afiseaza toate masinile impreuna cu cele care sunt trecute pe lista de test drive
SELECT distinct *
FROM (Vehicles V
LEFT JOIN Vehicle_Test_Drive VTD ON VTD.VID = V.VID);

--Afiseaza toate masinile impreuna cu cumparatorii lor (daca este cazul) [top 3]
SELECT *
FROM (Buyer B
RIGHT JOIN Vehicles V ON V.VID = B.BID);
--Afiseaza toti cumparatorii si toti vanzatorii [top 3]
SELECT top 3*
FROM (Buyer B
FULL JOIN Owners OD ON OD.OID = B.BID);

--e. 2 queries using the IN operator to introduce a subquery in the WHERE clause; in at least one query, the subquery should include a subquery in its own WHERE clause;
--Afiseaza toate locurile de parcare a caror masini sunt puse la vanzare cu pretul mai mic de 4500
Select *
from Place_for_sale P
where P.PSID IN (Select PSID
					from Vehicles
					where Price<6500.10)

--Afiseaza park-urile care au unul sau mai multe vehicule cu pretul mai mare sau egal decat 20000
select Park_Name as 'Over 20000$ for only one car: '
from Park
where PID in (select PID
				from Place_for_sale
				where PSID in (select PSID
								from Vehicles
								where Price>=20000.00))


--f. 2 queries using the EXISTS operator to introduce a subquery in the WHERE clause;
--Afiseaza masinile care au facut deja un test drive
select *
from Vehicles V
where exists(
	select *
	from Vehicle_Test_Drive VTD
	where V.VID=VTD.VID);

--Afiseaza proprietarii care deja au vandut o masina, a caror nume incepe cu D
select distinct *
from Owners O
where exists(
	select *
	from Vehicles V
	where V.OID=O.OID) and
		exists(select *
			from Buyer
			where O_Name like 'D%');

--g. 2 queries with a subquery in the FROM clause;
--Afiseaza toti cumparatorii de vehicule in ordine alfabetica 
select distinct *
from (Select B.B_Name as 'Name: ', B.BID as 'Buyer ID: '
		from Buyer B
		inner JOIN Owners OD ON (OD.OID = B.BID)) rez
		order by rez.[Name: ];

--Afiseaza toate masinile impreuna cu cele care sunt trecute pe lista de test drive in ordine alfabetica
SELECT distinct *
FROM (Select V.VID as 'ID:', V.Model as 'Model:'
		from Vehicles V
		LEFT JOIN Vehicle_Test_Drive VTD ON (VTD.VID = V.VID)) rez
		order by rez.[Model:]

--h. 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause; 2 of the latter will also have a subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX;
--Afiseaza masinile care au avut macar un test drive
SELECT V.VID, V.Mark
FROM Vehicles V INNER JOIN Vehicle_Test_Drive VT ON VT.VID = V.VID
group by V.VID, V.Mark
having count(*)>=1

--Afiseaza suma pretului masinilor detinute de un proprietar al carui nume incepe cu 'D'
select SUM(price) as 'Suma pret: '
From Vehicles V
where V.OID in (Select O.OID 
			from Owners O
			Where O_Name like 'D%');

--Afiseaza media pretului masinilor detinute de un proprietar al carui nume incepe cu 'D'
select AVG(price) as 'Suma pret: '
From Vehicles V
where V.OID in (Select O.OID
			from Owners O
			Where O_Name like 'D%');

--Afiseaza cel mai mic pret al unei masini detinute de un proprietar al carui nume incepe cu 'M'
select MIN(price) as 'Suma pret: '
From Vehicles V
where V.OID in (Select O.OID 
			from Owners O
			Where O_Name like 'D%');

--i. 4 queries using ANY and ALL to introduce a subquery in the WHERE clause; 2 of them should be rewritten with aggregation operators, while the other 2 should also be expressed with [NOT] IN.
--Afiseaza prima masina care a efectuat un test drive
select top 1 CONCAT(V.Mark,' ',V.Model) as 'Primul test drive:'
from Vehicles V
where V.VID = Any (Select VT.VID
				from Vehicle_Test_Drive VT);
		
--Afiseaza proprietarii a caror masini au pretul mai mic decat media
Select *
from Owners O
where O.OID < ALL (Select V.OID
			from Vehicles V
			where price > (Select AVG (price)
							From Vehicles V
							Where O_Name like 'D%'));

--Afiseaza masinile care au locul de parcare mai mic de 10
Select CONCAT(V.Mark,' ',V.Model) as '<10'
from Vehicles V
where V.PSID IN (Select PSID
					from Place_for_sale
					where Size<10)

--Afiseaza masinile puse la vanzare care nu au facut inca un test drive
select *
from Vehicles V
where V.VID NOT IN (Select VID 
					from Vehicle_Test_Drive);

