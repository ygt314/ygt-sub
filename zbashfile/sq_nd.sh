echo -n "a=";read a;b=0
if ((a<0));then
    a=$((-a));b=1
fi;x=$a
for i in $(seq 1 10000)
do
    x0=$x;if ((a==0));then
        x=0;break
    fi;x1=$((x+a/x));x=$((x1/2))
    if [ $x = $x0 ];then
        break
    fi
done;if ((x<0));then
    x="${x:1}"
fi;echo x=$x
sq0=$x;ss=${#x}
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
fi;if ((b==1));then
    echo "${ans}i"
else
    echo $ans
fi