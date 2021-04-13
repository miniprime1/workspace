import java.util.*;

public class Echo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Echo v1.0 (Exit: Ctrl+D)");
            while (true) {
                System.out.print("\nEnter Text: ");
                String input = scanner.nextLine();
                System.out.println("Typed Text: " + input);
            }
        } catch (NoSuchElementException e) {
            System.out.print('\n');
        } catch (Exception e) {
            System.out.println("\nError: " + e.toString());
        } finally {
            scanner.close();
            System.exit(0);
        }
    }
}