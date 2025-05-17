d_x_t()
{
d=$(echo "4*($v0)^2+8*($a)*($x)"|bc -l);j=$(echo "$d>=0"|bc -l)
}
s2t()
{
ans=0;d_x_t;if [ $j = 1 ];then
    ans=$(echo "(-1)*($v0)/($a)+sqrt(($d))/(($a)*2)"|bc -l);ans2=$(echo "(-1)*($v0)/($a)-sqrt(($d))/(($a)*2)"|bc -l);ans="$ans or $ans2"
fi
}
v=0;v0=0;a=0;t=0;x=0
echo "x=v₀t+1/2*at²";echo -n "x_t>";read s;if [ -z $s ];then
    echo "noties:no value of solve"
fi
while [ "$s"x != quitx ] && [ "$s"x != exitx ]
do
    if [ -z $s ];then
        echo -n "x_t>";read s;continue
    fi;echo -n ">>>";read -n 1 j;echo
    if [ "$j"x = vx ];then
        j=v0;echo -n "v₀:>"
    elif [ "$j"x = sx ];then
        case $s in
            x)ans=$(echo "($v0)*($t)+($a)*($t)*($t)/2"|bc -l);;
            v0)ans=$(echo "($x)/($t)-($a)*($t)/2"|bc -l);;
            a)ans=$(echo "2*(($x)-($v0)*($t))/($t)^2"|bc -l);;
            t)s2t;;
        esac;echo "$s=$ans";eval "$s='$ans'";continue
    elif [ "$j"x = qx ];then
        echo -n "x_t>";read s;continue
    else
        echo -n "$j:>"
    fi;read va;eval "$j=$va"
done