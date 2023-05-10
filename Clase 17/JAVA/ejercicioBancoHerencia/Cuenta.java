package ejercicioBancoHerencia;

public class Cuenta extends ServicioBancario{
    private String tipo;
    private String divisa;

    public Cuenta(int id, String tipo, String divisa){
        super(id);
        this.tipo = tipo;
        this.divisa = divisa;
    }

    public void depositar(double deposito){
        if(deposito > 0)
            this.saldo += deposito;
        else
            System.out.println("Operacion no valida: Valor negativo");
    }

    public void retirar(double retiro){
        if(retiro > 0 && retiro >= this.saldo)
            this.saldo -= retiro;
        else
            System.out.println("Operacion no valida: Valor Negativo o Sin Saldo Suficiente");
    }
}