#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LUNG 1024

typedef struct
{
    char *cognome;
    char *nome;
    int anno;
}Persona;

int contarighe(FILE *fp, char *riga, int lung){

    int cont=0;
    while ( fgets(riga, lung, fp) )
    {
        cont++;
    }

    return cont;
}

void leggifile(Persona *p, FILE *fp, char *riga, int lung){

    int i=0;
    while (fgets(riga, lung, fp))
    {
        (p + i)->cognome = strdup(strtok(riga, ","));
        (p + i)->nome = strdup(strtok(NULL, ","));
        (p + i)->anno = atoi(strtok(NULL, "\n"));
        //printf("%d: %s, %s, %d \n", i+1, (p+i)->cognome, (p+i)->nome, (p+i)->anno );
        i++; 
        
    }
    
}

void bubblesort(Persona *p, int dim){
    
    for (int i = dim-1; i > 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            if ((p+1)->anno < (p+j)->anno)
            {
                Persona temp;
                temp = *(p+i);
                *(p+i)=*(p+j);
                *(p+j)=temp;
            }  
        } 
    } 
}

void stampa(Persona *p, int dim){

    for (int i = 0; i < dim; i++)
    {
        printf("%s, %s, %d \n", (p+i)->cognome, (p+i)->nome, (p+i)->anno);
    }
    
}

int main()
{
    FILE *fp;
    int dim;
    char *riga;
    Persona *p;
    //apro il file
    fp = fopen("file.csv", "r");
    //controllo file
    if (fp==NULL)
    {
        printf("ERRORE");
    }else{
        //conto le righe
        riga=(char*)malloc(sizeof (char)*LUNG);
        dim = contarighe(fp, riga, LUNG);
        //printf("%d", dim);
        //chiudo il file
        fclose(fp);
    }
    //riapro il file
    fp = fopen("file.csv", "r");
    //malloc di persona
    p=(Persona*)malloc(sizeof(Persona)*dim);
    //salvo i dati nella struttura
    leggifile(p, fp, riga, LUNG);
    //bubble sort decrescente
    bubblesort(p, dim);
    //stampa
    stampa(p, dim);
   
    
    
    return 0;
}
