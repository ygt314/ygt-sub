function to2b(str)
{
let str1=""
for(let i of str)
{
    if(i==="+")
    {str1+="%2B";}
    else
    {str1+=i;}
}
return str1
}
function getweb(resw,txtw)
{
    var varweb=document.getElementById(resw).src;
    document.getElementById(txtw).innerHTML=varweb;
}
function dra_rep(ww,n,rw)
{
    if(n==1)
    {
    window.alert("即将跳转");
    window.location.replace(ww);
    }
    else
    {document.getElementById(rw).src=ww;}
}
function dra_rep1(ww,n,rw)
{
    if(n==1)
    {
    window.alert("即将跳转");
    window.location.replace(ww);
    }
    else
    {
    alert("该网站不支持画中画");
    document.getElementById(rw).src=ww;
    }
}
function myweb(vw,n,rw)
{
    var varweb=document.getElementById(vw).value;//varweb-resweb
    varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function myweb_opt(v,w,n,rw)
{
    var varweb=document.getElementById(v).value+document.getElementById(w).value;//varweb-resweb
    varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function mybai(vb,n,rw)
{
    var bai=document.getElementById(vb).value;//varbai-resweb
    var varweb=`https://m.baidu.com/from=844b/s?word=${bai}`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function my360(vs,n,rw)
{
    var so=document.getElementById(vs).value;//vs-rw
    var varweb=`http://m.so.com/s?q=${so}`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function myvk(vk,n,rw)
{
    var vk=document.getElementById(vk).value;//vk-rw
    var varweb=`https://www.kuaishou.com/search/video?searchKey=${vk}`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function mydou(vd,n,rw)
{
    var dou=document.getElementById(vd).value;//vd-rw
    var varweb=`https://www.douyin.com/search/${dou}?aid=d7ebeda6-3bb8-4a02-b6bd-e941ab907704&publish_time=0&sort_type=0&source=normal_search&type=general`;varweb=to2b(varweb);
    dra_rep1(varweb,n,rw);
}
function mybi(vb,n,rw)
{
    var bili=document.getElementById(vb).value;//vb-rw
    var varweb=`https://m.bilibili.com/search?keyword=${bili}`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function dhzh(zh,n,rw)
{
    var duhan=document.getElementById(zh).value;//mh-rw
    var varweb=`https://hanyu.baidu.com/s?wd=${duhan}`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function myhan(mh,n,rw)
{
    var duhan=document.getElementById(mh).value;//mh-rw
    var varweb=`https://hanyu.baidu.com/sentence/search?from=aladdin&gssda_res={}&query=${duhan}&smpid=&srcid=51328&tab_type=&wd=${duhan}&ret_type=sentence-multi`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function duhan1(dh,n,rw)
{
    var duhan=document.getElementById(dh).value;//dh-rw
    var varweb=`https://hanyu.baidu.com/hanyu-page/sentence/index?from=aladdin&gssda_res={}&query=${duhan}&smpid=&srcid=51328&tab_type=&wd=${duhan}&ret_type=sentence-multi&sid=92275e132f8b380462f6dafa31d7147f&type=sentence&pn=1&ps=20&index=0`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function trans(vfb,n,rw)
{
    var word=document.getElementById(vfb).value;//vfb-rw
    var varweb=`https://fanyi.baidu.com/#en/zh/${word}`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function checal(n,rw)
{
    var varweb="./chemistry/ChemCalcu-master/";//(all)-rw
    dra_rep(varweb,n,rw);
}
function mybj(eb,n,rw)
{
    var word=document.getElementById(eb).value;//eb-rw
    var varweb=`https://easylearn.baidu.com/edu-page/tiangong/composition/search-list?query=${word}&sort=智能排序`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function meta(mt,n,rw)
{
    var word=document.getElementById(mt).value;//mt-rw
    var varweb=`https://metaso.cn/?q=${word}`;varweb=to2b(varweb);
    dra_rep(varweb,n,rw);
}
function woal(wa,n,rw)
{
    var word=document.getElementById(wa).value;//wo-rw
    var varweb=`https://www.wolframalpha.com/input?i=${word}`;varweb=to2b(varweb);
    dra_rep1(varweb,n,rw);
}
function qcemb(qc,n,rw)
{
    var word=document.getElementById(qc).value;//qcem-rw
    var varweb=`https://zh.webqc.org/molecular-weight-of-${word}.html`;varweb=to2b(varweb);
    dra_rep1(varweb,n,rw);
}
function qcequ(qc,n,rw)
{
    var word=document.getElementById(qc).value;//qceq-rw
    var varweb=`https://zh.webqc.org/balance.php?reaction=${word}`;varweb=to2b(varweb);
    dra_rep1(varweb,n,rw);
}
function nujs(nu,n,rw)
{
    var word=document.getElementById(nu).value;//qceq-rw
    var varweb=`https://zh.numberempire.com/expressioncalculator.php?function=${word}&result_type=expression&_p1=2337`;varweb=to2b(varweb);
    dra_rep1(varweb,n,rw);
}
function nufa(nu,n,rw)
{
    var word=document.getElementById(nu).value;//qceq-rw
    var varweb=`https://zh.numberempire.com/factoringcalculator.php?function=${word}&_p1=2337`;varweb=to2b(varweb);
    dra_rep1(varweb,n,rw);
}
function nusi(nu,n,rw)
{
    var word=document.getElementById(nu).value;//qceq-rw
    var varweb=`https://zh.numberempire.com/simplifyexpression.php?function=${word}&_p1=2337`;varweb=to2b(varweb);
    dra_rep1(varweb,n,rw);
}
function nueq_x(nu,n,rw)
{
    var word=document.getElementById(nu).value;//qceq-rw
    var varweb=`https://zh.numberempire.com/equationsolver.php?function=${word}&var=x&result_type=false&answers=&_p1=2337`;varweb=to2b(varweb);
    dra_rep1(varweb,n,rw);
}
function m3u8_hx(mm,n,rw)
{
    var url=document.getElementById(mm).value;//m3u8_url
    var varweb=`https://m.haixingdmx.com/hdst/player/artplayer/index.html?url=${url}`;
    dra_rep(varweb,n,rw);
}
function hx_dm(hx,n,rw)
{
    var word=document.getElementById(mm).value;//dm_word
    var varweb=`https://m.haixingdmx.com/hdst/player/artplayer/index.html?url=${word}`;
    dra_rep(varweb,n,rw);
}