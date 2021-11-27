import java.util.Scanner;

public class quadrant {
    public static void main(String[] args) {
        Scanner in = new Scanner (System.in);
        int n = in.nextInt();
        int x = in.nextInt();
        
        if (n>=0 && x>=0){
                System.out.println("1");
            }else 
            if( n>=0 && x<0){
                System.out.println("4");
            }else
            if (n<0 && x<0){
                System.out.println("3");
            }else {
                System.out.println("2");
            }
    }
}
