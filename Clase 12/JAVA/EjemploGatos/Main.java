package EjemploGatos;

class Main{
    public static void main(String[] args) {
        Gato oscar = new Gato("Oscar", "macho", 5, 7, "marron", "rayado");
        oscar.meow();

        Gato luna = new Gato("Luna", "hembra", 2, 5, "gris", "lisa");
        luna.purr();

        System.out.println("Los nombres de los gatos son " + oscar.getName() + " y " + luna.getName());

        // Clase 13 - Encapsulamiento

        System.out.println("El color del gato " + oscar.getName() + " es " + oscar.getColor());
        System.out.println("El gato " + oscar.getName() + " tiene " + oscar.getAge() + " anios");
        oscar.happyBirthday();
        oscar.setAge(0);
        System.out.println("El gato " + oscar.getName() + " tiene " + oscar.getAge() + " anios");
        oscar.setColor("gris");
        System.out.println("El color del gato " + oscar.getName() + " es " + oscar.getColor());
    }
}