#include <stdlib.h>
#include "lists.h"


/**
 * insert_node - function to insert to an orderes singly list
 * @head: pointer to the head of the list
 * @number: the number to be added to the list
 * Return: address to the new list or Null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (current_node == NULL || current_node->n >= number)
	{
		new->next = current_node;
		*head = new;
		return (new);
	}
	while (current_node && current_node->next && current_node->next->n < number)
		current_node = current_node->next;

	new->next = current_node->next;
	current_node->next = new;

	return (new);
}
