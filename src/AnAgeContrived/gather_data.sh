#!/usr/bin/env bash

{ time python main.py --training-num 80 --test-num 80 --n-step 40 ; } 2> temp
echo "Training Num: 60 Test Num: 60" >> output.txt
(cat temp | grep real) >> output.txt
(cat temp | grep user) >> output.txt
(cat temp | grep sys) >> output.txt

{ time python main.py --training-num 60 --test-num 60 --n-step 40 ; } 2> temp
echo "Training Num: 60 Test Num: 60" >> output.txt
(cat temp | grep real) >> output.txt
(cat temp | grep user) >> output.txt
(cat temp | grep sys) >> output.txt

rm temp