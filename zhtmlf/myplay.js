var murl="music/METAMORPHOSIS - INTERWORLD.mp3",playn=0;
function musu(id)
{
var mu=document.getElementById(id),y=1;
if(mu.paused) {y=0;}
return y;
}
function pmsu(id,re)
{
var playm=document.getElementById(id);
if(musu(id)==1)
{
    document.getElementById(re).innerHTML="播放";
} else {
    document.getElementById(re).innerHTML="暂停";
}
}
function mplay(id,re)
{
// var playm=new Audio(murl),id='myplay';
var playm=document.getElementById(id);
if(musu(id)==0|playn==0)
{
    playn=1;playm.play();//播放mp3这个音频对象
} else {
    playm.pause();//暂停
    // player.load();
}
pmsu(id,re);
}