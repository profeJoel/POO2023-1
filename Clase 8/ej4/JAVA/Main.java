public class Main{
    public static int contarCaracteres(String p){
        return p.length();
    }

    public static void main(String[] args){
        String palabra = "programacion"; 
        System.out.println("La palabra es: " + palabra); 

        System.out.println("La palabra tiene: " + contarCaracteres(palabra) + " letras");
    }
}