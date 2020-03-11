#include <iostream>

int ninetyNineBottles() 
{
  int bottles{99};

  while (bottles > 0) 
  {
    printf("\n%d %s of beer on the wall!\nTake one down, pass it around.\n",
                 bottles, 
                 bottles > 1 ? "bottles":"bottle");
    --bottles;
  }

  std::cout << "\nOh, no!  We're all out of beer!\n";

  return 0;
}
