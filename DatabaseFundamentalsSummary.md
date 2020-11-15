# Database Fundamentals Summary

* Performing a Conditional Search • 
* Working with Functions • 
* Organizing Data • 
* Retrieving Data from Multiple Tables • 
* Indexes  
* Updating/Deleting Tables
* Backup and Restore

### Performing a Conditional Search

#### Single Search Condition
SELECT ordnum, sldate, qty, partnum, repid FROM sales
WHERE repid =  'NO2';

We would like to view ordnum, sldate, qty, partnum, and repid columns from sales table and the condition is where repid column equals to 'NO2.' 

### Multiple Conditional Operators
#### sss
