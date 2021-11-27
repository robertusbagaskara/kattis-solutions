import java.util.Scanner;

public class grassseed {
    public static void main(String[] args) {
        float total_harga=0;
        Scanner in = new Scanner(System.in);
        float x = in.nextFloat();
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
            float a = in.nextFloat();
            float b = in.nextFloat();
            total_harga = total_harga + x*a*b;
        }
        System.out.println(total_harga);
        
        
        
        
        
    }
}
