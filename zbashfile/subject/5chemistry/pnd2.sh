for i in $(seq 8000 9000)
do
    ai=$(o_10 $i 16);echo -n "\u$ai"
    if((i%25==0&i>8000));then
        echo
    fi
done