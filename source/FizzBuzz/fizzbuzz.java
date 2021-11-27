import java.util.Scanner;

class fizzbuzz {
    public static void main(String[] args) {
        int a,b,c,d;
        Scanner in = new Scanner(System.in);
        c = in.nextInt();
        d = in.nextInt();
        b = in.nextInt();
        in.close();
        
        for (a = 1 ; a<=b; a++){
        if (a%c == 0 && a%d == 0){
            System.out.println("FizzBuzz");
            
        }
        else if (a%c == 0){
            System.out.println("Fizz");
        }
         else if (a%d == 0){
            System.out.println("Buzz");
        }
         else {
             System.out.println(a);
         }
    }
    }
}
