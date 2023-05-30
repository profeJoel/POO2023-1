public class Main {
    public static void main(String[] args){
        //Lambda Expression : (params) -> {expression};
        serVivo perro = (comida) -> "El perro come " + comida;
        System.out.println(perro.come("gato"));
        //imprimirElemento(perro, "gato");
    }

}