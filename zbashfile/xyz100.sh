echo "x+2y+3z=100,且x,y,z∈N*">xyz100.txt;i=0
echo "time>0/165000\c";a=0
for x in $(seq 1 100)
do
    for y in $(seq 1 50)
    do
        for z in $(seq 1 33)
        do
            a=$((a+1))
            if ((x+2*y+3*z==100));then
                echo "$x+2*$y+3*$z=100">>xyz100.txt;i=$((i+1));echo -e "\c\rtime>$a/165000"
            fi
        done
    done
done
echo "正确次数:$i">>xyz100.txt