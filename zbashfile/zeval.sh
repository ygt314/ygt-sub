echo "已进入自定义命令行"
source /sdcard/zbashfile/.bashrc
for i in $(seq 1 100)
do
    echo -n "Enter cmd:>>>";read b
	if [ "$b"x = "exit"x ];then
	    echo "已退回系统命令行";break
    elif [ "$b"x = "rm -rf *"x ];then
        echo -e "警告:该命令会强制删除所有文件\n已跳过该命令";continue
    fi
    if [ "$b"x = "rm"x ];then
        echo -e "警告:该命令会删除文件。\n已跳过该命令。";continue
    elif [ "${b:0:4}"x = "rm *"x ];then
        echo -e "警告:该命令会删除所在目录所有文件\n已跳过该命令";continue
    fi
    if [ "${b:0:4}"x = "rm -"x ];then
        echo -e "警告:该命令会删除所在目录所有文件\n已跳过该命令";continue   
    elif [ -z $b ];then
        echo "没有命令";continue
	fi
	if [ "${b:0:2}"x = "rm"x ];then
	    echo -e "警告:该命令可能会删除文件\n已跳过该命令";continue
	else
 	    eval $b
	fi
done
echo "程序已结束"