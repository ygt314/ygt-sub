echo "学科termux布署"
curl -V > /dev/null 2>&1
if [ $? != 0 ];then
    echo "[警告]:没有curl，使用系统curl..."
    function curl() { /system/bin/curl $@; }
fi

file_v="subter_1.2.2"
fmt=""

# 检测可用工具: unzip优先→tar→系统tar
unzip -v > /dev/null 2>&1
if [ $? = 0 ];then
    fmt="zip"
    echo "使用 unzip 解压"
else
    tar --version > /dev/null 2>&1
    if [ $? = 0 ];then
        fmt="tar"
        echo "使用 tar 解压"
    else
        echo "[警告]:没有tar，尝试系统tar..."
        function tar() { /system/bin/tar $@; }
        fmt="tar"
        echo "使用系统tar"
    fi
fi

echo "下载并布署项目 ($fmt)"
if [ "$fmt" = "zip" ];then
    curl -L "https://gitee.com/ygt314159/subject-termux/raw/master/${file_v}.zip" -o sbt.zip
    cd && unzip -o sbt.zip && rm sbt.zip
else
    curl -L "https://gitee.com/ygt314159/subject-termux/raw/master/${file_v}.tar" -o sbt.tar
    cd && tar -xf sbt.tar && rm sbt.tar
fi

cd && echo "执行ppht.sh" && bash ppht.sh
cd && echo "即将运行初始化脚本" && bash terset.sh
