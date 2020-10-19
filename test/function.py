#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 107transfer
## File description:
## maths python
##

import sys

import error


def func_in_tab(a):
    tab = []
    j = 0
    for i in range(a, len(sys.argv), 2):
        num = sys.argv[i]
        num = num.split('*')
        error.error_arg(num)
        for a in range(0, len(num)):
            num[a] = int(num[a])
        tab.insert(j, num)
        j += 1
    return tab


def calc_poly(list, incr):
    nume = []
    tab = []
    for r in range(0, len(list)):
        cpy = []
        for c in range(0, len(list[r])):
            cpy.append(list[r][c] * (incr ** c))
        tab.insert(r, cpy)
    for r in range(0, len(tab)):
        x = 0
        for c in range(0, len(tab[r])):
            x += tab[r][c]
        if len(tab[r]) == 1:
            nume.append(tab[r][0])
        else:
            nume.append(x)
    return nume


def func_calc(num, den):
    incr = 0.000
    while incr <= 1.001:
        nume = calc_poly(num, incr)
        deno = calc_poly(den, incr)
        if len(nume) >= 2:
            for z in range(0, len(nume) - 1):
                if deno[z] == 0:
                    sys.stderr.write("Division by 0\n")
                    sys.exit(84)
                x = (float(nume[z]) / float(deno[z])) * (float(nume[z + 1]) / float(deno[z + 1]))
        else:
            if deno[0] == 0:
                sys.stderr.write("Division by 0\n")
                sys.exit(84)
            x = float(nume[0]) / float(deno[0])
        print("%.3f -> " % incr, end='')
        print("%.5f" % x)
        incr += 0.001
    return 0
