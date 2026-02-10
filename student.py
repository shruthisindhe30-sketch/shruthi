import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

cur.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (name, age, course))

conn.commit()
print("Student added successfully")

conn.close()

import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

student_id = int(input("Enter student ID to update: "))
new_course = input("Enter new course: ")

cur.execute("UPDATE students SET course = ? WHERE id = ?",
            (new_course, student_id))

conn.commit()
print("Student updated successfully")

conn.close()

import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

student_id = int(input("Enter student ID to delete: "))

cur.execute("DELETE FROM students WHERE id = ?", (student_id,))

conn.commit()
print("Student deleted successfully")

conn.close()

