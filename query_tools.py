
# Problem 1a
query_1a = """
SELECT name 
FROM employees 
WHERE department = 'engineering' 
AND salary > 85000 
ORDER BY salary DESC;
"""

# Problem 1b
query_1b = """
SELECT ROUND(AVG(salary), 2) as avg_salary
FROM employees
WHERE title LIKE '%Senior%';
"""

# Problem 2
def extract_ids_above_threshold(records, threshold):
    """Returns a list of IDs of employees whose salary exceeds the threshold."""
    return [record[0] for record in records if record[4] > threshold]

def project_department_counts(records):
    """Returns a dictionary mapping each department to its employee count."""
    from collections import defaultdict
    counts = defaultdict(int)
    for record in records:
        counts[record[2]] += 1
    return dict(counts)

# Problem 3
class SalaryStepper:
    def __init__(self, start, stop, step=5000):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

# Problem 4
def filtered_names(records):
    """Yields names of employees in engineering, name starts with 'J', salary >= 90000"""
    return (record[1] for record in records 
            if (record[2] == 'engineering' 
                and record[1].startswith('J') 
                and record[4] >= 90000))
