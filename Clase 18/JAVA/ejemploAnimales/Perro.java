package ejemploAnimales;

public class Perro extends Animal{
    protected int poderMandibula;

    public Perro(int id, String nombre, String especie, int poderMandibula){
        super(id, nombre, especie);
        this.poderMandibula = poderMandibula;
    }

    public void haceGuau(){
        System.out.println(this.nombre + " hace GUAU!!!!");
    }

    // Polimorfismo por sobrecarga
    public void seLava(){
        System.out.println(this.nombre + " se lava en una tina...");
    }

    // Polimorfismo Por Inclusion
    @Override
    public void haceSonido(){
        this.haceGuau();
    }
}