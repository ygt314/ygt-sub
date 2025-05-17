N=$1
if [ -z $1 ];then
    echo -n "mypi_N=";read N
fi;ans=0
for n in $(seq 1 $N)
do
    ans=$(echo "$ans+(2/$N)*(sqrt($N-$n+1)*sqrt($N+$n)-sqrt($N+$n-1)*sqrt($N-$n))"|bc -l)
    if [ $((n%(N/100+1))) -eq 0 ];then
        echo -e "\r$n:>$ans\c"
    fi
done
echo -e "\rThe answer is $ans ."