let sysz=[3293,6093];
let sysm=[124,215];
let sysn=[25,14];
var sn=666;
function syht(an,num)
{
sn=sysm[an];
if(num<=0|num>sysn[an])
{
window.alert("一共有"+sysn[an]+"章");
return sn+".html";
}
else
{return sn+"_"+(sysz[an]+eval(num))+".html";}
}