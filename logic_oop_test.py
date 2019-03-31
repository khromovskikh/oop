import unittest
import logic_oop


class TestConstructor(unittest.TestCase):
    def test_input_shapes(self):
        c = logic_oop.Container()
        s = logic_oop.Sphere()
        s.r = '2'; s.d = '2'; s.t='2';
        t = logic_oop.Tetrahedron()
        t.a = '3'; t.d = '3'; t.t = '3';
        p = logic_oop.Parallelepiped()
        p.h = '1'; p.w = '1'; p.l = '1'; p.d = '1'; p.t = '1'

        shapes_list = [p, s, t]

        # self.assertEqual(c.input_shapes("input_oop.txt"), shapes_list)


class TestSphere(unittest.TestCase):

    def test_square(self):
        sphere = logic_oop.Sphere()
        sphere.r = 5
        sphere.d = 10
        sphere.t = 300

        self.assertEqual(sphere.square(),523.5833333333334)

class TestParrallelepiped(unittest.TestCase):

    def test_square(self):
        parr = logic_oop.Parallelepiped()
        parr.h = 2
        parr.w =4
        parr.l = 6
        parr.d = 8
        parr.t = 10

        self.assertEqual(parr.square(), 88)


class TestTetrahedron(unittest.TestCase):
    def test_square(self):
        tetr = logic_oop.Tetrahedron()
        tetr.a = 4
        tetr.d = 7
        tetr.t = 9

        self.assertEqual(tetr.square(), 6.928203230275509)


class TestContainer(unittest.TestCase):
    def setUp(self):
        input_name = "input_oop.txt"
        output_name = "output_oop.txt"
        self.c = logic_oop.Container()
        self.c.clear_file()
        self.c.input_shapes(input_name)
        self.c.output(output_name)
        self.c.input_shapes(input_name)
        self.c.sort()
        self.c.output(output_name)
        self.c.input_shapes(input_name)
        self.c.sort()
        self.c.output(output_name, True)

    def test_output(self):
        with open("output_oop.txt") as output_file:
            with open("output_oop_gold.txt") as output_file_gold:
                output = output_file.read()
                output_gold = output_file_gold.read()

                self.assertEqual(output, output_gold)
        output_file_gold.close()
        output_file.close()

    def test_clear(self):
        self.c.clear_file()

        with open("output_oop.txt") as output_file:
            with open("output_oop_gold_clear.txt") as output_file_gold:
                output = output_file.read()
                output_gold = output_file_gold.read()

                self.assertEqual(output, output_gold)

        output_file_gold.close()
        output_file.close()

    def test_sort(self):
        n = len(self.c.shapes_list)
        gold = [5.196152422706632, 6, 33.50933333333334]

        for i in range(n):
            self.assertEqual(self.c.shapes_list[i].square, gold[i])

if __name__ == '__main__':
    unittest.main()