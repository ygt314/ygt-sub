x1=n;x2=n;x3=n;x4=n;x5=n;x6=n;x7=n;x8=n;x9=n
a1=x1;a2=x2;a3=x3;a4=x4;a5=x5;a6=x6;a7=x7;a8=x8;a9=x9
while true
do
    clear;echo 数字九宫格输入
    echo "type：整数"
    echo "- - - - - - - - - - - - - -"
    echo "预览:";echo "[$a1] [$a2] [$a3]"
    echo "[$a4] [$a5] [$a6]";echo "[$a7] [$a8] [$a9]"
    echo "- - - - - - - - - - - - - -"
    echo -n "var:>>";read -n 1 varstr;echo
    if [ -z $varstr ];then
        echo "no var.";continue
    elif [ $varstr = q ];then
        clear;echo "your input:"
        echo "[$x1] [$x2] [$x3]";echo "[$x4] [$x5] [$x6]"
        echo "[$x7] [$x8] [$x9]";break
    else
        echo -n "x$varstr:>>";read x
    fi
    varx="x$varstr";eval "$varx=$x;a$varstr=$x"
    if [ -z $x ];then
        eval "$varx=n;a$varstr=$varx"
    fi
done
s_e()
{
echo "--step $js_time">>sdstr.txt
for n in $(seq 0 7)
do
    sem=0;sne=$strs;astr=${astn[$n]};sn=${strn[$n]}
    for x in $(seq 0 2)
    do
        eval $(echo "stm=\$\{$astr[$x]\};stn=\$\{$sn[$x]\}")
        eval "stm=$stm;str=$stn"
        echo "$stm:$str">>sdstr.txt
        if [ $str = n ];then
            sem=$((sem+1));strm=$stm
        else
            sne=$((sne-str))
        fi
    done
    if [ $sem -eq 1 ];then
        eval "$strm=$sne";break
    fi
done
}
t_a()
{
for i in $(seq 0 7)
do
    ta=0;sne=$strs;astr=${astn[$i]};sn=${strn[$i]}
    for x in $(seq 0 2)
    do
        eval $(echo "stm=\$\{$astr[$x]\};stn=\$\{$sn[$x]\}")
        eval "stm=$stm;str=$stn"
        if [ $str = n ];then
            tn=0;break 2
        else
            tn=1;sne=$((sne-str))
        fi
    done
    if [ $sne -ne 0 ];then
        break
    else
        ta=1
    fi
done
}
echo -n "三数和:";read strs
echo "#test stm:str">sdstr.txt
echo "#sd_step">sdstep.txt
for js_time in $(seq 1 50)
do
    str1=($x1 $x2 $x3);str4=($x1 $x4 $x7)
    str2=($x4 $x5 $x6);str5=($x2 $x5 $x8)
    str3=($x7 $x8 $x9);str6=($x3 $x6 $x9)
    str7=($x1 $x5 $x9);str8=($x3 $x5 $x7)
    strn=(str1 str2 str3 str4 str5 str6 str7 str8)
    ast1=(x1 x2 x3);ast4=(x1 x4 x7)
    ast2=(x4 x5 x6);ast5=(x2 x5 x8)
    ast3=(x7 x8 x9);ast6=(x3 x6 x9)
    ast7=(x1 x5 x9);ast8=(x3 x5 x7)
    astn=(ast1 ast2 ast3 ast4 ast5 ast6 ast7 ast8);t_a
    if [ $tn -eq 1 ];then
        break
    fi
    s_e;clear
    echo "正在计算中...($js_time)"
    echo "[$x1] [$x2] [$x3]"
    echo "[$x4] [$x5] [$x6]"
    echo "[$x7] [$x8] [$x9]"
    echo "--step $js_time">>sdstep.txt
    echo "[$x1] [$x2] [$x3]">>sdstep.txt
    echo "[$x4] [$x5] [$x6]">>sdstep.txt
    echo "[$x7] [$x8] [$x9]">>sdstep.txt
done
clear
if [ $tn -eq 0 ];then
    echo 这个题暂时不能算出来
else
    echo 计算完成
fi
echo 结果如下
echo "[$x1] [$x2] [$x3]"
echo "[$x4] [$x5] [$x6]"
echo "[$x7] [$x8] [$x9]"
if [ $ta -eq 1 ];then
    echo 计算结果正确
else
    echo 计算结果错误
fi
echo "共计算了$js_time次"