prsz1y()
{
j=$(cat ~/.szdata1 |wc -l);j=$((j+1));echo -n>sz1$i.txt
for k in $(seq 1 $j)
do
    if ((k%11==$1%11));then
        echo "$(head -$k ~/.szdata1|tail -n 1)"
        echo "$(head -$k ~/.szdata1|tail -n 1)">>sz1$i.txt
    fi
done
echo "+---end---$1"
}
echo -n>szdw1.txt
for i in $(seq 3 2 11)
do
    prsz1y $i;echo "$(tail -n 32 sz1$i.txt)">>szdw1.txt
done