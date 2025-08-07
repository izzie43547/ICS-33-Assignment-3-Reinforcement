"""
ICS 33 - Assignment 3 - Reinforcement
SQL queries and Python utility functions for employee data analysis.
"""

# Problem 1a: SQL Query for engineering employees earning > $85,000
query_1a = """
SELECT name 
FROM employees 
WHERE department = 'engineering' 
    AND salary > 85000 
ORDER BY salary DESC;
"""

# Problem 1b: SQL Query for average salary of employees with 'Senior' in title
query_1b = """
SELECT ROUND(AVG(salary), 2) as avg_salary
FROM employees
WHERE title LIKE '%Senior%';
"""

def extract_ids_above_threshold(records, threshold):
    """
    Returns a list of IDs of employees whose salary exceeds the threshold.
    
    Args:
        records: List of employee records (dictionaries)
        threshold: Salary threshold (exclusive)
        
    Returns:
        List of employee IDs (integers) for employees with salary > threshold
    """
    return [record['id'] for record in records if record['salary'] > threshold]


def project_department_counts(records):
    """
    Returns a dictionary mapping each department to its employee count.
    
    Args:
        records: List of employee records (dictionaries)
        
    Returns:
        Dictionary with department names as keys and employee counts as values
    """
    from collections import defaultdict
    dept_counts = defaultdict(int)
    for record in records:
        dept_counts[record['department']] += 1
    return dict(dept_counts)


class SalaryStepper:
    """
    Iterator that yields salary values starting from start, incrementing by step,
    until reaching stop (exclusive).
    """
    def __init__(self, start, stop, step=5000):
        """Initialize the SalaryStepper with start, stop, and step values."""
        self.current = start
        self.stop = stop
        self.step = step
        
    def __iter__(self):
        """Return the iterator object itself."""
        return self
        
    def __next__(self):
        """Return the next salary value in the sequence."""
        if self.current >= self.stop:
            raise StopIteration
        current = self.current
        self.current += self.step
        return current


def filtered_names(records):
    """
    Generator that yields names of employees who:
    - Work in the 'engineering' department
    - Have names starting with 'J'
    - Have a salary >= $90,000
    
    Args:
        records: Iterable of employee records (dictionaries)
        
    Yields:
        Names of employees matching all criteria
    """
    return (
        record['name']
        for record in records
        if (record['department'] == 'engineering' and
            record['name'].startswith('J') and
            record['salary'] >= 90000)
    )
