sn=$(cat nb1.txt)
for nbi in $(seq 0 ${#sn})
do
    source sen_us.sh "${sn:$nbi:1}"
done