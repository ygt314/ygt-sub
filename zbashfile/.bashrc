myf=/sdcard/zbashfile
mpy=$myf/python
zexe=/sdcard/zexe
mqpy=/sdcard/qpython/scripts3
source $myf/.htmlrc
source $myf/.mypwrc
source $myf/.pwrc
source $myf/.subrc
source $myf/.pyrc
cdf()
{
cd $myf
}
echo "日历:"
cal
qpy()
{
~/bin/python3.sh $@
}
pff()
{
sh $myf/pff.sh $1
}
pf()
{
sh $myf/pf.sh $1
}
source $myf/.mathrc
cngt_d
source $myf/.bcrc
source $myf/.cmstrc
source $myf/.enrc
input_str()
{
put=""
while [ -z $put ]
do
    echo -n "$1"
    read put
done
if [ ! -z $2 ];then
    eval "$2=$put"
fi
}
put()
{
if [ "$1"x = intx ];then
    input_int $2 $3
elif [ "$1"x = strx ];then
    input_str $2 $3
fi
}
history_c()
{
filename="$1"
clear;sleep 0.5
echo "清理$2历史中";sleep 0.5
echo "q跳过(2s)";echo " 回车开始"
read -t 2 -n 1 hisa
if [ "$hisa"x = "q"x ];then
    echo;echo "$2历史已取消清理"
else
    echo "#hello world!">~/$filename
    echo "$2历史已清理"
fi
}