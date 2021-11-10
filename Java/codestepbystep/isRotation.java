public class isRotation{ 
    
    //ignore the code above this line. It is required if you're running it in an ide but if you're putting it in codestepbystep you don't need it
    //the line below this one establishes the method
    //make sure you put static boolean. You have to put boolean because that is what this function will be returning
    //the stuff in the parenthesis are the parameters. When codestepbystep tests this function in will plug in strings for var1 and var2
    static boolean isRotation(String var1, String var2) {
        
        //establishing future variables
        int var1Length;
        int pos = 0;
        char firstLetter;
        boolean endValue = true;
        
        //Here I am setting some variables to be different based on whether there is an empty parameteter or not (I need to skip the loop that will be used later in the code)
        //this loop has to be skipped because if it runs it will have no input for the things inside it and it will throw an error
        //the way I wrote the program relied on there being a parameter with something in it for it to run the for loop
        //so I need to skip the loop and return true or false depending on if they are both empty or just one
        //if they are both empty then they are equal so I would return true
        //if only one's empty then I need to return false because then they would not be equal
        //either way I need to skip the loop so I made the variable that the loop relied on to be equal to 0 so that it would skip over the loop
        
        //if one string was empty and the other one was not then I set the variable endValue to false because they are not equal (the if statement)
        //I set the endValue to true if both strings were empty because those are the same (the else if statement)
        //I set the variables to all be normal (what I would have if there wasn't that stupid test case with the empty string) if neither string was empty (the else statement)
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
        //var1Length was created so that I could skip the loop by setting it to zero, but also use it to run the loop if the length was greater than 0
        else {
            firstLetter = var1.charAt(0);
            pos = var2.indexOf(firstLetter);
            var1Length = var1.length();
        }
        
        //I made a loop that runs for the length of var1
        for (int i = 0; i < var1Length; i++) {
            
            //pos was equating to -1 when it coudn't find firstLetter in var2
            //so if the letter isn't even in the word then it is obviously not a rotation
            //so I set the endValue to false and did a break which skips the rest of the for loop
            if (pos < 0) {
                endValue = false;
                break;
            }
            
            //if the length of the variales is different then they aren't the same so I set it to false and skipped the rest of the loop again
            if (var1Length != var2.length()) {
                endValue = false;
                break;
            }
            
            //says to reset the position to 0 if it gets to the end of the word
            if (pos == var1Length) {
                pos = 0;
            }
            
            //so you can see what is happening internally in the program
            System.out.println("letter at pos " + pos + ": " + var2.charAt(pos));
            System.out.println("letter at i " + i + ": " + var1.charAt(i));
            
            //remember how we started the pos variable at where the first letter of the first word first appeared?
            //well we compare them now. On the first iteration of the for loop i = 0, which means var1.charAt(i) will equal the first letter of the first word
            //and because we set pos to find that first letter in the second word they should both be the same, so we check it
            //if they aren't equal then the words are not the same
            //when the loop goes around again both pos and i will have increased by one, therefor moving on to the characters after the ones we just compared
            //so now it looks again to see if these next characters are also the same
            //if they are then it iterates again, otherwise it breaks and returns false
            //becaue we set endValue to be true at the top if we never change it it will stay like that
            //so if all the characters match up the loop will finish iterating (because we have it set to only go up to the first word length)
            //and the endValue will equal true still, and then it will return that
            if (var1.charAt(i) != var2.charAt(pos)) {
                endValue = false;
                break;
            }
        pos++;
        }
    System.out.println("endValue: " + endValue);
    return endValue;
    }
    
    //this is just me calling the function because I made it in an ide. When you enter it in codestepbystep don't put anything in there below this comment
    public static void main(String[] args) {
        isRotation("goat", "tgoa");
    }
}
