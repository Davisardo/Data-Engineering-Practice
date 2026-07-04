# import unittest

# from mymodule import square, double


# class TestSquare(unittest.TestCase):
#     """Uji fungsi square()."""

#     def test1(self):
#         self.assertEqual(square(2), 4)          # 2 kuadrat = 4
#         self.assertEqual(square(3.0), 9.0)      # 3.0 kuadrat = 9.0
#         self.assertNotEqual(square(-3), -9)     # kuadrat tidak boleh negatif


# class TestDouble(unittest.TestCase):
#     """Uji fungsi double()."""

#     def test1(self):
#         self.assertEqual(double(2), 4)          # 2 kali 2 = 4
#         self.assertEqual(double(-3.1), -6.2)    # -3.1 kali 2 = -6.2
#         self.assertEqual(double(0), 0)          # kasus batas: nol


# unittest.main()

import unittest

from mymodule import add


class TestAdd(unittest.TestCase):
    """Uji fungsi add()."""

    def test1(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.3, 3.6), 5.9)
        self.assertEqual(add('hello', 'world'), 'helloworld')
        self.assertEqual(add(2.3000, 4.300), 6.6)
        self.assertNotEqual(add(-2, -2), 0)


unittest.main()