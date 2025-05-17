test_rm()
{
if [ -z $1 ];then
    str="没有命令";return 0
elif [ "$1"x = exitx ];then
    str="退出命令";return 0
fi
if [ "$1"x = "rm -rf *"x ];then
    str="警告:该命令会强制删除所有文件";return 1
elif [ ${1:0:4}x = "rm -"x ];then
    str="警告:该命令可能会删除所在目录所有文件";return 1
fi
if [ ${1:0:4}x = "rm *"x ];then
    str="警告:该命令会删除所在目录所有文件";return 1
elif [ ${1:0:2}x = rmx ];then
    str="警告:该命令可能会删除文件";return 1
fi
if [ "$1"x = rmx ];then
    str="提示:这是删除文件的命令";return 1
else
    str="提示:这不是删除文件的命令";return 0
fi
}
if [ -z $1 ];then
    echo -n "cmd>>";read cmd
    test_rm $cmd;echo $?
else
    for cmd in $@
    do
        echo "cmd>>$cmd"
        test_rm $cmd;echo $?
    done
fi