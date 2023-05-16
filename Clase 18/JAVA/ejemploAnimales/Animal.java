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

    // Polimorfismo Parametrico
    public Animal(int id){
        this.id = id;
        this.nombre = "";
        this.especie = "";
    }

    public void seMueve(){
        if(this.nombre == "")
            System.out.println("Animal X se esta moviendo");
        else
            System.out.println(this.nombre + " se esta moviendo");
    }

    public void haceSonido(){
        if(this.nombre == "")
            System.out.println("Animal X hace un sonido...");
        else
            System.out.println(this.nombre + " hace un sonido...");
    }
}