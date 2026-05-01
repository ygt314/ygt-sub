echo 学科termux布署
curl -V > /dev/null
if [ $? != 0 ];then
    echo [警告]:没有curl
    function curl()
    {
    /system/bin/curl $@
    }
    echo 使用系统curl...
fi;cd;zip_j=1
echo 检查unzip
unzip -v > /dev/null
if [ $? != 0 ];then
    echo [警告]:没有unzip
    zip_j=0
    echo 即将尝试tar
fi;cd;echo 检查tar
unzip -v > /dev/null
if [ $? != 0 ];then
    echo [警告]:没有tar
    function tar()
    {
    /system/bin/tar $@
    }
    echo 即将使用系统tar
fi;echo 下载并布署项目
if [ $zip_j = 1 ];then
    curl https://gitee.com/ygt314159/subject-termux/raw/master/subter_1.1.9.zip > sbt.zip
    cd;unzip sbt.zip
    rm sbt.zip
else
    curl https://gitee.com/ygt314159/subject-termux/raw/master/subter_1.1.9.tar>sbt.tar
    cd;tar -xvf sbt.tar
    rm sbt.tar
fi;cd;echo 执行ppht.sh
bash ppht.sh
cd;echo 即将运行初始化脚本
bash terset.sh
