#include  <stdio.h>
#include  <stdlib.h>

typedef struct  node 
{
    int  valore;
    char nome[20];
    struct  node* next;
}Node;



void inserimentoOrdinato(Node **head, Node *element)
{
    Node *curr = *head, *prev = NULL;

    while (curr != NULL)
    {
        if (element->valore >= curr->valore)
            break;

        prev = curr;
        curr = curr->next;
    }

    if (prev == NULL)
        *head = element;
    else
        prev->next = element;

    element->next = curr;
}

void liberaSpazio()
{
    


}

int main(int argc, char const *argv[])
{
    Node* lista=NULL;
    Node* temp=NULL;

    for (int j = 0; j < 3; j++)
    {
        temp=(Node*)malloc(sizeof(Node));
        printf("inserisci un numero: ");
        scanf("%d", &temp->valore);
        printf("inseirsci il nome: ");
        scanf("%s", temp->nome);
        inserimentoOrdinato(&lista, temp);
    }
    

    while (lista != NULL)
    {
        printf("%d %s\n", lista->valore, lista->nome);
        lista=lista->next;
    }
    
}