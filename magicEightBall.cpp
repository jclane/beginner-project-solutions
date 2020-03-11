#include <functional>
#include <iostream>
#include <limits>
#include <random>
#include <string>
#include <unistd.h>

int magicEightBall()
{
  bool keepAsking{true};
  while (keepAsking)
  {
    getQuestion();
    think();
    printAnswer();
    keepAsking = continuePlaying();
  }

  return 0;
}

std::string getQuestion()
{
  std::cout << "Enter your question:" << std::endl;
  std::string question;

  std::cin >> question;
  if (std::cin.fail())
  {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Invalid option.  Please try again." << std::endl;
    getQuestion();
  }

  return question;
}

void think()
{
  std::cout << "\nHmmmm...\nLet me consult my friends on the other side..." <<
              std::endl;
  sleep(5);
}

int getRandomNum() 
{
  std::random_device rd; // obtain a random number from hardware
  std::mt19937 mt(rd()); // seed the generator
  std::uniform_int_distribution<> range(1, 20); // define the range
  
  return range(mt);
}

void printAnswer()
{
  int randomNum{getRandomNum()};
  std::string answer;
  switch (randomNum)
  {
    case 0:
      answer = "It is certain.";
      break;
    case 1:
      answer = "It is decidedly so.";
      break;
    case 2:
      answer = "You may rely on it.";
      break;
    case 3:
      answer = "As I see it, yes.";
      break;
    case 4: 
      answer = "Most likely.";
      break;
    case 5: 
      answer = "Outlook good.";
      break;
    case 6: 
      answer = "Yes.";
      break;
    case 7: 
      answer = "Signs point to yes.";
      break;
    case 8: 
      answer = "Reply hazy, try again";
      break;
    case 9: 
      answer = "Ask again later.";
      break;
    case 10: 
      answer = "Better not tell you now.";
      break;
    case 11: 
      answer = "Cannot predict now.";
      break;
    case 12: 
      answer = "Concentrate and ask again.";
      break;
    case 13: 
      answer = "Don't count on it.";
      break;
    case 14: 
      answer = "My reply is no.";
      break;
    case 15: 
      answer = "My sources say no.";
      break;
    case 16: 
      answer = "Outlook not so good.";
      break;
    case 17: 
      answer = "Very doubtful.";
      break;
    case 18:
      answer = "You are better off not knowing.";
      break;
    case 19:
      answer = "Only time will tell.";
      break;
  }

  std::cout << answer << std::endl;
}

bool continuePlaying()
{
  std::cout << "Continue [y/n]?" << std::endl;
  char response{'z'};
  std::cin >> response;

  if (std::cin.fail())
  {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Invalid option.  Please try again." << std::endl;
  }


  return (response == 'y') ? true : false;
}
