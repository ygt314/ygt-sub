for i in $(seq 0 10000)
do
    ai=$(o_10 $i 16);echo -n "\u$ai"
    if((i%25==0&i>0));then
        echo
    fi
done