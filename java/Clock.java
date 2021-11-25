import java.text.SimpleDateFormat;
import java.util.Date;

public class clock {
    public static void main(String[] args) {
        while (true) {
            Date today = new Date();
            SimpleDateFormat now = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
            System.out.print(now.format(today));
            try {Thread.sleep(1000);} catch (Exception e) {System.out.println(e);}
            System.out.print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
        }
    }
}