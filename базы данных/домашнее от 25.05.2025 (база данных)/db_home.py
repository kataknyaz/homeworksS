import sqlite3

# 1. Создание базы данных
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# 2. Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    major TEXT NOT NULL
)
''')

# Создаем таблицу grades
cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
''')

# 3. Добавляем данные

students_data = [
    ('Oleg', 20, 'Математика'),
    ('Anna', 22, 'Биология'),
    ('Katya', 21, 'Химия'),
    ('Boris', 23, 'Физика'),
    ('Dima', 19, 'Литература')
]

cursor.executemany('INSERT INTO students (name, age, major) VALUES (?, ?, ?)', students_data)


grades_data = [
    (1, 'Физика', 4),
    (1, 'Математика', 5),
    (1, 'Химия', 3),
    (2, 'Физика', 5),
    (2, 'Литература', 3),
    (2, 'Биология', 4),
    (3, 'Литература', 3),
    (3, 'Математика', 4),
    (4, 'Химия', 5),
    (5, 'Биология', 4)
]

cursor.executemany('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', grades_data)



# Запрос для вывода всех студентов и их средний балл
cursor.execute('''
SELECT s.name, AVG(g.grade) AS average_grade  
FROM students s                                
JOIN grades g ON s.id = g.student_id          
GROUP BY s.id                                  
''')
average_grades = cursor.fetchall()  

# Выводим студентов и их средний балл на экран
print("Студенты и их средний балл:")
for row in average_grades:  
    print(f"{row[0]}: {row[1]}")  

# Запрос для вывода студентов с средним баллом выше 4
cursor.execute('''
SELECT s.name, AVG(g.grade) AS average_grade  
FROM students s                                
JOIN grades g ON s.id = g.student_id         
GROUP BY s.id                                  
HAVING AVG(g.grade) > 4                        
''')
high_achievers = cursor.fetchall()  

# Выводим студентов с высоким средним баллом на экран
print("\nСтуденты с средним баллом выше 4:")
for row in high_achievers:  
    print(f"{row[0]}: {row[1]}")  

# Запрос для вывода количества студентов по каждой специальности (major)
cursor.execute('''
SELECT major, COUNT(*) AS student_count   
FROM students                             
GROUP BY major                            
''')
major_counts = cursor.fetchall()  

# Выводим количество студентов по специальностям 
print("Количество студентов по специальностям:")
for row in major_counts:  
    print(f"{row[0]}: {row[1]}")  


conn.commit()  
conn.close()   
 