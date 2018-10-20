import java.util.*;

/**
 * Write a description of class PalindromeChecker here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class PalindromeChecker
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class PalindromeChecker
     */
    public PalindromeChecker()
    {
        super();
    }

    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    public static boolean isPalindrome(String str) {
        String strRev = new StringBuilder(str).reverse().toString();
        System.out.println("THE REVERSED STRING IS: "+ strRev);
        return str.equals(strRev);
    }

    public static void main(String args[]) {
        while (true) {
            Scanner in = new Scanner(System.in);
            System.out.println("ENTER YOUR STRING: ");
            String a = in.nextLine();
            System.out.println("GIVEN STRING IS: "+ a);
            if (a.equals("exit")) {
                System.out.println("Bye ...");
                break;
            }
            
            boolean isPal = PalindromeChecker.isPalindrome(a);

            if(isPal)    
                System.out.println("ITS A PALINDROME");
            else
                System.out.println("ITS NOT A PALINDROME");
        }
    }

    /*# -- Challenge Section --

    1. Can you print all palindromes that are obtained by multiplying any 2 three-digit numbers?
    2. Which is the largest number of such palindrome numbers obtained above?

     */

}
