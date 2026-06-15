vvf=~/.htmrc;vj=0
mymas=https://gitee.com/ygt314159/subject-termux/raw/master
myre=https://gitee.com/ygt314159/subject-termux/releases/download/
#下载zhtmlf
down_zh()
{
cd;echo 下载zhtmlf
curl -L $myres/zhtmlf.zip > zhtmlf.zip;echo 下载完成
[ -e zhtmlf ] && echo 删除旧版本 && rm -rf zhtmlf
echo 安装新版本;unzip zhtmlf.zip -d zhtmlf
cd;echo 安装完成
}
#下载play音乐播放器
down_mu()
{
cd ~/zhtmlf/music;echo 下载play音乐播放器
curl -L $myres/player.zip > player.zip;echo 下载完成
[ -e player ] && echo 删除旧版本 && rm -rf player
echo 安装新版本;unzip player.zip -d player
cd;echo 安装完成
}
#下载函数棋
down_fn()
{
cd ~/zhtmlf;echo 下载函数棋
curl -L $myres/zhtmlf/fnchess_1.0.0.zip > fncs.zip;echo 下载完成
[ -e 函数棋1.0.0 ] && echo 删除旧版本 && rm -rf 函数棋1.0.0
echo 安装新版本;unzip fncs.zip -d 函数棋1.0.0
cd;echo 安装完成
}
#识别版本
if [ -e $vvf ];then
    zvz=$(head -1 $vvf)
else
    zvz=x
fi;xvx=$(curl -L $mymas/.htmrc|head -1)
if [ x$zvz = x$xvx ];then
    echo zhtmlf is new
    echo 该版本已经最新
else
    vj=1
fi
#更新zhtmlf
if [ $vj = 1 ];then
    curl -L $mymas/.htmrc>$vvf
    source $vvf;myres=$myre/$vn
    down_zh;down_mu;down_fn
fi