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

--Question NO : 1068. Product Sales Analysis I

SELECT Product.product_name,Sales.year,Sales.price FROM Sales
INNER JOIN Product ON Product.product_id = Sales.product_id;

<-------------------------------------------------------------------------------------------------------------------------------->

--Question NO : 1581. Customer Who Visited but Did Not Make Any Transactions

SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;

<-------------------------------------------------------------------------------------------------------------------------------->