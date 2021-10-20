import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Fibonacci {
  
  public static void main(String[] args) {
    boolean running = true;
    while (running) {
      String option = getOption();
      if (option.startsWith("q")) {
        break;
      } else {
        int num = getNumber();
        int result =  option.startsWith("l") ? fibonacciLoop(num) : fibonacciRecursive(num);
        System.out.println(result);
      }
    }
  }

  private static boolean validOption(String optionInput) {
    String option = optionInput.toLowerCase();
    if (!option.equals("") && option.startsWith("l") || option.startsWith("r") || option.startsWith("q")) {
      return true;
    }
    
    return false;
  }

  private static String getOption() {
    String option = "";
    while (!validOption(option)) {
      option = getInput("Use loop method or rescursive method? >> ['l', 'r', or 'q' to quit]: ");
    }
    
    return option;
  }
  
  public static boolean isNumeric(String strNum) {
    if (strNum == null) {
        return false;
    }
    try {
        int n = Integer.parseInt(strNum);
    } catch (NumberFormatException err) {
        return false;
    }
    return true;
  }

  private static int getNumber() {
    String numStr = "";
    while (!isNumeric(numStr)) {
      numStr = getInput("Enter a number: ");
    }
    
    return Integer.parseInt(numStr);
  }

  private static String getInput(String msg) {
    System.out.println(msg);
    Scanner s = new Scanner(System.in);
    String input = s.nextLine();
    return input;
  }
  
  public static int fibonacciLoop(int num) {
    List<Integer> sequence = new ArrayList<Integer>();
    int count = num;
    int num1 = 0;
    int num2 = 1;
      
    int i = 1;
    while (i < count) {
      int result = num1 + num2;
      num1 = num2;
      num2 = result;
      sequence.add(result);
      i++;
    }
      
    return sequence.get(sequence.size() - 1);
  }

  public static int fibonacciRecursive(int num) {
    if (num < 2) {
      return num;
    }
    
    return fibonacciRecursive(num - 1) + fibonacciRecursive(num - 2);
  }
}
