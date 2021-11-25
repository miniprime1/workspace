import java.util.*;
import static java.lang.System.*;

public class UpdownGame {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rnd = new Random();
        int opt, ans, x, y;
        out.println("Up/Down Game v1.0");
        out.println("Copyright (c) 2020 miniprime1\n");
        out.println("Difficult");
        out.println("1. Easy (1~10)");
        out.println("2. Normal (1~100)");
        out.println("3. Hard (1~1000)");
        out.println("4. Extreme (1~10000)");
        out.println("5. Custom (?~?)");
        out.print("Your choice: ");
        opt = Integer.parseInt(input.nextLine());

        if (opt == 1) {
            out.println("\nDifficult: Easy (1~10)");
            ans = rnd.nextInt(10) + 1;
        } else if (opt == 2) {
            out.println("\nDifficult: Normal (1~100)");
            ans = rnd.nextInt(100) + 1;
        } else if (opt == 3) {
            out.println("\nDifficult: Hard (1~1000)");
            ans = rnd.nextInt(1000) + 1;
        } else if (opt == 4) {
            out.println("\nDifficult: Extreme (1~10000)");
            ans = rnd.nextInt(10000) + 1;
        } else if (opt == 5) {
            out.print("\nEnter 1st input: ");
            x = Integer.parseInt(input.nextLine());
            out.print("Enter 1st input: ");
            y = Integer.parseInt(input.nextLine());
            out.println("\nDifficult: Custom (" + x + '~' + y + ")");
            ans = rnd.nextInt(10) + 1;
        } else {
            out.println("\nError: invalid choice");
            out.println("Difficult will be a Normal (1~100)");
            ans = rnd.nextInt(10) + 1;
        }

        while (true) {
            out.print("\nEnter number: ");
            int user = Integer.parseInt(input.nextLine());
            if (user > ans) {out.println("Down!");}
            if (user < ans) {out.println("Up!");}
            if (user == ans) { out.println("Answer!"); break; }
        }

        input.close();
    }
}