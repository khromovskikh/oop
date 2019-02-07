import abc  # библиотека для реализации абстрактных классов


class Shape(abc.ABC):  # создаем класс фигур
    def __init_(self):
        self.density = 0  # у всех фигур будет плотность

    @abc.abstractmethod  # штука, чтобы показать, что метод будет абстрактным (декоратор)
    def output_shape(self, output_stream):
        pass


class Parallelepiped(Shape):  # создаем класс параллелепипедов, дочерний классу фигур
    def __init_(self):
        super().__init__(self)  # Вызываем конструктор базового класса, чтобы получить значение плотности

    def input_shape(self, h, w, l, d):  # Присваиваем значения полям класса
        self.height = h
        self.width = w
        self.length = l
        self.density = d

    def output_shape(self, output_stream):  # Вывод значений полей
        output_stream.write(": It's parallelepiped: "
                            "h = " + self.height + ", "
                            "w = " + self.width + ", "
                            "l = " + self.length + ", "
                            "d = " + self.density + "\n")


class Sphere(Shape):  # Создаем класс шара, дочерный классу фигур
    def __init_(self):
        Shape.__init__(self)  # тоже говорим, что есть значение плотности

    def input_shape(self, r, d):  # Тоже присваиваем значения полям класса
        self.radius = r
        self.density = d

    def output_shape(self, output_stream):  # Тоже выводим значения полей
        output_stream.write(": It's sphere: "
                            "r = " + self.radius + ", "
                            "d = " + self.density + "\n")


class Container:
    def __init__(self):
        self.shapes_list = []

    def input_shapes(self, input_name):  # Вводим фигуры
        try:
            file = open(input_name)

        except OSError:
            return print("Файл с данными не найден.")

        for line in file:
            if int(line) == 1:  # Если 1, то параллелепипед
                h, w, l, d = file.readline().split(" ")  # получаем значения переменных из следующей строки
                tmp_parr = Parallelepiped()  # создаем объект класса
                tmp_parr.input_shape(h, w, l, d.strip())  # делаем отдельный метод, как в методичке
                self.shapes_list.append(tmp_parr)  # добавляем в конец списка наш объект
            elif int(line) == 2:  # если 2, то шар
                r, d = file.readline().split(" ")
                tmp_sphere = Sphere()
                tmp_sphere.input_shape(r, d.strip())
                self.shapes_list.append(tmp_sphere)
            else:
                print("Ошибка в формате записи данных в файле.")

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
