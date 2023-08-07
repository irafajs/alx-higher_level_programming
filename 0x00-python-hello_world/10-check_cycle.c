#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check cycle in a singly list availability
 * @list: passed param to a struct
 *
 * Return: 0 at success
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (01);
		}
	}
	return (0);
}
