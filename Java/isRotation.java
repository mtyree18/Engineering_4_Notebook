public class isRotation{ 
   static boolean isRotation(String var1, String var2) {
       
      //variables
      String reverse = "";
      boolean isReverse = false;
      char ch;
      int test, pos;
      char firstLetter = var1.charAt(0);
      pos = var2.indexOf(firstLetter);
      
      //loop checking for same letters
      for (int i = 0; i < var1.length(); i++) {
        if (pos == var1.length()) {
            pos = 0;
            if (var1.charAt(i) != var2.charAt(pos)) {
                return false;
            }
            pos++;
        }
        System.out.print("i: " + i);
        System.out.print("pos: " + pos);
      }
      return true;
   }

   public static void main(String[] args) {
      isRotation("goat", "atgo");
   }

}
