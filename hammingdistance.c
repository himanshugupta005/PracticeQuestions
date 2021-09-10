#include<stdio.h>
int hamming_distance(int, int);
void main()
{
    int num1, num2, hd;
    printf("enter the number");
    scanf("%d %d", &num1, &num2);
    hd= hamming_distance(num1, num2);
    printf("hamming_ distance is %d\n", hd);
}
int hamming_distance(int x, int y)
{
    int re, count=0;
    re=x^y;
    while(re>0)
    {
        count+=re&1;
        re=re>>1;
    }
    return 0;
}    
