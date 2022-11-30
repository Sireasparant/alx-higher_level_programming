#ifndef LIST_H
#define LIST_H
#include <stdlib.h>

/**
 * struct listint_s - Singly linked list
 * @n: integer
 * @next: pointer to next node
 * 
 * Description: singly linked list node structure
*/

typedef struct listint_s
{
    /* data */
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);
#endif /* LIST_H */
