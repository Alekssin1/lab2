class Student:

    def __init__(self, name, surname, record_book_number, *grades):
        if not isinstance(name, str) or not name:
            raise TypeError("Name must be a string!")
        self.__name = name
        if not isinstance(surname, str) or not surname:
            raise TypeError("Surname must be a string!")
        self.__surname = surname
        self.__record_book_number = record_book_number
        for i in grades:
            if not isinstance(i, int) and i <= 0:
                raise TypeError("Grade must be a integer > 0")
        self.__grades = grades
        self.average_score = self.get_average_score(self.grades)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def record_book_number(self):
        return self.__surname

    @property
    def grades(self):
        return self.__grades

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Name must be a string!")
        self.__name = value

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Surname must be a string!")
        self.__surname = value

    @record_book_number.setter
    def record_book_number(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Name must be a string!")
        self.__record_book_number = value

    @grades.setter
    def grades(self, grades):
        for i in grades:
            if not isinstance(i, int) and i <= 0:
                raise TypeError("Grade must be a integer > 0")
            if not isinstance(grades, list):
                raise TypeError("Grades must be a list")
        self.__grades = grades
        self.average_score = self.get_average_score(self.grades)

    @staticmethod
    def get_average_score(grades):
        return sum(grades) / len(grades)

    def __str__(self):
        """Return student data"""
        return '\nStudent data:\nSurname: ' + self.__surname + '\nName: ' + self.__name + '\nRecord book number: ' \
               + self.__record_book_number + '\nGrades: ' + " ".join(map(str, self.__grades)) \
               + '\nAverage score: ' + str(self.average_score) + '\n'


MAX_STUDENTS = 20


class Group:

    def __init__(self, faculty, course, group_name, **students):
        if not isinstance(faculty, str) or not str:
            raise TypeError("Faculty must be a string!")
        self.faculty = faculty
        if not isinstance(course, int) or course < 0:
            raise TypeError("U must enter a integer > 0")
        self.course = course
        if not isinstance(group_name, str) or not str:
            raise TypeError("Faculty must be a string!")
        self.group_name = group_name
        self.students = {}
        self.best5 = {}
        for key in students:
            if not Group.checking_elements(students[key].name, students[key].surname, self.students) and len(
                    self.students) < MAX_STUDENTS:
                self.students[key] = students[key]
        self.best_users()

    @staticmethod
    def checking_elements(name, surname, dictionary):
        """Check that there is no student in the group with the same name and surname"""
        for key, value in dictionary.items():
            if (value.name, value.surname) == (name == surname):
                return True
            return False

    def best_users(self):
        """Sorts students by average score in descending order and records the top 5"""
        for key, student in sorted(self.students.items(), key=lambda x: x[1].average_score, reverse=True)[:5]:
            self.best5[key] = student

    def __str__(self):
        """Return group data, and five best students"""
        return 'Faculty: ' + self.faculty + '\nCourse: ' + str(self.course) + '\nGroup name: ' \
               + self.group_name + '\n' + '\n'.join(list(map(str, list(self.best5.values())))) + '\n'


person1 = Student("Slava", "Moskalenko", "TI-0101", 4, 4, 5, 5, 5)
person2 = Student("Slava", "Moskal", "TI-0103", 2, 4, 3, 4, 5)
person3 = Student("Slava", "Moska", "TI-0104", 5, 5, 4, 2, 5)
person4 = Student("Slava", "Mosk", "TI-0105", 2, 3, 3, 2, 3)
person5 = Student("Slava", "Mos", "TI-0106", 5, 4, 3, 3, 4)
person6 = Student("Slava", "Mo", "TI-0107", 5, 3, 3, 4, 5)
person7 = Student("Slava", "Moskalenko", "TI-0102", 5, 5, 5, 5, 5)
person7.name = "Ivan"
person7.grades = [4, 5, 5, 5, 5]
person8 = Student("Alex", "Moskalenko", "TI-0108", 2, 3, 2, 1, 5)
person9 = Student("Alex", "Moskalenk", "TI-0109", 4, 2, 4, 4, 5)
person10 = Student("Alex", "Moskalen", "TI-0110", 5, 3, 3, 4, 5)
person11 = Student("Alex", "Moskale", "TI-0111", 5, 5, 5, 5, 5)
person12 = Student("Alex", "Moskal", "TI-0112", 4, 3, 4, 4, 5)
person13 = Student("Alex", "Moska", "TI-0113", 4, 4, 5, 2, 5)
person14 = Student("Alex", "Mosk", "TI-0114", 4, 5, 3, 4, 5)
person15 = Student("Alex", "Mos", "TI-0115", 4, 4, 5, 4, 5)
person16 = Student("Anthony", "Moskalenko", "TI-0116", 2, 4, 4, 4, 5)
person17 = Student("Anthony", "Moskalenk", "TI-0117", 3, 4, 4, 4, 5)
person18 = Student("Anthony", "Moskalen", "TI-0118", 4, 4, 4, 4, 5)
person19 = Student("Anthony", "Moskale", "TI-0119", 4, 4, 5, 4, 5)
person20 = Student("Anthony", "Moskal", "TI-0120", 4, 4, 2, 4, 5)
person21 = Student("Anthony", "Moska", "TI-0121", 4, 4, 1, 4, 5)
person22 = Student("Karl", "Firzen", "TI-0122", 3, 3, 5, 4, 2)
group = Group("TEF", 2, "TI-01", first=person1, second=person2, third=person3, fourth=person4, fifth=person5,
              sixth=person6, seventh=person7, eightth=person8, nineth=person9, tenth=person10, eleventh=person11,
              twelweth=person12, thirdteenth=person13, fourteenth=person14, fiveteenth=person15, sixteenth=person16,
              seventeenth=person17, eighteenth=person18, nineteenth=person19, twentyth=person20,
              twentyoneth=person21, twentytwoth=person22)
print(group)
