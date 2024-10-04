#!/bin/bash

tabula -b PDFs -f CSV -o TXTs -p all
mv PDFs/*csv CSVs
cp CSVs/*csv Processing
