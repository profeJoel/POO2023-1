package ejercicioBancoHerencia;

public class Inversion extends ServicioBancario{
    private double interes;
    private int diasPlazo;

    public Inversion(int id, double capital, double interes, int diasPlazo){
        super(id);
        this.setSaldo(capital);
        this.interes = interes;
        this.diasPlazo = diasPlazo;
    }

    public double calcularEgreso(){
        return (this.saldo + this.calculoInteres());
    }

    private double calculoInteres(){
        return (this.saldo * (this.interes/100) * this.diasPlazo);
    }
}