//Tomohiko Sakamoto算法(2),来确定当前日期是星期几
int dow(int y,int m,int d)
{
    y-=m<3;
    return(y+y/4-y/100+y/400+"-bed=pen+mad."[m]+d)%7;
}