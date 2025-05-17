s_n()
{
if [ -z $2 ];then
    sh str_float.sh $1
elif [ "${1:-1}"x = ix ] || [ "$1"x = intx ];then
    sh str_int.sh $2
else
    sh str_float.sh $2
fi
}
if [ -z $1 ];then
    echo -n "str:>";read str;s_n $str
else
    s_n $1 $2
fi