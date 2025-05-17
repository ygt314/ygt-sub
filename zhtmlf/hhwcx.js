function hhw(str)
{
var hpn=hhwe.indexOf(str);
var hpc=hhwc[hpn];
if(hpn==-1)
{
    hpc=hhwen(str);
}
var hp=str+"--"+hpc;
return hp;
}
function hhwen(str1)
{
var hpn=hhwc.indexOf(str1);
var hp=hhwe[hpn];
if(hpn==-1)
{
    hp="不存在";
}
return hp;
}