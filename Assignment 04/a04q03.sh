#!/bin/bash
me="Luis Morales"
echo "======================="
echo "Developer: "$me
echo "======================="
#
#
#
# Here are the criteria……

# b. Pay is calculated based on a ‘category’ of the employee. There are three categories and each category has a pay rate, and they are
# Casual[C]: rate = $8.25/hr
# Permanent[P]: rate = $12.50/hr
# Staff[S]: rate = $20.00/hr
# Hourly Rates:
cRate=8.25
pRate=12.50
sRate=20.00


 while :
  do
   echo "ABC Enterprises – Weekly Pay Calculation Process"
   read -p "Enter Employee Category (C,P, or S. 0 to quit): " eCat

#  c. User enters the category of the employee (C, P or S) and then the Hours/week (do not worry about overtime hours etc. Consider all 
#  hours [Regular and Overtime] get the same pay rate). PS: If the user enters an unknown option, show an error message (Look at the screen dump below)
   case $eCat in
       C|c)
	    rate=$cRate
		read -p "Enter hours worked: " hours
        echo "Calculated Weekly Pay @$rate/hr = $`echo "scale=2;$rate*$hours" | bc`"
		;;
	   P|p)
	    rate=$pRate
		read -p "Enter hours worked: " hours
        echo "Calculated Weekly Pay @$rate/hr = $`echo "scale=2;$rate*$hours" | bc`"
		;;
	   S|s)
	    rate=$sRate
		read -p "Enter hours worked: " hours
        echo "Calculated Weekly Pay @$rate/hr = $`echo "scale=2;$rate*$hours" | bc`"
		;;
# a. The script MUST CONTINUE in a loop until user decides to stop. User stops the pay calculations by entering 0.
	   0)
	     echo ""
		 echo "Thank you, Bye!"
		 break
		 ;;
	   *)
		echo "Sorry, unknown option entered" 
   esac
   echo ""
   echo ""
#         d. Script must run a menu as follows
#         ABC Enterprises – Weekly Pay Calculation Process
#         Enter Employee Category (C, P or S. 0 to quit):
#         Enter hours worked:
#         Script must produce the calculated result as:
#         Calculated Weekly Pay @rate/hr = $ 99999.99
   done
