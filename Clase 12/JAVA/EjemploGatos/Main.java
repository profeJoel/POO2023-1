package EjemploGatos;

class Main{
    public static void main(String[] args) {
        Gato oscar = new Gato("Oscar", "macho", 5, 7, "marron", "rayado");
        oscar.meow();

        Gato luna = new Gato("Luna", "hembra", 2, 5, "gris", "lisa");
        luna.purr();

        System.out.println("Los nombres de los gatos son " + oscar.name + " y " + luna.name);

        // Clase 13 - Encapsulamiento

        System.out.println("El color del gato " + oscar.name + " es " + oscar.color);
        oscar.color = "verde";
        System.out.println("El color del gato " + oscar.name + " es " + oscar.color);
    }
}