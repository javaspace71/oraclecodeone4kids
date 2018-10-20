/**
 * Write a description of class HelloStudent here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class HelloStudent {
    
    public static void main(String[] args) {
        int count = 7;
        String message = "Hello Student!";
        
        // Display the message
                System.out.println("------------------");
                System.out.println(message + "  Welcome to BlueJ"); 
                System.out.println("------------------");
        
             for(int i=0; i<count; i++) {
                    int times = i + 1;
                    System.out.println(times + ": " + message);
             }
    
    } // end of main    () method
    
    public void printStudent(int count, String message) {
        for(int i=0; i<count; i++) {
                    int times = i + 1;
                    System.out.println(times + ": " + message);
        }
    }
    
    /*# -- Challenge Section --
       
       1. override toString() method
       
       2. add an instance method, printStudent(int count) 
       that takes count as a variable and prints Hello Student
       
       3. Create an object instance of HelloStudent within main and 
       pass the count parameter with different values
       
    */
} //end of HelloStudent class

