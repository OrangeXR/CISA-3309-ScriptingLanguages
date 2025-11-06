# Write a bash script to Read the values for b1, b2, h and L and then calculate 
# and print the volume of the trapezoidal prism to 4 decimal places.
# Here is an example run:
# ================================
# Author: Print Your Name Here
# ================================
# Enter base (b1): 3.4
# Enter base (b2): 6.2
# Enter base (h) : 4.5
# Enter base (L) : 5.5
# Volume of the Trapezoidal Prism = 118.8000 cubic units.
# 
# Author
me="Luis Morales"
echo "================================"
echo "Author: "$me
echo "================================"
# Volume problem
b1=3.4;b2=6.2;h=4.5;L=5.5;
# Concatenate all the statements
echo -n "Volume of the Trapezoidal Prism =  `echo "scale=4;($b1+$b2)*$h*$L*.5" | bc`"; echo -n " cubic units."