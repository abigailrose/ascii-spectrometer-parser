#!/usr/bin/env python3

import csv;

filename = input("enter filename to be parsed: ")

with open(filename) as file:
    new_filename = filename[:-3]
    new_filename += "csv"
    outfile = open("parsed-" + new_filename, 'a')
    line = file.readline()
    while(line):
        if any(c.isalpha() for c in line):
            line = file.readline()
            continue
        if line == "\n":
            line = file.readline()
            continue
        else:
            first, second = line.split()
            outfile.write(first)
            outfile.write(',')
            outfile.write(second)
            outfile.write("\n")
            line = file.readline()
            
    outfile.close()
            
    