import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

class User {

  CoinMap coinMap = new CoinMap();
  Map<String, String> userCoins = new HashMap<String, String>();
  int totalCoins;
  double rollsNeeded;

  private int getTotalWeight(String coinType, String weightMeasurement, double weight) {
    double total = weight / coinMap.getWeight(coinType, weightMeasurement);

    return (int) Math.rint(total);
  }

  private double getTotalValue(String coinType, int count) {
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

  /**
   * Constructor for CoinMap class.
   */
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
  /*
  public static boolean validateCoinType(String inputStr) {
    for (String str: new String[] {"penny", "nickle", "dime", "quarter"}) {
      if (str.trim().contains(inputStr)) {
        return true;
      }
    }
    return false;
  }
  */

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
    for (String str: new String[] {"1", "2", "3", "4", "5", "6"}) {
      if (str.trim().contains(inputStr)) {
        return true;
      }
    }

    return false;
  }

  public static boolean validateInput(String inputType, String inputStr) {
    boolean result = false;
    switch (inputType) {
      case ("command"):
        result = validateCommands(inputStr);
        break;
      case ("weight"):
        result = validateCoinWeight(inputStr);
        break;
      default:
        result = false;;
    }

    return result;
  }

}

class MainMenu {

  String[] MENU = new String[7];
  InputValidator V = new InputValidator();
  private boolean keepAdding = true;

  /**
   * Constructor for MainMenu class.
   */
  public MainMenu() {
    MENU[0] = "\nCoins by weight:\n\n";
    MENU[1] = "\t1. Penny\n";
    MENU[2] = "\t2. Nickle\n";
    MENU[3] = "\t3. Dime\n";
    MENU[4] = "\t4. Quarter\n";
    MENU[5] = "\t5. Show me the money!\n";
    MENU[6] = "\t6. Quit\n";
  }

  /**
   * Print the menu.
   */
  public void showMenu() {
    StringBuilder sb = new StringBuilder();
    for (String str : this.MENU) {
      sb.append(str);
    }

    System.out.println(sb.toString());
  }

  public void setKeepAdding(boolean value) {
    this.keepAdding = value;
  }

  public boolean getKeepAdding() {
    return this.keepAdding;
  }

  public String getInput() {
    Scanner s = new Scanner(System.in);
    String input = s.nextLine();
    return input;
  }

  public Map<String, String> handleInput(String inputStr) {
    String coinType = "null";
    String msg;
    msg = "Enter total weight in grams [g] or pounds [lbs]:";
    switch (inputStr) {
      case "1":
        coinType = "penny";
        break;
      case "2":
        coinType = "nickle";
        break;
      case "3":
        coinType = "dime";
        break;
      case "4":
        coinType = "quarter";
        break;
      case "5":
        msg = "\nCalculating totals...\n";
        break;
      case "6":
        msg = "\nGoodbye.";
        break;
    }

    Map<String, String> response = new HashMap<String, String>();
    response.put("msg", msg);
    if (!coinType.equals("null")) {
      response.put("type", coinType);
      String inputWeight = "";
      do {
        System.out.println(response.get("msg"));
        inputWeight = getInput();
      } while (!V.validateInput("weight", inputWeight));
      response.put("weight", inputWeight);
    } else {
      if (inputStr.equals("5")) {
        response.put("type", "totals");
      } else {
        response.put("type", "quit");
      }
    }

    return response;
  }

}

class CoinByWeight {

  public static void main(String[] args) {
    MainMenu menu = new MainMenu();
    User user = new User();
    do {
      menu.showMenu();
      String input = "";
      do {
        System.out.println("Enter a command [1-6]:");
        input = menu.getInput();
      } while (!menu.V.validateInput("command", input));

      Map<String, String> inputResponse = new HashMap<String, String>();
      inputResponse = menu.handleInput(input);
      switch (inputResponse.get("type")) {
        case "quit":
          System.out.println(inputResponse.get("msg"));
          menu.setKeepAdding(false);
          break;
        case "totals":
          System.out.println(inputResponse.get("msg"));
          System.out.println(user.getResults());
          System.out.println("Continue? [y/n]");
          String cont = menu.getInput();
          String lowerCont = cont.toLowerCase();
          if (lowerCont.equals("n") | lowerCont.equals("no")) {
            menu.setKeepAdding(false);
          }
          break;
        default:
          user.userCoins.put(inputResponse.get("type"), inputResponse.get("weight"));
      }
    } while (menu.getKeepAdding());
  }

}
