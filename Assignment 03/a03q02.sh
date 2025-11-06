# Use the examples given in class note page 31 and write a script named .myaliases and 
# create aliases for the following bash commands. (Make sure to include the .myaliases file in the zip file) (25%)
# 	echo Working directory is $PWD
# 	cat $0
# 	ls --color=auto
# 	sudo -- sh -c "apt update && apt upgrade"
# 	vnstat -i eth0'
# 	ls -ltr
# 	rm -i
# 	cp -i
# 	df -h
# 	/path/to/script.pl arg1
#
alias wd="echo Working directory is $PWD"
alias ca="cat $0"
alias col="ls --color=auto"
alias sup="sudo -- sh -c "apt update && apt upgrade""
alias vn="vnstat -i eth0"
alias lis="ls -ltr"
alias remo="rm -i"
alias copy="cp -i"
alias space="df -h"
alias scr="/path/to/script.pl arg1"