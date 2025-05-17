echo "即将开始查看日期10s"
sleep 0.5
for i in $(seq 1 20)
do
    sleep 0.5
    clear
    cal;date
done
