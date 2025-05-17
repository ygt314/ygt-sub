dss()
{
if [ -z $1 ];then
    s=10
else
    s=$1
fi
for i in $(seq $s -1 1)
do
    clear;echo "倒数数进行中"
    echo "new--> [$i] / [$s]";read -t 0.97 -n1 a
    if [ "$a"x = qx ];then
        break
    elif [ "$a"x = sx ];then
        clear;echo "倒数数暂停"
        echo "new-->[$i]/[$s]";read -n1
    fi
done
clear
echo "倒数数结束"
echo "new--> [0] / [$1]"
echo "时间到"
}
echo "倒数数"
echo -n "s-->"
read s
dss $s