s=$1;right=0;wrong=0
if [ -z $1 ];then
    echo -n "nbran:times-->";read s;clear
fi
for i in $(seq 1 $s)
do
    ans=$((RANDOM%2))
    if [ $ans -eq 1 ];then
        right=$((right+1));echo -e "\r$i:正\c"
    elif [ $ans -eq 0 ];then
        wrong=$((wrong+1));echo -e "\r$i:反\c"
    fi
done
clear;pr=$((right*100/s));pw=$((wrong*100/s))
echo "正:$right($pr%)";echo "反:$wrong($pw%)"