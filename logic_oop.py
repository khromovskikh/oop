import abc  # библиотека для реализации абстрактных классов

import math


class Shape:  # создаем класс фигур
    shapes_list = []

    def __init_(self):
        self.density = 0  # у всех фигур будет плотность
        self.temperature = 0

    @abc.abstractmethod  # штука, чтобы показать, что метод будет абстрактным (декоратор)
    def output_shape(self, output_stream):
        pass

    def input_shape(self, shapes_list, shape_type, shape_params):
        if int(shape_type) == 1:  # Если 1, то параллелепипед
            parr = Parallelepiped()  # создаем объект класса
            parr.input_shape(shape_params, shapes_list)
        elif int(shape_type) == 2:  # если 2, то шар
            sphere = Sphere()
            sphere.input_shape(shape_params, shapes_list)
        elif int(shape_type) == 3:  # если 3, то тетраэдер
            tetrahedron = Tetrahedron()
            tetrahedron.input_shape(shape_params, shapes_list)
        else:
            print("Ошибка в формате записи данных в файле.")

    @abc.abstractmethod
    def square(self, shape):
        pass

    def compare(self, shape0, shape1):
        return shape0.square() < shape1.square()

    def output_sphere(self, output_stream):
        output_stream.write("\n")


class Parallelepiped(Shape):  # создаем класс параллелепипедов, дочерний классу фигур
    def __init_(self,):
        super().__init__(self)  # Вызываем конструктор базового класса, чтобы получить значение плотности

    def input_shape(self, line, shapes_list):  # Присваиваем значения полям класса
        self.h, self.w, self.l, self.d, self.t = line  # получаем значения переменных из следующей строки
        if self.h.isdigit or (int(self.h) <= 0):

            print("Введены неверные параметры параллелепипеда.")
            quit()

        if self.w.isdigit or (int(self.w) <= 0):
            print("Введены неверные параметры параллелепипеда.")
            quit()

        if self.d.isdigit or (int(self.d) <= 0):
            print("Введены неверные параметры параллелепипеда.")
            quit()

        if self.t.isdigit or (int(self.t) <= 0):
            print("Введены неверные параметры параллелепипеда.")
            quit()

        self.t.strip()
        shapes_list.append(self)

    def output_shape(self, output_stream):  # Вывод значений полей
        output_stream.write(": It's parallelepiped: "
                            "h = " + self.h + ", "
                            "w = " + self.w + ", "
                            "l = " + self.l + ", "
                            "d = " + self.d.strip() + ", "
                            "t = " + self.t.strip())

    def square(self):
        return (int(self.w)*int(self.l) + int(self.l)*int(self.h) + int(self.w)*int(self.h))*2


class Sphere(Shape):  # Создаем класс шара, дочерный классу фигур
    def __init_(self):
        Shape.__init__(self)  # тоже говорим, что есть значение плотности

    def input_shape(self, line, shapes_list):  # Тоже присваиваем значения полям класса
        self.r, self.d, self.t = line  # получаем значения переменных из следующей строки

        if self.r.isdigit or (int(self.r) <= 0):
            print("Введены неверные параметры сферы.")
            quit()

        if self.d.isdigit or (int(self.d) <= 0):
            print("Введены неверные параметры сферы.")
            quit()

        if self.t.isdigit or (int(self.t) <= 0):
            print("Введены неверные параметры сферы.")
            quit()

        self.t.strip()
        shapes_list.append(self)

    def output_shape(self, output_stream):  # Тоже выводим значения полей
        output_stream.write(": It's sphere: "
                            "r = " + self.r + ", "
                            "d = " + self.d.strip() + ", "
                            "t = " + self.t.strip())

    def square(self):
        return 3.1415*4*int(self.r)*int(self.r)

    def output_sphere(self, output_stream):
        self.output_shape(output_stream)
        output_stream.write(" | square: " + str(self.square()) + "\n")


class Tetrahedron(Shape):
    def __init_(self):
        Shape.__init__(self)  # тоже говорим, что есть значение плотности

    def input_shape(self, line, shapes_list):  # Тоже присваиваем значения полям класса
        self.a, self.d, self.t = line  # получаем значения переменных из следующей строки

        if self.a.isdigit or (int(self.a) <= 0):
            print("Введены неверные параметры тетраэдра.")
            quit()

        if self.d.isdigit or (int(self.d) <= 0):
            print("Введены неверные параметры тетраэдра.")
            quit()

        if self.t.isdigit or (int(self.t) <= 0):
            print("Введены неверные параметры тетраэдра.")
            quit()

        self.d.strip()
        shapes_list.append(self)

    def output_shape(self, output_stream):  # Тоже выводим значения полей
        output_stream.write(": It's tetrahedron: "
                            "a = " + self.a + ", "
                            "d = " + self.d.strip() + ", "
                            "t = " + self.t.strip())

    def square(self):
        return math.sqrt(3)*int(self.a)


class Container:
    def __init__(self):
        self.shapes_list = []

    def input_shapes(self, input_name):  # Вводим фигуры
        try:
            file = open(input_name)

        except OSError:
            return print("Файл с данными не найден.")

        shape = Shape()
        for line in file:
            shape.input_shape(self.shapes_list, line, file.readline().split(" "))

    def output(self, file_name, filter=False):
        count = 0  # счетччик для номера фигуры
        output_file = open(file_name, 'a')  # Открываем файл на запись

        # выводим количество фигур в контейнере
        output_file.write("Container's length = " + str(len(self.shapes_list)) + "\n")

        while len(self.shapes_list) != 0:  # если список не пуст, то берем последнюю фигуру из списка и выводим
            shape = self.shapes_list.pop()
            output_file.write(str(count))
            if filter:
                shape.output_sphere(output_file)
            else:
                shape.output_shape(output_file)
                output_file.write(" | square: " + str(shape.square()) + "\n")
            count += 1

        output_file.write("\nEmpty container\n"
                          "Container contains " + str(len(self.shapes_list)) + "\n\n")

    def sort(self):
        self.shapes_list.reverse()
        n = len(self.shapes_list)

        for i in range(n):
            for j in range(0, n - i - 1):
                s = Shape()
                if s.compare(self.shapes_list[j], self.shapes_list[j + 1]):
                    self.shapes_list[j], self.shapes_list[j + 1] = self.shapes_list[j + 1], self.shapes_list[j]

    def clear_file(self):
        output_file = open("output_oop.txt", 'w')
        output_file.seek(0)
        output_file.truncate()
