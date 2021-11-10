public class isRotation{ 
    static boolean isRotation(String var1, String var2) {
        
        //variables
        int var1Length;
        int pos = 0;
        char firstLetter;
        boolean endValue = true;
        
        //setting the variables to be certain things when there is an empty string (I need to skip the loop)
        //the way I wrote the program relied on there being a string with something in it for it to run the for loop
        //so I need to skip the loop and return true or false depending on if they are both empty or just one
        //either way I need to skip the loop so I made the variable that the loop relied on 0 so that it would skip over it
        
        //I set the endValue to false if one string was empty and the other wasn't because they were obviously not the same then I skipped the loop
        //I set the endValue to true if both strings were empty because those are the same, then I skipped the loop
        //I set the variables to all be normal (what I would have if there wasn't that stupid test case with the empty string)
        if (var1.length() < 1 && var2.length() > 0) {
            endValue = false;
            var1Length = 0;
        }
        
        else if (var1.length() < 1 && var2.length() < 1) {
            endValue = true;
            var1Length = 0;
        }
        
        //firstLetter stores the first letter of var1
        //pos stores where firstLetter appears in var2
        //var1Length was created so that I could skip the loop by setting it to zero, but also use it to run the loop if it was greater than 0
        else {
            firstLetter = var1.charAt(0);
            pos = var2.indexOf(firstLetter);
            var1Length = var1.length();
        }
        
        //I made a loop that runs for the duration of the length of var1
        for (int i = 0; i < var1Length; i++) {
            
            //says that if the first letter from var1 isn't found in var2, then break the loop
            if (pos < 0) {
                endValue = false;
                break;
            }
            
            // says that if the variables don't have the same length then return false
            if (var1Length != var2.length()) {
                endValue = false;
                break;
            }
            
            //says to reset the position to 0 if it gets to the end of the word
            if (pos == var1Length) {
                pos = 0;
            }
            
            System.out.println("letter at pos " + pos + ": " + var2.charAt(pos));
            System.out.println("letter at i " + i + ": " + var1.charAt(i));
            
            /*because the value of i (what we are running the loop based off of)
            and pos should be the same, it makes sure of this by checking if they are the same.
            If they are not the same then endValue is false because the words are not the same
            */
            if (var1.charAt(i) != var2.charAt(pos)) {
                endValue = false;
                break;
            }
        pos++;
        }
    System.out.println("endValue: " + endValue);
    return endValue;
    }

    public static void main(String[] args) {
        isRotation("goat", "tgoa");
    }
}
