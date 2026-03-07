import java.util.Scanner;

public class Solution {
    public static int feetToSteps(double userFeet) {
        return (int) (userFeet / 2.5);
    }

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        double feetWalked = scnr.nextDouble();
        System.out.println(feetToSteps(feetWalked));
    }
}
