#include "lists.h"

/**
 * is_palindrome - check if the list is palindrome
 * @head: passed argument as a double pointer
 *
 * Return: 1 at success
 */
int is_palindrome(listint_t **head)
{
	listint_t *gacye = *head;
	listint_t *vuba = *head;
	listint_t *haba = NULL;
	listint_t *idaho;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (vuba != NULL && vuba->next != NULL)
	{
		vuba = vuba->next->next;
		idaho = gacye->next;
		gacye->next = haba;
		haba = gacye;
		gacye = idaho;
	}
	if (vuba != NULL)
	{
		gacye = gacye->next;
	}
	while (haba != NULL && gacye != NULL)
	{
		if (haba->n != gacye->n)
		{
			return (0);
		}
		haba = haba->next;
		gacye = gacye->next;
	}
	return (1);
}

