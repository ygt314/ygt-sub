od_xt()
{
echo -ne "\u$1";d=$(ran 2);d=$((d+3))
if ((htmi%d==0));then
    sleep 0.1
fi
}
p_br()
{
if [ $1 = 1 ];then
    para=$((para+1));echo "($para)";paj=0
else
    echo;paj=1;sleep 0.3
fi
}
c_od()
{
odj=0
if [ $1 = con- ];then
    odj=1
fi
}
c_br()
{
brj=0
if [ $1 = "<br>" ];then
    brj=1
fi
}
hfs=$1;if [ -z $hfs ];then
    ls *tml;ls con_x*;echo -n "file>>";read hfs
fi;htmx=$(cat $hfs)
htmn=${#htmx};htmn=$((htmn-4))
htmi=0;xtj=0;paj=0;para=1
echo "(1)"
while [ $htmi -le $htmn ]
do
    chs=${htmx:$htmi:4};c_br $chs;c_od $chs
    if [ $xtj = 1 ];then
        od_xt $chs
    fi;xtj=0
    if [ $brj = 1 ];then
        p_br $paj;htmi=$((htmi+4))
    elif [ $odj = 1 ];then
        xtj=1;htmi=$((htmi+4))
    else
        htmi=$((htmi+1))
    fi
done