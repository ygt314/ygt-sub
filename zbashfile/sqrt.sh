echo -n "a=";read a;aj=0
if [ "${a:0:1}"x = -x ];then
    a=${a:1};aj=1
fi;ss=${#a}
if ((ss>10));then
    echo error:a:too large;return 0
fi;s2=$(((ss+1)/2));s0="10000000000"
b=0;if ((s2>1));then
    b="${s0:0:$s2}"
fi;for i in $(seq $b $a)
do
    if ((i*i<=a));then
        ans=$i
    else
        break
    fi
done;sq0=$ans;ss=${#i}
echo -n "scale=";read s
if [ -z $s ];then
    s=1
fi;if ((s>10-ss));then
    s=$((10-ss))
fi;if ((s==0));then
    ans=$sq0
elif ((s>0));then
    f=0;i=$sq0
    nbc=$((20*i))
    nbb=$nbc
    nba=$((a-i*i))
    for k in $(seq 1 $s)
    do
        nba=$((nba*100))
        nbb=$((nbb-1))
        for j in $(seq 0 9)
        do
            nbb=$((nbb+2))
            nba=$((nba-nbb))
            if [ $nba -le 0 ];then
                nba=$((nba+nbb))
                nbb=$((nbb-2))
                f=$((f*10+j));break
            elif [ $j -eq 9 ];then
                echo 'error:j>9'
            fi
        done;nbc=$((nbc*10+j*20))
        nbb=$nbc
    done
    ans="$i.$f"
fi
if ((aj==1));then
    echo "${ans}i"
else
    echo $ans
fi