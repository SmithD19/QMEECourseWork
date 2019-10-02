#!/bin/bash
# Author: d.smith3@pgr.reading.ac.uk
# Script: CountLines.sh
# Desc: Count lines in a file!
# Arguments: $NumLines $1
# Date: Oct 2019

NumLines=`wc -l < $1`
echo "The file $1 has $NumLines lines"
echo