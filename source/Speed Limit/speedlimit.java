import java.util.Scanner;

public class speedlimit {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(true){
             int loop = scan.nextInt();
             if (loop == -1) {
                break;
            }
        int []arrInt=new int[loop];
        int sum = 0;
        int cross;
         for (int i = 0; i < loop; i++) {
             int alpha = scan.nextInt();
             int beta = scan.nextInt();
             arrInt[i]=beta;
             if (i==0) {
                 cross = alpha*arrInt[i];
             }else{
                 cross = alpha*(arrInt[i]-arrInt[i-1]);
             }
             sum = sum + cross;
         }System.out.println(sum+" miles");
         
        }
       
           
     }
}
