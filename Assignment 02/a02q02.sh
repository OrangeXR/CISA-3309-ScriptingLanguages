#!/bin/bash
#
echo "Enter Users Full Name: <Enter a first name B last name; alpha and space only>"
read uName
IFS=' '
read -a strarr <<< "$uName"
echo "Enter Users ID: <Enter a 6 digit number; digits only>"
read userID 
echo "Enter Users Job Location: <Enter 4 characters>"
read jobLocal
echo "Enter Users Manager Code: <Enter a 6 digit number; digits only>"
read manCode
echo " "
echo " "
echo "==================="
echo "User name: "${strarr[0]}" "${strarr[1]} 
echo "User ID: "$userID
echo "Job Location "$jobLocal
echo "Manager Code: "$manCode
echo "==================="

echo "Name: ""$uName ", "User ID: ""$userID", "Job Location: ""$jobLocal", "Manager Code: ""$manCode" >> test_users/${strarr[0]}"_"${strarr[1]}".usr"