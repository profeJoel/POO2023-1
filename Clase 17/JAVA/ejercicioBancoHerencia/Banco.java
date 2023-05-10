package ejercicioBancoHerencia;

import java.util.ArrayList;

public class Banco{
    private int id;
    private String razonSocial;
    private String nombreFantasia;
    private String rut;
    private ArrayList<Cliente> listaClientes;

    public Banco(int id, String razonSocial, String nombreFantasia, String rut){
        this.id = id;
        this.razonSocial = razonSocial;
        this.nombreFantasia = nombreFantasia;
        this.rut = rut;
        //Se crea el objeto de la lista vacia de tipo Cliente
        this.listaClientes = new ArrayList<Cliente>();
    }

    public void agregarCliente(Cliente c){
        this.listaClientes.add(c);
    }

    public Cliente getCliente(int i){
        return this.listaClientes.get(i);
    }
}