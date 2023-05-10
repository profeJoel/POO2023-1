package ejercicioBancoHerencia;

public class ServicioBancario{

    protected int id;
    protected double saldo;

    public ServicioBancario(int id){
        this.id = id;
        this.saldo = 0;
    }

    public Double getSaldo(){
        return this.saldo;
    }

    public void setSaldo(double s){
        this.saldo = s;
    }

    public String getInfo(){
        String texto = "Servicio id " + this.id + "[saldo: $" + this.saldo + ".-]";
        return texto;
    }


}