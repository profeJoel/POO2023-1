package ejemploAnimales;

public class Gato extends Animal{
    protected String tipoPelaje;

    public Gato(int id, String nombre, String especie, String tipoPelaje){
        super(id, nombre, especie);
        this.tipoPelaje = tipoPelaje;
    }

    public void haceMiau(){
        System.out.println(this.nombre + " hace MIUAUUU!!!!");
    }

    // Polimorfismo por sobrecarga
    public void seLava(){
        System.out.println(this.nombre + " se lava con la lengua...");
    }

    // Polimorfismo Por Inclusion
    @Override
    public void haceSonido(){
        this.haceMiau();
    }
}

