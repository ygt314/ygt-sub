echo "日期形式:年月日时分.秒"
echo -n "开始日期:"
read date1
start_date=$(date -d "$date1" +%s)
echo -n "结束日期:"
read date2
end_date=$(date -d "$date2" +%s)
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
ans_day=$((date_day%30))
date_mon=$((date_day/30))
ans_mon=$((date_mon%12))
date_y=$((date_mon/12))
ans_y=$((date_y%100))
ans_c=$((date_y/100))
ans_date="$ans_c $ans_y/$ans_mon/$ans_day"
ans_time="$ans_h:$ans_m:$ans_s"
echo "结果:$ans_date $ans_time"
echo "结果:$date_s"