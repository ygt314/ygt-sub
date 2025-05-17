sn=$(cat nb.txt)
for nbi in $(seq 0 ${#sn})
do
    source sen_us2.sh "${sn:$nbi:1}"
done