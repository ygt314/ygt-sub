vvf=~/.htmrc;vj=0
mymas=https://gitee.com/ygt314159/subject-termux/raw/master
#下载play音乐
down_mu()
{
echo 下载play音乐
bash ~/zhtmlf/music/player/flac/down.sh
bash ~/zhtmlf/music/player/wav/down.sh
echo 下载完成
}
#下载函数棋
down_fn()
{
cd ~/zhtmlf;echo 下载函数棋
curl $mymas/zhtmlf/fnchess_1.0.0.zip > fncs.zip;echo 下载完成
unzip fncs.zip -d 函数棋1.0.0;echo 安装完成
}
#识别版本
if [ -e $vvf ];then
    zvz=$(head -1 $vvf)
else
    zvz=x
fi;xvx=$(curl $mymas/.htmrc|head -1)
if [ x$zvz = x$xvx ];then
    echo zhtmlf is new
    echo 该版本已经最新
else
    vj=1
fi
#更新zhtmlf
if [ $vj = 1 ];then
    curl $mymas/.htmlrc>$vvf
    curl $mymas/zhtmlf/zhtmlf.zip>zhf.zip
    if [ -e zhtmlf ];then
        cd ~/zhtmlf
    else
        mkdir zhtmlf;cd ~/zhtmlf
    fi;unzip -o zhf.zip && rm zhf.zip
    down_mu;down_fn
fi