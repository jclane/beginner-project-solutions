import java.awt.Component;
import java.awt.Container;
import java.awt.Frame;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.Timer;

import java.util.Random;

class AppWindow {
  private JFrame frame = new JFrame("Magic Eight Ball");
  private JLabel statusLabel = new JLabel();
  private JLabel responseLabel = new JLabel();

  private static final Insets insets = new Insets(0, 0, 0, 0);

  public AppWindow() {
    this.frame.setSize(500,300);
    this.frame.setLayout(new GridBagLayout());
    this.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    addComponent(this.frame, this.statusLabel, 0,  0, 1, 1, GridBagConstraints.CENTER, GridBagConstraints.BOTH);
    addComponent(this.frame, this.responseLabel, 0, 1, 1, 1, GridBagConstraints.CENTER, GridBagConstraints.BOTH);

    JTextField questionField = new JTextField(20);
    addComponent(this.frame, questionField, 0, 2, 1, 1, GridBagConstraints.WEST, GridBagConstraints.BOTH);
    JButton submitButton = new JButton("Ask");
    submitButton.addActionListener(new ActionListener(){
      @Override
      public void actionPerformed(ActionEvent e) {
        if (questionField.getText().length() > 1) {
          consultOracle(questionField.getText());
        }
      }
    });
    addComponent(this.frame, submitButton, 1, 2, 1, 1, GridBagConstraints.CENTER, GridBagConstraints.BOTH);
    JButton clearButton = new JButton("Clear");
    clearButton.addActionListener(new ActionListener(){
      @Override
      public void actionPerformed(ActionEvent e) {
        System.out.println(e);
      }
    });
    addComponent(this.frame, clearButton, 2, 2, 1, 1, GridBagConstraints.CENTER, GridBagConstraints.BOTH);
    JButton quitButton = new JButton("Quit");
    quitButton.addActionListener(new ActionListener(){
      @Override
      public void actionPerformed(ActionEvent e) {
        for (Frame frame : Frame.getFrames()) {
          frame.dispose();
        }
      }
    });
    addComponent(this.frame, quitButton, 2, 3, 10, 1, GridBagConstraints.EAST, GridBagConstraints.BOTH);

    this.frame.pack();
    this.frame.setVisible(true);

  }

  /**
   * From: http://www.java2s.com/Tutorial/Java/0240__Swing/UsingGridBagConstraints.htm
   */
  private void addComponent(Container container, Component component, int gridx, int gridy,
      int gridwidth, int gridheight, int anchor, int fill) {
    GridBagConstraints gbc = new GridBagConstraints(gridx, gridy, gridwidth, gridheight, 1.0, 1.0,
        anchor, fill, insets, 0, 0);
    container.add(component, gbc);
  }

  private void consultOracle(String question) {
    JFrame popup = new JFrame();
    final JDialog messagePopup = new JDialog(popup, "Consulting the Oracle...", true);
    messagePopup.setSize(250, 75);
    messagePopup.add(new JLabel("Consulting my friends on the other side..."));
    Timer timer = new Timer(4000, new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e) {
        messagePopup.setVisible(false);
        messagePopup.dispose();
      }
    });
    timer.setRepeats(false);
    timer.start();
    messagePopup.setVisible(true);

    final String[] RESPONSE = { "It is certain.", "It is decidedly so.",
                                "Without a doubt.", "Yes - definitely.",
                                "You may rely on it.", "As I see it, yes.",
                                "Most likely.", "Outlook good.", "Yes.",
                                "Signs point to yes.", "Reply hazy, try again",
                                "Ask again later.", "Better not tell you now.",
                                "Cannot predict now.",
                                "Concentrate and ask again.",
                                "Don't count on it.", "My reply is no.",
                                "My sources say no.", "Outlook not so good.",
                                "Very doubtful." };
    Random rand = new Random();
    this.responseLabel.setText(RESPONSE[rand.nextInt(20)]);
  }

}

class MagicEightBall {

  public static void main(String[] args) {
    AppWindow window = new AppWindow();
  }

}
