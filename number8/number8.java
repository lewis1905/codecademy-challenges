import java.util.Random;

public class Magic8 {

//generating random number betweeen 0 and 7.
static int random = (int)(Math.random() * 6 + 1);

public static void main (String[] args){

//switch statement with outcomes.
switch (random) {

  case 0:
  System.out.println("As I see it, yes");
  break;

  case 1:
  System.out.println("Concentrate and ask again");
  break;

  case 2:
  System.out.println("Don’t count on it");
  break; 

  case 3:
  System.out.println("My sources say no");
  break;

  case 4:
  System.out.println("Outlook not so good");
  break;

  case 5:
  System.out.println("Reply hazy try again");
  break;

  case 6:
  System.out.println("Signs point to yes");
  break;

  case 7:
  System.out.println("You may rely on it");
  break;
}

}
}