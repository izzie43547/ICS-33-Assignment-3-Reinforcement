import sqlite3
import os

def create_database():
    # Remove existing database file if it exists
    if os.path.exists('employees.db'):
        os.remove('employees.db')
    
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    
    # Create employees table
    cursor.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        title TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
    ''')
    
    # Sample data including test cases for the assignment
    employees = [
        (1, 'John Smith', 'engineering', 'Senior Software Engineer', 120000),
        (2, 'Jane Doe', 'engineering', 'Software Engineer', 90000),
        (3, 'Mike Johnson', 'sales', 'Sales Manager', 110000),
        (4, 'Sarah Williams', 'engineering', 'Junior Developer', 70000),
        (5, 'James Brown', 'engineering', 'Senior Developer', 130000),
        (6, 'Jennifer Davis', 'hr', 'HR Manager', 95000),
        (7, 'Robert Miller', 'engineering', 'Senior Systems Architect', 140000),
        (8, 'Jessica Wilson', 'marketing', 'Marketing Director', 115000),
        (9, 'Thomas Moore', 'engineering', 'DevOps Engineer', 105000),
        (10, 'Lisa Taylor', 'engineering', 'Senior QA Engineer', 98000)
    ]
    
    # Insert sample data
    cursor.executemany('''
    INSERT INTO employees (id, name, department, title, salary)
    VALUES (?, ?, ?, ?, ?)
    ''', employees)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database 'employees.db' created successfully with sample data!")

if __name__ == '__main__':
    create_database()
