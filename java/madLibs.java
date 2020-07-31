import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class madLibs {
  
  private static String getInput(String msg) {
    System.out.print(msg);
    Scanner sc = new Scanner(System.in);
    
    return sc.nextLine();   
  }
  
  public static void main(String[] args) {
    
    System.out.printf("\nThis is the story:\n" +
                      "\n\tThe %s %s %s %s over the %s.\n\n",
                     "[adjective]", "[adjective]", "[noun]",
                     "[verb]", "[adjective]", "[noun]");
    
    String[] msgs = {
      "Please enter an adjective >> ",
      "PLease enter another adjective >> ",
      "Please enter a noun >> ",
      "Please enter a verb >> ",
      "Please enter an adjective >> ",
      "Please enter a noun >> ",
    };
    
    List<String> inputs = new ArrayList<String>();
    for (String msg : msgs) {
      inputs.add(getInput(msg));
    }
       
    System.out.printf("\nThe %s %s %s %s over the %s %s.\n",
                     inputs.get(0), inputs.get(1), inputs.get(2),
                     inputs.get(3), inputs.get(4), inputs.get(5));    
  }
  
}
