import java.util.Scanner;

public class autori {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String scan = scanner.next();
        String[] scan_split = scan.split("-");
        for (int i = 0; i < scan_split.length ; i++) {
            String scan_print = scan_split[i];
            System.out.print(scan_print.substring(0,1).toUpperCase());
        }
    }
}
