echo "即将倒数10s"
sleep 0.4
for i in $(seq 10 -1 1)
do
    clear
    echo "[$i]"
    sleep 0.98
done
clear
echo "时间到"