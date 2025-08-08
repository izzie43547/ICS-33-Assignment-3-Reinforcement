# ICS 33 - Assignment 3 - Reinforcement: Query Analysis

## Project Overview
This assignment focuses on SQL query analysis and Python database operations. It includes SQL queries for employee data analysis and demonstrates lazy evaluation techniques in Python.

## Project Structure
- `create_db.py`: Script for creating and populating the employee database
- `query_tools.py`: Contains Python functions for querying and processing employee data
- `employees.db`: SQLite database containing employee information
- `query_analysis.txt`: Contains SQL queries and explanations
- `query_analysis.pdf`: Detailed analysis document

## Database Schema
The SQLite database contains an `employees` table with the following structure:
- `id`: Integer (Primary Key)
- `name`: Text (Employee name)
- `department`: Text (Department name)
- `title`: Text (Job title)
- `salary`: Integer (Annual salary in dollars)

## SQL Queries

### Query 1a: Engineering Salaries
```sql
SELECT name 
FROM employees 
WHERE department = 'engineering' 
    AND salary > 85000 
ORDER BY salary DESC;
```
This query retrieves names of all engineering employees earning more than $85,000, ordered by salary in descending order.

### Query 1b: Average Salary Calculation
```sql
SELECT ROUND(AVG(salary), 2) as avg_salary
FROM employees
WHERE title LIKE '%Senior%';
```
This query calculates the average salary of employees with 'Senior' in their job title, rounded to two decimal places.

## Python Utilities

### 1. `extract_ids_above_threshold(records, threshold)`
Returns a list of employee IDs for employees whose salary exceeds the specified threshold.

**Parameters:**
- `records`: List of employee records (dictionaries)
- `threshold`: Salary threshold (exclusive)

**Returns:**
- List of employee IDs (integers) for employees with salary > threshold

### 2. `project_department_counts(records)`
Returns a dictionary mapping each department to its employee count.

**Parameters:**
- `records`: List of employee records (dictionaries)

**Returns:**
- Dictionary with department names as keys and employee counts as values

### 3. `SalaryStepper` Class
An iterator that yields salary values in a specified range with a given step size.

**Methods:**
- `__init__(self, start, stop, step=5000)`: Initialize with start, stop, and step values
- `__iter__(self)`: Returns the iterator object itself
- `__next__(self)`: Returns the next salary value in the sequence

### 4. `filtered_names(records)`
A generator function that yields names of employees who:
- Work in the 'engineering' department
- Have names starting with 'J'
- Have a salary >= $90,000

**Parameters:**
- `records`: Iterable of employee records (dictionaries)

**Yields:**
- Names of employees matching all criteria

**Lazy Evaluation Benefits:**
1. **Memory Efficiency**: Processes one record at a time without creating intermediate lists
2. **Performance**: Enables early termination of iteration when only partial results are needed
3. **Scalability**: Can handle large data streams that wouldn't fit in memory

## Setup and Execution
1. Ensure Python 3.x is installed.
2. Run `create_db.py` to initialize the database:
   ```
   python create_db.py
   ```
3. Use the functions in `query_tools.py` to interact with the database.

## Dependencies
- Python 3.x
- sqlite3 (included in Python standard library)
