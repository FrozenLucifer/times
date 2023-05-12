#!/bin/bash

i=1
for sort_c in ../progs/sort*.c
do
    n=${sort_c/"../progs/sort"/}
    n=${n/".c"/}
    gcc ../progs/main_template.c $sort_c -o ../apps/app_$n.exe
    i=$((i+1))
done