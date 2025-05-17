prsz2y()
{
j=$(cat ~/.szdata2 |wc -l);j=$((j+1));echo -n>sz2$i.txt
for k in $(seq 1 $j)
do
    if ((k%11==$1%11));then
        echo "$(head -$k ~/.szdata2|tail -n 1)"
        echo "$(head -$k ~/.szdata2|tail -n 1)">>sz2$i.txt
    fi
done
echo "+---end---$1"
}
echo -n>szdw2.txt
for i in $(seq 3 2 11)
do
    prsz2y $i;echo "$(tail -n 32 sz2$i.txt)">>szdw2.txt
done