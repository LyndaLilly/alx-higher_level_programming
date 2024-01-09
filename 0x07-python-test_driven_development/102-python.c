#include "Python.h"

/**
 * print_python_string - this prints python string.
 * @p: thos os the python string to e printed.
 */
void print_python_string(PyObject *p)
{
	long int br;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	br = ((PyASCIIObject *)(p))->br;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", br);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &br));
}
