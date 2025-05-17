var t=-2;v=-1;
var x=1;y=2;
var a=3;b=4;
var ans=0;str="";
min=Math.min;abs=Math.abs;max=Math.max;
sinr=Math.sin;cosr=Math.cos;tanr=Math.tan;
sqrt=Math.sqrt;
asinr=Math.asin;acosr=Math.acos;atanr=Math.atan;
exp=Math.exp;lg=Math.log10;ln=Math.log;
const pi=Math.PI;
const e=Math.E;
const phi=(sqrt(5)-1)/2;
function mathjs()
{
var varx=document.getElementById('varX').value;
var y=eval(varx);
document.getElementById('resx').innerHTML=y;
}
function bisjs()
{
var f=document.getElementById("varf").value,ss=document.getElementById("vars").value;
var aa=document.getElementById("vara").value,bb=document.getElementById("varb").value;
var y=bisec(f,ss,aa,bb);
document.getElementById("resx").innerHTML=y;
}
function sin(n)
{return sinr(n/180*pi);}
function cos(n)
{return cosr(n/180*pi);}
function tan(n)
{return tanr(n/180*pi);}
function asin(n)
{return asinr(n/180*pi);}
function acos(n)
{return acosr(n/180*pi);}
function atan(n)
{return atanr(n/180*pi);}
function dsh_j(n)
{
var ans=0,i=0;
for(i=1;i<=n;i++)//循环区间,条件
{ if(i%2!=0) {ans=1/i+ans;}}
//分母n%2不等于0,累加结果
return ans;//返回打印结果
}
function dsh(n)
{
var ans=0,x=0;
for(i=1;i<=n;i++)//循环区间,条件
{ans=1/i+ans;}//分母+1,累加结果
return ans;//返回打印结果
}
function sum(str,m,n)
{
var ans=0,x=0;
for(x=m;x<=n;x++)//循环区间,条件
{ans=ans+eval(str);}//x+1,累加结果
return ans;//返回打印结果
}
function fx(x,str)
{
var ans=eval(str);//计算函数值
return ans;
}
function bisec(str,s,a0,b0)
{
var a=a0,b=b0;//初始区间x∈(a0,b0)
while(abs(a-b)>=s)
{
c=(a+b)/2;
if(fx(a,str)*fx(c,str)<0)
{b=c;}//零点判断
else if(fx(c,str)==0)
{a=c;break;}
else
{a=c;}
}
tips="Use bisection method for f(x)="+str+"<br>";
return tips+"x≈"+a;//二分法
}