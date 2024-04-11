#include <stdio.h>

int main() {

  int n;
  int sum = 0;
  int i=1;

  scanf("%d",&n);

  while(i<=n)
    {
      sum+=i;
      //printf("i:%d ",i);
      //printf("sum:%d\n",sum);
      i++;

    }

  printf("%d",sum);

  return 0;
}