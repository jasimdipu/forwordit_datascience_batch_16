from student import Student


class StudentImpl(Student):

    # encapsulation -> private(__), protected(_), public

    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept
        self._sem = "4th"

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name

    def getdept(self):
        return self.__dept

    def setdept(self, dept):
        self.__dept = dept

    def __str__(self):
        return self.__name+" "+self.__dept


student = StudentImpl("Tahir", "CSE")
print(student._sem)
