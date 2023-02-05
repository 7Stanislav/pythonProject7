"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""

class Road:
    __length = 0
    __width = 0
    weight = 0
    thickness = 0

    def mass(self, __length, __width, weight, thickness):
        self.__length = __length
        self.__width = __width
        self.weight = weight
        self.thickness = thickness
        total_mass = __length * __width * weight * thickness
        total_mass_t = total_mass / 1000
        print(f"{__length}м*{__width}м*{weight}кг*{thickness}м = {int(total_mass)} кг = {total_mass_t} т")

a = Road()

__length = int(input("Введите длину в метрах: "))
__width = int(input("Введите ширину в метрах: "))
weight = int(input("Введите массу асфальта в кг: "))
thickness = float(input("Введите толшину асфальта в м: "))
a.mass(__length, __width, weight, thickness)
