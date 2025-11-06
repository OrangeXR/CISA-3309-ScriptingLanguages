#!/bin/bash
#
echo "Enter Users Full Name: "
read uName
IFS=' '
read -a strarr <<< "$uName"

echo "==================="
echo "User name: "${strarr[0]}" "${strarr[1]} 
echo "==================="



if [ ! -f ./test_users/${strarr[0]}"_"${strarr[1]}.usr ]
then
	echo "file: ${strarr[0]}"_"${strarr[1]} does not exist"
else
	more ./test_users/${strarr[0]}"_"${strarr[1]}.usr
fi 
