import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

class Coin {
  String type;
  Double[] weight;
  double value;
  int rolls;

  public Coin(String coinType) {
    Map<String, Double> valueMap = new HashMap<String, Double>();
    valueMap.put("penny", 0.01);
    valueMap.put("nickle", 0.05);
    valueMap.put("dime", 0.10);
    valueMap.put("quarter", 0.25);

    Map<String, Double[]> weightMap = new HashMap<String, Double[]>();
    weightMap.put("penny", new Double[] {2.50, 0.0055115565546});
    weightMap.put("nickle", new Double[] {5.00, 0.011023113109});
    weightMap.put("dime", new Double[] {2.268, 0.0050000841064});
    weightMap.put("quarter", new Double[] {5.67, 0.012698626302});

    Map<String, Integer> rollMap = new HashMap<String, Integer>();
    rollMap.put("penny", 50);
    rollMap.put("dime", 40);
    rollMap.put("nickle", 50);
    rollMap.put("quarter", 40);

    this.type = coinType;
    this.weight = weightMap.get(coinType);
    this.value = valueMap.get(coinType);
    this.rolls = rollMap.get(coinType);
  }

  public String getType() {
    return this.type;
  }

  public double getWeight(String weightMeasurement) {
    double weight = (weightMeasurement.equals("g")) ? this.weight[0] : (weightMeasurement.equals("lbs")) ? this.weight[1] : null;
    return weight;
  }

  public double getValue() {
    return this.value;
  }

  public int getRolls() {
    return this.rolls;
  }

}

class CoinByWeight {

  public static void main(String[] args) {
    List<Coin> userTotal = new ArrayList<Coin>();
    String input = askForInput();
    if (validateInput(input)) {
      System.out.println("VALID INPUT");
      userTotal.add(createCoin(input));
    } else {
      System.out.println("NOT VALID");
    }
    System.out.println(userTotal);
  }

  public static boolean validateInput(String inputStr) {
    for (String str: new String[] {"penny", "nickle", "dime", "quarter"}) {
      if (str.trim().contains(inputStr)) {
        return true;
      }
    }
    return false;
  }

  public static Coin createCoin(String coinType) {
    return new Coin(coinType);
  }

  public static String askForInput() {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Enter coin type:");
    String input = scanner.nextLine();
    return input;
  }
}
