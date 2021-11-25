public class MultiplicationTable {
    public static void main(String[] args) {
        System.out.println("Multiplication Table v1.0");
        for (int i=1; i<=12; i++) {
            System.out.print('\n');
            for (int j=1; j<=12; j++) {
                System.out.println(i + " * " + j + " = " + (i*j));
            }
        }
    }
}