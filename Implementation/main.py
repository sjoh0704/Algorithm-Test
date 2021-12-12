from Student import Student, PFStudent, LGStudent


def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'

    while carryOn == 'Y':
        name = input("이름")
        midterm = float(input("중간고사: "))
        final = float(input("기말고사: "))
        category = input("카테고리 입력(LG or PF): ")
        if category.upper() == 'LG':
            st = LGStudent(name, midterm, final)
        else:
            st = PFStudent(name, midterm, final)
        listOfStudents.append(st)
        carryOn = input("계속 할건가요?(y/n)").upper()
    return listOfStudents


def displayResults(listOfStudents):
    print("\nName\nGrade")
    numberOfLGStudents = 0
    listOfStudents.sort(key=lambda x: x.getName())
    for st in listOfStudents:
        print(st)

        if isinstance(st, LGStudent):
            numberOfLGStudents += 1
    
    print("LG학생수: ", numberOfLGStudents)
    print('PF학생수: ', len(listOfStudents)-numberOfLGStudents)




if __name__ == '__main__':

    listOfStudents = obtainListOfStudents()
    displayResults(listOfStudents)
