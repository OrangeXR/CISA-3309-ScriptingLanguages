# Define a variable for the number of students in the class
stuNum=60
# Use this variable to print it on screen with a title
echo "The number of students in the class is: " $stuNum
# Write a bash statement to set a symbolic link named paySalaries to the paySalary.exe file
ln -s processors/salaries/workers/executables/paySalary.exe paySalaries
# 1.Open any editor and create a test.txt file and type in "hello world" in the file and save it.
# 2.Write a bash command to count the number of characters in the test.txt file.
wc -c < test.txt
# 3 Standard streams in Unix/Linux are: stdin, stdout, stderror