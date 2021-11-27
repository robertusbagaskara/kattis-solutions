import java.util.Scanner;

public class spavanac {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        if ((n==0) && m>=0 && m<45){
            System.out.println((n+23)+" "+(m+15));
        }
        else if(n==0 && m>=45){
            System.out.println((n)+" "+(m-45));
        }
        else if (n<=23 && m>=0 && m<45 ){
            System.out.println((n-1)+" "+(m+15));
        }
        else if (n<=23 && m>=45 ){
            System.out.println((n)+" "+(m-45));
        }
       
    }
}
