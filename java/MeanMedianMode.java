import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class MeanMedianMode {
  public static void main(String[] args) {
    List<Integer> nums = getNums();

    String mean = getMean(nums);
    List<Integer> median = getMedian(nums);
    List<Integer> mode = getMode(nums);

    System.out.println("Mean: " + mean);
    System.out.println("Median: "
        + median.toString()
          .substring(1, median.toString()
          .length() - 1));
    System.out.println("Mode: " + mode.toString().substring(1, mode.toString().length() - 1));

  }

  private static List<Integer> getNums() {
    String numStr = getInput("Enter a list of numbers seperated by commas (ex. 1, 2, 3): ");
    return Stream.of(numStr.split(","))
        .map(String::trim)
        .map(Integer::parseInt)
        .collect(Collectors.toList());
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

  public static String getMean(List<Integer> nums) {
    double mean = (double) nums.stream().mapToInt(Integer::intValue).sum() / nums.size();
    return roundMean(mean);
  }

  public static List<Integer> getMedian(List<Integer> nums) {
    Collections.sort(nums);
    List<Integer> median = new ArrayList<Integer>();
    median.add(nums.get(nums.size() / 2));
    if (nums.size() % 2 == 0) {
      median.add(nums.get((nums.size() / 2) - 1));
    }

    return median;
  }

  public static List<Integer> getMode(List<Integer> nums) {
    Map<Integer, Long> counts = nums.stream()
        .collect(Collectors.groupingBy(e -> e, Collectors.counting()));
    Long max = counts.entrySet().stream()
          .max((a, b) -> a.getValue() > b.getValue() ? 1 : -1)
          .get().getValue();

    return counts.entrySet().stream()
        .filter(e -> e.getValue() == max)
        .map(e -> e .getKey())
        .collect(Collectors.toList());
  }
}
