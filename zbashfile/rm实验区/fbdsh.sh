b=1
if [ -z $1 ];then
    echo -n "fib_dsh:number-->"
    read num
else
    num=$1
fi
echo "---begin---">fb_dsh.txt
ans=1
f="1/1"
echo "1/1=1">>fb_dsh.txt
echo "1/1=1"
sleep 0.2
for i in $(seq -w 1 $num)
do
    clear
    a=$b
    b=$((a+c))
    c=$a
    ans=$(echo "$ans+1/$b"|bc -l)
    f="$f+1/$b"
    echo "$f"
    echo "=$ans"
    echo "$i|ans+1/$b=$ans">>fb_dsh.txt
    read -n 1 -t 0.2 j
    if [ "$j"x = "q"x ];then
        echo "quit"
        break
    fi
done
echo -e "$(date)\n$f\n=$ans">>.fbdsh_history
echo "---end---">>fb_dsh.txt