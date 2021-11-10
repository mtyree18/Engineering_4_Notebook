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
            
            // says that if the variables don't have the same length then return false
            if (var1.length() != var2.length()) {
                endValue = false;
                break;
            }
            
            //says to reset the position to 0 if it gets to the end of the word
            if (pos == var1.length()) {
                pos = 0;
            }
            
            /*because the value of i (what we are running the loop based off of)
            and pos should be the same, it makes sure of this by checking if they are the same.
            If they are not the same then endValue is false because the words are not the same. This loop
            also shows the value of i and pos so you can see any possible problems you might be having.
            */
            if (var1.charAt(i) != var2.charAt(pos)) {
                endValue = false;
                System.out.println("i: " + i);
                System.out.println("letter at pos " + pos + ": " + var2.charAt(pos));
                System.out.println("letter at i " + i + ": " + var1.charAt(i));
                break;
            }
        pos++;
        }
    System.out.println("endValue: " + endValue);
    return endValue;
    }

    public static void main(String[] args) {
        isRotation("y", "y");
    }
}
