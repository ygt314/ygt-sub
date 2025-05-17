a=0;b=0;c=0
while true
do
    clear;echo "二次函数(一般式)输入"
    echo "type：有限小数和整数"
    echo "- - - - - - - - - - - - - -"
    fabc "$a" "$b" $c;echo "预览:$func";
    echo "- - - - - - - - - - - - - -"
    echo -n "var:>>";read -n 1 varstr;echo
    if [ -z $varstr ];then
        echo "no var.";continue
    elif [ $varstr = q ];then
        clear;echo "your function:$func";break
    else
        echo -n "$varstr:>>";read $varstr
    fi
    if [ -z $"$varstr" ];then
        "$varstr"=0
    fi
done
echo "二次函数坐标计算,仅支持有限小数和整数"
echo -n "自变量最小值x=";read x0
echo -n "自变量最大值x=";read x1
echo -n "间隔dx=";read dx
for i in $(seq $x0 $dx $x1)
do
    y=$(echo "$a*$i^2+$b*$i+$c"|bc -l)
    y=$(printf "%.12g" $y);echo "($i,$y)"
done