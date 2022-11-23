#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    char name[200];
    struct node *next;

}Node;

int main()
{
    Node *list=(Node*)malloc(sizeof (Node));
    Node *temp=(Node*)malloc(sizeof (Node));

    printf("inserisci un nome ");
    gets(list->name);
    list->next=NULL;
    printf("nome 1: %s\n", list->name);

    //printf("%s\n", list->name);

    printf("inserisci un nome ");
    gets(temp->name);
    printf("nome 2: %s\n", temp->name);
    temp->next=NULL;

    list->next= temp;

    printf("%s\n", list->next->name);

    printf("inserisci un nome ");
    scanf("%s", temp->name);
    printf("nome 3: %s\n", temp->name);
    temp->next=NULL;

    list->next->next = temp;

    //printf("%s\n", list->next->name);
    
    printf("\n%s  %s  %s",list->name, list->next->name, list->next->next->name);
    //printf("\n%s  %s", list->name, list->next->name);
    free(list);
    free(temp);
    
    return 0;
}

