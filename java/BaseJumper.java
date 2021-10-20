import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Stream;

class BaseJumper {
  public static void main(String[] args) {
    String[] arr = {"!", "!", "!"};
    while (!basesValid(arr) || !numberValid(arr[0], arr[1])) {
      String input = getInput("\nEnter a number, the current and desired bases seperated by commas: (ex. 100110, 2, 10)");
      arr = Arrays.stream(input.split(",")).map(String::trim).toArray(String[]::new);
    }

    System.out.println("\nResult: " + convert(arr[0], arr[1], arr[2]));
  }

  private static String getInput(String msg) {
    System.out.println(msg);
    Scanner s = new Scanner(System.in);
    String input = s.nextLine();
    return input;
  }

  public static boolean numberValid(String strNum, String strBase) {
    if (strNum == null) {
        return false;
    }
    try {
        int n = Integer.parseInt(strNum, Integer.parseInt(strBase));
    } catch (NumberFormatException err) {
        return false;
    }

    return true;
  }

  public static boolean inRange(int num, int min, int max) {
    return (num >= min && num <= max) ? true : false;
  }

  public static boolean basesValid(String[] arr) {
    return arr.length != 3 ||
        !Arrays.asList(arr).stream()
            .skip(1)
            .anyMatch(el -> !numberValid(el, "10") || !inRange(Integer.parseInt(el), 2, 16));
  }

  public static String convert(String numStr, String sourceBase, String targetBase) {
    int s = Integer.parseInt(sourceBase);
    int t = Integer.parseInt(targetBase);
    return Integer.toString(Integer.parseInt(numStr, s), t);
  }
}
