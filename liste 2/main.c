#include  <stdio.h>
#include  <stdlib.h>

typedef struct  node 
{
    int  valore;
    struct  node* next;
}Node;


void insertHead(struct node** head, int newvalore){

    Node* newtesta = (Node*)malloc(sizeof(Node));
    
    newtesta->valore = newvalore;   //carico il nuovo valore nel node nuovo
    newtesta->next = (*head);       //il next punterà alla testa attuale
    (*head) = newtesta;             //assegno la nuova testa
    
}

void inserisciinordine(Node **head, Node *elemento){
    Node *curr = *head, *prev=NULL;

    while (curr != NULL)
    {
        if (elemento->valore <= curr->valore)
        {
            break;
        }
        prev = curr;
        curr = curr->next;
    }

    if (prev == NULL)
    {
        *head = elemento;
    }else{
        prev->next = elemento;
    }
    elemento->next=curr;
}

int main(int argc, char const *argv[])
{
    Node* lista;
    Node* temp;

    lista=(Node*)malloc(sizeof(Node)*3);
    temp=(Node*)malloc(sizeof(Node)*4);
    
    insertHead(&lista, 5);
    insertHead(&lista, 7);
    insertHead(&lista, 2);
    insertHead(&temp, 9);
    inserisciinordine(&lista, temp);
    inserisciinordine(&lista, temp);

    for (int i = 0; i < 4; i++)
    {
        printf("%d\n", lista->valore);
        lista=lista->next;
    }

    return 0;
}