import java.util.Scanner;

class HigherOrLower {
  public static void main(String[] args) {
    int randomNum = generateRandomNum();
    showIntro();

    boolean running = true;
    while (running) {
      int guesses = 0;
      boolean winning = false;
      while (!winning) {
        int guess = Integer.parseInt(getInput("\nGuess (ex. 1-100): "));
        guesses++;
        winning = handleGuess(guess, randomNum);
      }

      running = keepPlaying();
      if (running) {
        randomNum = generateRandomNum();
        showIntro();
      } else {
        System.out.println("It took you " + guesses + " guesses to guess correctly.");
      }
    }
  }

  public static int generateRandomNum() {
    return (int) Math.round(Math.random() * 100);
  }

  private static void showIntro() {
    System.out.println("High or Lower: The Number Guessing Game");
    System.out.println("\nHOW TO PLAY:");
    System.out.println("\n\t* I have selected a number between 1 and 100.");
    System.out.println("\t* You must input a number in an effort to guess the number I have selected.");
    System.out.println("\t* If the number you have guessed is too low, I will tell you.");
    System.out.println("\t* Likewise, if the number is too high, I will also tell you that.");
  }

  private static String getInput(String msg) {
    System.out.println(msg);
    Scanner s = new Scanner(System.in);
    String input = s.nextLine();
    return input;
  }

  private static boolean handleGuess(int guess, int randomNum) {
    if (guess < randomNum) {
      System.out.println("Higher.");
    } else if (guess > randomNum) {
      System.out.println("Lower.");
    } else if (guess == randomNum) {
      System.out.println("Congratulations you have guessed correctly!");
      return true;
    }

    return false;
  }

  private static boolean keepPlaying() {
    return getInput("Would you like to keep playing? [y/n]").equals("y");
  }
}
