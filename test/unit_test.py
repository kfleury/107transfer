#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 107transfer_2019
## File description:
## unit_test
##

import unittest

import error
import function


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.var = "USAGE\n" \
                   "\t./107transfer [num den]*\n" \
                   "\nDESCRIPTION\n" \
                   "\tnum\tpolynomial numerator defined by its coefficients\n" \
                   "\tden\tpolynomial denominator defined by its coefficients"
        pass

    def test_usage(self):
        self.assertEqual(self.var, "USAGE\n"
                                   "\t./107transfer [num den]*\n"
                                   "\nDESCRIPTION\n"
                                   "\tnum\tpolynomial numerator defined by its coefficients\n"
                                   "\tden\tpolynomial denominator defined by its coefficients")

    def test_is_float(self):
        self.assertEqual(error.is_float("1.5"), 1)

    def test_is_not_float(self):
        self.assertNotEqual(error.is_float("1.5"), 0)

    def test_nbr_arg(self):
        with self.assertRaises(SystemExit) as cm:
            error.error_nbr_arg(1)
        self.assertEqual(cm.exception.code, 84)

    def test_nbr_arg1(self):
        with self.assertRaises(SystemExit) as cm:
            error.error_nbr_arg(2)
        self.assertEqual(cm.exception.code, 84)

    def test_nbr_arg2(self):
        with self.assertRaises(SystemExit) as cm:
            error.error_nbr_arg(4)
        self.assertEqual(cm.exception.code, 84)

    def test_nbr_arg3(self):
        self.assertEqual(error.error_nbr_arg(3), 0)

    def test_is_number(self):
        with self.assertRaises(SystemExit) as cm:
            error.error_arg(5)
        self.assertEqual(cm.exception.code, 84)

    def test_calc_poly_num(self):
        self.assertEqual(function.calc_poly([[2, 4, 6]], 0.000), [2.0])

    def test_calc_poly_num1(self):
        self.assertEqual(function.calc_poly([[2, 4, 6]], 0.001), [2.004006])

    def test_calc_poly_num2(self):
        self.assertEqual(function.calc_poly([[2, 4, 6]], 0.002), [2.008024])

    def test_calc_poly_num3(self):
        self.assertEqual(function.calc_poly([[2, 4, 6]], 0.003), [2.012054])

    def test_calc_poly_num4(self):
        self.assertEqual(function.calc_poly([[2, 4, 6]], 0.999), [11.984006])

    def test_calc_poly_den(self):
        self.assertEqual(function.calc_poly([[8, 8, 8]], 0.000), [8.0])

    def test_calc_poly_den1(self):
        self.assertEqual(function.calc_poly([[8, 8, 8]], 0.001), [8.008007999999998])

    def test_calc_poly_den2(self):
        self.assertEqual(function.calc_poly([[8, 8, 8]], 0.002), [8.016032])

    def test_calc_poly_den3(self):
        self.assertEqual(function.calc_poly([[8, 8, 8]], 0.003), [8.024071999999999])

    def test_calc_poly_den4(self):
        self.assertEqual(function.calc_poly([[8, 8, 8]], 0.999), [23.976008])


if __name__ == '__main__':
    unittest.main()
