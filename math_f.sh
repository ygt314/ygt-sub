source ~/.mathrc;cnmt_d
ans=0
echo -e "关键字(赋值时不能命名):i,jt,str,str2,quit\n在>>>后输入数字表达式(输入quit退出)"
for i in $(seq 1 50)
do
    echo -n ">>>"
    read str
    str2="|-->$str<--|"
    if [[ "$str2" == *"="* ]] && [[ "$str2" != *"=="* ]];then
        if [[ "$str2" == *"!"* ]] && [[ "$str2" == *"<"* ]] && [[ "$str2" == *">"* ]];then
            echo $(($str))
            ans=$(($str))
            jt=1
        else
            (($str))
            jt=1
            echo $str2
        fi
    elif [ "$str"x = "quit"x ] || [ "$str"x = "exit"x ];then
        echo "END"
        jt=0
        break
    else
        (($str)) >/dev/null
        if [ $? -eq 1 ];then
            ans2=$(eval "$str")
            echo "$ans2"
            jt=1
        else
            echo $(($str))
            ans=$(($str))
            jt=1
        fi
    fi
done
if [ "$jt" = "1" ] && [ "$str"x != "quit"x ];then
    echo "休息一下,已自动退出"
fi