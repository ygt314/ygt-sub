n=0
for tt in $(cat help.help)
do
    if [ n = 0 ];then
        echo [开始];continue
    fi;file="$(echo "$tt"|cut -d . -f 2)";n=$((n+1))
    echo :高考篇目:"$tt" > "$file".txt
done
echo [结束]