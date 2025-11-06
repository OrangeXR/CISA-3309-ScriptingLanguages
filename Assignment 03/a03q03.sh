a=5;b=19;d=35;e=150.55;
echo "scale=4;$a/$b" | bc
echo "scale=3;$a/$d*19" | bc
echo "scale=2;($e-$d)*(7/9)" | bc
echo "scale=3;($e/$d)*0.5" | bc
echo "scale=5;($b/$d)*($e/$d)+0.5" | bc