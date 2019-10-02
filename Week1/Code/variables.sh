#!/bin/bash

# Author: d.smith3@pgr.reading.ac.uk
# Script: variables.sh
# Desc: Varibale demonstrations
# Arguments: $MyVar $a $b $mysum
# Date: Oct 2019

# Show how variables are used
MyVar='a string'
echo 'the current value of the string is' $MyVar
echo 'Please eneter a new string'
read MyVar 
echo 'This is what the current variable is ...' $MyVar

# Reading multiple variables
echo 'Enter the two numbers sepereated by space(s)'
read a b
echo 'You entered' $a 'and' $b '. Their sum is:'
mysum=`expr $a + $b`
echo $mysum