if [ -z $myf ];then
    myf="/sdcard/zbashfile/"
fi
echo "日历:"
cal
if [ -z $1 ];then
    source $myf/math_s.sh
elif [ "$1"x = "-l"x ];then
    source $myf/math_f.sh
else
    sh $myf/math_s.sh
fi