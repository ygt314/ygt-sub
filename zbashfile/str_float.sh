s_f()
{
if [ ! -z $1 ];then
    str=$1
fi
echo $str|tr -d -c '0-9.'
}
if [ -z $1 ];then
    echo -n "str:>";read str;s_f $str
else
    s_f $1
fi