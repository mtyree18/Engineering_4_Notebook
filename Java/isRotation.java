public class isRotation{ 
    static boolean isRotation(String var1, String var2) {
       
        //variables
        boolean endValue = true;
        int pos;
        char firstLetter = var1.charAt(0);
        pos = var2.indexOf(firstLetter);
      
        //loop checking for same letters
        for (int i = 0; i < var1.length(); i++) {
            
            //says that if the first letter from var1 isn't found in var2, then break the loop
            if (pos < 0) {
                endValue = false;
                break;
            }
            
            if (var1.length() != var2.length()) {
                endValue = false;
                break;
            }
            
            //says to reset the position to 0 if it gets to the end 
            if (pos == var1.length()) {
                pos = 0;
            }
            if (var1.charAt(i) != var2.charAt(pos)) {
                endValue = false;
                break;
                System.out.println("i: " + i);
                System.out.println("pos: " + pos);
                System.out.println("letter at pos: " + var2.charAt(pos));
                System.out.println("letter at i: " + var1.charAt(i));
            }
        pos++;
        }
    System.out.println("endValue: " + endValue);
    return endValue;
    }

    public static void main(String[] args) {
        isRotation("goat", "oatg");
    }

}
