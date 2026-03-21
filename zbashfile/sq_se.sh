echo -n "a=";read a;
b=0;if ((a<0));then
    a=$((-a));b=1
fi;x=$a;x1=0;x2=$x
while ((x2-x1>1))
do
    x=$(((x1+x2)/2))
    if ((x*x>a));then
        x2=$x
    elif ((x*x==a));then
        x1=$x;break
    else
        x1=$x
    fi
done;echo x=$x1
sq0=$x1;ss=${#x1}
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
fi;if ((aj==1));then
    echo "${ans}i"
else
    echo $ans
fi