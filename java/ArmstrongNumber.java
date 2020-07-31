import java.lang.Math;
import java.util.Scanner;

class ArmstrongNumber {

  private static Scanner sc = new Scanner(System.in);

  private static boolean isNumeric(final String str) {
    return str.matches("-?\\d+?"); // match a number with optional '-' and decimal.
  }

  private static String getInput(String msg) {
    System.out.println(msg);
    String input = "";

    if (sc.hasNextLine()) {
      input = sc.nextLine();
    }

    return input;
  }

  private static boolean isArmstrongNumber(final String num) {
    int result = 0;
    for (int i = 0; i < num.length(); i++) {
      result += Math.pow((double) num.charAt(i) - '0', (double) num.length());
    }

    return result == Integer.parseInt(num);
  }

  private static boolean continuePlaying() {
    System.out.println("Would you like to check another number?");
    String resp = "";

    if (sc.hasNextLine()) {
      resp = Main.sc.nextLine();
    }

    return resp.toUpperCase().charAt(0) == 'Y';
  }

  public static void main(String[] args) {
    boolean keepAsking = true;

    while (keepAsking) {
      String num = "";
      boolean isValidNumber = false;
      while (!isValidNumber) {
        num = getInput("Enter a number:");
        isValidNumber = isNumeric(num);
      }

      System.out.println(isArmstrongNumber(num));
      keepAsking = continuePlaying();
    }
  }
}
