
/**
 * Write a description of class FahrenheitGUI here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
// ********************************************************************
//  FahrenheitGUI.java Author: Lewis/Loftus
//  Minor changes by THC.
//
//  Demonstrates the use of JFrame and JTextArea GUI components.
//********************************************************************

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class FahrenheitGUI {
  private int WIDTH = 300;
  private int HEIGHT = 75;
  private JFrame frame;
  private JPanel panel;
  private JPanel panel2;
  private JPanel panel3;
  private JLabel inputLabel, resultLabel;
  private JTextField fahrenheit;

  //-----------------------------------------------------------------
  //  Sets up the GUI.
  //-----------------------------------------------------------------

  public FahrenheitGUI() {
    frame = new JFrame("Temperature Conversion");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    inputLabel = new JLabel("Enter Fahrenheit temperature:");
    JLabel outputLabel = new JLabel("Temperature in Celsius: ");
    resultLabel = new JLabel("---");

    fahrenheit = new JTextField(7);
    fahrenheit.addActionListener(new TempListener());

    panel = new JPanel();
    panel2 = new JPanel();
    panel3 = new JPanel();
    
    panel.setPreferredSize(new Dimension(WIDTH, HEIGHT));
    panel.setBackground(Color.yellow);
    
    panel2.add(inputLabel);
    panel2.add(fahrenheit);
    panel3.add(outputLabel);
    panel3.add(resultLabel);
    
    panel.add(panel2);
    panel.add(panel3);

    frame.getContentPane().add(panel);

  }

  //-----------------------------------------------------------------
  //  Displays the primary application frame.
  //-----------------------------------------------------------------

  public void display() {
    frame.pack();
    frame.setVisible(true);

  }

  //*****************************************************************
  //  Represents an action listener for the temperature input field.
  //*****************************************************************

  private class TempListener implements ActionListener {
    //--------------------------------------------------------------
    //  Performs the conversion when the enter key is pressed in
    //  the text field.
    //--------------------------------------------------------------

    public void actionPerformed(ActionEvent event) {
      int fahrenheitTemp, celsiusTemp;

      String text = fahrenheit.getText();

      fahrenheitTemp = Integer.parseInt(text);
      celsiusTemp = (fahrenheitTemp - 32) * 5 / 9;

      resultLabel.setText(Integer.toString(celsiusTemp));
    }
  }
}