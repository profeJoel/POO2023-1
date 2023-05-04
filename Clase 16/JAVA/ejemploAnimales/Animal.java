package ejemploAnimales;

public class Animal{
    protected int id;
    protected String nombre;
    protected String especie;

    public Animal(int id, String nombre, String especie){
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
    }

    public void seMueve(){
        System.out.println(this.nombre + " se esta moviendo");
    }

    public void haceSonido(){
        System.out.print(this.nombre + " hace un sonido...");
    }
}