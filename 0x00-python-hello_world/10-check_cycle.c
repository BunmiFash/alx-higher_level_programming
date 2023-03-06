#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check if a singly list contains circle
 * @list: pointer to the list to check
 * Return: 1 if there is a circle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *first;
	listint_t *secound;

	if (list == NULL || list->next == NULL)
		return (0);
	first = list->next;
	secound = list->next->next;

	while (first && secound && secound->next)
	{
		if (first == secound)
			return (1);

		first = first->next;
		secound = secound->next->next;
	}
	return (0);

}
