import java.util.Scanner;
import java.lang.Math;
import java.util.HashMap;
import java.util.Random;

class Main {
  
  private int pScore = 0;
  private int cScore = 0;
  private boolean gameRunning = true;
  
  private void showScore() {
    System.out.println("\tCurrent Scores");
    System.out.println("\t----------------");
    System.out.println("\tPlayer  : " + pScore);
    System.out.println("\tComputer: "+ cScore + "\n");
  }

  private void showMenu() {
    System.out.println("WELCOME TO rockPaperScissors!");
    if (pScore > 0 || cScore > 0) {
      showScore();
    }
    System.out.println("1. rock");
    System.out.println("2. paper");
    System.out.println("3. scissors");          
  }

  private String getMove(int move) {
    HashMap<Integer, String> OPTIONS = new HashMap<>();
    OPTIONS.put(1, "rock");
    OPTIONS.put(2, "paper");
    OPTIONS.put(3, "scissors");
    return OPTIONS.get(move);
  }

  private boolean win(String playerMove, String compMove) {
    if (playerMove == "rock" && compMove != "paper") {
      return true;
    } else if (playerMove == "paper" && compMove != "rock") {
      return true;
    } else if (playerMove == "scissors" && compMove != "rock") {
      return true;
    } else {
      return false;
    }
  }

  private void round() {
    Scanner sc = new Scanner(System.in);
    System.out.println("\nMake your move! >> ");
    String playerMove = getMove(sc.nextInt());
    Random rand = new Random();
    String computerMove = getMove(rand.nextInt(3) + 1);
    
    System.out.println("\nYou chose: " + playerMove);
    System.out.println("Computer chose: " + computerMove);

    if (win(playerMove, computerMove)) {
      System.out.println("\nYou win!");
      pScore++;
    } else { 
      System.out.println("\nComputer wins!");
      cScore++;
    }
  }

  private void playAgain() {
    Scanner sc = new Scanner(System.in);
    System.out.println("Continue? [y/n] >> ");
    char response = sc.nextLine().toLowerCase().charAt(0);
    if (response == 'n') {
      showScore();
      gameRunning = false;
    }
  }

  public void run() {
    while (gameRunning == true) {
      showMenu();
      round();
      playAgain();
    }
  }

  public static void main(String[] args) { 
    Main game = new Main();
    game.run();
  }
  
}
