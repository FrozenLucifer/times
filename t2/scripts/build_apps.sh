#!/bin/bash

for sort_c in ../progs/sort*.c
do
    for opt in O0 O2;
    do
        n=${sort_c/"../progs/sort"/}
        n=${n/".c"/}
        gcc ../progs/main_template.c $sort_c -o ../apps/app_"$n"_$opt.exe
    done
done
