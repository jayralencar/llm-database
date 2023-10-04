import sqlite3

con = sqlite3.connect('example.db')

cur = con.cursor()
# create student grades table
cur.execute('''CREATE TABLE student_grades
               (id INTEGER PRIMARY KEY, name TEXT, grade REAL)''')

# insert some data
cur.execute("INSERT INTO student_grades VALUES (1, 'John', 3.5)")
cur.execute("INSERT INTO student_grades VALUES (2, 'Jane', 3.8)")
cur.execute("INSERT INTO student_grades VALUES (3, 'Jack', 2.7)")
cur.execute("INSERT INTO student_grades VALUES (4, 'Jill', 3.9)")
cur.execute("INSERT INTO student_grades VALUES (5, 'Joe', 3.2)")
cur.execute("INSERT INTO student_grades VALUES (6, 'Jen', 3.7)")
cur.execute("INSERT INTO student_grades VALUES (7, 'Jess', 3.4)")
cur.execute("INSERT INTO student_grades VALUES (8, 'James', 3.3)")
cur.execute("INSERT INTO student_grades VALUES (9, 'Judy', 3.1)")
cur.execute("INSERT INTO student_grades VALUES (10, 'Jeff', 3.6)")
con.commit()

con.close()