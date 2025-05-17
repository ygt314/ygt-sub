a=0;b=0;c=0
if [ -z $myf ];then
    myf="/sdcard/zbashfile/"
fi
source $myf/.mathrc
while true
do
    clear;echo "二次函数(一般式)输入"
    echo "type：整数"
    echo "- - - - - - - - - - - - - -"
    fabc "$a" "$b" $c;echo "预览:$func";
    echo "- - - - - - - - - - - - - -"
    echo -n "var:>>";read -n 1 varstr;echo
    if [ -z $varstr ];then
        echo "no var.";continue
    elif [ $varstr = q ];then
        clear;echo "your function:$func";break
    else
        input_int "$varstr=" $varstr
    fi
    if [ -z $"$varstr" ];then
        "$varstr"=0
    fi
done
echo "二次函数坐标计算,仅支持整数"
echo -n "自变量最小整数值x="
read x0
echo -n "自变量最大整数值x="
read x1
echo -n "间隔dx="
read dx
for i in $(seq $x0 $dx $x1)
do
    y=$(($a*$i*$i+$b*$i+$c))
    echo "($i,$y)"
done