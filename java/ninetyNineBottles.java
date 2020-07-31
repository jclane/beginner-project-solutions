class Main {
  public static void main(String[] args) {
    for (int beers = 99; beers > -1; beers--) {
      if (beers > 0) {
        System.out.println(String.format("%s %s of beer on the wall.", beers, (beers > 1 ? "bottles":"bottle")));
        System.out.println("Take one down, pass it around.");
        System.out.println(String.format("%s %s of beer on the wall\n.", beers - 1, (beers > 1 ? "bottles":"bottle")));
      } else { 
        System.out.println("Oh, no!  We're all out of beer!");
      }
    }
  }
}
