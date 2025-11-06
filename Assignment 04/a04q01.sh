#!/bin/bash
me="Luis Morales"
echo "======================="
echo "Developer: "$me
echo "======================="
#
# Use loops: Write a bash script to produce the output using a step-value-loop: (20%)
# 1, 5, 9, 13, 17, 21, 25
#
# Your output must print the numbers horizontally (1 first and 25 last), comma separated as shown above. 
# Hints: Look at the scaling examples(for precision printing) in page 59 of class note and 
# bash_sec_09_example_7.sh in in page 74 of class note as a guideline. You MUST use a step -value-loop as 
# in the example. Other methods will get only partial credit. (YOU MUST INCLUDE THE SCRIPT FILE (.sh file) IN THE ZIP)
#
#declare -i b
#b=1
#echo -n $b
#echo -n ", "
#b=b+4
#echo -n $b
#echo -n ", "
#b=b+4
#echo -n $b
#echo -n ", "
#b=b+4
#echo -n $b
#echo -n ", "
#b=b+4
#echo -n  $b
#echo -n ", "
#b=b+4
#echo -n  $b
#echo -n ", "
#b=b+4
#echo -n  $b
#
for i in {1..25..4}
  do
   echo -n "$i, "
  done
  