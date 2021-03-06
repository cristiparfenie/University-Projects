CREATE TABLE Park(
   PID INT NOT NULL,
   Park_Name VARCHAR(20) NOT NULL,
   Park_Address CHAR (25),       
   PRIMARY KEY (PID)
);

CREATE TABLE Manager(
	MID INT NOT NULL,
	M_Name VARCHAR(20) NOT NULL,
	M_Address CHAR (25),
	Salary INT NOT NULL,
	PID INT UNIQUE FOREIGN KEY REFERENCES Park(PID),
	PRIMARY KEY (MID),
);

CREATE TABLE Maintenance_Team(
	TID INT NOT NULL,
	T_Address CHAR (25),
	PID INT UNIQUE FOREIGN KEY REFERENCES Park(PID),
	PRIMARY KEY (TID),
	
);

CREATE TABLE Employees(
	EID INT NOT NULL,
	EName VARCHAR(20) NOT NULL,
	Salary INT NOT NULL,
	TID INT NOT NULL,
	PRIMARY KEY (EID),
	FOREIGN KEY (TID) REFERENCES Maintenance_Team(TID)
);

CREATE TABLE Place_for_sale(
	PSID INT NOT NULL,
	Size DECIMAL (18,2),
	PID INT NOT NULL,
	PRIMARY KEY (PSID),
	FOREIGN KEY (PID) REFERENCES Park(PID)
);

CREATE TABLE Owners(
	OID INT NOT NULL,
	O_Name CHAR (25),
	O_Address CHAR (25),
	PRIMARY KEY (OID)
);

CREATE TABLE Buyer(
	BID INT NOT NULL,
	B_Name CHAR (25),
	B_Address CHAR (25),
	PRIMARY KEY (BID)
);

CREATE TABLE Vehicles(
	VID INT NOT NULL,
	Type_Vehicle CHAR (25),
	Mark CHAR (25),
	Model CHAR (25),
	Price DECIMAL (18,2),
	Fuel_Type CHAR (25),
	PID INT NOT NULL,
	OID INT NOT NULL,
	BID INT NOT NULL,
	PSID int UNIQUE FOREIGN KEY REFERENCES Place_for_sale(PSID),
	PRIMARY KEY (VID),
	FOREIGN KEY (PID) REFERENCES Park(PID),
	FOREIGN KEY (OID) REFERENCES Owners(OID),
	FOREIGN KEY (BID) REFERENCES Buyer(BID),
	);

CREATE TABLE Test_Drive_Order(
	TOID INT NOT NULL,
	TO_Name CHAR (25),
	PRIMARY KEY (TOID)
);

CREATE TABLE Vehicle_Test_Drive(
	VID INT NOT NULL,
	TOID INT NOT NULL,
	Status CHAR (15),
	PRIMARY KEY (VID,TOID),
	FOREIGN KEY (VID) REFERENCES Vehicles(VID),
	FOREIGN KEY (TOID) REFERENCES Test_Drive_Order(TOID)
);
