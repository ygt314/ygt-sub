clear;echo "日历:"
cal
if [ -z "$1"x ];then
    chmod 777 math_s.sh
    ~/math_s.sh
elif [ "$1"x = "-l"x ];then
    source ~/mathrc/cnmtrc
    cnmt_d
    chmod 777 math_f.sh
    ~/math_f.sh
else
    chmod 777 math_s.sh
    ~/math_s.sh
fi