import java.util.*;

public class DiceSimulator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rnd = new Random();
        System.out.println("Dice Rolling Simulator v1.0");
        System.out.println("Copyright (c) 2020 miniprime1\n");
        System.out.println("Press enter key to roll dice");
        input.nextLine();
        int num = rnd.nextInt(6) + 1;
        if (num == 1) {
            System.out.println("[-----]");
            System.out.println("[     ]");
            System.out.println("[  O  ]");
            System.out.println("[     ]");
            System.out.println("[-----]");
            System.out.println("Result: 1");
        }
        if (num == 2) {
            System.out.println("[-----]");
            System.out.println("[ O   ]");
            System.out.println("[     ]");
            System.out.println("[   O ]");
            System.out.println("[-----]");
            System.out.println("Result: 2");
        }
        if (num == 3) {
            System.out.println("[-----]");
            System.out.println("[     ]");
            System.out.println("[O O O]");
            System.out.println("[     ]");
            System.out.println("[-----]");
            System.out.println("Result: 3");
        }
        if (num == 4) {
            System.out.println("[-----]");
            System.out.println("[O   O]");
            System.out.println("[     ]");
            System.out.println("[O   O]");
            System.out.println("[-----]");
            System.out.println("Result: 4");
        }
        if (num == 5) {
            System.out.println("[-----]");
            System.out.println("[O   O]");
            System.out.println("[  O  ]");
            System.out.println("[O   O]");
            System.out.println("[-----]");
            System.out.println("Result: 5");
        }
        if (num == 6) {
            System.out.println("[-----]");
            System.out.println("[O O O]");
            System.out.println("[     ]");
            System.out.println("[O O O]");
            System.out.println("[-----]");
            System.out.println("Result: 6");
        }
    }
}