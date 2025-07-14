tis="文";zjle="zj_zz.txt"
tit()
{
head -1 $file
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
echo $title;echo $title>$zjle
echo 判断章节式;n=9
for i in $(seq 1 $n)
do
    ss=$(head -$i $file|tail -n 1)
    zjj;if [ $nj = 1 ];then
        echo method:$med;break
    fi;i=$((i+1))
    if [ $((i%25)) = 0 ];then
        echo -e "process:$((i*100/n))%\c\r"
    fi
done
echo 获取章节;n=$(wc -l <$file)
dl=$((n/1000));st=$((n-dl*1000))
head -$st $file|sed -n -E "$med">>$zjle
for i in $(seq 1000 -1 1)
do
    d=$dl;s=$((i*d))
    echo -e "\r[$((100-i/10))%]\c"
    tail -n $s $file|head -$d|sed -n -E "$med">>$zjle
done;echo -e "\r[已完成]"
echo 获取成功