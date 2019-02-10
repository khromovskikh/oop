import abc  # библиотека для реализации абстрактных классов


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
        else:
            print("Ошибка в формате записи данных в файле.")


class Parallelepiped(Shape):  # создаем класс параллелепипедов, дочерний классу фигур
    def __init_(self,):
        super().__init__(self)  # Вызываем конструктор базового класса, чтобы получить значение плотности

    def input_shape(self, line, shapes_list):  # Присваиваем значения полям класса
        self.h, self.w, self.l, self.d, self.t = line  # получаем значения переменных из следующей строки
        self.t.strip()
        shapes_list.append(self)

    def output_shape(self, output_stream):  # Вывод значений полей
        output_stream.write(": It's parallelepiped: "
                            "h = " + self.h + ", "
                            "w = " + self.w + ", "
                            "l = " + self.l + ", "
                            "d = " + self.d + ", "
                            "t = " + self.t + "\n")


class Sphere(Shape):  # Создаем класс шара, дочерный классу фигур
    def __init_(self):
        Shape.__init__(self)  # тоже говорим, что есть значение плотности

    def input_shape(self, line, shapes_list):  # Тоже присваиваем значения полям класса
        self.r, self.d, self.t = line  # получаем значения переменных из следующей строки
        self.t.strip()
        shapes_list.append(self)

    def output_shape(self, output_stream):  # Тоже выводим значения полей
        output_stream.write(": It's sphere: "
                            "r = " + self.r + ", "
                            "d = " + self.d + ", "
                            "t = " + self.t + "\n")


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

    def output(self, file_name):
        count = 0  # счетччик для номера фигуры
        output_file = open(file_name, 'w')  # Открываем файл на запись

        # выводим количество фигур в контейнере
        output_file.write("Container's length = " + str(len(self.shapes_list)) + "\n")

        while len(self.shapes_list) != 0:  # если список не пуст, то берем последнюю фигуру из списка и выводим
            shape = self.shapes_list.pop()

            output_file.write(str(count))
            shape.output_shape(output_file)
            count += 1

        output_file.write("\nEmpty container\n"
                          "Container contains " + str(len(self.shapes_list)))
