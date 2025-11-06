# - a greeting to the user by (user) name, (Such as Good Morning rainyday)
echo "Hello, " $(whoami)
# - prints the current date, and
echo "Today's date is: " $(date)
# - prints a list of users currently running processors on your computer (use ps command)
$'ps'