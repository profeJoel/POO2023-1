package ejercicioBancoHerencia;

public class Credito extends ServicioBancario{
    private double interes;
    private int cuotas;
    private double montoCuota;
    private int cuotasPagadas;

    public Credito(int id, double prestamo, double interes, int cuotas, double montoCuota){
        super(id);
        this.setSaldo(prestamo);
        this.interes = interes;
        this.cuotas = cuotas;
        this.montoCuota = montoCuota;
        this.cuotasPagadas = 0;
    }

    public void pagarCuota(){
        this.saldo -= this.montoCuota + this.calculoInteres();
        this.cuotasPagadas++;
    }

    private double calculoInteres(){
        return (this.montoCuota*(this.interes/100)*(this.cuotasPagadas+1));
    }
}