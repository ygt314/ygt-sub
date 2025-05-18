echo -n "输入pi值位数: "
read a
time(q=$(echo "scale=$a;a(1)*4" |bc -l))