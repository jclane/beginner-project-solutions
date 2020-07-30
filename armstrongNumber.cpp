#include <iostream>
#include <cmath>

bool isNumber(const std::string s){
   for(int i = 0; i < s.length(); i++)//for each char in string,
      if(! (s[i] >= '0' && s[i] <= '9') ) return false;
   return true;
}

std::string getNumber()
{
  std::cout << "\nEnter a number:" << std::endl;
  std::string num;

  std::cin >> num;
  if (std::cin.fail())
  { 
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Invalid option.  Please try again." << std::endl;
  }

  return num;
}

bool isArmstrongNumber(const std::string num)
{
  const int n = num.length();

  int result = 0;
  for (int i = 0; i < n; i++)
  {
    result += std::pow(num[i] - '0', n);
  }

  return std::to_string(result) == num;
}

void armstrongNumber()
{
  bool keepAsking = true;
  while (keepAsking)
  {
    std::string num;
    bool validInput;
    do {
      num = getNumber();
      validInput = isNumber(num);
    } while (!validInput);

    std::cout << std::boolalpha << isArmstrongNumber(num) << std::endl;
    keepAsking = continuePlaying();
  }
}
