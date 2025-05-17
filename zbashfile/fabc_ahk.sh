if [ -z $myf ];then
    myf="/sdcard/zbashfile/"
fi
source $myf/.mathrc
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
sleep 0.6;echo "y=ax²+bx+c-->y=a(x+h)²+k"
sleep 0.6;ahk_l "$a" "$b" $c