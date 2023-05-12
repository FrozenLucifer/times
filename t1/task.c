#include <stdio.h>
#include <sys/time.h>
#include <time.h>
#define N 5
#define TIME_1SEC {1, 0}
#define TIME_100MSEC {0, 100000000}
#define TIME_50MSEC {0, 50000000}
#define TIME_10MSEC {0, 10000000}


int nanosleep(const struct timespec *tw, struct timespec *tr);

int clock_gettime(clockid_t clockid, struct timespec *tp);

clock_t clock(void);


long long int get_by_gettimeofday(struct timespec t)
{
    struct timeval start, end;
    struct timespec tmp;
    gettimeofday(&start, NULL);
    nanosleep(&t, &tmp);
    gettimeofday(&end, NULL);
    long long int delta = (end.tv_sec - start.tv_sec) * 1000000 + end.tv_usec - start.tv_usec; //микросекунды
    return delta;
}

long long int get_by_clock_gettime(struct timespec t)
{
    struct timespec start, end;
    struct timespec tmp;
    clock_gettime(CLOCK_REALTIME, &start);
    nanosleep(&t, &tmp);
    clock_gettime(CLOCK_REALTIME, &end);
    long long int delta = (end.tv_sec - start.tv_sec) * 1000000000 + end.tv_nsec - start.tv_nsec; //наносекунды
    return delta;
}

long long int get_by_clock(struct timespec t)
{
    clock_t start, end;
    struct timespec tmp;
    start = clock();
    nanosleep(&t, &tmp);
    end = clock();
    long long int delta = end - start; //
    return delta;
}

void run_gettimeofday(struct timespec t)
{
    printf("%ld\n", CLOCKS_PER_SEC);
    printf("...gettimeofday...\n");
    for (int i = 0; i < N; i++)
    {
        printf("%lld mcs\n", get_by_gettimeofday(t));
    }
}


void run_clock_gettime(struct timespec t)
{
    printf("...clock_gettime...\n");
    for (int i = 0; i < N; i++)
    {
        printf("%lld ns\n", get_by_clock_gettime(t));
    }
}


void run_clock(struct timespec t)
{
    printf("...clock...\n");
    for (int i = 0; i < N; i++)
    {
        printf("%lld clocks\n", get_by_clock(t));
    }
}


int main()
{

    struct timespec t = TIME_1SEC, tim2;
    // long long int sum = 0;

    // run_gettimeofday(t);

    // run_clock_gettime(t);

    run_clock(t);

    return 0;
}



