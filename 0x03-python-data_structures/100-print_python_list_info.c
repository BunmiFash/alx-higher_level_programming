#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* * print_python_list_info - prints infos about a python list
* * @p: the python object o check details
* **/

void print_python_list_info(PyObject *p){
long int n = PyList_Size(p);
int i;
PyListObject *object = (PyListObject *)p;

printf("[*] Size of the Python List = %li\n", n);
printf("[*] Allocated = %li\n", object->allocated);
for (i = 0; i < n; i++)
printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
}
