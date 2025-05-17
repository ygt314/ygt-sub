rcxs()
{
if [ -z $cxstr ];then
    return 0
fi;len=${#cxstr};act=$((len-1));cxstr="${cxstr:0:$act}"
}
cxmd()
{
case $1 in
    n)echo -n n=;read cxn;;
esac
}
while true
do
    jn="";if [ -z $cxstr ];then
        jn=a
    fi;clear;echo 搜索方程式;echo "type:Aa1+="
    echo --------------------;echo 搜索:$cxstr
    echo --------------------;cxeq $jn$cxstr
    read -n 1 cxj;case $cxj in
        -)rcxs;;
        x)cxstr="";;
        w)cxstr="${cxstr:1}";;
        q)echo -e "\rBye bye!";break;;
        :)read cxmd;cxmd $cxmd;;
        *)cxstr=$cxstr$cxj;;
    esac
done