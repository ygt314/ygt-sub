str=$1;if [ -z $1 ];then
    echo -n "str:>";read $str
fi;str=${str:0:1};for i in $(seq 0 1000)
do
    ai=$(o_10 $i 16);j=0;if [ $(echo "\u$ai")x = "$str"x ];then
        j=1;break
    fi;if((i%5==0));then
        echo -e "\rprogress:$((i/10))%\c"
    fi
done;echo;if ((j==1));then
    echo u$ai
else
    echo not found
fi