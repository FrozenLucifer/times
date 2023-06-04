#include <stdio.h>

void swap(int *, int *);

void sort(int *a, size_t n)
{
    int min_el, min_i;
    for (size_t i = 0; i < n; i++)
    {
        min_el = a[i];
        min_i = i;
        for (size_t j = i; j < n; j++)
        {
            if (a[j] < min_el)
            {
                min_el = a[j];
                min_i = j;
            }
        }
        swap(a + i, a + min_i);
    }
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}