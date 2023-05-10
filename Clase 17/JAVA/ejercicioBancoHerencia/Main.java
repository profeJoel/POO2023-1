package ejercicioBancoHerencia;

public class Main{
    public static void main(String[] args) {
        
        Banco ULagosBank = new Banco(1, "Banco de los Estudiantes de la Universidad de Los Lagos Chile S.A.", "ULagosBank","100.000.001-0");

        Cliente a = new Cliente(1, "Esteban", "Dido", "Roba");

        Cuenta servicio1 = new Cuenta(1, "Cuenta Corriente", "CLP");
        Credito servicio2 = new Credito(2, 100000000, 2.8, 360, 500000);
        Inversion servicio3 = new Inversion(3, 7000000, 9.3, 100);

        a.agregarServicio(servicio1);
        a.agregarServicio(servicio2);
        a.agregarServicio(servicio3);

        ULagosBank.agregarCliente(a);
        System.out.println(ULagosBank.getCliente(0).mostrarDatos());
    }
}