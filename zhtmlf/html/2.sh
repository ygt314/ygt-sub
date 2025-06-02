source html_txtrc
while true
do
    echo -n "url:>";read murl
    if [ -z $murl ];then
        clear;echo no url
    elif [ $murl = quit ] || [ $murl = exit ];then
        break
    else
        curl $murl -o 2.html;clear
        echo "($murl)";pht 2.html -s
    fi
done