#!/bin/bash

bash build_apps.sh

# bash clear_data.sh
bash update_data.sh 1

python3 make_preproc.py
python3 make_postproc.py