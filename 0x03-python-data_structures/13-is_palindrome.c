#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - check if function is a palindrome
 * @head: passed argument as a double pointer
 *
 * Return: 0 at success
 */

int is_palindrome(listint_t **head)
{
	listint_t *gake = *head;
	listint_t *cyane = *head;
	listint_t *haba = NULL;
	listint_t *idaho = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (0);
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
	return (0);
}
