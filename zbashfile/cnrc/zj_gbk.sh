i=2;j=0;tis="文"
gtu()
{
head -$i $file|iconv -f gbk -t utf-8
}
tit()
{
head -1 $file|iconv -f gbk -t utf-8
}
titf()
{
echo $file|cut -d . -f 1
}
source zjrc;file=$1
echo txt:;if [ -z $file ];then
    ls *.txt;echo opt_txt:;read file
else
    echo $file
fi;title=$tis:$(tit$2)
echo $title;echo $title>zj_gbk.txt
n=$(cat $file|wc -l)
while [ $i -le $n ]
do
    ss=$(gtu|tail -n 1)
    zjj;if [ $nj = 1 ];then
        echo $ss>>zj_gbk.txt
    fi;nad;i=$((i+d))
    if [ "$1"x = px ] && [ $((i%25)) = 0 ];then
        echo -e "\rprocess:$((i*100/n))%\c"
    fi
done;echo