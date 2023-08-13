#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

int is_palindrome(listint_t **head)
{
	listint_t *gake = *head;
	listint_t *cyane = *head;
	listint_t *haba = NULL;
	listint_t *idaho = NULL;
	/*listint_t *igi_cyambere = *head;*/

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (cyane != NULL && cyane->next != NULL)
	{
		cyane = cyane->next->next;
		idaho = gake->next;
		haba = gake;
		gake = idaho;
	}
	if (cyane != NULL)
	{
		gake = gake->next;
	}
	while (haba != NULL && gake != NULL)
	{
		if (haba->n !=  gake->n)
		{
			return (0);
		}
		haba = haba->next;
		gake = gake->next;
	}
	return(1);
}

