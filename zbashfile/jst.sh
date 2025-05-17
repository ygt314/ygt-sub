myf=/sdcard/zbashfile/
source $myf/.mathrc
jst()
{
tm=$1;ans=$2
echo "题目:$tm"
if [ -z $2 ];then
    echo -n "答案:";read ans
fi
if [ -z $ans ];then
    n=$((n+1))
else
    j="$(($tm==$ans))"
    if [ $j -eq 1 ];then
        echo "正确";r=$((r+1))
    else
        echo "错误";e=$((e+1))
        echo "正确答案:$tm=$((tm))"
    fi
fi
}
add_tm()
{
if [ ${1:0:1} = "(" ];then
    ans2=""
fi;fhd="";fhn=${#1}
for fhs in $(seq 1 $fhn)
do
    addn="$(ran $fw)";fh0="${1:$((fhs-1)):1}"
    fh1=${1:$fhs:1};addf=$fhd$fh0;fhd=""
    if [ "$fh1"x = "(x" ];then
        fhd=$addf;continue
    fi;if [ "$fh0"x = ")x" ];then
        fhd=$addf;continue
    fi;ans2="$ans2$addf$addn"
done;if [ "${1:$((fhn-1))}"x = ")x" ];then
    ans2="$ans2)"
fi
}
r=0;e=0;n=0
echo -n "范围:";read fw
echo -n "运算:";read fh
echo -n "个数:";read t
for i in $(seq 1 $t)
do
    ans2="$(ran $fw)";add_tm "$fh"
    jst $ans2
done;echo [即将结算]
sleep 2;clear;f=$((100*r/t))
echo "一共做了$t道题"
echo "做对了$r道题,做错了$e道题"
echo "还有$n道题没有做";echo "得分:$f"