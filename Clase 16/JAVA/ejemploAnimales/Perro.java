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
}