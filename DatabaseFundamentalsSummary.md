# Database Fundamentals Summary

* Performing a Conditional Search
* Working with Functions 
* Organizing Data  
* Retrieving Data from Multiple Tables  
* Indexes  
* Updating/Deleting Tables
* Backup and Restore

### Performing a Conditional Search

#### Single Search Condition
SELECT ordnum, sldate, qty, partnum, repid FROM sales
WHERE repid =  'NO2';

We would like to view ordnum, sldate, qty, partnum, and repid columns from sales table and the condition is where repid column equals to 'NO2.' 

### Multiple Conditional Operators
* SELECT partnum, bktitle, slprice FROM titles WHERE slprice > 40 AND partnum > 1000
In this query, the program will show us partnum, bktitle, and slprice columns from titles table where slprice is greater than 40 and partnum is greater than 1000.
* There are OR, AND, NOT, BETWEEN, AND NOT, and IN operators which are used to specify conditions in an SQL statement and to serve as conjuctions for multiple conditions in a statement. Arithmetic operators can perform arithmetical operations on numeric operands involved.
There are IS NULL and IS NOT NULL clauses which can show us if there's a null value in the column/s. 
* There are also wildcards option where we can modify and specify for each column/s how we want to view. For example, the wildcard '%' permits substituting one or more characters in a field, and this wildcard ' _ ' permits susbstituting a single character in a syntax expression. For instance, this 'c%' will give us any book title value that begins with "c."
