public class Gato extends Animal{
    public Gato(String nombre, String especie){
        this.nombre = nombre;
        this.especie = especie;
    }

    public void hacerSonido(){
        System.out.println("Miauu...");
    }
}