INSERT INTO students (name, second_name) VALUES ('Dima', 'Serbov')

INSERT INTO books (title, taken_by_student_id)
VALUES
  ('NoNameBook1', '20098'),
  ('NoNameBook2', '20098'),
  ('NoNameBook3', '20098');

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Solo', 'feb 2025', 'may 2025')

UPDATE students SET group_id = 4910 WHERE id = 20098

INSERT INTO subjets (title)
VALUES
  ('Subjets№1'),
  ('Subjets№2'),
  ('Subjets№3');

INSERT INTO lessons (title, subjet_id)
VALUES
  ('Lesson1ForSubjets№1', 10055),
  ('Lesson2ForSubjets№1', 10055),
  ('Lesson1ForSubjets№2', 10056),
  ('Lesson2ForSubjets№2', 10056),
  ('Lesson1ForSubjets№3', 10057),
  ('Lesson2ForSubjets№3', 10057);


INSERT INTO marks (value, lesson_id, student_id)
VALUES
  ('5', 9416, 20098),
  ('4', 9417, 20098),
  ('3', 9418, 20098),
  ('5', 9419, 20098),
  ('2', 9420, 20098),
  ('5', 9421, 20098);


SELECT *
FROM `st-onl`.marks m
WHERE m.student_id = 20098;


SELECT *
FROM `st-onl`.books
WHERE taken_by_student_id = 20098;




SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title, m.value, l.title, subj.title
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON l.id = m.lesson_id
LEFT JOIN subjets subj ON subj.id = l.subject_id
WHERE s.id = 20098;