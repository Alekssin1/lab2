class Student:

    def __init__(self, name, surname, record_book_number, *grades):
        self.name = name
        self.surname = surname
        self.record_book_number = record_book_number
        for i in grades:
            if not isinstance(i, int):
                raise TypeError("Grade must be a integer > 0")
        self.grades = grades
        self.average_score = sum(self.grades) / len(self.grades)

    def __str__(self):
        return '\nStudent data:\nSurname: ' + self.surname + '\nName: ' + self.name + '\nRecord book number: ' \
               + self.record_book_number + '\nGrades: ' + " ".join(map(str, self.grades)) \
               + '\nAverage score: ' + str(self.average_score) + '\n'


class Group:

    def __init__(self, faculty, course, group_name, **students):
        self.faculty = faculty
        if not isinstance(course, int) or course < 0:
            raise TypeError("U must enter a integer > 0")
        self.course = course
        self.group_name = group_name
        self.students = {}
        self.best5 = {}
        for key in students:
            if not Group.checking_elements(students[key].name, students[key].surname, self.students) and len(
                    self.students) < 20:
                self.students[key] = students[key]
        self.best_users()

    @staticmethod
    def checking_elements(name, surname, dictionary):
        for key, value in dictionary.items():
            if value.name == name and value.surname == surname:
                return True
            return False

    def best_users(self):
        for key, student in sorted(self.students.items(), key=lambda x: x[1].average_score, reverse=True)[:5]:
            self.best5[key] = student

    def __str__(self):
        return 'Faculty: ' + self.faculty + '\nCourse: ' + str(self.course) + '\nGroup name: ' \
               + self.group_name + '\n' + '\n'.join(list(map(str, list(self.best5.values())))) + '\n'


person1 = Student("Slava", "Moskalenko", "TI-0101", 1, 4, 4, 4, 5)
person2 = Student("Slava", "Moskalenko", "TI-0102", 5, 5, 5, 5, 5)
person3 = Student("Slava", "Moskal", "TI-0103", 2, 4, 3, 4, 5)
person4 = Student("Slava", "Moska", "TI-0104", 5, 5, 4, 2, 5)
person5 = Student("Slava", "Mosk", "TI-0105", 2, 3, 3, 2, 3)
person6 = Student("Slava", "Mos", "TI-0106", 5, 4, 3, 3, 4)
person7 = Student("Slava", "Mo", "TI-0107", 5, 3, 3, 4, 5)
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
