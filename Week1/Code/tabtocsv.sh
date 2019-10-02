#!/bin/bash
# Author: d.smith3@pgr.reading.ac.uk
# Script: tabtocsv.sh
# Desc: Substitute tabs to commas for deliminated files and saves to a csv file
# Arguments: 1 -> tab deliminated file
# Date: Oct 2019

echo "Creating a comma deliminated version of $1 ..."
cat $1 | tr -s "\t" "," >> $1.csv
echo "Done!"

exit