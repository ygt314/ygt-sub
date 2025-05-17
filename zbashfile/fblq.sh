b=1
if [ -z $1 ];then
    read num
else
    num=$1
fi
echo "---begin---">fb_lq.txt
for i in $(seq -w 1 $num)
do
    echo "$i|$b"
    echo "$i|$b">>fb_lq.txt
    a=$b
    b=$((a+c))
    c=$a
    read -n 1 -t 0.2 j
    if [ "$j"x = "q"x ];then
        echo "quit"
        break
    fi
done
echo "---end---">>fb_lq.txt