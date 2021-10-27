class Student:

    def __init__(self, name, surname, record_book_number, *grades):
        self.name = name
        self.surname = surname
        self.record_book_number = record_book_number
        self.grades = grades
        self.average_score = self.get_average_score(self.grades)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Name must be a string!")
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Surname must be a string!")
        self.__surname = value

    @property
    def record_book_number(self):
        return self.__surname

    @record_book_number.setter
    def record_book_number(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Record book number must be a string!")
        self.__record_book_number = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        for i in grades:
            if not isinstance(i, int) and i <= 0:
                raise TypeError("Grade must be a integer > 0")
        if not isinstance(grades, tuple):
            raise TypeError("Grades must be a list")
        self.__grades = grades
        self.average_score = self.get_average_score(self.grades)

    @staticmethod
    def get_average_score(grades):
        return sum(grades) / len(grades)

    def __str__(self):
        """Return student data"""
        return '\nStudent data:\nSurname: ' + self.surname + '\nName: ' + self.name + '\nRecord book number: ' \
               + self.record_book_number + '\nGrades: ' + " ".join(map(str, self.grades)) \
               + '\nAverage score: ' + str(self.average_score) + '\n'


MAX_STUDENTS = 20


class Group:

    def __init__(self, faculty, course, group_name, **students):
        self.faculty = faculty
        self.course = course
        self.group_name = group_name
        self.students = students
        self.best_users = self.students

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Faculty must be a string!")
        self.__faculty = value

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError("U must enter a integer > 0")
        self.__course = value

    @property
    def group_name(self):
        return self.__group_name

    @group_name.setter
    def group_name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Group name must be a string!")
        self.__group_name = value

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        self.__students = {}
        if not isinstance(value, dict) or not value:
            raise TypeError("Group name must be a string!")
        for key in value:
            if not Group.checking_elements(value[key].name, value[key].surname, self.__students) and len(
                    self.__students) < MAX_STUDENTS:
                self.__students[key] = value[key]

    @property
    def best_users(self):
        """Sorts students by average score in descending order and records the top 5"""
        return self.__best_users

    @best_users.setter
    def best_users(self, dictionary):
        self.__best_users = {}
        for key, dictionary in sorted(dictionary.items(), key=lambda x: x[1].average_score, reverse=True)[:5]:
            self.__best_users[key] = dictionary

    @staticmethod
    def checking_elements(name, surname, dictionary):
        """Check that there is no student in the group with the same name and surname"""
        for key, value in dictionary.items():
            if (value.name, value.surname) == (name, surname):
                return True
        return False

    def __str__(self):
        """Return group data, and five best students"""
        return 'Faculty: ' + self.faculty + '\nCourse: ' + str(self.course) + '\nGroup name: ' \
               + self.group_name + '\n' + '\n'.join(list(map(str, list(self.best_users.values())))) + '\n'


person1 = Student("Slava", "Moskalenko", "TI-0101", 4, 4, 5, 5, 5)
person2 = Student("Slava", "Moskal", "TI-0103", 2, 4, 3, 4, 5)
person3 = Student("Slava", "Moska", "TI-0104", 5, 5, 4, 2, 5)
person4 = Student("Slava", "Mosk", "TI-0105", 2, 3, 3, 2, 3)
person5 = Student("Slava", "Mos", "TI-0106", 5, 4, 3, 3, 4)
person6 = Student("Slava", "Mo", "TI-0107", 5, 3, 3, 4, 5)
person7 = Student("Slava", "Moskalenko", "TI-0102", 5, 5, 5, 5, 5)
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
