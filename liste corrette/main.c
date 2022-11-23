/*crea  una  lista e la  stampa*/
#include  <stdio.h>
#include  <stdlib.h>

typedef struct  node 
{
    int  valore;
    struct  node* next;
}Node;

void stampa(Node* l){
    printf("%d  %p\n", l->valore, l->next);
    if (l->next != NULL)
    {
        stampa(l->next);
    }
    
}

void contatore(Node* l, int i){
    i++;

    if (l->next != NULL)
    {
        contatore(l->next, i);
    }

    if (l->next == NULL)
    {
        printf("%d", i);
    }
}

int  main()
{
    int n;
    Node* lista;
    Node* l;
    lista=NULL;
    
    do
    {
        printf("Inserisci  un  naturale o  -1 per  terminare\n");
        scanf("%d",&n);
        if (n>=0) 
        {
            if (lista==NULL) /*  prima  iterazione  */ 
            {
                lista = (Node*)  malloc(sizeof(Node));
                l = lista;
            }
            else /*  iterazioni  successive  */
            {
                l->next = (Node*)  malloc(sizeof(Node));
                l = l->next;
            }
            l->valore = n;
            l->next = NULL;
        }
    } while (n>=0);
    
    l=lista;
    int i=0;
    stampa(l);
    contatore(l, i);
    
    /*
    l=lista;
    printf("numeri  inseriti: \n");

    int i=0;
    while (l!=NULL)
    {
        printf("%d - %p \n",l->valore, l->next);
        l=l->next;
    }
    printf("\n");

    
    l=lista;
    while (l!=NULL)
    {
        l=l->next;
        i++;
    }

    printf("contatore: %d", i);
    */
    
    return  0;
    }