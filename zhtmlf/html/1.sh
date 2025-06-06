source html_txtrc;ls *html
while true
do
    echo -n "html:>";read myh;clear
    if [ -z $myh ];then
        echo no file name
    elif [ ${myh:0:2} = ls ];then
        ls ${myh:3}
    elif [ $myh = quit ] || [ $myh = exit ];then
        break
    else
        echo "$myh:";pht $myh -s
    fi
done