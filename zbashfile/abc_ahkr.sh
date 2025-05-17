if [ -z $myf ];then
    myf="/sdcard/zbashfile/"
fi
source $myf/mathrc/absrc
source $myf/mathrc/yfrc
source $myf/mathrc/a_bcrc
echo "您正在进行一般式化顶点式"
for i in $(seq 1 30)
do
    echo -n "a=";read a;a1=$a
    if [ -z $a ];then
        a=0
    fi
    if [ $a = quit ] || [ $a = exit ];then
        break
    fi
    echo -n "b=";read b
    if [ -z $b ];then
        b=0
    fi
    if [ $b = quit ] || [ $b = exit ];then
        break
    fi
    if [ $b -gt 0 ];then
        b1="+${b}x"
    elif [ $b -lt 0 ];then
        b1="-${b}x"
    else
        b1=""
    fi
    echo -n "c=";read c
    if [ -z $c ];then
        c=0
    fi
    if [ $c = quit ] || [ $c = exit ];then
        break
    fi
    if [ $c -gt 0 ];then
        c1="+$c"
    elif [ $c -lt 0 ];then
        c1="-$c"
    else
        c1=""
    fi
    echo "y=${a}x²$b1$c1";echo "     ↓"
    if [ $a = 0 ];then
        if [ $b = 0 ];then
            echo 常值函数不能配方
        else
            echo 一次函数不能配方
        fi
        continue
    fi
    h1=$b;h2=$((a*2))
    k1=$((4*a*c-b*b));k2=$((a*4))
    hh=$(eval "a_br $h1 $h2 10") &>/dev/null
    kk=$(eval "a_br $k1 $k2 10") &>/dev/null
    yfz $h1 $h2;h="$aa/$bb"
    yfz $k1 $k2;k="$aa/$bb"
    echo "y=$a(x$h)²$k";echo "     ↓"
    echo "y=$a(x$hh...)²$kk..."
done