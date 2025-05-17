s_i()
{
if [ ! -z $1 ];then
    str=$1
fi
echo $str|tr -d -c '0-9'
}
if [ -z $1 ];then
    echo -n "str:>";read str;s_i $str
else
    s_i $1
fi