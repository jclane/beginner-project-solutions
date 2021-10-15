import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Arrays;
import java.util.Scanner;

class MeanMedianMode {
  public static void main(String[] args) {
    int[] nums = new int[]{1, 2, 3, 980, 324, 4298};
    String mean = getMean(nums);
    System.out.println(mean);
  }

  private static String getInput(String msg) {
    System.out.println(msg);
    Scanner s = new Scanner(System.in);
    String input = s.nextLine();
    return input;
  }
  
  public static String roundMean(Double num) {
    int decimalPlaces = Integer.parseInt(getInput("Enter number of decimal places to round to: "));
    BigDecimal bd = new BigDecimal(Double.toString(num));
    bd = bd.setScale(decimalPlaces, RoundingMode.HALF_UP);
    return Double.toString(bd.doubleValue());
  }
  
  public static String getMean(int[] nums) {
    double mean = (double) Arrays.stream(nums).sum() / nums.length;
    return roundMean(mean);
  }
}
