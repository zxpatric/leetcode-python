class Student:
    # _id = -1
    # _age = -1

    def __init__(self, id, age):
        self._id = id
        self._age = age

    def printMe(self):
        print ("I am ", self._age, " years old and my Id is ", self._id)

def prepareTestData():
    students = []
    students.append (Student (1, 19))
    students.append (Student (4, 21))
    students.append (Student (3, 20))
    return students

def printResults (students):
    for s in students:
        s.printMe()

# python .sort is a TimSort (combination of merge sort and insertion sort, but stable)

def runStudentLambda():
    students = student.prepareTestData()
    student.printResults(students)
    students.sort(key=lambda student: student._id)
    print ("after sorting:" )
    student.printResults(students)
    print ("after reverse sorting:" )
    students.sort(key=lambda student: student._age, reverse=True)
    student.printResults(students)
