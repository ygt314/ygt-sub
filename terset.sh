getpg()
{
echo $hello
apt install -y $@
}
hello=工具;na=busybox
getpg getconf screenfetch
#getconf LONG_BIT查看系统位数
getpg busybox tree
na=天气狗;getpg wego
hello='C(gcc已内置)'
na=clang;getpg $na
hello='Shell math'
na=BC;getpg bc
na=mma;getpg mathomatic
na=gnuplot;getpg $na
hello=en-speak
na=speak;getpg espeak
hello=Python
na=python;getpg $na
apt upgrade python-pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
echo "apt search python:apt python page"
na=Math
getpg python-numpy python-scipy python-pyarrow
na=Image
getpg python-tkinter python-pillow matplotlib
na=xml;getpg python-lxml
hello=lua
na="Lua 5.4.7";getpg lua54
hello=文件处理
na=Vim;getpg vim
na=zip;getpg zip unzip gzip
na=doc;getpg pandoc grep gawk
na=play;getpg sox mpv mpg123
na=jpg;getpg openjpeg
na=音频处理;getpg ffmpeg
hello='git(ee)';na=Git
getpg git
hello=AI智能
na=本地;getpg ollama
na=在线;getpg aichat
hello=网络
na=SSL;echo openssl:python已依赖
na=SSH;echo openssh:git已依赖
na=ndJS;getpg nodejs
na=下载器;getpg wget aria2
na=浏览器;getpg w3m
echo 使用node命令开始js
#管理包用npm,启用包用npx
echo node_pg:npx,npm
echo [http-server,mapscii,he...]
echo [准备包];npm update;echo [已完成]
#ping内置