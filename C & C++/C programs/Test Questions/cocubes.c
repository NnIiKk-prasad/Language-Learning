// Cocubes programming questions

/*#include <stdio.h>
#include <stdlib.h>

int main()
{
int a[6] ={16, 19, 4, 3, 8, 3};
int i,j,n,flag =0;
n=sizeof(a)/sizeof(a[0]);
printf("Hello Nikhil Going to get the leader letters !\n");
for(i=0;i<n;i++)
{
    flag=1;
    for(j=i+1;j<n;j++)
    {
        if(a[i]<a[j])
            { flag=0; break;}
    }
    if(flag==1)
       { printf("%d\n",a[i]); }
}
return 0;
}*/

/*#include <stdio.h>
#include <stdlib.h>
int max_diff(int[],int);
void main()
{
    int n,arr[]={2, 3, 10, 6, 4, 8, 1};
    n=sizeof(arr)/sizeof(arr[0]);
    printf("Maximum diff= %d",max_diff(arr,n));
}
int max_diff(int arr[],int n)
{
    int round,i,temp,diff;
    for(round=1;round<=n;round++)
    {
        for(i=0;i<=n-round-1;i++)
        {
            if(arr[i]>arr[i+1])
            {
                temp=arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
            }
        }
    }
    diff=arr[n-1]-arr[0];
    return(diff);
}*/

/*#include <stdio.h>
#include <stdlib.h>
main()
{
    int n,m;
    printf("Enter the values for n & m:");
    scanf("%d%d",&n,&m);
    if(m==0)
        printf("m should not be zero");
    else
        printf("The number closest to %d and divisible by %d is %d\n",n,m,clst_num(n,m));
    getchar();
}
int clst_num(int n,int m)
{
    int q,n1,n2;
    q=n/m;
    n1=q*m;
    if(n*m>0)
        n2=m*(q+1);
    else
        n2=m*(q-1);
    if(abs(n-n1) < abs(n-n2))
        return(n1);
    return(n2);
}*/

/*#include <stdio.h>
#include <stdlib.h>
main()
{
    char s[]="1C1B1B0A0";
    printf("%c",bool_expr(s));
}
int bool_expr(char s[])
{
    int i,n;
    n=strlen(s);
    for(i=0;i<n;i+=2)
    {
        switch(s[i+1])
        {
            case 'A':
                if(s[i]=='0'||s[i+2]=='0')
                    s[i+2]='0';
                else
                    s[i+2]='1';
                     break;
            case 'B':
                if(s[i]=='1'||s[i+2]=='1')
                    s[i+2]='1';
                else
                    s[i+2]='0';
                      break;
            case 'C':
                if(s[i]==s[i+2])
                    s[i+2]='0';
                else
                    s[i+2]='1';
                    break;
            default: break;
        }
    }
    return(s[n-1]);
}*/

/*#include<stdio.h>
#include<string.h>
int palin(char *ptr)
{
char *s,*s1;
s=ptr;
s1=ptr+strlen(ptr)-1;
while(s1>s)
{
if(*s!=*s1)
{
return 0;
}
s++;
s1--;
}
return 1;
}
void main()
{
int i,j,flag=1,cnt=0,k=0;
char *ptr,str[200],str1[50];
printf("\nEnter input string\n");
scanf("%s",str);
ptr=str;
while(flag==1)
{
j=palin(ptr);
if(j==1)
{
break;
}
else{
str1[k++]=*ptr;
ptr++;
cnt++;

}
}
str1[k++]='\0';
printf("%d\n",cnt);
printf("%s",strrev(str1));

}*/

/*#include <stdio.h>
#include<stdlib.h>
int main()
{
char str[1000] = "aaaaabbbccccccccdaa";
char str_err [10] = "invalid";
int i,count,length;
for(i=0;str[i]!='\0';i++);
length = i;
i = 0;
count = 0;
while(i < length)
{
if(str[i] == str[i+1])
count ++;
else
{
if(count == 1)
printf("%c ",str[i]);
else if(count <= 9)
printf("%c%d ",str[i],count);
else
{
printf("%c",str[i]);
printf("%s ",str_err);
}
count = 1;
}
i++;
}
return 0;
}*/

/*#include<stdio.h>
int lcm(int,int);
int main(){
int a,b,c,l,k;
printf("Enter any three positive integers ");
scanf("%d%d%d",&a,&b,&c);
l = lcm(a,b);
k= lcm(l,c);
printf("LCM(%d,%d,%d)= %d",a,b,c,k);
return 0;
}

int lcm(int a,int b){
int temp;
for(temp=a>b?a:b;temp<=a*b;temp++)
if(temp % a == 0 && temp % b == 0)
break;
return temp;
}*/
