while true
do
    word_file=$1;mkey=0
    if [ -z $1 ];then
        echo -n "word_file:>>";read word_file
    else
        mkey=1
    fi
    result=$(python $enf/word_listen.py $(cat $word_file.w))
    res_f="$men/.listen_history"
    echo "$(date)">>"$res_f"
    echo "$result"
    echo "$result">>"$res_f"
    if [ $mkey eq 1 ];then
        break
    elif [ "$word_file"x = quitx ] && [ "$word_file"x = exitx ];then
        break
    fi
done