#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

#ifndef N_MAX
#define N_MAX 10
#endif

#ifndef SORTED
#define SORTED 1
#endif

int create_array_random(int *, size_t);
int create_array_sorted(int *, size_t);

void output(int *, size_t);

void sort(int *, size_t);

long long int get_time_mcs()
{
    struct timeval t;
    gettimeofday(&t, NULL);
    long long int res = t.tv_sec * 1000000 + t.tv_usec; // микросекунды
    return res;
}

int main()
{
    srand(time(NULL));
    int a[N_MAX];
    size_t n = N_MAX;
    // printf("Input array: ");
    if (SORTED)
        create_array_sorted(a, n);
    else
        create_array_random(a, n);
    long long int start = get_time_mcs();
    // output(a, n);
    sort(a, n);
    // output(a, n);
    long long int end = get_time_mcs();
    printf("%lld", end - start);
    return 0;
}

void output(int *a, size_t n)
{
    size_t i = 0;
    printf("Array:");
    while (i < n)
    {
        printf(" %d", a[i]);
        i += 1;
    }
    printf("\n");
}

int create_array_random(int *a, size_t n)
{
    for (int i = 0; i < n; i++)
        a[i] = rand() % 1000;
}

int create_array_sorted(int *a, size_t n)
{
    for (int i = 0; i < n; i++)
        a[i] = i;
}