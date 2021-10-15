import java.math.BigDecimal;
import java.util.concurrent.atomic.AtomicReference;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class ChangeCalculator {
  public static void main(String[] args) {
    boolean running = true;
    while (running) {
      BigDecimal totalCost = getMonetaryInput("Enter total cost");
      BigDecimal amountTendered = getMonetaryInput("Enter amount tendered");
      Map<String, Integer> coinsNeeded = getCoinsNeeded(calculateChange(amountTendered, totalCost));
      System.out.println(coinsNeeded);
      running = Character.toLowerCase(getInput("Continue? [y/n]: ").charAt(0)) == 'y';
    }
    System.out.println("\nQuitting...\n");
  }

  private static String getInput(String msg) {
    System.out.println(msg);
    Scanner s = new Scanner(System.in);
    String input = s.nextLine();
    return input;
  }

  private static BigDecimal getMonetaryInput(String msg) {
    msg = msg + " (ex. 2.47): ";
    BigDecimal value = new BigDecimal(getInput(msg));
    return value;
  }

  private static AtomicReference<BigDecimal> calculateChange(BigDecimal num1, BigDecimal num2) {
    return new AtomicReference<BigDecimal>(num1.subtract(num2));
  }

  private static Map<String, Integer> getCoinsNeeded(AtomicReference<BigDecimal> change) {
    Map<String, Integer> coinsNeeded = Stream.of(new Object[][] {
        {"Quarters", 0}, {"Dimes", 0}, {"Nickles", 0}, {"Pennies", 0}
    }).collect(Collectors.toMap(data -> (String) data[0], data -> (Integer) data[1]));

    Map<String, BigDecimal> valueMap = new LinkedHashMap<String, BigDecimal>();
    valueMap.put("Quarters", new BigDecimal("0.25"));
    valueMap.put("Dimes", new BigDecimal("0.10"));
    valueMap.put("Nickles", new BigDecimal("0.05"));
    valueMap.put("Pennies", new BigDecimal("0.01"));

    valueMap.forEach((coin, value) -> {
      while (change.get().subtract(value).compareTo(BigDecimal.ZERO) >= 0) {
        coinsNeeded.put(coin, coinsNeeded.get(coin) + 1);
        change.set(change.get().subtract(value));
      }
    });

    return coinsNeeded;
  }
}
