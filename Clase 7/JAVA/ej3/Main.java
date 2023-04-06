import java.util.Scanner;

public class Main{

    public static void ingresarMatriz(int[][] m){
        Scanner lector = new Scanner(System.in);
        for(int i = 0; i < 3; i++){//para filas
            for(int j = 0; j < 3; j++){//para columnas
                System.out.print("Ingrese el valor de la celda ["+i+"]["+j+"]");
                m[i][j] = lector.nextInt();
            }
        }
    }

    public static void imprimirMatriz(int[][] m){
        for(int i = 0; i < 3; i++){//para filas
            for(int j = 0; j < 3; j++){//para columnas
                System.out.print(m[i][j] + " ");
            }
            System.out.println(" ");
        }
    }

    public static void verificarCuboMagico(int[][] m){
        int sumaGlobal = 0;
        int sumaFila = 0;
        int sumaColumna = 0;
        int sumaDiagonal = 0;

        //Para Filas
        for(int i = 0; i < 3; i++){//para filas
            for(int j = 0; j < 3; j++){//para columnas
                sumaFila += m[i][j];
            }
            if(sumaGlobal == 0)
                sumaGlobal = sumaFila;
            if(sumaFila != sumaGlobal){
                System.out.println("El cubo no es magico");
                return;
            }
            sumaFila = 0;
        }
        //Para Columnas
        for(int j = 0; j < 3; j++){//para filas
            for(int i = 0; i < 3; i++){//para columnas
                sumaColumna += m[i][j];
            }
            if(sumaGlobal == 0)
                sumaGlobal = sumaColumna;
            if(sumaColumna != sumaGlobal){
                System.out.println("El cubo no es magico");
                return;
            }
            sumaColumna = 0;
        }
        //Para diagonales
        for(int i = 0; i < 3; i++){//para filas
            for(int j = 0; j < 3; j++){//para columnas
                if(i == j)
                    sumaDiagonal += m[i][j];
            }
        }
        if(sumaGlobal == 0)
            sumaGlobal = sumaDiagonal;
        if(sumaDiagonal != sumaGlobal){
            System.out.println("El cubo no es magico");
            return;
        }
        sumaDiagonal = 0;

        //Para diagonales
        for(int i = 0; i < 3; i++){//para filas
            for(int j = 0; j < 3; j++){//para columnas
                if(i + j == 2)
                    sumaDiagonal += m[i][j];
            }
        }
        if(sumaGlobal == 0)
            sumaGlobal = sumaDiagonal;
        if(sumaDiagonal != sumaGlobal){
            System.out.println("El cubo no es magico");
            return;
        }
        sumaDiagonal = 0;
        //Conclusion de la Funcion
        System.out.println("El Cubo es Magico!!!");
    }

    public static void verificarCuboMagico2(int[][] m){
        int sumaFila0 = 0;
        int sumaFila1 = 0;
        int sumaFila2 = 0;
        int sumaColumna0 = 0;
        int sumaColumna1 = 0;
        int sumaColumna2 = 0;
        int sumaDiagonal1 = 0;
        int sumaDiagonal2 = 0;

        //Para Filas
        for(int i = 0; i < 3; i++){//para filas
            for(int j = 0; j < 3; j++){//para columnas
                //filas
                if(i == 0) sumaFila0 += m[i][j];
                if(i == 1) sumaFila1 += m[i][j];
                if(i == 2) sumaFila2 += m[i][j];

                //columnas
                if(j == 0) sumaColumna0 += m[i][j];
                if(j == 1) sumaColumna1 += m[i][j];
                if(j == 2) sumaColumna2 += m[i][j];

                //diagonales
                if(i == j) sumaDiagonal1 += m[i][j];
                if(i + j == 2) sumaDiagonal2 += m[i][j];
            }
        }
        if(sumaFila0 != sumaFila1 || sumaFila0 != sumaFila2 || sumaFila1 != sumaFila2 || sumaFila0 != sumaColumna0 || sumaColumna0 != sumaColumna1 || sumaColumna0 != sumaColumna2 || sumaColumna1 != sumaColumna2 || sumaColumna0 != sumaDiagonal1 || sumaDiagonal1 != sumaDiagonal2){
            System.out.println("El cubo no es magico");
            return;
        }
        //Conclusion de la Funcion
        System.out.println("El Cubo es Magico!!!");
    }


    public static void main(String[] args){

        // explicita
        //int[][] cubo = {{1,2,3},{4,5,6},{7,8,9}};
        // declaracion  de matriz en java con valor de dimension
        int[][] cubo = new int[3][3];
        ingresarMatriz(cubo);
        imprimirMatriz(cubo);
        verificarCuboMagico2(cubo);
    }
}