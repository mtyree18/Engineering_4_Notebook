public class removeAll{
  static String removeAll(String var1, String character) {
    int remove;
    String var1New = "There were no matching characters";
    remove = var1.indexOf(character);
      for (int i = 0; i < var1.length(); i++) {
        char c = var1.charAt(i);
        String current = String.valueOf(c);
          if (current.equals(character)) {
            var1New = var1.replace(character, "");
          }
      }
    System.out.print(var1New);
    return var1New;
  }
public static void main(String[]args){
    removeAll("google", "o");
}
}
