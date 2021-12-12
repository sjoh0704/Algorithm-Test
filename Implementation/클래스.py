class Student:
    def __init__(self, name="", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final=final
    
    def setName(self, name):
        self._name = name
    
    def setMidterm(self, midterm):
        self._midterm = midterm
    
    def setFinal(self, final):
        self._final = final
    
    def __str__(self):
        return "{0} {1} {2}".format(self._name, self._midterm, self._final)

def main():
    s1 = Student("jason", 40, 50)
    print(s1)

main()


