class Student:
    language = "Russian"
    publisher = "Lama"
    tip = "Студент"
    universitet = "ПГУ"

    def __init__(self, imya, familiya, vozrast, kurs, sredniy_ball):
        self.imya = imya
        self.familiya = familiya
        self.vozrast = vozrast
        self.kurs = kurs
        self.sredniy_ball = sredniy_ball
        self._propuski = 0
    def __str__(self):
        return f"Студент {self.imya} {self.familiya}, {self.kurs} курс"
    def __len__(self):
        return self.kurs

    def pozdravit(self):

        return f"Привет, я {self.imya}!"

    def poluchit_dvoyku(self):
        self.sredniy_ball = self.sredniy_ball - 0.5
        if self.sredniy_ball < 2:
            self.sredniy_ball = 2
        return f"Ой, теперь средний балл {self.sredniy_ball}"

    def progulivat(self, skolko):
        self._propuski = self._propuski + skolko
        return f"Прогулял {skolko} пар. Всего пропусков: {self._propuski}"

    def perevesti_na_kurs(self, noviy_kurs):
        if noviy_kurs > 0 and noviy_kurs <= 6:
            self.kurs = noviy_kurs
            return f"Теперь на {self.kurs} курсе"
        else:
            return "Такого курса нет"

    def pokazat_propuski(self):
        return self._propuski

student1 = Student("Иван", "Петров", 19, 2, 4.5)
student2 = Student("Мария", "Иванова", 20, 3, 4.8)
student3 = Student("Алексей", "Сидоров", 18, 1, 3.9)

print("=== НАШИ СТУДЕНТЫ ===")
print(student1)
print(student2)
print(student3)

print("\n=== ПРИВЕТСТВИЯ ===")
print(student1.pozdravit())
print(student2.pozdravit())

print("\n=== ПРО КУРСЫ ===")
print(f"{student1.imya} учится на {len(student1)} курсе")
print(student2.perevesti_na_kurs(4))

print("\n=== ПРО ОЦЕНКИ ===")
print(f"У {student3.imya} балл: {student3.sredniy_ball}")
print(student3.poluchit_dvoyku())
print(f"Теперь балл: {student3.sredniy_ball}")

print("\n=== ПРО ПРОГУЛЫ ===")
print(student1.progulivat(2))
print(student1.progulivat(1))
print(f"Всего пропусков: {student1.pokazat_propuski()}")

print("\n=== АТРИБУТЫ КЛАССА ===")
print(f"Тип: {Student.tip}")
print(f"Все учатся в: {Student.universitet}")