#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define DIM 1024
#define L_VET 16600


typedef struct{
        char *tokenNome;
        int tokenNumero;
        char *tokenPlatform;
        int *tokenAnno;
        char *tokenGenere;
        char *tokenPublisher;
        float tokenAmerica;
        float tokenEuropa;
        float tokenGiappone;
        float tokenAltro;
        float tokenGlobal;
    }Game;


int main()
{
    FILE *fp;
    char riga[DIM];
    Game gioco[L_VET];
    Game *a = gioco;

    fp= fopen("vgsales.csv", "r");

    if (fp == NULL){
        printf("ERRORE ");
        return 0;
    }
    printf("sono dentro ");

    int k=0;
    while(fgets(riga, DIM, fp)){
         // 1 array della riga, 2 dimensione array
         (*a).tokenNumero = atoi(strtok(riga, ","));
         (*a).tokenNome = strtok(NULL, ",");
         (*a).tokenPlatform = strtok(NULL, ",");
         (*a).tokenAnno = atoi(strtok(NULL, ","));
         (*a).tokenGenere = strtok(NULL, ",");
         (*a).tokenPublisher = strtok(NULL, ",");
         (*a).tokenAmerica = atof(strtok(NULL, ","));
         (*a).tokenEuropa = atof(strtok(NULL, ","));
         (*a).tokenGiappone = atof(strtok(NULL, ","));
         (*a).tokenAltro = atof(strtok(NULL, ","));
         (*a).tokenGlobal = atof(strtok(NULL, "\n"));

         printf("\n %s -- %d -- %s -- %d -- %s -- %s -- %.2f -- %.2f -- %.2f -- %.2f -- %.2f\n", 
         (*a).tokenNome, (*a).tokenNumero, (*a).tokenPlatform, (*a).tokenAnno, (*a).tokenGenere, (*a).tokenPublisher, (*a).tokenAmerica, (*a).tokenEuropa, (*a).tokenGiappone, (*a).tokenAltro, (*a).tokenGlobal);

         a++;

    }

    fclose(fp);

    return 1;
}
