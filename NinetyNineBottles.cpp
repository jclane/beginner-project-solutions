#include <iostream>

int main() {
  int n = 99;

  while (n > 0) {
    printf("%d %s of beer on the wall! Take one down, pass it around.\n",
            n, n > 1 ? "bottles":"bottle");
    n--;
  }

  std::cout << "\nOh, no!  We're all out of beer!\n";

  return 0;
}
