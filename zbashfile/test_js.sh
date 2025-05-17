put_tm()
{
put=""
while [ -z $put ]
do
    echo "提示:没有题目"
    echo -n "$1";read put
done
if [ ! -z $2 ];then
    eval "$2=$put"
fi
}
t=0;r=0;e=0;n=0
for i in $(seq 1 100)
do
    echo -n "题目:";read tm
    if [ "$tm"x = quitx ] || [ "$tm"x = exitx ];then
        t=$((i-1));break
    fi
    echo -n "答案:";read ans
    if [ -z $ans ];then
        n=$((n+1));continue
    elif [ $ans = quit ] || [ $ans = exit ];then
        n=$((n+1));t=$i;break
    fi
    if [ -z $tm ];then
        put_tm "题目:" tm
    fi
    j="$(($tm==$ans))"
    if [ $j -eq 1 ];then
        echo "正确";r=$((r+1))
    else
        echo "错误";e=$((e+1))
    fi
done
clear;f=$((100*r/t))
echo "一共做了$t道题"
echo "做对了$r道题,做错了$e道题"
echo "还有$n道题没有做";echo "得分:$f"