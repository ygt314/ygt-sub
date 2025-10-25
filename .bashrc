zbash=/sdcard/zbashfile;mp3f=~/mym/mp3
m4af=~/mym/m4a;myf=$HOME;mcl=$myf/clang
source ~/autoclearc
echo "日历:";cal
chmod 777 ~/*.py;chmod 777 ~/*.sh
source ~/.cnrc;source ~/.htmrc
source ~/.mathrc;cngt_d
source ~/.cmstrc;source ~/.bcrc
source ~/.subrc;source ~/.enrc
source ~/.pwrc;source ~/.mypwrc
source ~/.pyrc;source ~/startcmdrc
cdf()
{
cd $zbash
}
cdh()
{
cd ~/zhtmlf/html
source html_txtrc
}
math()
{
~/math.sh $1
}
pff()
{
~/pff.sh $1
}
run_()
{
ps3="$PS3"
PS3="run_choice:"
select rn in py sh bash c cd exe
do
    if [ ! -z $rn ];then
        break
    fi
done;PS3=$ps3
}
run()
{
rn=$1;if [ -z $1 ];then
    run_;read -p file: -e run_f
    run $rn ${run_f:-run}
fi;if [ -z $1 ];then
    rn=run
fi;echo "run_$rn:>$2"
case $rn in
    py)python $2;;
    sh)sh $2;;
    bash)bash $2;;
    c)gcc $2.c -lm -o $mcl/exe/$2.o
    cd $mcl/exe;run exe $2.o;cd -;;
    exe)chmod +x $2;./$2;;
    run)echo run [type] [file];;
    *)echo not understand;;
esac
}
m4a_mp3()
{
ffmpeg -i $1 -vn -ar 44100 -ac 2 -ab 192K -f mp3 ~/downloads/my.mp3
echo "mp3>:~/downloads/my.mp3"
}
nb()
{
nt=$2;n=$1
if [ -z $1 ] || [ "$1"x = -hx ] || [ "$1"x = --helpx ];then
    echo "nb [music] [times] [a(dd)|r(an)|o(↻)]"
    echo you can use;return 0
fi;if [ -z $2 ];then
    nt=1
fi;for i in $(seq 1 $nt)
do
    nbf=~/$n.mp3;mpv $nbf
    case $3 in
        a)j=1;;
        r)j=$(ran 6);;
        *)j=0;;
    esac;n=$((j+n));n=$((n%6))
done
}
input_str()
{
put=""
while [ -z $put ]
do
    echo -n "$1";read put
done
if [ ! -z $2 ];then
    eval "$2=$put"
fi
}
put()
{
if [ "$1"x = intx ];then
    input_int $2 $3
elif [ "$1"x = strx ];then
    input_str $2 $3
fi
}
echo py_c:clear python_history
py_c()
{
echo 520>~/.python_history
}
echo vim_c:clear viminfo
vim_c()
{
rm ~/.viminfo
}