import java.util.Scanner;

public class sibice {
    public static void main(String[] args) {
        Scanner in = new Scanner (System.in);
        int n = in.nextInt();
        int a = in.nextInt();
        int b = in.nextInt();
        for (int i = 0; i < n; i++) {
            int num = in.nextInt();
            if (num*num <= (a*a) + (b*b)){
                System.out.println("DA");
            }else{
                System.out.println("NE");
            }
            
        }
    }
}
