// -----C - Quizzes-----

/*#include<stdio.h>
main()
{
    char ch;
    for(ch='0';ch<=255;ch++)
        printf("%c", ch);
}*/

/*int main()
{
    char *p;
    printf("%d %d ", sizeof(*p), sizeof(p));
    getchar();
    return 0;
}*/

/*int main()
{
  char arr[]  = "geeksforgeeks";
  char *ptr  = arr;
  while(*ptr != '\0')
      ++*ptr++;//here value of *ptr and ptr is incremented
  printf("%s",arr);
  return 0;
}*/

/*int main()
{
 int c=5;
 printf("%d\n%d\n%d", c, c <<= 2, c >>= 2);
}*/

/*main()
{
    float f=1.5;
    double d=1.5;
    if(d==f)
    {
        printf("same");
    }
    else
    {
        printf("different");
    }
}*/

/*#include<stdio.h>
main()
{
  while(printf("%d",printf("az")))
   printf("by");
}*/

/*#include<stdio.h>
int main()
{
    int i=-3, j=2, k=0, m;
    m = ++i || ++j && ++k;
    printf("%d, %d, %d, %d\n", i, j, k, m);
    return 0;
}*/

/*#include<stdio.h>
 int main()
 {
     char ch;
     ch = 'A';
     printf("The letter is");
     printf(" %c", ch >= 'A' && ch <= 'Z' ? ch + 'a' - 'A':ch);
     printf("\nNow the letter is");
     printf(" %c", ch >= 'A' && ch <= 'Z' ? ch : ch + 'a' - 'A');
     return 0;
}*/

/*#include<stdio.h>
int main()
{
    int a[] = {10, 20, 30, 40, 50};
    int j;
    for(j=0; j<5; j++)
        {
            printf("%d\n", a);
            a++;
        }
    return 0;
}*/

/*#include<stdio.h>
void main() { int x = 97; int y = sizeof(x++); printf("x is %d", x); }*/

/*#include<stdio.h>
void main() { char *s = "hello"; char *p = s; printf("%p\t%p", p, s); }*/

/*#include<stdio.h>
#define foo(m, n) m * n = 10
int main() { printf("in main\n"); }*/

/*#include <stdio.h>
#include <string.h>
void swap(char *x, char *y)
{
char temp;
temp = *x;
*x = *y;
*y = temp;
}
void permute(char *a, int l, int r)
{
int i;
if (l == r)
printf("%s\n", a);
else
{
for (i = l; i <= r; i++)
{
swap((a+l), (a+i));
permute(a, l+1, r);
swap((a+l), (a+i)); //backtrack
}
}
}
int main()
{
char str[] = "ABC";
int n = strlen(str);
permute(str, 0, n-1);
return 0;
}*/

/*#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char *str1 = malloc(6 * sizeof(char));
    char *str2 = malloc(6 * sizeof(char));
    char *str3 = malloc(6 * sizeof(char));
    printf("ENter 3 words :");
    scanf("%s%s%s", str1, str2, str3);
    int p1 = strlen(str1);
    int p2 = strlen(str2);
    int p3 = strlen(str3);
    for (int i = 0; i < p1; i++)
    {
        if (str1[i] == 'a' || str1[i] == 'e' || str1[i] == 'i' || str1[i] == 'o' || str1[i] == 'u')
        {
            str1[i] = '$';
        }
    }
    for (int i = 0; i < p2; i++)
    {
        if (str2[i] != 'a' && str2[i] != 'e' && str2[i] != 'i' && str2[i] != 'o' && str2[i] != 'u')
        {
            str2[i] = '#';
        }
    }
    for (int i = 0; i < p3; i++)
    {
        str3[i] = str3[i] - 32;
    }

    printf("%s", str1);
    printf("%s", str2);
    printf("%s", str3);

    return 0;
}*/

/*#include <stdio.h>
int main()
{
    int a[5] = {1, 53, 3, 4, 5};
    int i;
    for (i = 0; i < 5; i++)
        if ((char)a[i] == '5')
            printf("%d\n", a[i]);
        else
            printf("FAIL\n");
}*/

/*#include<stdio.h>
int main()
{
   int n;
   for(n = 7; n!=0; n--)
     printf("n = %d", n--);
   getchar();
   return 0;
}*/

/*#include<stdio.h>
int main()
{
   printf("%x", -1<<1);
   getchar();
   return 0;
}*/

/*#include <stdio.h>
int main()
{
static int a[]={0,1,2,3,4};
int *p[]={a,a+1,a+2,a+3,a+4};
int**ptr=p;
ptr++;
printf("%d %d %d \n",ptr-p,*ptr-a,**ptr);
++ptr;
printf("%d %d %d \n",ptr-p,*ptr-a,**ptr);
}*/

/*char* getString()
{
 static   char str[] = "Will I be printed?";
    printf("%s\n",str);
    return str;
}
int main()
{
    char *p=getString();
    printf("%s", p);
    getchar();
}*/

/*int main()
{
    static int i=5;
    if(--i){
        main();//all calls to main share same i
        printf("%d ",i);
    }
}*/

/*int main()
{
    int x,y,t;
    t=scanf("%d%d",&x,&y);//scanf() returns no. of inputs
    printf("%d",t);
    return 1;
}*/

/*#include <stdio.h>
int main()
{
   printf("\new_c_question\by");
   printf("\rgeeksforgeeks");// \r goes back to start of the line and starts printing characters
   return 0;
}*/

/*# include<stdio.h>
# include<stdlib.h>
int* fun()
{
    int *a;
    a = (int*)malloc(sizeof(int));
    return(a);
}
int main()
{
    int *p;
    p=fun();
    *p = 6;
    printf("%d\n",*p);
    getchar();
    return(0);
}*/

/*#include <stdio.h>
int main()
{
    int i;
    i = (1, 2, 3);//Associativity of comma operator is from left to right
    printf("i  = %d\n", i);
    getchar();
     return 0;
}*/

/*int main()
{
    char a[2][3][3] = {'g','e','e','k','s','f','o','r','g','e','e','k','s'};
    printf("%s ", **a);
    getchar();
    return 0;
}*/

/*int main()
{
   char str[]= "geeks\nforgeeks";
   char *ptr1, *ptr2;
   ptr1 = &str[3];
   ptr2 = str + 5;
   printf("%c", ++*str - --*ptr1 + *ptr2 + 2);
   printf("%s", str);
   return 0;
}*/

/*#include <stdio.h>
int main()
{
    int c = 5, no = 1000;
    do {
        no /= c;
    } while(c--);//It goes inside the do-while loop for c = 0 also

    printf ("%d\n", no);
    return 0;
}*/

/*int main()
{
    while(1)
    {
        if(printf("\n%d",printf("%d",254)))//printf always returns the no. of bytes it has output
            break;
        else
            continue;
    }
    return 0;
}*/

/*int main()
{
    unsigned int i=10;
    while(--i >= 0)
        printf("%u ",i);
    return 0;
}*/

/*#include <stdio.h>
    void reverse(int);
    int main()
    {
        reverse(1);
    }
    void reverse(int i)
    {
        if (i > 5)
            return ;
        printf("%d ", i);
         reverse((++i,++i));
    }*/

/*#include <stdio.h>
    int x = 0;
    int main()
    {
        int i = (f() + g()) || g();
        int j = g() || (f() + g());
        printf("%d %d",i,j);
    }
    int f()
    {
        if (x == 0)
            return x+1;
        else
            return x-1;
    }
    int g()
    {
        return x++;
    }*/

/*int main()
{
    unsigned int i=4294967295;
    while ( i++ != 0 );
    printf("%d",i);
    return 0;
}*/
