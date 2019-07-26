import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

class User {
  CoinMap coinMap = new CoinMap();
  Map<String, String> userCoins = new HashMap<String, String>();
  int totalCoins;
  double rollsNeeded;

  public int getTotalWeight(String coinType, String weightMeasurement, double weight) {
    double total = weight / coinMap.getWeight(coinType, weightMeasurement);
    return (int) Math.rint(total);
  }

  public double getTotalValue(String coinType, int count) {
    double total = count * coinMap.getValue(coinType);
    return total;
  }

  public String getResults() {
    StringBuilder sb = new StringBuilder();
    Map<String, Integer> totalCoins = new HashMap<String, Integer>();
    Map<String, Double> coinValueTotals = new HashMap<String, Double>();

    double totalValue = 0;

    for (Map.Entry<String, String> entry : userCoins.entrySet()) {
      String type = entry.getKey();
      String weight = entry.getValue();
      String weightMeasurement = (weight.endsWith("g")) ? "g" : "lbs";
      int coinsTotal = getTotalWeight(type, weightMeasurement, Double.parseDouble(weight.replace(weightMeasurement, "")));
      totalCoins.put(type, coinsTotal);
      coinValueTotals.put(type, getTotalValue(type, coinsTotal));
    }

    sb.append("\nTotal coins: ");
    for (Map.Entry<String, Integer> entry : totalCoins.entrySet()) {
      String type = (entry.getValue() > 0.01) ? (entry.getKey().equals("penny")) ? "pennies" : entry.getKey() + "s" : entry.getKey();
      double value = coinValueTotals.get(entry.getKey());
      totalValue += value;
      sb.append(String.format("\n\t" + type + ": " + Integer.toString(entry.getValue()) + " ($ %.2f)", value));
    }

    sb.append(String.format("\n\nTotal value: $ %.2f", totalValue));
    return sb.toString();
  }

}

class CoinMap {
  Map<String, Double> valueMap = new HashMap<String, Double>();
  Map<String, Double[]> weightMap = new HashMap<String, Double[]>();
  Map<String, Integer> rollMap = new HashMap<String, Integer>();

  public CoinMap() {
    valueMap.put("penny", 0.01);
    valueMap.put("nickle", 0.05);
    valueMap.put("dime", 0.10);
    valueMap.put("quarter", 0.25);
    weightMap.put("penny", new Double[] {2.50, 0.0055115565546});
    weightMap.put("nickle", new Double[] {5.00, 0.011023113109});
    weightMap.put("dime", new Double[] {2.268, 0.0050000841064});
    weightMap.put("quarter", new Double[] {5.67, 0.012698626302});
    rollMap.put("penny", 50);
    rollMap.put("dime", 40);
    rollMap.put("nickle", 50);
    rollMap.put("quarter", 40);
  }

  public double getWeight(String typeStr, String weightMeasurement) {
    double weight = (weightMeasurement.equals("g")) ? weightMap.get(typeStr)[0] : (weightMeasurement.equals("lbs")) ? weightMap.get(typeStr)[1] : null;
    return weight;
  }

  public double getValue(String typeStr) {
    return valueMap.get(typeStr);
  }

  public int getRolls(String typeStr) {
    return rollMap.get(typeStr);
  }

}

class InputValidator {
  public static boolean validateCoinType(String inputStr) {
    for (String str: new String[] {"penny", "nickle", "dime", "quarter"}) {
      if (str.trim().contains(inputStr)) {
        return true;
      }
    }
    return false;
  }

  public static boolean validateCoinWeight(String inputStr) {
    String numWithWeightType = inputStr;
    String numStr = "";
    for (String str: new String[] {"g", "lbs"}) {
      if (numWithWeightType.endsWith(str.trim())) {
        numStr = numWithWeightType.replace(str.trim(), "");
        break;
      }
    }

    try {
      double num = Double.parseDouble(numStr);
    } catch (NumberFormatException | NullPointerException nfe) {
      return false;
    }
    return true;
  }

  public static boolean validateCommands(String inputStr) {
    String inputLower = inputStr.toLowerCase();
    for (String str: new String[] {"y", "n", "yes", "no"}) {
      if (str.trim().contains(inputLower)) {
        return true;
      }
    }
    return false;
  }

  public static boolean validateInput(String inputType, String inputStr) {
    if (inputType.equals("type")) {
      return validateCoinType(inputStr);
    } else if (inputType.equals("weight")) {
      return validateCoinWeight(inputStr);
    } else {
      return validateCommands(inputStr);
    }
  }

}

class CoinByWeight {
  public static void main(String[] args) {
    User user = new User();
    boolean keepAdding = true;
    while (keepAdding) {
      String coin = askForInput("type");
      String weight = askForInput("weight");
      user.userCoins.put(coin, weight);
      keepAdding = Boolean.parseBoolean(askForInput("quit"));
    }
    System.out.println(user.getResults());
  }

  public static String askForInput(String inputType) {
    Scanner s = new Scanner(System.in);
    InputValidator v = new InputValidator();
    String input = "null";
    String msg = "";
    switch (inputType) {
      case "type":
        msg = "Enter coin type:";
        break;
      case "weight":
        msg = "Enter total coin weight followed by g or lbs:";
        break;
      case "quit":
        msg = "Keep adding? [y/n] ";
        break;
    }

    while (!v.validateInput(inputType, input)) {
      System.out.println(msg);
      input = s.nextLine();
      if (inputType.equals("quit")) {
        if (input.toLowerCase().startsWith("y")) {
          return "true";
        } else {
          return "false";
        }
      }
    }
    return input;
  }
}
