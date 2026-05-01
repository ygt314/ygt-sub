getpg()
{
echo $hello
apt install -y $@
}
hello=工具;na=busybox
getpg getconf screenfetch
#getconf LONG_BIT查看系统位数
getpg busybox termux-tools
na=tree;getpg $na
hello='C(gcc已内置)'
na=clang;getpg $na
hello='Shell math'
na=BC;getpg bc
na=gnuplot;getpg $na
hello=en-speak
na=speak;getpg espeak
hello=Python
na=python;getpg $na
hello=Rust
na=rust;getpg $na
apt upgrade python-pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
echo "apt search python:apt python page"
pip install -r requirements.txt
na=Math
getpg python-numpy python-scipy python-pyarrow
na=Image
getpg python-tkinter python-pillow matplotlib
na=xml;getpg python-lxml
hello=lua
na="Lua 5.4.7";getpg lua54
hello=mc文件管理器
na=mc;getpg $na
hello=文件处理
na=Vim;getpg vim
na=zip;getpg zip unzip gzip
na=doc;getpg pandoc grep gawk mandoc glow
na=play;getpg sox mpv mpg123
na=jpg;getpg openjpeg
na=音频处理;getpg ffmpeg
hello='git(ee,hub)';na=Git
getpg git
hello=AI智能
na=本地;getpg ollama tgpt
echo ollama需下载模型，tgpt自带模型
# tgpt自带模型，也可用API
hello=网络
na=SSL;echo openssl:python已依赖
na=SSH;echo openssh:git已依赖
na=ndJS;getpg nodejs
na=下载器;getpg wget aria2 yt-dlp
pip install you-get
#wget:网页下载 aria2c:高速多协议下载
#yt-dlp you-get:音视频提取
na=浏览器;getpg curl w3m
#curl(ie)网络请求，w3m网页浏览
#1. w3m 2. lynx 3. elinks 4. links2
echo 使用node命令开始js
#管理包用npm,启用包用npx
echo node_pg:npx,npm
echo [准备包];npm update;echo [已完成]
#ping内置