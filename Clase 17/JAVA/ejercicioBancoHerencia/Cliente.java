package ejercicioBancoHerencia;

import java.util.ArrayList;

public class Cliente{
    private int id;
    private String nombre;
    private String apellidoPaterno;
    private String apellidoMaterno;
    private ArrayList<ServicioBancario> listaServicios;

    public Cliente(int id, String nombre, String apellidoPaterno, String apellidoMaterno){
        this.id = id;
        this.nombre = nombre;
        this.apellidoPaterno = apellidoPaterno;
        this.apellidoMaterno = apellidoMaterno;
        this.listaServicios = new ArrayList<ServicioBancario>();
    }

    public void agregarServicio(ServicioBancario s){
        this.listaServicios.add(s);
    }

    public String mostrarDatos(){
        String texto = "Cliente id " + this.id + "\nNombre Completo: " + this.nombre + " " + this.apellidoPaterno + " " + this.apellidoMaterno + "\nLista de Servicios:";
        for (ServicioBancario s : this.listaServicios) {
            texto += "\n- " + s.getInfo();
        }
        return texto;
    }


}