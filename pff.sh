mffe()
{
if [ -z $1 ];then
    echo "no filename";return 0
fi;j=$(cat $1 |wc -l)
echo "+--start--"
j=$((j+1));m=0
for k in $(seq -w 1 $j)
do
    read -s -n 1 -t 0.4 a &>/dev/null
    m=$((m+1))
    if [ "$a"x = qx ];then
        echo quit;break
    else
        echo "$k|$(head -$m $1|tail -n 1)"
    fi
done;echo "+---end---"
}
mff()
{
clear;echo "请在>>>后面输入文件名称"
echo 输入quit退出,支持ls命令
for key in $(seq 0 30)
do
    read -p ">>>" -e zfile
    if [ -z "$zfile" ];then
        echo 请输入文件名称或ls指令
        continue
    fi;if [ "${zfile:0:2}"x = lsx ];then
        ls ${zfile:2};continue
    elif [ "$zfile"x = quitx ];then
        echo 已退出;break
    fi;mffe $zfile
done
}
if [ -z $1 ];then
    mff
else
    mffe $1
fi