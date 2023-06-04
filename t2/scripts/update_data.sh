#!/bin/bash

methods=$1
opts=$2
arrays=$3
sizes=$4
count_tests=$5

echo TESTING STARTED...
for method in $methods; do
    for opt in $opts; do
        for array in $arrays; do
            for size in $sizes; do
                app=app_"$method"_"$opt"_"$array"_"$size".exe
                output=../dataset/"$method"_"$opt"_"$array"_"$size".txt
                i=0
                while [ "$i" -lt "$count_tests" ]; do
                    echo -n -e "\e[Ktesting $app $i/$count_tests\r"
                    ../apps/"$app" >> $output
                    echo >> $output
                    i=$((i+1))
                done
            done
        done
    done
done
echo -e "\e[KTESTING SUCCES"  