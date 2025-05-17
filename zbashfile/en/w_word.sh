if [ -z $myf ];then
    myf=/sdcard/zbashfile
fi
if [ -z $enf ];then
    source $myf/.enrc
fi
word_file=$1
if [ -z $1 ];then
    echo -n "word_file:>>";read word_file
fi
result=$(python $enf/word_write.py $(cat $word_file.w))
res_f="$men/$(date +%y%m%d%H%M)_w.txt"
echo "$(date)">"$res_f"
echo "$result"
echo "$result">>"$res_f"