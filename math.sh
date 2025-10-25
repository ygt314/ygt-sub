clear;echo "日历:";cal
if [ -z "$1"x ];then
    bash math_s.sh
elif [ "$1"x = "-l"x ];then
    bash math_f.sh
else
    bash math_s.sh
fi