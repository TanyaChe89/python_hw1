# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class ParentClass:
    def __init__(self):
        print("Конструктор класса-родителя")

    @abstractmethod
    def count_dresses(self, n):
        pass


class CoatClass(ParentClass):

    def __init__(self):
        super().__init__()

    def count_dresses(self, v):
        result = (v/6.5 + 0.5)
        print(f"Для пошива {v} пальто необходимо ткани = {result}")


class SuitClass(ParentClass):

    def __init__(self):
        super().__init__()

    def count_dresses(self, h):
        result = (2*h + 0.3)
        print(f"Для пошива {h} костюма необходимо ткани = {result}")


if __name__ == '__main__':
    c = CoatClass()
    c.count_dresses(10)

    s = SuitClass()
    s.count_dresses(10)
