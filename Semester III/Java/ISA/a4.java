import java.applet.*;
import  java.awt.*;
import java.awt.event.*;
/*<applet  code=a4width=300 height=300></applet>*/
public class a4 extends Applet implements ActionListener
{Label l1,l2;
TextField t1,t2,t3;
Button b1,b2,b3,b4;
public void init()
{
setLayout(new FlowLayout());
l1=new Label("Number 1");
l2=new Label("Number 2");t1=new TextField(5);
t2=new TextField(5);
t3=new TextField(5);
b1=new Button("Add");
b2=new Button("Sub");
b3=new Button("Mul");
b4=new Button("Div");
b1.addActionListener(this);
b2.addActionListener(this);
b3.addActionListener(this);
b4.addActionListener(this);
add(l1);
add(t1);
add(l2);
add(t2);
add(b1);
add(b2);
add(b3);
add(b4);
add(t3);
}
public void actionPerformed(ActionEvent ae)
{String s=ae.getActionCommand();
int n1=Integer.parseInt(t1.getText());
int n2=Integer.parseInt(t2.getText());
int n;
if(s.equals("Add"))
{n=n1+n2;}else if(s.equals("Sub"))
{n=n1-n2;
}
else if(s.equals("Mul"))
{n=n1*n2;
}else
{n=n1/n2;
}
String p=Integer.toString(n);
t3.setText(p);
}}