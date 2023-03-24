#include<stdio.h>

typedef struct vehiculo{
    char marca[20];
    char modelo[50];
    int anho;
}autito;

void ingreso_valores(autito *a)
{
    printf("Ingrese la marca: ");
    fgets(a->marca, 20, stdin);
    fflush(stdin);
    printf("Ingrese Modelo: ");
    fgets(a->modelo, 50, stdin);
    printf("Ingrese Anho: ");
    scanf("%d", &a->anho);
    fflush(stdin);
}

void mostrar_valores(autito a)
{
    printf("\nEl auto es: \nMARCA: %sMODELO: %sANHO: %d", a.marca, a.modelo, a.anho);
}

int main(){

    //declaración simple
    autito mio;
    autito nomina[5];
    //ingreso_valores(&mio);
    int i;
    for(i = 0; i<5; i++){
        printf("\nAUTO %d", i+1);
        ingreso_valores(&nomina[i]);
    }
    /*printf("Ingrese la marca");
    //scanf("%s", mio.marca);
    //gets(mio.marca);
    fgets(mio.marca, 20, stdin);
    printf("Ingrese Modelo");
    fgets(mio.modelo, 50, stdin);
    printf("Ingrese Anho");
    scanf("%d", &mio.anho);
    */
    for (i = 0; i < 5; i++){
        printf("\nAUTO %d", i+1);
        mostrar_valores(nomina[i]);
    }
    
    //printf("El auto es: \nMARCA: %s\nMODELO: %s\nANHO: %d", mio.marca, mio.modelo, mio.anho);
    

    return 0;
}