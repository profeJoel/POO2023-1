package ejemploAnimales;

public class Main{
    public static void main(String[] args) {
        Animal animal1 = new Animal(1,"Animal 1", "indeterminada");

        animal1.seMueve();
        animal1.haceSonido();

        Gato tom = new Gato(2, "Tom", "Felino", "liso y corto");
        Perro spike = new Perro(3, "Spike", "Canino", 75);
        Vaca lola = new Vaca (4, "Lola", "Vacuno", 7);

        tom.seMueve();
        spike.seMueve();
        lola.seMueve();

        tom.haceSonido();
        spike.haceSonido();
        lola.haceSonido();

        tom.haceMiau();
        spike.haceGuau();
        lola.haceMu();

        // experimentos
        //animal1.haceMiau();
        //lola.haceMiau();
    }
}