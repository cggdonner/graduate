-- Catherine Donner
-- Task 4, DBMS Individual Project

-- DROP TABLE statements
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Assembly;
DROP TABLE IF EXISTS Begin_Manufacture;
DROP TABLE IF EXISTS Process;
DROP TABLE IF EXISTS Paint_Process;
DROP TABLE IF EXISTS Fit_Process;
DROP TABLE IF EXISTS Cut_Process;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Job;
DROP TABLE IF EXISTS Paint_Job;
DROP TABLE IF EXISTS Fit_Job;
DROP TABLE IF EXISTS Cut_Job;
DROP TABLE IF EXISTS Assign;
DROP TABLE IF EXISTS Cost_Transaction;
DROP TABLE IF EXISTS Account;
DROP TABLE IF EXISTS Assembly_Account;
DROP TABLE IF EXISTS Department_Account;
DROP TABLE IF EXISTS Process_Account;
DROP TABLE IF EXISTS Account_For_Assembly;
DROP TABLE IF EXISTS Account_For_Process;
DROP TABLE IF EXISTS Account_For_Department;

-- CREATE TABLE statements
CREATE TABLE Customer (
	Name varchar(25) PRIMARY KEY,
	Address varchar(100),
	Category int,
    CONSTRAINT Category_check CHECK (Category BETWEEN 0 AND 10)
);

CREATE TABLE Assembly (
	Assembly_Id int PRIMARY KEY,
	Date_Ordered date,
	Assembly_Details varchar(100),
	Customer_Name varchar(25) FOREIGN KEY REFERENCES Customer(Name)
);

CREATE TABLE Department (
	Department_Number int PRIMARY KEY,
	Department_Data varchar(50)
);

CREATE TABLE Process (
	Process_Id int PRIMARY KEY,
	Process_Data varchar(100),
	Department_Number int FOREIGN KEY REFERENCES Department(Department_Number)
);

CREATE TABLE Paint_Process (
    Process_Id int FOREIGN KEY REFERENCES Process(Process_Id),
	Paint_Type varchar(25),
	Painting_Method varchar(25),
    PRIMARY KEY(Process_Id)
);

CREATE TABLE Fit_Process (
	Process_Id int FOREIGN KEY REFERENCES Process(Process_Id),
	Fit_Type varchar(25),
    PRIMARY KEY(Process_Id)
);

CREATE TABLE Cut_Process (
	Process_Id int FOREIGN KEY REFERENCES Process(Process_Id),
    Cutting_Type varchar(25),
	Machine_Type varchar(25),
    PRIMARY KEY (Process_Id)
);

CREATE TABLE Begin_Manufacture (
    Assembly_Id int FOREIGN KEY REFERENCES Assembly(Assembly_Id),
	Process_Id int FOREIGN KEY REFERENCES Process(Process_Id),
    PRIMARY KEY(Assembly_Id, Process_Id)
); -- this was changed from Begin to Begin_Manufacture to not confuse SQL BEGIN syntax

CREATE TABLE Job (
	Job_No int PRIMARY KEY,
	Commence_Date date,
	Complete_Date date
);

CREATE TABLE Paint_Job (
	Job_No int FOREIGN KEY REFERENCES Job(Job_No),
	Color varchar(25),
	Volume int,
	Labor_Time int,
    PRIMARY KEY (Job_No)
);

CREATE TABLE Fit_Job (
	Job_No int FOREIGN KEY REFERENCES Job(Job_No),
	Labor_Time int,
    PRIMARY KEY(Job_No)
);

CREATE TABLE Cut_Job (
    Job_No int FOREIGN KEY REFERENCES Job(Job_No),
    Machine_Type varchar(25),
    Machine_Time_Used int,
    Material_Used varchar(25),
    Labor_Time int,
    PRIMARY KEY(Job_No)
);

CREATE TABLE Assign (
	Job_No int FOREIGN KEY REFERENCES Job(Job_No),
	Assembly_Id int FOREIGN KEY REFERENCES Assembly(Assembly_Id),
	Process_Id int FOREIGN KEY REFERENCES Process(Process_Id),
    PRIMARY KEY(Job_No)
);

CREATE TABLE Account (
	Account_No int PRIMARY KEY,
	Establish_Date date
);

CREATE TABLE Assembly_Account (
	Account_No int FOREIGN KEY REFERENCES Account(Account_No),
	Details_1 float,
    PRIMARY KEY(Account_No)
);

CREATE TABLE Department_Account (
	Account_No int FOREIGN KEY REFERENCES Account(Account_No),
	Details_2 float,
    PRIMARY KEY(Account_No)
);

CREATE TABLE Process_Account (
    Account_No int FOREIGN KEY REFERENCES Account(Account_No),
	Details_3 float,
    PRIMARY KEY(Account_No)
);

CREATE TABLE Cost_Transaction (
	Transaction_No int PRIMARY KEY,
	Sup_Cost float,
	Job_No int FOREIGN KEY REFERENCES Job(Job_No),
    Account_No int FOREIGN KEY REFERENCES Account(Account_No)
); -- changed from Transaction to Cost_Transaction to not confuse SQL syntax

CREATE TABLE Account_For_Assembly (
    Account_No int FOREIGN KEY REFERENCES Assembly_Account(Account_No),
	Assembly_Id int FOREIGN KEY REFERENCES Assembly(Assembly_Id),
    PRIMARY KEY(Assembly_Id)
);

CREATE TABLE Account_For_Process (
    Account_No int FOREIGN KEY REFERENCES Process_Account(Account_No),
	Process_Id int FOREIGN KEY REFERENCES Process(Process_Id),
    PRIMARY KEY(Process_Id)
);

CREATE TABLE Account_For_Department (
    Account_No int FOREIGN KEY REFERENCES Department_Account(Account_No),
	Department_Number int FOREIGN KEY REFERENCES Department(Department_Number),
    PRIMARY KEY(Department_Number)
);

-- CREATE INDEX statements
CREATE INDEX category_index ON Customer (Category);
CREATE INDEX dept_no_index ON Process (Department_Number);
CREATE INDEX complete_date_index ON Job (Complete_Date);
CREATE INDEX assembly_id_index ON Assign (Assembly_Id);