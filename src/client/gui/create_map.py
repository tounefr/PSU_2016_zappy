#!/usr/bin/python3

from random import *

def create_map(x, y):
    file = open("n2","w")

    L = [1,2]
    i = 0
    while(i < x + 2):
        file.write("e")
        i += 1
    file.write("\n")
    j = 0;
    while (j < y):
        k = 0;
        file.write("e")
        while (k < x):
            rando = choice(L)
            if (rando == 1):
                file.write("0")
            else:
                file.write("m")
            k += 1
        file.write("e")
        file.write("\n")
        j += 1
    i = 0
    while(i < x + 2):
        file.write("e")
        i += 1

create_map(20,10)
