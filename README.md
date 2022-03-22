# GPACalculator
Python program that prints out all your classes, hours and GPA (per semester and total) to the terminal

This was made specfically in mind for A&M Students, so it currently only supports whole letter grades (A,B,C,D,F,X,S)
A - 4.0
B - 3.0
C - 2.0
D - 1.0
F - 0.0
S - Credits that don't count toward GPA (like AP/DC Credits, or Transfered Classes)
X - Classes you haven't taken yet


The core of the program is OOP, specifically the Course class and Semester clas


Course class:
  Subject: Four letter (all uppercase) subject (like MATH or ENGR)
  Number: 3 digit course number (MATH 151)
  Name: Class's actual name (MATH 151 = Calculus 1)
  Letter: Letter grade received.
  Credit: Number of Credit Hours this class is worth
  Grade: Calculated from given letter
  GPA: GPA for this course (credit * grade)
  
Semester class:
  Name: Name of the given semester (Freshman Fall, Freshman Spring)
  Classes: List of Course objects
  Hours: Sum of hours from Classes
  Grades: Sum of grades from Classes
  GPA: GPA for this semester (hours/grades)
