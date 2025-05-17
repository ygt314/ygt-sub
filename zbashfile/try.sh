try()
{
(($1))&>/dev/null;ans=$?
if $1&>/dev/null;then
    echo true
elif [ "$ans"x = 0x ];then
    echo $(($1))
else
    echo false
fi
}
while [ "$a"x != exitx ] || [ "$a"x != quitx ]
do
    echo -n "cmd:>";read a;try $a
done