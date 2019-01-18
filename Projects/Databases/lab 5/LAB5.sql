use [LAB5]
--a. Write queries on Ta such that their corresponding execution plans contain the following operators:

	--clustered index scan; 
		select * from Vehicles
    
	--clustered index seek;
		select * from Vehicles
		where Price >= 9000
    
	--nonclustered index scan;
		drop index idx_1 on Vehicles
		create nonclustered index [idx_1] on Vehicles(Price)
		select Price from Vehicles
		

    --nonclustered index seek.
	select Price from Vehicles where Price >=9000

	--key look-up
	select * from Vehicles with (index=idx_1) where Price =6000;




	--b. Write a query on table Tb with a WHERE clause of the form WHERE b2 = value and analyze its execution plan. 
	-- Create a nonclustered index that can speed up the query. 
	-- Recheck the query’s execution plan (operators, SELECT’s estimated subtree cost).
	
	--nonclustered: 0.0032842
	drop index idx_2 on Test_Drive_Order
	create nonclustered index idx_2 on Test_Drive_Order(TO_Nr)
	select TO_Nr from Test_Drive_Order
	where TO_Nr = 2

	--clustered: 0.0032875
	select TO_Nr from Test_Drive_Order
	where TO_Nr = 2

	

	--c. Create a view that joins at least 2 tables. 
	-- Check whether existing indexes are helpful; if not, reassess existing indexes / examine the cardinality of the tables.
	
	drop view NrOfVehiclesWithTestDriveOrder
	create view NrOfVehiclesWithTestDriveOrder
	as
	select v.Price as Vehicles
	FROM ((Vehicles V
	INNER JOIN Vehicle_Test_Drive VT ON VT.VID = V.VID)
	INNER JOIN Test_Drive_Order  TDO ON TDO.TOID = VT.TOID)
	where V.Price >= 6000

	--clustered: 0.0069017
	select * from NrOfVehiclesWithTestDriveOrder

	--nonclustered: 0.0068971
	drop index idx_1 on Vehicles
	select * from NrOfVehiclesWithTestDriveOrder
