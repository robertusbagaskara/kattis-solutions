import java.util.Scanner;

public class nastyhacks {
    public static void main(String[] args) {
        Scanner in = new Scanner (System.in);
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int c = in.nextInt();
            if(a+c < b){
                System.out.println("advertise");
            }else if (a+c>b){
                System.out.println("do not advertise");
            }else{
                System.out.println("does not matter");
            }
            
        }
        
    }
}
