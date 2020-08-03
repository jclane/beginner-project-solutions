#include <iostream>
#include <map>

int getComputerMove()
{
  return std::rand() % 3 + 1;
}

int getSelection()
{
  std::cout << "\nEnter selection [1-3]: " << std::endl;
  int num;

  std::cin >> num;
  if (std::cin.fail() || num > 3 || num < 1)
  { 
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Invalid option.  Please try again." << std::endl;
  }

  return num;
}

void showGameMenu()
{
  std::cout << "\nWelcome to ROCK.PAPER.SCISSORS (*EXTREME*)\n" << std::endl;
  std::cout << "1. Rock\n2. Paper\n3. Scissors" << std::endl;
}

bool didPlayerWin(int playerMove, int computerMove)
{

  switch (playerMove)
  {
    case 1:
      return (computerMove == 3);
    case 2:
      return (computerMove == 1);
    case 3:
      return (computerMove == 2);
  }

  return false;
}

bool anotherRound()
{
  std::cout << "Continue playing? [y/N]" << std::endl;
  std::string resp;

  std::cin >> resp;
  if (std::cin.fail())
  { 
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Invalid option.  Please try again." << std::endl;
  }

  return (std::tolower(resp[0]) == 'y');
}

void rockPaperScissors()
{
  struct score {
    int wins = 0;
  } player, computer;

  std::map<int, std::string> moves;
  moves[1] = "Rock";
  moves[2] = "Paper";
  moves[3] = "Scissors";

  std::srand(time(NULL));

  bool keepPlaying = true;
  while (keepPlaying)
  {
    showGameMenu();
    if (player.wins || computer.wins) {
      std::cout << "\nPlayer wins: " << player.wins << " / Computer wins: " << computer.wins << std::endl;
    }

    int playerMove = getSelection();
    int computerMove = getComputerMove();
    while (computerMove == playerMove)
    {
      computerMove = getComputerMove();
    }
    
    std::cout << "\nPlayer has selected: " << moves[playerMove] << std::endl;
    std::cout << "Computer has selected: " << moves[computerMove] << std::endl;
    
    if (didPlayerWin(playerMove, computerMove)) {
      std::cout << "You win!" << std::endl;
      player.wins++;
    } else {
      std::cout << "You lose!" << std::endl;
      computer.wins++;
    }

    keepPlaying = anotherRound();
  }
}
