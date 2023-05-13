#!/bin/bash

for type in 1 2 3
do
    for opt in O0 O2
    do
        for result in ../dataset/$type/$opt/*.txt
        do  
            rm $result -f
        done
    done
done