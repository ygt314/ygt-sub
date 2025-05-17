for i in $(seq -1000 1000)
do
    if (($(echo "$i==$i+1"|bc)));then
        echo -e "\r$i=$((i+1))  "
    else
        echo -e "\r$i≠$((i+1))\c"
    fi
done