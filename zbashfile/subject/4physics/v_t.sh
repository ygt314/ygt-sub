v=0;v0=0;a=0;t=0
echo "v=v₀+at";echo -n "v_t>";read s;if [ -z $s ];then
    echo "noties:no value of solve"
fi
while [ "$s"x != quitx ] && [ "$s"x != exitx ]
do
    if [ -z $s ];then
        echo -n "v_t>";read s;continue
    fi;echo -n ">>>";read -n 1 j;if [ "$j"x = vx ];then
        read -n 1 j1
    else
        j1=1
    fi;echo;if [ "$j1"x = 0x ];then
        j=v0;echo -n "v₀:>"
    elif [ "$j"x = sx ];then
        case $s in
            v)ans=$(echo "($v0)+($a)*($t)"|bc -l);;
            v0)ans=$(echo "($v)-($a)*($t)"|bc -l);;
            a)ans=$(echo "(($v)-($v0))/($t)"|bc -l);;
            t)ans=$(echo "(($v)-($v0))/($a)"|bc -l);;
        esac;echo "$s=$ans";eval "$s=$ans";continue
    elif [ "$j"x = qx ];then
        echo -n "v_t>";read s;continue
    else
        echo -n "$j:>"
    fi;read va;eval "$j=$va"
done