#include <stdio.h>

int main(void) 
{
  int x = 20;
  int y = 30;

  printf("x = %i\n", x);  
  printf("y = %i\n", y);

  // swapping
  int temp = x;
  x = y;
  y = temp;


  printf("x is now = %i\n", x);  
  printf("y is now = %i\n", y);
}