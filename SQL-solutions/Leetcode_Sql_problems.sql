<-------------------------------------------------------------------------------------------------------------------------------->
--Question NO : 1757. Recyclable and Low Fat Products

SELECT product_id FROM Products WHERE low_fats = 'Y' and recyclable ="Y";

<-------------------------------------------------------------------------------------------------------------------------------->

--Question NO : 584. Find Customer Referee

SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS null;

<-------------------------------------------------------------------------------------------------------------------------------->

--Question NO : 595. Big Countries

SELECT name,population,area FROM World WHERE area >= 3000000 OR population >= 25000000;

<-------------------------------------------------------------------------------------------------------------------------------->

--Question NO : 1148. Article Views I

SELECT DISTINCT  author_id AS id FROM Views WHERE author_id = viewer_id ORDER BY id ;

<-------------------------------------------------------------------------------------------------------------------------------->

--Question NO : 1683. Invalid Tweets

SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content) > 15;

<-------------------------------------------------------------------------------------------------------------------------------->

--Question NO : 1378. Replace Employee ID With The Unique Identifier

SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;

<-------------------------------------------------------------------------------------------------------------------------------->
