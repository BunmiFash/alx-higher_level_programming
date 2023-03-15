#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - function to print py info
* @p: py obj
* Return: void
*/
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, lm;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
	{
		lm = 10;
	}
	else
	{
		lm = size + 1;
	}

	printf("  first %ld bytes:", lm);

	for (i = 0; i < lm; i++)
	{
		if (string[i] >= 0)
		{
			printf(" %02x", string[i]);
		}
		else
		{
			printf(" %02x", 256 + string[i]);
		}

		printf("\n");
	}
}
/**
* print_python_list - info on py list
* @p: py obj
* Return: void
*/
void print_python_list(PyObject *p)
{

	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
		{
			print_python_bytes(obj);
		}
	}
}
