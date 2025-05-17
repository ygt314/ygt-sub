function show_date_time(yg,yz)
{
window.setTimeout("show_date_time("+yg+","+yz+")", 1000);
today=new Date();yn=today.getFullYear();
var y1=yg,key1=y1+"年",y2=yz,key2=y2+"年";
if(yg+0==0)
{y1=yn;key1="今年";}
else if(yg==2026)
{key1="本届";}
if(yz+0==0)
{y2=yn;key2="今年";}
else if(yz==2023)
{key2="本届";}
var gaokaoDay=new Date(y1,5,7,9,0,0);//这个日期是湖南省高考时间(年份,6月,7日,9点,0分,0秒)
var zhongkaoDay=new Date(y2,5,18,9,0,0);//这个日期是湖南省中考时间(年份,6月,18日,9点,0分,0秒)
gaokaotimeold=(gaokaoDay.getTime()-today.getTime());
zhongkaotimeold=(zhongkaoDay.getTime()-today.getTime());
gaokaosectimeold=gaokaotimeold/1000;
zhongkaosectimeold=zhongkaotimeold/1000;
gaokaosecondsold=Math.floor(gaokaosectimeold);
zhongkaosecondsold=Math.floor(zhongkaosectimeold);
gaokaoseconds=gaokaosecondsold%60
zhongkaoseconds=zhongkaosecondsold%60
e_gaokaominsold=(gaokaosecondsold-gaokaoseconds)/60;
e_zhongkaominsold=(zhongkaosecondsold-zhongkaoseconds)/60;
gaokaominsold=e_gaokaominsold%60;
zhongkaominsold=e_zhongkaominsold%60;
e_gaokaohrsold=(e_gaokaominsold-gaokaominsold)/60;
e_zhongkaohrsold=(e_zhongkaominsold-zhongkaominsold)/60;
gaokaohrsold=e_gaokaohrsold%24;
zhongkaohrsold=e_zhongkaohrsold%24;
gaokaodaysold=(e_gaokaohrsold-gaokaohrsold)/24;
zhongkaodaysold=(e_zhongkaohrsold-zhongkaohrsold)/24;
if(gaokaosectimeold<=-226800)//高考结束后两天恢复高考显示
{gkcountdown.innerHTML="<div class=gkdjs><font><jljl>距离"+key1+"</jljl><jlgc>高考</jlgc></font><br><font class=sz>"+gaokaodaysold+"</font><font>天</font><br>"+gaokaohrsold+"小时"+gaokaominsold+"分"+gaokaoseconds+"秒"+"</div>";
} else if(gaokaosectimeold<=-115200)
{gkcountdown.innerHTML="<div class=gkdjs><font color=#f8c8a4>高考已结束</font><br/>预祝同学们金榜题名！</div>";
} else if(gaokaosectimeold<=0)
{gkcountdown.innerHTML="<div class=gkdjs><font color=#f8c8a4>高考进行中</font><br/>各位同学加油！</div>";
} else //显示倒计时
{gkcountdown.innerHTML="<div class=gkdjs><font><jljl>距离"+key1+"</jljl><jlgc>高考</jlgc></font><br><font class=sz>"+gaokaodaysold+"</font><font>天</font><br>"+gaokaohrsold+"小时"+gaokaominsold+"分"+gaokaoseconds+"秒"+"</div>";}
if(zhongkaosectimeold<=-226800)//中考结束后两天恢复中考显示
{zkcountdown.innerHTML="<div class=zkdjs><font><jljl>距离"+key2+"</jljl><jlzc>中考</jlzc></font><br><font class=sz>"+zhongkaodaysold+"</font><font>天</font><br>"+zhongkaohrsold+"小时"+zhongkaominsold+"分"+zhongkaoseconds+"秒"+"</div>";
} else if(zhongkaosectimeold<=-115200)
{zkcountdown.innerHTML="<div class=zkdjs><font color=#f8c8a4>中考已结束</font><br/>预祝同学们金榜题名！</div>";
} else if(zhongkaosectimeold<=0)
{zkcountdown.innerHTML="<div class=zkdjs><font color=#f8c8a4>中考进行中</font><br/>各位同学加油！</div>";
} else //显示倒计时
{zkcountdown.innerHTML="<div class=zkdjs><font><jljl>距离"+key2+"</jljl><jlzc>中考</jlzc></font><br><font class=sz>"+zhongkaodaysold+"</font><font>天</font><br>"+zhongkaohrsold+"小时"+zhongkaominsold+"分"+zhongkaoseconds+"秒"+"</div>";}
}
show_date_time(2026,2023);
