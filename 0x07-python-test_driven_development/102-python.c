#include "Python.h"

/**
 * print_python_string - this prints the python string.
 * @p: python string to be printed.
 */
void print_python_string(PyObject *p)
{
	long int wt;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	wt = ((PyASCIIObject *)(p))->wt;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", wt);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &wt));
}
