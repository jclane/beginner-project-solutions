#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>

std::vector<int> commaDelimitedSplit(std::string sidesStr)
{
  std::vector<int> result;
  std::string temp_ = "";
  for (int i = 0; i < sidesStr.length(); i++)
  {
    char c = sidesStr[i];
    if (c == ' ') {
      temp_ = "";
      continue;
    } 
    
    if (c == ',') {
      int num = 0;
      std::stringstream ss(temp_);
      ss >> num;
      result.push_back(num);
      temp_ = "";
      continue;
    } 
    
    if (c != ' ' && c != ',') {
      temp_ += c;
      if (i == sidesStr.length() - 1) {

        int num = 0;
        std::stringstream ss(temp_);
        ss >> num;
        result.push_back(num);
        temp_ = "";        
      }
    } 
  }
  
  return result;
}

std::string getSides()
{
  std::string sides;
  std::cout << "Enter triangle sides [ex. 3, 4, 6]:" << std::endl;
  std::cin.clear();
  std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  std::getline(std::cin, sides);

  return sides;
}

bool isPythagoreanTriple(std::vector<int> sides)
{
  if (std::pow(sides[0], 2) + std::pow(sides[1], 2) == std::pow(sides[2], 2)) {
    return true;
  }
  if (std::pow(sides[1], 2) + std::pow(sides[2], 2) == std::pow(sides[0], 2)) {
    return true;
  }
  if (std::pow(sides[2], 2) + std::pow(sides[0], 2) == std::pow(sides[1], 2)) {
    return true;
  }

  return false;
}

void checkPythagoreanTriple()
{
  std::string sidesStr = getSides();
  std::vector<int> sides = commaDelimitedSplit(sidesStr);
  std::cout << "\nIs Pythagorean Triple: " << std::boolalpha << isPythagoreanTriple(sides) << std::endl;

}
