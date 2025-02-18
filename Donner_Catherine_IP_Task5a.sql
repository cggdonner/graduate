-- Catherine Donner
-- Task 5a, DBMS Individual Project
-- Note that the values used in these statements are actual values that I used while 
-- implementing these queries. These values were substituted with ? in the Java program 
-- template queries. Feel free to replace with your own values.

-- Query 1
INSERT INTO Customer VALUES ('Charles', '500 South Street', 3);

-- Query 2
INSERT INTO Department VALUES (1, 'finance');

-- Query 3
INSERT INTO Process VALUES (1, 'paint process', 2);
INSERT INTO Paint_Process VALUES (1, 'oil', 'brush');
INSERT INTO Fit_Process VALUES (2, 'tight');
INSERT INTO Cut_Process VALUES (3, 'shears', 'saw machine');

-- Query 4
INSERT INTO Assembly VALUES (1, '2023-03-01', 'random assembly', 'Charles');
INSERT INTO Begin_Manufacture VALUES (1, 2);

-- Query 5
INSERT INTO Account VALUES (1, '2023-01-02');
INSERT INTO Assembly_Account VALUES (1, 0.00);
INSERT INTO Department_Account VALUES (2, 0.00);
INSERT INTO Process_Account VALUES (3, 0.00);
INSERT INTO Account_For_Assembly VALUES (1, 4);
INSERT INTO Account_For_Department VALUES (2, 5);
INSERT INTO Account_For_Process VALUES (3, 2);

-- Query 6
INSERT INTO Job VALUES (1, '2023-07-09', NULL);
INSERT INTO Assign VALUES (1, 5, 3);

-- Query 7
UPDATE Job SET Complete_Date='2023-07-27' WHERE Job_No=1;
INSERT INTO Paint_Job VALUES (1, 'red', 125, 100);
INSERT INTO Fit_Job VALUES (2, 40);
INSERT INTO Cut_Job VALUES (3, 'saw machine', 50, 'metal', 105);

-- Query 8
INSERT INTO Cost_Transaction VALUES (1, 90.04, 6, 1);
UPDATE Assembly_Account SET Details_1 = (Details_1 + 90.04) WHERE Account_No=1;
UPDATE Department_Account SET Details_2 = (Details_2 + 87.92) WHERE Account_No=2;
UPDATE Process_Account SET Details_3 = (Details_3 + 430.29) WHERE Account_No=6;

-- Query 9
SELECT SUM(Sup_Cost) FROM Cost_Transaction T 
JOIN Account_For_Assembly A ON A.Account_No = T.Account_No WHERE A.Assembly_Id=6;

-- Query 10
WITH AllJobLaborTimes AS (
    SELECT P.Department_Number, Labor_Time
    FROM Paint_Job PJ
    JOIN Job J ON J.Job_No = PJ.Job_No
    JOIN Assign A ON A.Job_No = J.Job_No
    JOIN Process P ON P.Process_Id = A.Process_Id
    WHERE J.Complete_Date = '2023-09-30'

    UNION

    SELECT P.Department_Number, Labor_Time
    FROM Fit_Job FJ
    JOIN Job J ON J.Job_No = FJ.Job_No
    JOIN Assign A ON A.Job_No = J.Job_No
    JOIN Process P ON P.Process_Id = A.Process_Id
    WHERE J.Complete_Date = '2023-09-30'

    UNION

    SELECT P.Department_Number, Labor_Time
    FROM Cut_Job CJ
    JOIN Job J ON J.Job_No = CJ.Job_No
    JOIN Assign A ON A.Job_No = J.Job_No
    JOIN Process P ON P.Process_Id = A.Process_Id
    WHERE J.Complete_Date = '2023-09-30'
)
SELECT Department_Number, SUM(Labor_Time)
FROM AllJobLaborTimes
GROUP BY Department_Number;

-- Query 11
SELECT P.*, J.Commence_Date FROM Process P 
JOIN Assign A ON A.Process_Id = P.Process_Id 
JOIN Job J ON J.Job_No = A.Job_No WHERE A.Assembly_Id=1 
ORDER BY J.Commence_Date;

-- Query 12
SELECT * FROM Customer WHERE Category BETWEEN 6 AND 8 ORDER BY Name ASC;

-- Query 13
DELETE FROM Cut_Job WHERE Job_No BETWEEN 30 AND 35;

-- Query 14
UPDATE Paint_Job SET Color='green' WHERE Job_No=1;

-- Error 1
INSERT INTO Customer VALUES ('Dean', '401 West Main St.', 15); -- Category not between 1 and 10

-- Error 2
INSERT INTO Customer VALUES ('Charles', '401 South Street', 8); -- Cannot insert duplicate primary key

-- Error 3
INSERT INTO Department VALUES ('hhg', 'legal'); -- Department number not an int



