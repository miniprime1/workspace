import java.awt.*;
import javax.swing.*;

public class HelloWorldGUI {
    public static void main(String[] args) {
        JFrame f = new JFrame("");
        f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        f.setLayout(new FlowLayout());
        f.add(new JLabel("Hello, World!"));
        f.pack();
        f.setVisible(true);
    }

}