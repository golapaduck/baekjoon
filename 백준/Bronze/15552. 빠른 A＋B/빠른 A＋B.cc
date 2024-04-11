#include <stdio.h>

int main() {

  int T;

  int Tarr1[999999], Tarr2[999999],sumarr[999999];

  scanf("%d",&T);

  for(int i=0; i<T; i++){
    scanf("%d %d",&Tarr1[i],&Tarr2[i]);
    sumarr[i]=Tarr1[i]+Tarr2[i];
  }

    for(int i=0; i<T; i++){
    printf("%d\n",sumarr[i]);
  }


  return 0;
}