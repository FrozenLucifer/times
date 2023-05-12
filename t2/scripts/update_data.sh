#!/bin/bash

count_tests=1000

for app in ../apps/app*.exe
do
    app_n=${app/"../apps/app_"/}
    app_n=${app_n/".exe"/}
    for test in ../tests/*.txt
    do  
        test_n=${test/"../tests/"/}
        test_n=${test_n/".txt"/}

        output=../dataset/$app_n/"output_"$test_n.txt

        i=0
        while [ "$i" -lt "$count_tests" ]; do
            ../apps/app_1.exe < "$test" >> $output
            echo >> $output
            i=$((i+1))
        done

    done
done