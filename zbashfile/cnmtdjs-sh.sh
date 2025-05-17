cnmt()
{
y1=$1
if [ -z $y1 ];then
    y1=$(date +%Y)
fi
echo "日期形式:星期 月 日 时:分:秒 时区 年"
date1=$(date)
echo "现在时间:$date1"
start_date=$(date +%s)
date2=$(date -d "06180900$y1")
echo "中考时间:$date2"
end_date=$(date -d "06180900$y1" +%s)
date_difference=$((end_date-start_date))
date_difference2=$((start_date-end_date))
if [ $date_difference -le 0 ];then
    date_difference=$date_difference2
fi
date_s=$date_difference
ans_s=$((date_s%60))
date_m=$((date_s/60))
ans_m=$((date_m%60))
date_h=$((date_m/60))
ans_h=$((date_h%24))
date_day=$((date_h/24))
ans_day=$date_day
ans_date="$ans_day"
ans_time="$ans_h:$ans_m:$ans_s"
echo "距$y1中考还有"
echo "${ans_date}day$ans_time"
echo "==[$date_s]second"
}
year=$(date +%Y)
while true
do
    read -t 0.9 -n 1 a
    if [ "$a"x = "q"x ];then
        echo -e "\nquit"
        break
    elif [ "$a"x = "y"x ];then
        clear
        echo "更改年份"
        echo -n "y-->"
        read -t 5 year -n 4
    fi
    clear
    cnmt $year
done