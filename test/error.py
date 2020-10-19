#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 107transfer
## File description:
## maths python
##
import sys


def usage():
    print("USAGE")
    print("\t./107transfer [num den]*")
    print("\nDESCRIPTION")
    print("\tnum\tpolynomial numerator defined by its coefficients")
    print("\tden\tpolynomial denominator defined by its coefficients")


def is_float(string):
    try:
        float(string)
        return 1
    except ValueError:
        return 0


def error_arg(ac):
    for i in range(1, ac):
        if not sys.argv[i].isdigit():
            if is_float(sys.argv[i]) == 0:
                print("Error : '" + sys.argv[i] + "' is not a number")
                sys.exit(84)


def error_nbr_arg(ac):
    if ac == 1:
        sys.stderr.write("This program needs arguments\n")
        sys.exit(84)
    if (ac - 1) % 2 != 0:
        sys.stderr.write("The number of arg must be peer\n")
        sys.exit(84)
    return 0


def all_error(ac):
    error_nbr_arg(ac)
    error_arg(ac)
