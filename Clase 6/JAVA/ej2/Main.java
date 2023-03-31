import java.util.Scanner;

public class Main{
    public static int fibonacci(int n){
        if(n==0 || n==1)
            return 1;
        else
            return fibonacci(n-1) + fibonacci(n-2);
    }
    public static void main(String[] args) {
        Scanner lector = new Scanner(System.in);        
        System.out.println("Ingrese N: ");
        int n = lector.nextInt();
        System.out.println("Fibonacci de " + n + " es " + fibonacci(n));
    }
}