djs()
{
ealt=$EPOCHREALTIME
tie="${ealt:4:6}${ealt:11:2}";tie1=$((tie+$1*100))
while true
do
    clear;ealt=$EPOCHREALTIME;
    tie="${ealt:4:6}${ealt:11:2}";dif1=$((tie1-tie))
    if [ $dif1 -lt 0 ];then
        echo "time out!";break
    fi
    int=$((dif1/100));intl=${#int}
    echo "new-->[$int.$((${dif1:$intl}))] / [$(($1))]";sleep 0.13
done
}
echo -n "djs.sh:>";read dif
djs $dif