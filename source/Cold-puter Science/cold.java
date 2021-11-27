import java.util.Scanner;

public class cold {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int loop = scan.nextInt();
        int a = 0;
        for (int i = 0; i < loop; i++) {
            int input = scan.nextInt();
            scan.close();
            if (input<0) {
                a = a+1;
            }
        }
        System.out.println(a);
    }
}
