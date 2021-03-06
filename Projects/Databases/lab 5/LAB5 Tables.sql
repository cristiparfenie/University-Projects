CREATE TABLE Vehicles(
	VID INT NOT NULL,
	Type_Vehicle CHAR (25),
	Mark CHAR (25),
	Model CHAR (25),
	Price DECIMAL (18,2),
	PRIMARY KEY (VID),
	);

CREATE TABLE Test_Drive_Order(
	TOID INT NOT NULL,
	TO_Nr INT NOT NULL,
	PRIMARY KEY (TOID)
);

CREATE TABLE Vehicle_Test_Drive(
	VID INT NOT NULL,
	TOID INT NOT NULL,
	Stare CHAR (15),
	PRIMARY KEY (VID,TOID),
	FOREIGN KEY (VID) REFERENCES Vehicles(VID),
	FOREIGN KEY (TOID) REFERENCES Test_Drive_Order(TOID)
);