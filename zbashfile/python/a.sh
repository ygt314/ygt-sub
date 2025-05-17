if [ -z $mpy ];then
    mpy="/storage/emulated/0/zbashfile/python"
fi
echo "已进入命令行模式";ae=0
for i in $(seq 1 30)
do
	echo -n "$ae|a--$i>>";read a
	if [ -z $a ];then
	    continue
	elif [ "$a"x = "clear"x ];then
	    clear;ae=0;continue
	fi
	if [ "$a"x = "py"x ];then
		python $mpy/equation_axbxc0.py;ae=$?
	elif [ "$a"x = "exit"x ];then
	    break
	else 
 	    echo -e "error:$a command no found"
 	    ae=1;continue
	fi
	echo -e "即将进行根计算,\n请将根参数写入"
	echo -n "x1=";read x1
	echo -n "x2=";read x2
	echo -e "正进行根计算中,\n请输入表达式(输入q结束)"
	for t in $(seq 1 30)
	do
	    echo -n "$t:>>";read b
        if [ "$b"x = "q"x ];then
            break
        else
            echo -n "-->"
	        echo "x1=eval('$x1');x2=eval('$x2');print(eval('$b'))"|python
        fi
    done
done
