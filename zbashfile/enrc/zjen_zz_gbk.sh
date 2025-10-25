tis="text";zjle="zj_zz_gbk.txt"
gtu()
{
head -$i $file|iconv -f gbk -t utf-8
}
tgtu()
{
tail -n $s $file|iconv -f gbk -t utf-8
}
tit()
{
head -1 $file|iconv -f gbk -t utf-8
}
titf()
{
echo $file|cut -d . -f 1
}
source zjenrc;source zjrc;file=$1
echo txt:;if [ -z $file ];then
    ls *.txt;echo opt_txt:;read file
else
    echo $file
fi;title=$tis:$(tit$2)
echo $title;echo $title>$zjle
echo judging_chapter_form;n=9
for i in $(seq 1 $n)
do
    ss=$(gtu|tail -n 1)
    zjj_en;if [ $nj = 1 ];then
        echo method:$med;break
    fi;i=$((i+1))
    if [ $((i%25)) = 0 ];then
        echo -e "process:$((i*100/n))%\c\r"
    fi
done
echo Get chapters;n=$(wc -l <$file)
dl=$((n/1000));i=$((n-dl*1000))
gtu|sed -n -E "$med">>$zjle
for i in $(seq 1000 -1 1)
do
    d=$dl;s=$((i*d))
    echo -e "\r[$((100-i/10))%]\c"
    tgtu|head -$d|sed -n -E "$med">>$zjle
done;echo -e "\r[.Done.]"
echo Get successful