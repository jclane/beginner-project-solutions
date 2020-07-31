import java.util.Scanner;
import java.lang.Math;

class Main {

  private static boolean checkPythagoreanTriple(String str) { 
    String[] temp = str.split(" ");
    int[] nums = new int[temp.length];
    for (int i = 0; i < temp.length; i++) {
      nums[i] = Integer.parseInt(temp[i]);
    }
    if (Math.pow(nums[0], 2) + Math.pow(nums[1], 2) == Math.pow(nums[2], 2)) {
      return true;
    }
    if (Math.pow(nums[1], 2) + Math.pow(nums[2], 2) == Math.pow(nums[0], 2)) {
      return true;
    }
    if (Math.pow(nums[2], 2) + Math.pow(nums[0], 2) == Math.pow(nums[1], 2)) {
      return true;
    }
    return false;
  }

  public static void main(String[] args) {
    while (true) {
      Scanner sc = new Scanner(System.in);
      System.out.println("\nEnter three numbers seperated by a space [3 4 5] >>  ");
      String input = sc.nextLine();
      System.out.println(checkPythagoreanTriple(input));
    }
  }
}
