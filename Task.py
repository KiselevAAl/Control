class Persona():

    def __init__(self, surname, date, faculty):
        self.surname = surname
        self.date = date
        self.faculty = faculty

    @classmethod
    def print_info(self):
        print('Информация о персоне: ')


class Enrollee(Persona):
    def __init__(self, surname, date, faculty):
        super().__init__(surname, date, faculty)

    def print_info(self):
        return ('Фамилия: {}\nДата рождения: {}\nФакультет: {}'.
                format(self.surname, self.date, self.faculty))

class Student(Persona):
    def __init__(self, surname, date, faculty, curs):
        super().__init__(surname, date, faculty, curs)

    def print_info2(self):
        return ('Фамилия: {}\nДата рождения: {}\nФакультет: {}\nКурс: {}'.
                format(self.surname, self.date, self.faculty, self.curs))

class Teacher(Persona):
    def __init__(self, surname, date, faculty, curs,post, experience,):
        super().__init__(surname, date, faculty, curs)
        self.post = post
        self.experience = experience

    def print_info3(self):
        return ('Фамилия: {}\nДата рождения: {}\nФакультет: {}\nДолжность: {}\nСтаж: {}'.
                format(self.surname, self.date, self.faculty, self.post, self.experience))


persona1 = Persona('Киселёва', 28.03, 'Факультет информатики')
persona1.print_info(Enrollee('Кобыличенко', 29.02, 'Факультет искусст', ))
persona1.print_info2(Student('Мвуратова', 01.02, 'Факультет информатики', ))
persona1.print_info3(Teacher('Задирей', 29.05, 'Факультет информатики', ))

