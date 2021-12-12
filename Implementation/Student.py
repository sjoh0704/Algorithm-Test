class Student:
    def __init__(self, name="", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final=final
    
    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name
    
    def setMidterm(self, midterm):
        self._midterm = midterm
    
    def setFinal(self, final):
        self._final = final
    
    def __str__(self):
        return "{0} {1} {2}".format(self._name, self._midterm, self._final)


class LGStudent(Student):
    
    def calSemesterGrade(self):
        avg = round((self._final + self._midterm)/2)
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        else: 
            return 'C'


class PFStudent(Student):
    
    def calSemesterGrade(self):
        avg = round((self._final + self._midterm)/2)
        if avg >= 60:
            return 'P'
        else:
            return 'F'
        


if __name__== '__main__':
    s1 = Student("jason", 40, 50)
    print(s1)

    s2 = LGStudent("martin", 40, 90)
    print(s2)
    print(s2.calSemesterGrade())

    s3=PFStudent("Jerry", 60, 50)
    print(s3)
    print(s3.calSemesterGrade())


