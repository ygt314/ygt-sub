enf="$myf/en"
s_w()
{
word=$1;ipakey=$2;res_f="$enf/.listen_history"
if [ -z $1 ];then
    echo -n "you_word:>";read word
fi
if [ -z $2 ];then
    ipakey=1
fi
echo "$(date)">>"$res_f"
echo "read:>$word"
echo "read:>$word">>"$res_f"
if [ "$ipakey"x = 2x ];then
    result=$(echo "$word"|speak -x)
else
    result=$(echo "$word"|speak --ipa)
fi
echo "$result"
echo "$result">>"$res_f"
if [ "$word"x = quitx ] || [ "$word"x = exitx ];then
    echo Ending;return 0
elif [ -z $1 ];then
    s_w
fi
}
s_w $1 $2