import json
import csv
import time
from abc import ABC, abstractmethod

#DECORATORS

# def admin_only(func):
#     def wrapper(*args, **kwargs):
#         user = input("Enter role (admin/user): ")
#         if user.lower() != "admin":
#             print("Access Denied: Admin privileges required")
#             return
#         return func(*args, **kwargs)
#     return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] Execution Time: {round(end-start, 4)} seconds")
        return result
    return wrapper


#DESCRIPTORS

class MarksDescriptor:
    def __get__(self, obj, objtype=None):
        return obj._marks

    def __set__(self, obj, value):
        if all(0 <= m <= 100 for m in value):
            obj._marks = value
        else:
            raise ValueError("Marks should be between 0 and 100")


class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        obj._salary = value


#ABSTRACT CLASS

class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass


# STUDENT CLASS

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    @logger
    @timer
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        print("\nStudent Performance Report")
        print("--------------------------------")
        print(f"Student Name : {self.name}")
        print(f"Marks        : {self.marks}")
        print(f"Average      : {round(avg,1)}")
        print(f"Grade        : {grade}")
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks)/len(self.marks) > sum(other.marks)/len(other.marks)


# FACULTY CLASS

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department}")


# COURSE CLASS

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty
        self.students = []

    def enroll(self, student):
        self.students.append(student)
        student.courses.append(self)

    def __add__(self, other):
        return self.credits + other.credits


#ITERATOR

class CourseIterator:
    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.courses):
            c = self.courses[self.index]
            self.index += 1
            return c
        else:
            raise StopIteration


#GENERATOR

def student_generator(students):
    print("\nStudent Record Generator")
    print("Fetching Student Records...")
    print("--------------------------------")
    for s in students:
        yield f"{s.pid} - {s.name}"


#FILE HANDLING

def save_to_json(students):
    data = []
    for s in students:
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Student data successfully saved to students.json")


def generate_csv_report(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students:
            avg = sum(s.marks)/len(s.marks)
            grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
            writer.writerow([s.pid, s.name, s.department, round(avg,1), grade])
    print("CSV Report generated: students_report.csv")


#MAIN SYSTEM

students = []
faculty_list = []
courses = []

while True:
    print("\nSMART UNIVERSITY MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Enroll Student to Course")
    print("5. Calculate Student Performance")
    print("6. Compare Two Students")
    print("7. Generate Reports")
    print("8. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ")
            if any(s.pid == sid for s in students):
                raise ValueError("Student ID already exists")

            name = input("Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Enter 5 marks: ").split()))

            s = Student(sid, name, dept, sem, marks)
            students.append(s)

            print("\nStudent Created Successfully")
            print(f"ID        : {sid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")
            print(f"Semester  : {sem}")

        elif choice == "2":
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            sal = int(input("Salary: "))

            f = Faculty(fid, name, dept, sal)
            faculty_list.append(f)

            print("\nFaculty Created Successfully")
            print(f"ID        : {fid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")

        elif choice == "3":
            code = input("Course Code: ")
            name = input("Course Name: ")
            credits = int(input("Credits: "))
            fid = input("Faculty ID: ")

            faculty = next(f for f in faculty_list if f.pid == fid)
            c = Course(code, name, credits, faculty)
            courses.append(c)

            print("\nCourse Added Successfully")
            print(f"Course Code : {code}")
            print(f"Course Name : {name}")
            print(f"Credits     : {credits}")
            print(f"Faculty     : {faculty.name}")

        elif choice == "4":
            sid = input("Student ID: ")
            code = input("Course Code: ")

            student = next(s for s in students if s.pid == sid)
            course = next(c for c in courses if c.code == code)
            course.enroll(student)

            print("\nEnrollment Successful")
            print(f"Student Name : {student.name}")
            print(f"Course       : {course.name}")

        elif choice == "5":
            sid = input("Student ID: ")
            student = next(s for s in students if s.pid == sid)
            student.calculate_performance()

        elif choice == "6":
            s1 = next(s for s in students if s.pid == input("First Student ID: "))
            s2 = next(s for s in students if s.pid == input("Second Student ID: "))
            print("\nComparing Students Performance")
            print(f"{s1.name} > {s2.name} : {s1 > s2}")

        elif choice == "7":
            generate_csv_report(students)
            save_to_json(students)

            for record in student_generator(students):
                print(record)

        elif choice == "8":
            print("\nThank you for using Smart University Management System")
            break

    except ValueError as e:
        print("Error:", e)
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError as e:
        print(e)
    except StopIteration:
        print("Error: Invalid ID")
