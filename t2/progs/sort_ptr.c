#include <stdio.h>

void swap(int *, int *);

void sort(int *a, size_t n)
{
    int* a_now_i = a;
    int* a_end = a + n;
    int *min_el_ptr;
    for (size_t i = 0; a_now_i != a_end; a_now_i++, i++)
    {
        min_el_ptr = a_now_i;
        int* a_now_j = a_now_i;
        for (size_t j = i; a_now_j != a_end; a_now_j++, j++)
        {
            if (*a_now_j < *min_el_ptr)
            {
                min_el_ptr = a_now_j;
            }
        }
        swap(a_now_i, min_el_ptr);
    }
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}