#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 107transfer
## File description:
## maths python
##
import sys


def usage():
    var = "USAGE\n" \
          "\t./107transfer [num den]*\n" \
          "\nDESCRIPTION\n" \
          "\tnum\tpolynomial numerator defined by its coefficients\n" \
          "\tden\tpolynomial denominator defined by its coefficients"
    print(var)
    return 0


def is_float(string):
    try:
        float(string)
        return 1
    except ValueError:
        return 0


def error_arg(tab):
    for i in range(0, len(tab)):
        if not tab[i].isdigit():
            if is_float(tab[i]) == 0:
                print("Error : '" + tab[i] + "' is not a valid argument")
                sys.exit(84)
    return 0


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
    return 0
