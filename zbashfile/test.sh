s=$1
if [ -z "$1" ];then
    s=100
fi
ans=0
for x in $(seq 1 $s)
do
    ans=$(pym "$ans+(-1*$x*(-1)**$x)/($x**2+1)");echo -e "\c\r$x:>$ans   "
done
echo -e "\nThe answer is $ans"