#!/bin/bash
# Author: d.smith3@pgr.reading.ac.uk
# Script: ConcatenteTwoFiles.sh
# Desc: Merge Files
# Arguments: $1 $2 $3
# Date: Oct 2019

cat $1 > $3
cat $2 >> $3
echo "Merged files is"
cat $3