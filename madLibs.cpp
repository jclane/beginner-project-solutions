#include <iostream>

std::string getWord(const std::string wordType)
{
  std::string a_or_an = (wordType[0] == 'a') ? "an" : "a";
  std::cout << "Please enter " << a_or_an << " " << wordType << std::endl;
  std::cin.clear();
  std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  std::string word;
  std::cin >> word;

  return word;
}

void printStory(const std::string words[7])
{
  printf("\nThe %s %s %s %s over the %s %s.\n",
         words[0].c_str(), words[1].c_str(), words[3].c_str(),
         words[5].c_str(), words[2].c_str(), words[4].c_str());

  printf("\nI %s %s, but I didn't %s the %s.\n",
         words[5].c_str(), words[6].c_str(),
         words[5].c_str(), words[4].c_str());
}

void madLibs()
{
  std::string wordTypes[7] = {"adjective", "adjective",
                              "adjective", "noun",
                              "noun", "verb", "name"
                             };

  for (int i = 0; i < 7; i++)
  {
    wordTypes[i] = getWord(wordTypes[i]);
  }
  
  printStory(wordTypes);
}
