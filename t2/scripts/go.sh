#!/bin/bash

methods="a[i] *(a+i) ptr"
opts="O0 O2"
sizes="1 $(seq 250 250 10000)"
arrays="sorted unsorted"
count_tests=100

# bash build_apps.sh "$methods" "$opts" "$sizes"

# bash update_data.sh "$methods" "$opts" "$arrays" "$sizes" "$count_tests"

# python3 make_preproc.py "$methods" "$opts" "$arrays" "$sizes"

python3 make_postproc.py "$methods" "$opts" "$arrays" "$sizes"