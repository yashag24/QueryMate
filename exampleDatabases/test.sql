-- Drop tables if they exist (useful for testing)
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS assignments;

-- Departments Table
CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Employees Table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department_id INTEGER,
    salary INTEGER CHECK (salary > 0),
    hire_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE SET NULL
);

-- Projects Table
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    budget INTEGER CHECK (budget > 0),
    start_date DATE DEFAULT CURRENT_DATE
);

-- Assignments Table (Many-to-Many: Employees <-> Projects)
CREATE TABLE assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    project_id INTEGER,
    role TEXT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Insert Departments
INSERT INTO departments (name) VALUES ('Engineering'), ('Marketing'), ('HR');

-- Insert Employees
INSERT INTO employees (first_name, last_name, department_id, salary) VALUES
    ('Alice', 'Smith', 1, 75000),
    ('Bob', 'Johnson', 2, 60000),
    ('Charlie', 'Brown', 1, 90000),
    ('David', 'White', 3, 50000);

-- Insert Projects
INSERT INTO projects (name, budget) VALUES
    ('Project A', 100000),
    ('Project B', 150000),
    ('Project C', 200000);

-- Insert Assignments
INSERT INTO assignments (employee_id, project_id, role) VALUES
    (1, 1, 'Developer'),
    (2, 2, 'Marketing Lead'),
    (3, 1, 'Tech Lead'),
    (4, 3, 'HR Coordinator');
