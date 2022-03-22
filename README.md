# GPA Calculator
Python program that prints out all your classes, hours and GPA (per semester and total) to the terminal

This was made specfically in mind for A&M Undergrad Students, so it currently only supports the following letters from [A&M Catalogs Website](catalog.tamu.edu/undergraduate/general-information/grading-system/)
> A - Excellent, 4 grade points per hour
> 
> B - Good, 3 grade points per hour
> 
> C - Satisfactory, 2 grade points per hour
> 
> D - Passing, 1 grade point per hour
> 
> F - Failing, 0 grade points per hour (included in GPA calculation)
> 
> S[^1] - Satisfactory (no grade points, not included in GPA calculation)
> 
> X[^2] - Classes you haven't taken yet (no grade points, not included in GPA calculation)

[^1]: S includes AP/DC Credits,Transfered Credits, and Pass/Fail Classes. In the calculator, these count toward Total Transfer Hours

[^2]: Any letter not in the above list will not count toward GPA or Credit Hours (such as I for Incomplete, Q for Q-Drop, or U for Unsatisfactory)


# How to Use

The program starts with example code - a section on transfer credits, three semesters that have been completed, and a fourth semester currently being taken
The format for creating a course is 
> ExClass1 = Course("SUBJ",###,"Class Name",Letter Grade,Credit Hours)

The format for creating a semester is 
> ExSemester1 = Semester("Semester Name",[ExClass1,ExClass2,ExClass3])


# How it works
The core of the program is OOP, specifically the Course class and Semester clas


## Course class:
  - Subject: Four letter (all uppercase) subject (like MATH or ENGR)
  - Number: 3 digit course number (MATH **151**)
  - Name: Class's actual name (MATH 151 = Calculus 1)
  - Letter: Letter grade received.
  - Credit: Number of Credit Hours this class is worth
  - Grade: Calculated from given letter
  - GPA: GPA for this course (credit * grade)
  
## Semester class:
  - Name: Name of the given semester (Freshman Fall, Freshman Spring)
  - Classes: List of Course objects
  - Hours: Sum of hours from Classes
  - Grades: Sum of grades from Classes
  - GPA: GPA for this semester (hours/grades)

And that's pretty much it. The Semester and Course classes have toString methods that format the final output. Otherwise, the rest of the program is a loop that prints out all the classes of all the semesters, and the Institution Hours, Transfer Hours, and GPA
