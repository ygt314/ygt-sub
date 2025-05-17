function nxn(num)
{
if(num<=0|num>60)
{
window.alert("一共有60页");
return "01.htm";
}
if(num<10)
{num+=0;return "0"+num+".htm";}
else
{return num+".htm";}
}