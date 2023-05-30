public class Perro extends Animal{
    public Perro(String nombre, String especie){
        this.nombre = nombre;
        this.especie = especie;
    }

    public void hacerSonido(){
        System.out.println("Guauu...");
    }
}