#include <stdio.h>
#include <sys/time.h>

#define N_MAX 10000
#define ERROR_ARRAY_OVERFLOW 100

int stream_input_array(int *, size_t *);

void output(int *, size_t);

void sort(int *, size_t);

long long int get_time_mcs()
{
    struct timeval t;
    gettimeofday(&t, NULL);
    long long int res = t.tv_sec * 1000000 + t.tv_usec; //микросекунды
    return res;
}


int main()
{
    int status = 0, a[N_MAX];
    size_t n = 0;
    // printf("Input array: ");
    status = stream_input_array(a, &n);
    if (status != 1)
    {
        long long int start = get_time_mcs();
        sort(a, n);
        long long int end = get_time_mcs();
        printf("%lld", end - start);
        // output(a, n);
    }
    else
        printf("Incorrect input.");
    return status;
}

int stream_input_array(int *a, size_t *n)
{
    int status = 0, rc = 1, x;
    size_t i = 0;
    while (rc != 0 && !status)
    {
        rc = scanf("%d", &x);
        if (rc && *n == N_MAX)
            status = ERROR_ARRAY_OVERFLOW;
        else if (rc)
        {
            a[i] = x;
            *n += 1;
        }
        i++;
    }
    if (*n == 0)
        status = 1;
    return status;
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
}
