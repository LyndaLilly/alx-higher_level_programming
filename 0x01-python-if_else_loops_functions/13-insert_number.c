#include "lists.h"

/**
 * insert_node - this inserts the node
 * @head: this si the head node
 * @number: this si the num nide
 * Return: fail or success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *mx;

	mx = malloc(sizeof(listint_t));
	if (mx == NULL)
		return (NULL);
	mx->n = number;

	if (node == NULL || node->n >= number)
	{
		mx->next = node;
		*head = mx;
		return (mx);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	mx->next = node->next;
	node->next = mx;
	return (mx);
}
