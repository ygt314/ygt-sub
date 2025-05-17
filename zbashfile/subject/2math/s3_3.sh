for i in $(seq -1000 1000)
do
    if (($(echo "$i^3+($i+1)^3+($i+2)^3==($i+3)^3"|bc)));then
        echo -e "\r($i)³+($((i+1)))³+($((i+2)))³=($((i+3)))³    "
    else
        echo -e "\r($i)³+($((i+1)))³+($((i+2)))³≠($((i+3)))\c"
    fi
done