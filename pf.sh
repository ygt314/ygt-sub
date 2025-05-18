mpff=zchinese
mfe()
{
if [ "$1"x = namex ];then
    cat "$mpff/.name";echo
else
    echo "内容如下:"
    j=$(cat "$mpff/$1.txt" |wc -l);j=$((j+1))
    for m in $(seq 1 $j)
    do
        read -s -n 1 -t 0.5 a &>/dev/null
        if [ "$a"x = qx ];then
            echo quit;break
        fi
        strm="$(head -$m $mpff/$1.txt|tail -n 1)";k="${#strm}";s=0
        if [ "${strm:0:1}" = "#" ];then
            s=2
        fi
        for n in $(seq $s $k)
        do
            if [ "${strm:$n:1}" = "/" ];then
                sleep 0.2;continue
            elif [ "${strm:$n:1}" = "." ];then
                echo -n " ";continue
            fi
            echo -n "${strm:$n:1}"
            if [ "${strm:$n:1}" = "，" ] || [ "${strm:$n:1}" = "。" ];then
                sleep 0.2
            elif [ "${strm:$n:1}" = "？" ] || [ "${strm:$n:1}" = "！" ];then
                sleep 0.2
            elif [ $s -eq 2 ];then
                sleep 0.1
            fi
        done
        echo
    done
    echo "--end--"
fi
}
mf()
{
clear
echo -e "请在>>>后面输入古诗词名称，\n输入quit退出。\n输入name获取古诗"
for key in $(seq 0 30)
do
    echo -n ">>>";read zfile
    if [ "$zfile"x = namex ];then
        cat "$mpff/.name";echo
        echo 请输入古诗名称;continue
    fi
    if [ -z $zfile ];then
        echo 请输入古诗名称;continue
    elif [ "$zfile"x = quitx ];then
        echo 已退出;break
    fi
    echo "内容如下:"
    j=$(cat "$mpff/$zfile.txt" |wc -l);j=$((j+1))
    for m in $(seq 1 $j)
    do
        read -s -n 1 -t 0.5 a &>/dev/null
        if [ "$a"x = qx ];then
            echo quit;break
        fi
        strm="$(head -$m $mpff/$zfile.txt|tail -n 1)";k="${#strm}";s=0
        if [ "${strm:0:1}" = "#" ];then
            s=2
        fi
        for n in $(seq $s $k)
        do
            if [ "${strm:$n:1}" = "/" ];then
                sleep 0.1;continue
            elif [ "${strm:$n:1}" = "." ];then
                echo -n " ";continue
            fi
            echo -n "${strm:$n:1}"
            if [ "${strm:$n:1}" = "，" ] || [ "${strm:$n:1}" = "。" ];then
                sleep 0.1
            elif [ "${strm:$n:1}" = "？" ] || [ "${strm:$n:1}" = "！" ];then
                sleep 0.1
            elif [ $s -eq 2 ];then
                sleep 0.1
            fi
        done
        echo
    done
    echo "--end--"
done
}
if [ -z $1 ];then
    mf
else
    mfe $1
fi