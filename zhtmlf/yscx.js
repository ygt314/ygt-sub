function pn(num)
{
var yne=yse[num];
var ync=ysc[num];
var ypn=num+"--"+yne+"--"+ync;
if(num<0)
{
    ypn=num+"-->"+"无意义"
}
if(num>118)
{
    ypn=num+"-->"+"迄今为止只有118个元素"
}
return ypn;
}
function pne(num)
{
var yne=yse[num];
var ypne=num+"--"+yne;
if(num<0)
{
    ypne=num+"-->"+"无意义"
}
if(num>118)
{
    ypne=num+"-->"+"迄今为止只有118个元素"
}
return ypne;
}
function pnc(num)
{
var ync=ysc[num];
var ypnc=num+"--"+ync;
if(num<0)
{
    ypnc=num+"-->"+"无意义"
}
if(num>118)
{
    ypnc=num+"-->"+"迄今为止只有118个元素"
}
return ypnc;
}
function ys(m,n)
{
var str="";
for(var i=m;i<n;i++)
{
    str+=pn(i)+"&nbsp;&nbsp;";
    if(i%5==0)
    {
        str+="<br>";
    }
    else if(i>=118)
    {
        str+="<br>";
    }
}
str+=pn(i);
return str;
}
function ysb()
{
var str="";
str+=ys(0,20);
return str;
}