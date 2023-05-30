public class Post implements Texto, Imagen, Video{
    private int id;
    private String url;
    private String mensaje;

    public Post(int id, String url, String mensaje){
        this.id = id;
        this.url = url;
        this.mensaje = mensaje;
    }

    @Override
    public void verTexto(){
        System.out.println("> escribir: ");
    }

    @Override
    public void verImagen(){
        System.out.println("Estoy viendo la imagen...");
    }

    @Override
    public void verVideo(){
        System.out.println("Estoy reproduciendo el video...");
    }
}