package EjemploGatos;

public class Gato{
    //Atributos
    private String name;
    private String sex;
    private int age;
    private int weight;
    private String color;
    private String texture;

    //Metodos
    //El primer metodo siempre es el constructor que en Java se llama de la misma manera que la clase
    public Gato(String name, String sex, int age, int  weight, String color, String texture){
        //Un constructor permite crear toda la informacion y metodos  a un objeto.
        //this hace referencia a que son elementos que pertenecen al objeto utilizado
        this.name = name;
        this.sex = sex;
        this.age = age;
        this.weight = weight;
        this.color = color;
        this.texture = texture;
    }

    public void eat(){
        System.out.println(this.name + " esta comiendo");
    }

    public void move(){
        System.out.println(this.name + " se esta moviendo...");
    }

    public void meow(){
        System.out.println(this.name + " hace miauuuu");
    }

    public void purr(){
        System.out.println(this.name + " esta ronrroneando");
    }
    public void hunt_mice(){
        System.out.println(this.name + " capturo a un ratoncito...");
    }

    //Metodos Getters y Setters
    // Los getters solamente entregan informacion, datos no acceso al atributo
    public String getName(){
        return this.name;
    }

    public String getSex(){
        return this.sex;
    }

    public int getAge(){
        return this.age;
    }

    public int getWeight(){
        return this.weight;
    }

    public String getColor(){
        return this.color;
    }

    public String getTexture(){
        return this.texture;
    }

    // Los Setters permiten modificar los valores de los atributos bajo restricciones.
    public void happyBirthday(){
        this.setAge(this.age + 1);
    }
    public void setAge(int newAge){
        if(newAge >= 0 && newAge>=this.age)
            this.age = newAge;
    }

    public void setWeight(int newWeight){
        if(newWeight >= 0 && newWeight >= this.weight/2 && newWeight <= this.weight*2)
            this.weight = newWeight;
    }

    public void setColor(String newColor){
        if(newColor == "gris" || newColor == "blanco")
            this.color = newColor;
        else
            System.out.println("No se puede cambiar el color");
    }


}