#include<stdio.h>
#include<math.h>
//int add()
int main()
{
    double m,n,ans;
    char j;
    while(1)
    {
    printf("Hello math!>>>");
    scanf("%lf %c %lf",&m,&j,&n);
    switch(j)
    {
    case '+': ans=m+n;break;
    case '-': ans=m-n;break;
    case '*': ans=m*n;break;
    case '/': ans=m/n;break;
    case '^': ans=pow(m,n);break;
    case '<': m<n?printf("true\n"):printf("false\n");continue;
    case '>': m>n?printf("true\n"):printf("false\n");continue;
    case 'q': printf("Bye bye!\n");return 0;
    default : printf("string error or no support\n");continue;
    }
    printf("%g\n",ans);
    }
}