for i in $(seq 1 30)
do
    echo -n "deg:> ";read d;d1=$((d%360))
    d2=$((d1>0?-1:1))
    d2=$((d1*d1<180*180?d1:d2*(360+d2*d1)%360))
    echo "$((d))°=$d1°=$d2°"
done