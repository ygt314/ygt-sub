mffe()
{
if [ -z $1 ];then
    echo "no filename"
else
    echo "+--start--"
    j=$(cat $1 |wc -l);j=$((j+1));m=0
    for k in $(seq -w 1 $j)
    do
        read -s -n 1 -t 0.4 a &>/dev/null
        m=$((m+1))
        if [ "$a"x = qx ];then
            echo "quit";break
        else
            echo "$k|$(head -$m $1|tail -n 1)"
        fi
    done
    echo "+---end---"
fi
}
mff()
{
clear
echo -e "请在>>>后面输入文件名称，\n输入quit退出。\n支持ls命令"
for key in $(seq 0 30)
do
    echo -n ">>>";read zfile
    if [ -z $zfile ];then
        echo 请输入文件名称或指令;continue
    fi
    if [ "${zfile:0:2}"x = lsx ];then
        ls ${zfile:0:2};continue
    elif [ "$zfile"x = quitx ];then
        echo 已退出;break
    else
        echo "+--start--"
        j=$(cat $zfile |wc -l);j=$((j+1));m=0
        for k in $(seq -w 1 $j)
        do
            read -s -n 1 -t 0.4 a &>/dev/null
            m=$((m+1))
            if [ "$a"x = qx ];then
                echo "quit";break
            else
                echo "$k|$(head -$m $zfile|tail -n 1)"
            fi
        done
        echo "+---end---"
    fi
done
}
if [ -z $1 ];then
    mff
else
    mffe $1
fi