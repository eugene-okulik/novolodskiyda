import mysql.connector as mysql
import random

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

insert_new_student = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
cursor.execute(insert_new_student, ('Dimans', 'Serbovichev', None))
new_student_id = cursor.lastrowid

db.commit()
print(f'insert_new_student - {new_student_id}')

insert_book = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_book, [
        ('NewBookOne1', new_student_id),
        ('NewBookTwo2', new_student_id),
        ('NewBookThree3', new_student_id)
    ]
)

db.commit()

print('insert_book')

insert_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(insert_group, ('Solo2', 'march 2025', 'jun 2025'))
new_group_id = cursor.lastrowid

db.commit()

print(f'insert_group - {new_group_id}')

update_student_group = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(update_student_group, (new_group_id, new_student_id))

print('update_student_group')


def new_subjects(title):
    insert_subjects = "INSERT INTO subjets (title) VALUES (%s)"
    cursor.execute(insert_subjects, (title,))
    new_subjects_id = cursor.lastrowid
    db.commit()
    return new_subjects_id


subject_4 = new_subjects('Subjets№4')
print(f'subject_4 - {subject_4}')
subject_5 = new_subjects('Subjets№5')
print(f'subject_5 - {subject_5}')
subject_6 = new_subjects('Subjets№6')
print(f'subject_6 - {subject_6}')


def new_lessons_for_subject(id_sbject, count):
    insert_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    subject_lessons_id = []
    for pp_lesson in range(count):
        p_p = pp_lesson + 1
        cursor.execute(insert_lessons, (f'Lesson№{p_p}_{id_sbject}', id_sbject))
        new_lesson_id = cursor.lastrowid
        db.commit()
        subject_lessons_id.append(new_lesson_id)
    return subject_lessons_id


lessons_subject_4 = new_lessons_for_subject(subject_4, 2)
print(lessons_subject_4)
lessons_subject_5 = new_lessons_for_subject(subject_5, 2)
print(lessons_subject_5)
lessons_subject_6 = new_lessons_for_subject(subject_6, 2)
print(lessons_subject_6)


def marks(lessons, student_id):
    insert_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
    for lesson in lessons:
        cursor.execute(insert_marks, (random.randint(1, 10), lesson, student_id))
    db.commit()
    return print(f'Add marks to lessons {lessons}')


marks(lessons_subject_4, new_student_id)
marks(lessons_subject_5, new_student_id)
marks(lessons_subject_6, new_student_id)

select_marks = "SELECT * FROM `st-onl`.marks m WHERE m.student_id = %s"
cursor.execute(select_marks, (new_student_id,))
print(cursor.fetchall())

select_books = '''
SELECT *
FROM `st-onl`.books
WHERE taken_by_student_id = %s
'''
cursor.execute(select_books, (new_student_id,))
print(cursor.fetchall())

select_all_data = '''
SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title, m.value, l.title, subj.title
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON l.id = m.lesson_id
LEFT JOIN subjets subj ON subj.id = l.subject_id
WHERE s.id = %s
'''
cursor.execute(select_all_data, (new_student_id,))
print(cursor.fetchall())

db.close()
