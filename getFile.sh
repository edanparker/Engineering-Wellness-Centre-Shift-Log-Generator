#!/usr/bin/env bash

cd "$( dirname "${BASH_SOURCE[0]}" )"

curl -L "https://docs.google.com/spreadsheets/d/e/2PACX-1vTTmsjEUx3A2oV2aFigvCzXOcGRqaTsa8s8yMqW0QRPzKJG-Cw_Hy35nFt_0DcrUwGKWGLDuYuRDUFL/pub?output=csv" > ./test.csv

open test.txt

killall Terminal