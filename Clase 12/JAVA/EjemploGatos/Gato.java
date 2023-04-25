package EjemploGatos;

class Gato{
    //Atributos
    String name;
    String sex;
    int age;
    int weight;
    String color;
    String texture;

    //Metodos
    //El primer metodo siempre es el constructor que en Java se llama de la misma manera que la clase
    Gato(String name, String sex, int age, int  weight, String color, String texture){
        //Un constructor permite crear toda la informacion y metodos  a un objeto.
        //this hace referencia a que son elementos que pertenecen al objeto utilizado
        this.name = name;
        this.sex = sex;
        this.age = age;
        this.weight = weight;
        this.color = color;
        this.texture = texture;
    }

    void eat(){
        System.out.println(this.name + " esta comiendo");
    }

    void move(){
        System.out.println(this.name + " se esta moviendo...");
    }

    void meow(){
        System.out.println(this.name + " hace miauuuu");
    }

    void purr(){
        System.out.println(this.name + " esta ronrroneando");
    }
    void hunt_mice(){
        System.out.println(this.name + " capturo a un ratoncito...");
    }

}