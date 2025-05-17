for i in $(seq -1000 1000)
do
    if (($(echo "$i^2+($i+1)^2==($i+2)^2"|bc)));then
        echo -e "\r($i)²+($((i+1)))²=($((i+2)))²   "
    else
        echo -e "\r($i)²+($((i+1)))²≠($((i+2)))²\c"
    fi
done