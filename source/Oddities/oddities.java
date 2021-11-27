import java.util.Scanner;

public class oddities {

    public static void main(String[] args) {
      
        Scanner in = new Scanner(System.in);

        
        int a[] = new int[20];
        
        int n = in.nextInt();
        
        for(int i = 0; i < n; i++){
            a[i] = in.nextInt();
        }
        
        for (int i = 0; i < n; i++) {
            if(a[i] % 2 == 0){
                System.out.println(a[i] + " is even ");
            }else{
                System.out.println(a[i] + " is odd ");
            }
        }
        
    
    }

}
