import mysql.connector

# ==============================
# DATABASE CONNECTION
# ==============================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fearse",
    database="company_db"
)

cursor = conn.cursor()

# ==============================
# 1. Fetch employees with salary > 50000
# ==============================

query = "SELECT * FROM employees WHERE salary > %s"
cursor.execute(query, (50000,))

print("Employees with salary > 50000:")
for row in cursor.fetchall():
    print(row)


# ==============================
# 2. Insert a new employee
# ==============================

insert_query = """
INSERT INTO employees (name, department, salary)
VALUES (%s, %s, %s)
"""

new_employee = ("John Doe", "IT", 60000)

cursor.execute(insert_query, new_employee)
conn.commit()

print("New employee inserted successfully.")


# ==============================
# 3. Update salary by 10% for specific employee
# ==============================

employee_id = 1   # example employee id

update_query = """
UPDATE employees
SET salary = salary * 1.10
WHERE id = %s
"""

cursor.execute(update_query, (employee_id,))
conn.commit()

print("Salary updated by 10%.")

# ==============================
# CLOSE CONNECTION
# ==============================

cursor.close()
conn.close()
