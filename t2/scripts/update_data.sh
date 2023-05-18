#!/bin/bash

count_tests=$1

for type in 1 2 3
do
    for opt in O0 O2 
    do
        app=../apps/app_"$type"_"$opt".exe
        echo STARTED type: $type opt: $opt
        for test in ../tests/*.txt
        do  
            test_n=${test/"../tests/"/}
            test_n=${test_n/".txt"/}
            output=../dataset/$type/$opt/"output_"$test_n.txt

            i=0
            while [ "$i" -lt "$count_tests" ]; do
                $app < "$test" >> $output
                echo >> $output
                i=$((i+1))
            done
        done
        echo ENDED type: $type opt: $opt
    done
done