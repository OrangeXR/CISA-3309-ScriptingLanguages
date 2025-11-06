#!/bin/bash
# Define the list of eligible languages
declare -a languages=("English" "Spanish" "Chinese" "Italian" "Hindi")

while :
  do
   me="Luis Morales"
   echo "======================="
   echo "Developer: "$me
   echo "======================="
   echo "See what language courses you may take"
   read -p "Enter student's First Language(Enter: English, Spanish, Chinese, Italian, Hindi, or 0 to exit): " uLang
   
   case $uLang in
       English|Spanish|Chinese|Italian|Hindi)
	    echo ""
		echo "Your first language: $uLang"
		echo "You may take any two of the following courses:"
        printf '%s\n' ${languages[@]/$uLang/ }
		;;
	   0)
	     echo ""
		 echo "Thank you, Bye!"
		 break
		 ;;
	   *)
		echo "Please enter a valid language." 
   esac
   
   echo ""
   echo ""
   done
