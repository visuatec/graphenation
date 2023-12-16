#include <stdio.h>

void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}
int main(void) 
{
  int x = 20;
  int y = 30;

  printf("x = %i\n", x);  
  printf("y = %i\n", y);

  // swapping
  swap(&x, &y);


  printf("x is now = %i\n", x);  
  printf("y is now = %i\n", y);
}