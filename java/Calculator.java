import java.util.*;

public class Calculator {
    public static void main(String[] args) {
        var input = new Scanner(System.in);
        double x, y;

        System.out.println("Java Calculator v1.0");
        System.out.println("Copyright (c) 2020 miniprime1\n");
        System.out.println("Options");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.print("Enter choice: ");
        int choice = Integer.parseInt(input.nextLine());
        System.out.println(' ');

        if (choice == 1) {
            System.out.print("Enter 1st input: ");
            x = Double.parseDouble(input.nextLine());
            System.out.print("Enter 2nd input: ");
            y = Double.parseDouble(input.nextLine());
            System.out.println("\nResult: " + x + " + " + y + " = " + (x+y));
        } else if (choice == 2) {
            System.out.print("Enter 1st input: ");
            x = Double.parseDouble(input.nextLine());
            System.out.print("Enter 2nd input: ");
            y = Double.parseDouble(input.nextLine());
            System.out.println("\nResult: " + x + " + " + y + " = " + (x-y));
        } else if (choice == 3) {
            System.out.print("Enter 1st input: ");
            x = Double.parseDouble(input.nextLine());
            System.out.print("Enter 2nd input: ");
            y = Double.parseDouble(input.nextLine());
            System.out.println("\nResult: " + x + " + " + y + " = " + (x*y));
        } else if (choice == 1) {
            System.out.print("Enter 1st input: ");
            x = Double.parseDouble(input.nextLine());
            System.out.print("Enter 2nd input: ");
            y = Double.parseDouble(input.nextLine());
            System.out.println("\nResult: " + x + " + " + y + " = " + (x/y));
        } else {
            System.out.println("Error: invalid choice");
        }
        
        input.close();
    }
}
