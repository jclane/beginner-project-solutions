import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Hangman {
  String word;
  String[] blanks;
  int wrongGuesses;
  boolean running;
  String hangMan;
  final Map<Integer, String> WRONG_GUESS = Stream.of(new Object[][] {
      {0, " _____\n |   |\n     |\n     |\n     |\n     |\n     |\n ____|___\n"},
      {1, " _____\n |   |\n O   |\n     |\n     |\n     |\n     |\n ____|___\n"}, 
      {2, " _____\n |   |\n O   |\n |   |\n     |\n     |\n     |\n ____|___\n"}, 
      {3, " _____\n |   |\n O   |\n/|   |\n     |\n     |\n     |\n ____|___\n"}, 
      {4, " _____\n |   |\n O   |\n/|\\  |\n     |\n     |\n     |\n ____|___\n"}, 
      {5, " _____\n |   |\n O   |\n/|\\  |\n/    |\n     |\n     |\n ____|___\n"}, 
      {6, " _____\n |   |\n O   |\n/|\\  |\n/\\   |\n     |\n     |\n ____|___\n"},
  }).collect(Collectors.toMap(data -> (Integer) data[0], data -> (String) data[1]));
    
  public static void main(String[] args) {
    boolean running = true;
    while (running) {
      Hangman game = new Hangman();
      game.run();
      running = keepPlaying();
    }
  }
  
  private void run() {
    this.word = getRandomWord();
    this.blanks = new String[this.word.length()];
    this.wrongGuesses = 0;
    this.running = true;
    Arrays.fill(this.blanks, "_");
    print(this.hangMan);
    while (this.running) {
      String guess = getInput("Guess a letter:").toUpperCase();
      handleGuess(guess);
    }
  }
 
  private static String getRandomWord() {
    final String[] WORDS = {"HANGMAN", "CAVEMAN", "BATMAN", "CATMAN", "DUDEMAN", "HEMAN", "MANMAN"};
    Random rand = new Random();
    return WORDS[rand.nextInt(WORDS.length)];
  }
  
  private static String getInput(String msg) {
    System.out.println(msg);
    Scanner s = new Scanner(System.in);
    String input = s.nextLine();
    return input;
  }

  private static void print(String msg) {
    System.out.println(msg);
  }
  
  private void handleWrongGuess() {
    print(this.WRONG_GUESS.get(this.wrongGuesses));
  }

  private List<Integer> getIndices(String guess) {
    List<Integer> indices = new ArrayList<Integer>();
    int index = this.word.indexOf(guess);
    while (index >= 0) {
        indices.add(index);
        index = this.word.indexOf(guess, index + 1);
    }
    
    return indices;
  }

  private String[] updateBlanks(String guess) {
    final List<Integer> indices = getIndices(guess);
    for (int i : indices) {
      blanks[i] = new String(guess);
    }
    
    return blanks;
  }

  private void handleEndGame(String msg) {
    print(msg);
    this.running = false;
  }
  
  private void handleGuess(String guess) {
    if (this.word.contains(guess)) {
      updateBlanks(guess);
      if (String.join("", blanks).equals(this.word)) {
        handleEndGame("You win!");
      }
    } else {
      this.wrongGuesses++;
      hangMan = handleWrongGuess();
      if (this.wrongGuesses >= 6) {
        handleEndGame("You lose.\nThe word was: " + this.word);
      }
    }
    print(hangMan);
    print(String.join("", blanks));    
  }
}
