package ejemploAnimales;


public class Vaca extends Animal{
    protected int nEstomagos;

    public Vaca(int id, String nombre, String especie, int nEstomagos){
        super(id, nombre, especie);
        this.nEstomagos = nEstomagos;
    }

    public void haceMu(){
        System.out.println(this.nombre + " hace MUUUU!!!!");
    }

    // Polimorfismo Por Inclusion
    @Override
    public void haceSonido(){
        this.haceMu();
    }
}