from csv import reader as csv_reader
from string import ascii_letters
from random import randrange
'''Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. 
Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого 
предмета и по оценкам всех предметов вместе взятых.'''


class Name:
    __CYRILLIC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    __LETTERS = ascii_letters + __CYRILLIC + __CYRILLIC.lower()

    def __init__(self):
        super().__init__()

    def __set_name__(self, owner, name):
        self.inner_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.inner_name)

    def __set__(self, instance, value):
        self.check_name(value)
        setattr(instance, self.inner_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.inner_name}" нельзя удалять')

    def check_name(self, name: str):
        if not name.istitle():
            raise ValueError("Имя не начинается с заглавной буквы")
        for letter in ''.join(name.split()):
            if letter not in self.__LETTERS:
                raise ValueError(f"Недопустимый символ в имени: {letter}")


class Range:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Student:
    full_name = Name()
    input_score = Range(2, 5)
    input_test_results = Range(0, 100)

    def __init__(self, full_name: str, courses_path_csv: str):
        self.full_name = full_name
        self._courses = {}
        with open(courses_path_csv, 'r', encoding='utf-8') as f:
            file = csv_reader(f)
            for line in file:
                self._courses[str(line[0])] = {'Scores': [], 'Test_results': []}

    @property
    def courses(self):
        return self._courses

    def set_score(self, scored_course: str, score: int):
        self.input_score = score
        if scored_course in self._courses.keys():
            self._courses[scored_course]['Scores'].append(self.input_score)

    def set_test_results(self, scored_course: str, test_result: int):
        self.input_test_results = test_result
        if scored_course in self._courses.keys():
            self._courses[scored_course]['Test_results'].append(self.input_test_results)

    def get_average_tests(self, scored_course):
        if scored_course not in self.courses:
            return None
        results = self.courses[scored_course]['Test_results']
        return sum((i/len(results) for i in results))

    def get_average_score(self):
        scores = []
        for course in self.courses:
            scores.extend(self.courses[course]['Scores'])
        return sum((i/len(scores) for i in scores))

    def generate_random_score(self, count: int, ranges: tuple, score_type: str, course=None):
        if score_type == "Scores" and course in self.courses:
            for _ in range(count):
                student.set_score(course, randrange(*ranges))
        if score_type == "Test_results" and course in self.courses:
            for _ in range(count):
                student.set_test_results(course, randrange(*ranges))


if __name__ == "__main__":
    csvfile = "courses_list.csv"
    student = Student("Иван Иванович Иванов", csvfile)
    student.generate_random_score(10, (2, 5), "Scores", "Python")
    student.generate_random_score(10, (2, 5), "Scores", "HTML")
    student.generate_random_score(10, (0, 100), "Test_results", "Python")
    for course in student.courses:
        print(course, student.courses[course])
    print(f'{student.get_average_tests("Python"):.2f}')
    print(f'{student.get_average_score():.2f}')
