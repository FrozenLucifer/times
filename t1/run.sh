#!/bin/bash

# gcc *.c -c -std=c99 -Wall -Wfloat-equal -Wfloat-conversion -Wpedantic -Wextra
# gcc *.o -o app.exe -fprofile-arcs -ftest-coverage -lm

gcc task.c -o app.exe
./app.exe

FILES="*.out *.o *.exe *.gcov *.gcno *.gcda"
for file in $FILES
do
	rm "$file" -f
done
