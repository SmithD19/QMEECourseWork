#!/bin/bash

#!/bin/bash
# Author: d.smith3@pgr.reading.ac.uk
# Script: tiff2png
# Desc: Convert tiff images to png
# Arguments: $f
# Date: Oct 2019

for f in *.tif
    do 
        echo "Converting $f";
        convert "$f" "$(basename "$f" .tif).png";
    done