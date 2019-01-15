import java.util.Scanner;
import java.util.Random;
import java.lang.Thread;

class Main {

  private static void ask() {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a question: ");
    if (sc.hasNextLine()) {
      String q = sc.nextLine();
    }
  }

  private static void respond() {
    final String[] RESPONSE = { "It is certain.", "It is decidedly so.",
                                "Without a doubt.", "Yes - definitely.",
                                "You may rely on it.", "As I see it, yes.",
                                "Most likely.", "Outlook good.", "Yes.",
                                "Signs point to yes.", "Reply hazy, try again",
                                "Ask again later.", "Better not tell you now.",
                                "Cannot predict now.",
                                "Concentrate and ask again.",
                                "Don't count on it.", "My reply is no.",
                                "My sources say no.", "Outlook not so good.",
                                "Very doubtful." };
    Random rand = new Random();
    System.out.println(RESPONSE[rand.nextInt(20)] + "\n");
  }

  private static void think() {
    System.out.println("Thinking...");
    try {
      for (int i = 0; i < 4; i++) {
        Thread.sleep(4000);
      }
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }

  private static void playAgain() {
    Scanner ask = new Scanner(System.in);
    System.out.println("Ask another question?");
    if (ask.hasNextLine()) {
      String answer = ask.nextLine().substring(0).toLowerCase();
      if (answer.equals("y")) {
          return;
      } else {
          System.exit(0);
      }
    }
  }

  public static void main(String[] args) {
    while (true) {
      ask();
      think();
      respond();
    }
  }
}
