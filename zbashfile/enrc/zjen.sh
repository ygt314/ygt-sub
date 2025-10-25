i=2;j=0;tis="文"
tit()
{
head -1 $file
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
echo $title;echo $title>zj.txt
n=$(cat $file|wc -l)
while [ $i -le $n ]
do
    ss=$(head -$i $file|tail -n 1)
    zjj_en;if [ $nj = 1 ];then
        echo $ss>>zj.txt
    fi;nad;i=$((i+d))
    if [ "$1"x = px ] && [ $((i%25)) = 0 ];then
        echo -e "\rprocess:$((i*100/n))%\c"
    fi
done;echo