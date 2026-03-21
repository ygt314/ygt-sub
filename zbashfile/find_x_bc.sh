is_x()
{
y="${y:-1}";x_j=0
if [ $(bcm "abs($y)<10^(-9)") = 1 ];then
    x_j=1
fi
}
isxx()
{
str="x$x_n∈($x0,$x)"
if [ -z $y0 ];then
    echo -e "\ry0_nan\c"
elif [ $(bcm "($y0*$y)<0") = 1 ];then
    echo -e "\r$str     ";x_n=$((x_n+1))
fi
}
dx_s()
{
dx=$((x2-x1));s=1
if ((dx>100));then
    s=$((dx/100))
fi
}
find_x()
{
echo $x1[start]_;xn=0
for x in $(seq $x1 $s $x2)
do
    fx $f $x
    bcm "$func" &> /dev/null
    y=$ans;yj=1;xj=0
    if [ -z $y ];then
        echo x≠$x;yj=0;
    fi;is_x;if ((x_j==1));then
        echo -e "\rx$x_n=$x  ";x_n=$((x_n+1));xn=0
    elif ((yj0==1));then
        xn=$((xn+1))
    fi;if ((xn==2));then
        isxx;xn=1
    fi;x0=$x;y0=$y;yj0=$yj
done;echo -e "\r_[end]$x2"
}
str=s
while true
do
    read -p 'function> y=' -e f
    if [ -z $f ];then
        f=$f0
    fi;f="${f:=x}";echo -n 'x1=';read x1;x1="${x1:=-9}"
    echo -n 'x2=';read x2;x2="${x2:=9}";str=$f
    if [ "$str"x = exitx ] || [ "$str"x = quitx ];then
        echo quit;break
    fi;x1=$(floor $x1);x2=$(ceil $x2)
    x_n=1;x0="";dx_s;find_x;f0=$f
done