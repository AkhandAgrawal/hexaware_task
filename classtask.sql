--Exercise 1: Create a Table for Students
--Task:
--• Create a table Students with the following constraints:
--o student_id is an auto-incrementing primary key.
--o gender should only accept 'M' or 'F'.
--o age should be between 5 and 100.
CREATE TABLE Students (
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F')),
    age INT CHECK (age BETWEEN 5 AND 100)
);

--Exercise 2: Insert Data into the Students Table
INSERT INTO Students (student_name, gender, age) VALUES 
('Aryan Singh', 'M', 20),
('Vrishti Sharma', 'F', 22),
('Aman Tayal', 'M', 18),
('Suhani Sharma', 'F', 30),
('Kabir Verma', 'M', 25);
--Exercise 3: Create a Table for Subjects
--Task:
--• Create a table Subjects with the following columns:
--o subject_id: auto-incrementing primary key.
--o subject_name: should not accept NULL values.
CREATE TABLE Subjects (
    subject_id INT IDENTITY(1,1) PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL
);
--Exercise 4: Insert Data into Subjects Table
INSERT INTO Subjects (subject_name) VALUES 
('Mathematics'),
('Physics'),
('Chemistry'),
('Biology');
--Exercise 5: Create a Table for Enrollments with Foreign Keys
--Task:
--• Create a table Enrollments with:
--o student_id: foreign key referencing the student_id from the Students
--table.
--o subject_id: foreign key referencing the subject_id from the Subjects table.
--o Ensure that if a student or subject is deleted, the enrollment entry should 
--also be deleted
CREATE TABLE Enrollments (
    enrollment_id INT IDENTITY(1,1) PRIMARY KEY,
    student_id INT,
    subject_id INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id) ON DELETE CASCADE
);
--Exercise 6: Insert Data into Enrollments Table
INSERT INTO Enrollments (student_id, subject_id) VALUES
(1, 1), 
(1, 2), 
(2, 1), 
(3, 3), 
(4, 4); 
--Exercise 7: Update Student Age
--Task:
--• Update the age of a student in the Students table.
--Question:
--• Update the age of 'Jane Smith' to 23.
UPDATE Students
SET age = 23
WHERE student_name = 'Jane Smith';
--Exercise 8: Create a Table for Marks
--Task:
--• Create a table Marks with the following columns:
--o student_id: foreign key referencing Students.
--o subject_id: foreign key referencing Subjects.
--o marks: integer value between 0 and 100.
CREATE TABLE Marks (
    mark_id INT IDENTITY(1,1) PRIMARY KEY,
    student_id INT,
    subject_id INT,
    marks INT CHECK (marks BETWEEN 0 AND 100),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);
--Exercise 9: Insert Data into Marks Table
INSERT INTO Marks (student_id, subject_id, marks) VALUES 
(1, 1, 85),
(1, 2, 90), 
(2, 1, 88), 
(3, 3, 70), 
(4, 4, 95); 
--Exercise 10: Add a New Column to an Existing Table
--Task:
--• Add a new column email to the Students table that allows storing the student's 
--email address.
ALTER TABLE Students
ADD email VARCHAR(100);
--Exercise 11: Update the Email Address for a Student
--Task:
--• Update the email of one of the students in the Students table.
--Question:
--• Update the email of 'Tom Brown' to 'tom.brown@email.com'
UPDATE Students
SET email = 'aryan.singh@email.com'
WHERE student_name = 'Aryan Singh';
select * from students;
--Exercise 12: Remove a Foreign Key Constraint
--Task:
--• Remove the foreign key constraint on subject_id from the Marks table.
--Question:
--• Write a query to drop the foreign key constraint on the subject_id in the Marks
--table.
ALTER TABLE Marks
DROP CONSTRAINT FK__Marks__subject_i__4316F928;  
--Exercise 13: Add a Check Constraint
--Task:
--• Add a check constraint to the Marks table that ensures the marks column value 
--is between 0 and 100.
ALTER TABLE Marks
ADD CONSTRAINT CHK_Marks CHECK (marks BETWEEN 0 AND 100);
--Exercise 14: Add On Delete Cascade to a Foreign Key
--Task:
--• Modify the Marks table to ensure that if a student is deleted from the Students
--table, their corresponding marks are also deleted automatically.
--Question:
--• Write an SQL query to update the foreign key constraint on student_id in the 
--Marks table to add ON DELETE CASCADE.
ALTER TABLE Marks
DROP CONSTRAINT FK__Marks__student_i__4222D4EF; 
ALTER TABLE Marks
ADD CONSTRAINT FK_Marks_student FOREIGN KEY (student_id)
REFERENCES Students(student_id) ON DELETE CASCADE;
--Bonus Exercise: Create a Self-Referencing Table
--Task:
--• Create a table Employees with a manager_id that references another 
--employee_id in the same table.
CREATE TABLE Employees (
    employee_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);


--------------------------------------------------------------------------
--Task 15: Write a query to retrieve students' names and their respective subject names from the Students and
--Subjects tables, assuming that not every student has enrolled in a subject yet.
--Table Structure:
--Students (student_id, student_name)
--Subjects (subject_id, subject_name)
--Enrollments (student_id, subject_id)
SELECT s.student_name, sub.subject_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Subjects sub ON e.subject_id = sub.subject_id;


--Task 16: Write a query to retrieve all students, 
--even those who have not enrolled in any subjects, along with their enrolled subjects. 
SELECT s.student_name, sub.subject_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Subjects sub ON e.subject_id = sub.subject_id;


--Task 17: Retrieve all subjects, even if no students are enrolled in those subjects. 
--Also, retrieve the students who have enrolled in those subjects
SELECT sub.subject_name, s.student_name
FROM Subjects sub
LEFT JOIN Enrollments e ON sub.subject_id = e.subject_id
LEFT JOIN Students s ON e.student_id = s.student_id;


--Task 18: Retrieve all students and subjects, regardless of whether a student
--is enrolled in a subject or a subject has enrolled students.
SELECT s.student_name, sub.subject_name
FROM Students s
FULL OUTER JOIN Enrollments e ON s.student_id = e.student_id
FULL OUTER JOIN Subjects sub ON e.subject_id = sub.subject_id;


--Task 19: Show all students and all subjects, generating every possible combination.
SELECT s.student_name, sub.subject_name
FROM Students s
CROSS JOIN Subjects sub;


--Task 20: Retrieve each student's name and the total marks they scored across all subjects.
SELECT s.student_name, SUM(m.marks) AS total_marks
FROM Students s
JOIN Marks m ON s.student_id = m.student_id
GROUP BY s.student_name;


--Task 21: Write a query to list employees and their respective managers' names.
--Table Structure: Employees (employee_id, employee_name, manager_id)
INSERT INTO Employees (employee_name, manager_id) VALUES 
('John Smith', NULL),
('Alice Johnson', 1), 
('Bob Brown', 1),      
('David Green', 2),    
('Emily White', 3);    

SELECT e.employee_name AS employee, m.employee_name AS manager
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id;


--Task 22: Write a query to list students and their marks for each subject using an equi join.
SELECT s.student_name, sub.subject_name, m.marks
FROM Students s
JOIN Marks m ON s.student_id = m.student_id
JOIN Subjects sub ON m.subject_id = sub.subject_id;

--Task 23: Write a query to find subjects with an average mark greater than 70.
SELECT sub.subject_name, AVG(m.marks) AS average_marks
FROM Marks m
JOIN Subjects sub ON m.subject_id = sub.subject_id
GROUP BY sub.subject_name
HAVING AVG(m.marks) > 70;

--Bonus Task: Write a query to display students who are enrolled in more than two subjects.
SELECT s.student_name, COUNT(e.subject_id) AS subject_count
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
GROUP BY s.student_name
HAVING COUNT(e.subject_id) > 2;



SELECT 
    s.student_name, 
    m.marks,
    ROW_NUMBER() OVER (ORDER BY m.marks DESC) AS row_number
FROM 
    Students s
JOIN 
    Marks m ON s.student_id = m.student_id
WHERE 
    m.subject_id = 1; 

select s.student_name, sub.subject_name, m.marks, 
rank() over (partition by sub.subject_name order by m.marks desc) 
as subject_rank from students s join marks m on 
s.student_id = m.student_id join subjects sub on m.subject_id = sub.subject_id;

select s.student_name, sub.subject_name, m.marks, 
dense_rank() over (partition by sub.subject_name order by m.marks desc) 
as subject_rank from students s join marks m on
s.student_id = m.student_id join subjects sub on m.subject_id = sub.subject_id;

SELECT 
    s.student_name AS student_name,
    sub.subject_name,
    m.marks,
    NTILE(3) OVER (PARTITION BY sub.subject_name ORDER BY m.marks DESC) AS student_rank
FROM 
    Marks m
JOIN 
    Student s ON m.student_id = s.student_id
JOIN 
    Subject sub ON m.subject_id = sub.subject_id;


--Question: Retrieve the names of students who are enrolled in at least one subject. Use a subquery 
--with the IN operator to fetch the student details based on the enrollment table. Tables:
--Students(student_id, name)
--Enrollments(student_id, subject_id)
--Hint: Use the IN operator in a subquery to check if the student is in the Enrollments table.

SELECT student_name
FROM Students WHERE student_id IN (
    SELECT student_id
    FROM Enrollments
);


select s.student_id, s.marks from marks s where s.marks > (
    select max(m.marks) from marks m
    join subjects sub on m.subject_id = sub.subject_id
    where sub.subject_name = 'mathematics'
);

--Question: List all the students whose marks are greater than the average marks of any student in the "Physics" subject.
--Tables:
--Marks(student_id, subject_id, marks)

select s.student_id, s.marks from marks s where s.marks >(
	select avg(m.marks) from marks m join subjects sub on m.subject_id = sub.subject_id
    where sub.subject_name = 'physics'
);

