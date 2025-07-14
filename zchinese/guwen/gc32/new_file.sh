n=0;tit="高考篇目"
for tt in $(cat help.help)
do
    if [ n = 0 ];then
        echo [开始]
    fi;if [ "${tt:0:1}"x = "#x" ];then
        tit="${tt:1}";continue
    fi;file="$(echo "$tt"|cut -d . -f 2)";n=$((n+1))
    echo :$tit:"$tt" > "$file".txt
done
echo [结束]