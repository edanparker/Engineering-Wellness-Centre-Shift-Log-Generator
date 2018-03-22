#!/usr/bin/env bash

cd "$( dirname "${BASH_SOURCE[0]}" )"

curl -L "https://docs.google.com/spreadsheets/d/e/2PACX-1vRCnr0DlcJGfauyvRQcWqod0NbchoAv5C1j9eaYVe4QG8PONIy4NCA4igvurbIdfppw1wAHZSmtcGjE/pub?output=csv" >EWCdata_DO_NOT_MODIFY.csv

open EWCdata_DO_NOT_MODIFY.txt

killall Terminal
