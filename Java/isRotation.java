public class isRotation{ 
   static boolean isRotation(String var1, String var2) {
       
      //variables
      String reverse = "";
      boolean isReverse = false;
      char ch;
      firstLetter = var1[0];
      
      test = indexOf(var2 firstLetter);
      System.out.print(test);
   }
}
        /*  
      }
      //reverses var1
      for (int i=0; i < var1.length(); i++) {
         ch = var1.charAt(i);
         reverse = ch + reverse;
      }
      
      //checks if the reversed var1 is equal to var2, and if it is it returns true, otherwise it returns false
      System.out.println(var1);
      System.out.println(reverse);
      if (reverse.equals(var2) == true){
         isReverse = true;
      }
      else if (reverse.equals(var2) == false){
         isReverse = false;
      }
      System.out.println(isReverse);
      return (isReverse);
   }
   
   public static void main(String[] args) {
      isRotation("racecar", "racecar");
   }
}
