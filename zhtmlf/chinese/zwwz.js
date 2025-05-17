function emb(mb,n,rw)
{
var vn=document.getElementById(mb).value;//varweb-resweb
var varweb="https://easylearn.baidu.com/edu-page/tiangong/composition/search-list?query="+vn+"&grade=21&sort=智能排序"
if(n==1)
{
window.alert("即将跳转");
window.location.replace(varweb);
}
else
{document.getElementById(rw).src=varweb;}
}
function emb1(mb,n,rw)
{
var vn=document.getElementById(mb).value;//varweb-resweb
var varweb="https://easylearn.baidu.com/edu-page/tiangong/composition/?locSign=&query="+vn+"&grade=21&index=0&sort=智能排序"
if(n==1)
{
window.alert("即将跳转");
window.location.replace(varweb);
}
else
{document.getElementById(rw).src=varweb;}
}
function bdzw(bd,n,rw)
{
var zw=document.getElementById(bd).value;//varweb-resweb
var varweb="https://hanyu.baidu.com/zuowen?from=hanyu_index#/list?wd="+zw;
if(n==1)
{
window.alert("即将跳转");
window.location.replace(varweb);
}
else
{document.getElementById(rw).src=varweb;}
}
function rwzw(bd,n,rw)
{
var zw=document.getElementById(bd).value;//varweb-resweb
var varweb=`https://so.ruiwen.com/#!kw=${zw}!!`;
if(n==1)
{
window.alert("即将跳转");
window.location.replace(varweb);
}
else
{document.getElementById(rw).src=varweb;}
}
function znbd(bd,n,rw)
{
var zw=document.getElementById(bd).value;//varweb-resweb
var varweb="https://zhannei.baidu.com/cse/search?s=15991277701392786341&entry=1&q="+zw;
if(n==1)
{
window.alert("即将跳转");
window.location.replace(varweb);
}
else
{document.getElementById(rw).src=varweb;}
}