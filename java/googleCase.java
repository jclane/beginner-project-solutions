import java.util.Arrays;
import java.util.Scanner;

class googleCase {
  
  private static String googleFormat(String word) {
    return word.substring(0, 1).toLowerCase() + 
           word.substring(1, word.length()).toUpperCase();
  }

  private static String googleCasify(String str) {
    String[] strList = str.split("\\s+");
    StringBuilder sb = new StringBuilder();
    for (String word : strList) {
      sb.append(googleFormat(word));
      sb.append(" ");
    }

    return sb.toString();
  }
  
  private static String camelFormat(String word, Boolean firstWord) {
    if (firstWord) { return word.toLowerCase(); }
    return word.substring(0, 1).toUpperCase() +
           word.substring(1, word.length()).toLowerCase();    
  }
  
  private static String camelCasify(String str) {
    String[] strList = str.split("\\s+");
    StringBuilder sb = new StringBuilder();
    Boolean firstWord = true;
    for (String word : strList) {
      sb.append(camelFormat(word, firstWord));
      firstWord = false;
    }

    return sb.toString();
  }  
  
  public static void main(String[] args) {
    System.out.print("Enter sentence >> ");
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();
    System.out.printf("\nGoogle Case: %s", googleCasify(input));
    System.out.printf("\nCamel Case: %s", camelCasify(input));
  }
  
}
