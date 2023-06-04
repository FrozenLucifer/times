#!/bin/bash

methods=$1
opts=$2
sizes=$3

echo BUILDING STARTED...
for method in $methods; do
    for opt in $opts; do
        for size in $sizes; do
            echo -n -e "\e[Kbuilding app_"$method"_"$opt"_"$size".exe\r"
            gcc ../progs/main_template.c ../progs/sort_$method.c -o ../apps/app_"$method"_"$opt"_"unsorted"_"$size".exe -"$opt" -DN_MAX=$size -DSORTED=0
            gcc ../progs/main_template.c ../progs/sort_$method.c -o ../apps/app_"$method"_"$opt"_"sorted"_"$size".exe -"$opt" -DN_MAX=$size -DSORTED=1
        done
    done
done
echo -e "\e[KBUILDING SUCCES"
