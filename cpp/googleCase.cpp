#include <iostream>
#include <locale>
#include <algorithm>
#include <vector>

int camelCase() 
{
  bool keepAsking{true};
  while (keepAsking)
  {
    std::string text = getInput();
    std::string newText = changeCase(text);
    printOutput(newText);
    keepAsking = continuePlaying();
  }

  return 0;
}

std::string getInput()
{
  std::string input;
  std::cout << "Enter some text:" << std::endl;
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  std::getline(std::cin, input);

  return input;
}

std::vector<std::string> split(std::string text)
{
  std::vector<std::string> stringVec;
  std::string word;
  int ndex = 0;
  for (char c : text)
  {
    if (c != ' ') {
      if (ndex == 0)
      {
        word += std::tolower(c);
      } else {
        word += std::toupper(c);
      }
      ndex++;
    } else {
      stringVec.push_back(word);
      ndex = 0;
      word = " ";
    }
  }

  return stringVec;
}

std::string changeCase(std::string text)
{
  std::vector<std::string> textSplit = split(text);
  std::string newText;
  std::for_each(std::begin(textSplit), std::end(textSplit),
    [&](const std::string &w) 
    {
      newText += w;
    }
  );

  std::cout << textSplit[textSplit.size() - 1] << std::endl;

  return newText;
}

void printOutput(std::string text)
{
  std::cout << text << std::endl;
}
