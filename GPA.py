class Course:
    def __init__(self, subj, no, name, letter, credit):
        self.subj = subj
        self.no = no
        self.name = name
        self.letter = letter
        self.credit = credit
        self.grade = Course.Grade(letter)
        if (self.grade == "X" or self.grade == "S"):
            self.gpa == 0
        else:
            self.gpa = self.grade * self.credit
        
    def __str__(self):
        string = self.subj + "  " + str(self.no) + "    "
        string += self.name.ljust(26," ") + "Grade: " + self.letter.ljust(5," ")
        string += "Hours: " + str(self.credit).ljust(5," ")
        return string 
    
    def __repr__(self):
        return self.name
    
    def getGrade(self):
        return self.grade
    def getCredit(self):
        return self.credit
    
    def Grade(letter):
        if (letter == "A"):
            return 4        
        elif (letter == "B"):
            return 3       
        elif (letter == "C"):
            return 2     
        elif (letter == "D"):
            return 1
        elif (letter == "S"):#pass/fail class (AP/Transfered Credits)
            return 0
        elif (letter == "X"):#haven't taken yet
            return -1
        return 0
       
class Semester:  
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes
        self.hours = Semester.Hours(classes)
        self.grade = Semester.Grade(classes)
        self.gpa = self.grade/self.hours
        
    def __str__(self):
        print(self.name)
        print("-----------------------------------")
        for i in range(len(self.classes)):
            print(self.classes[i]) 
        #print("Credit Hours: {}".format(self.grade))
        
        if (self.gpa > 1):
            print("Hours: {}".format(self.hours))   
            print("GPA: {:.2f}".format(self.gpa))
        else:
            print("Credit Hours: {}".format(self.hours)) 
            #print("GPA: N/A")
        
        return ""

    def Hours(classes):
        hours = 0
        for i in range(len(classes)):
            hours += classes[i].getCredit()
        return hours            

    def Grade(classes):
        if (classes[0].getGrade() == -1):
            return -1
        
        grade = 0
        for i in range(len(classes)):
            if (classes[i].getGrade() > 0):    
                grade += classes[i].getGrade() * classes[i].getCredit()
        return grade

    def getGrade(self):
        return self.grade
    def getHour(self):
        return self.hours
        

AllClasses = []


AP_Lang = Course("ENGL",104,"Composition and Rhetoric","S",3)
AP_Lit = Course("ENGL",201,"Writing about Literature","S",3)
AP_WH = Course("HIST",104,"World History Since 1500","S",3)
AP_US1 = Course("HIST",105,"History of the US","S",3)
AP_US2 = Course("HIST",106,"History of the US","S",3)
AP_Transfer = Semester("Transfer",[AP_Lang,AP_Lit,AP_WH,AP_US1,AP_US2])
AllClasses.append(AP_Transfer)



Chem = Course("CHEM",107,"Chemistry","B",3)
ChemLab = Course("CHEM",117,"Chemistry Lab","B",1)
CLEN = Course("CLEN",181,"Engineering Semnair","S",0)
EngrPy = Course("ENGR",102,"Engineering Computation","A",2)
Calc1 = Course("MATH",151,"Calculus 1","A",4)
Jazz = Course("MUSC",225,"History of Jazz","A",3)
FreshmanFall = Semester("Freshman Fall",[Chem,ChemLab,CLEN,EngrPy,Calc1,Jazz])
AllClasses.append(FreshmanFall)

Comm = Course("COMM",315,"Communication","A",3)
Calc2 = Course("MATH",152,"Calculus 2","B",4)
PhysMech = Course("PHYS",206,"Newtonian Mechanics","A",3)
EngrMech = Course("ENGR",216,"Engr Mechanics Lab","A",2)
FreshmanSpring = Semester("Freshman Spring",[Comm,Calc2,PhysMech,EngrMech])
AllClasses.append(FreshmanSpring)

FedGov = Course("POLS",206,"National Government","S",3)
AllClasses.append(Semester("Freshman Summer",[FedGov]))



I_Program = Course("CSCE",121,"Intro to Program Design","A",4)
I_Computing = Course("CSCE",181,"Intro to Computing","A",1)
Discr_Comp = Course("CSCE",222,"Discrete Computing","C",3)
Calc3 = Course("MATH",251,"Calculus 3","D",3)
LinAlg = Course("MATH",304,"Linear Algebra","A",3)
SophomoreFall = Semester("Sophomore Fall",[I_Program,I_Computing,Discr_Comp,Calc3,LinAlg])
AllClasses.append(SophomoreFall)

Data_Struct = Course("CSCE",221,"Data Structures","X",4)
Comp_Org = Course("CSCE",312,"Computer Organization","X",4)
P_Languagues = Course("CSCE",314,"Programming Languages","X",3)
Geol = Course("GEOL",101,"Principles of Geology","X",3)
I_Psych = Course("PSYC",107,"Intro to Psychology","X",3)
SophomoreSpring = Semester("Sophomore Spring",[Data_Struct,Comp_Org,P_Languagues,Geol,I_Psych])
AllClasses.append(SophomoreSpring)



'''
StateGov = Course("POLS",207,"State Government","X",3)
AllClasses.append(Semester("Sophomore Summer",[StateGov]))


Comp_Sys = Course("CSCE",313,"Computer Systems","X",4)
P_Studio = Course("CSCE",315,"Programming Studio","X",3)
Seminar = Course("CSCE",481,"Seminar","X",1)
A_Musc = Course("PERF",386,"Evol of American Musical","X",3)
Stat1 = Course("STAT",211,"Statistics 1","X",3)
F_Vist = Course("VIST",375,"Found of Visualization","X",3)
JuniorFall = Semester("Junior Fall",[Comp_Sys,P_Studio,Seminar,A_Musc,Stat1,F_Vist])
AllClasses.append(JuniorFall)
'''



totalGrade = 0  
totalHours = 0  #Institution Hours
creditHours = 0 #Transfer Hours
print(chr(27) + "[2J") 
for i in range(len(AllClasses)):
    if (AllClasses[i].getGrade() > 0):   
        totalGrade += AllClasses[i].getGrade() 
        totalHours += AllClasses[i].getHour()
    elif (AllClasses[i].getGrade() == 0): 
        creditHours += AllClasses[i].getHour()
    print(AllClasses[i])
    print()




GPA = totalGrade/totalHours
print("Total Institution Hours: {}".format(totalHours))
print("Total Transfer: {}".format(creditHours)) 
print("Overall GPA: {:.4f}".format(GPA))



















