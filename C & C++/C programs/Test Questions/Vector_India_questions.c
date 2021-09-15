// Vector India programming questions

/*main()
{
int a=4,b=2;
a=b<<a+b>>2;
printf("%d",a);
}*/


/*main()
{
    int *ptr=(int *)malloc(sizeof(int));
    *ptr=4;
    printf("%d",(*ptr)+++*ptr++);
}*/


/*#define MAX 3
main()
{
    printf("MAX=%d\n",MAX);
    #undef MAX
    #ifdef MAX
    printf("Vector Institute");
    #endif // MAX
}*/


/*int array[]={1,2,3,4,5,6,7,8};
#define SIZE (sizeof(array)/sizeof(int))
main()
{
    if(-1<=SIZE)
        printf("1");

    else
        printf("2");
}*/


/*main()
{
int ptr[] = {1,2,23,6,5,6};
printf("%d",&ptr[3]-&ptr[0]);
}*/


/*main()
{
char input[] = "SSSWILTECH1\1\1";
int i, c;
for ( i=2; (c=input[i])!='\0'; i++) {
switch(c) {
case 'a': putchar ('i'); continue;
case '1': break;
case 1: while (( c = input[++i]) != '\1' && c!= '\0');
case 'E': case 'L': continue;
default: putchar(c);continue;
}
putchar(' ');
}
putchar('\n');
}*/


/*main()
{
int a[3][4] ={1,2,3,4,5,6,7,8,9,10,11,12} ;
int i, j , k=99 ;
for(i=0;i<3;i++)
for(j=0;j<4;j++)
if(a[i][j] < k) k = a[i][j];
printf("%d", k);
}*/


/*main()
{
    char p[] = "hello world!";
    p = "vector";
    printf("%s",p);
}*/


/*main()
{
enum _tag{ left=10, right, front=100, back};
printf("%d, %d, %d, %d", left, right, front, back);
}*/


/*main()
{
char as[] = "\\0\0";
int i = 0;
do{
switch( as[i++]) {case '\\' : printf("A");
break;
case 0 : printf("B");
break;
default : printf("C");
break;
}}
while(i<3);
}*/

/*#include<stdio.h>
main()
{
FILE *fs;
char c[10];
fs = fopen("source.txt", "r");
fseek(fs,0,SEEK_END);
fseek(fs,-3L,SEEK_CUR);
fgets(c,5,fs);
puts(c);
}*/


/*main()
{
int a=10,b;
b=a>=5?100:200;
printf("%d\n",b);
}*/


/*main()
{
extern int i;
i =20;
printf("%d\n",sizeof(i));
}*/


/*main()
{
int i = 10;
printf(" %d %d %d \n", ++i, i++, ++i);
}*/


/*main()
{
unsigned int k = 987 , i = 0;
char trans[10];
do {
trans[i++] =(char) (k%16 > 9 ? k%16 - 10 + 'a' : '\0' );
} while(k /= 16);
printf("%s\n", trans);
}*/


/*main()
{
struct test
{
char c;
int i;
char m;
} t1;
printf("%d %d\n", sizeof(t1), sizeof(t1.c));
}*/


/*main()
{
printf("%x",-1<<4);
}*/


/*main()
{
int var1=12, var2=35;
printf("%d",max(var1,var2));
}
int max(int x, int y)
{
    x>y?return x:return y;
}*/


/*main()
{
int x, arr[8]={11,22,33,44,55,66,77,88};
x=(arr+2)[3];
printf("%d",x);
}*/


/*struct tag{
    auto int x;
    static int y;
};
main()
{
    struct tag s;
    s.x=4;
    s.y=5;
    printf("%d",s.x);
}*/
