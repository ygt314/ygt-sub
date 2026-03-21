function nxn(num)
{
if(num<=0|num>60)
{
window.alert("一共有60页");
return "01.htm";
}
var nh=num+".htm";
if(num<10)
{return "0"+nh;}
else
{return nh;}
}