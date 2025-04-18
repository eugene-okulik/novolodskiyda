import os
from dotenv import load_dotenv
import mysql.connector as mysql
import csv

load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                        'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        query_select_data = '''
        SELECT
            s.name AS name,
            s.second_name AS second_name,
            g.title AS group_title,
            b.title AS book_title,
            subj.title AS subject_title,
            l.title AS lesson_title,
            m.value AS mark_value
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON b.taken_by_student_id = s.id
        LEFT JOIN marks m ON m.student_id = s.id
        LEFT JOIN lessons l ON m.lesson_id = l.id
        LEFT JOIN subjets subj ON l.subject_id = subj.id
        WHERE
            s.name = %s AND
            s.second_name = %s AND
            g.title = %s AND
            b.title = %s AND
            subj.title = %s AND
            l.title = %s AND
            m.value = %s;
        '''
        cursor.execute(
            query_select_data, (
                row['name'],
                row['second_name'],
                row['group_title'],
                row['book_title'],
                row['subject_title'],
                row['lesson_title'],
                row['mark_value']
            )
        )
        data = cursor.fetchall()
        print(data)
        if data == []:
            print(row)
        else:
            continue

db.close()
