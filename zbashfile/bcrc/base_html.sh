str=$1;img_s='<img src="';img_e='">';hh='base_html.html'
echo "<html>";echo "<html>">$hh
if [ -z $1 ];then
    echo "base_str:";read str
fi;img=$img_s$str$img_e
clear;echo "<html>"
echo $img;echo $img>>$hh
echo "</html>";echo "</html>">>$hh