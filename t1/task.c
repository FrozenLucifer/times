#include <stdio.h>
#include <sys/time.h>
#include <time.h>
#include <x86gprintrin.h>

#define N 10
#define TIME_1SEC {1, 0}
#define TIME_100MSEC {0, 100000000}
#define TIME_50MSEC {0, 50000000}
#define TIME_10MSEC {0, 10000000}
#define PROC_TICK 2800000000

#define NS_TO_S 1000000000
#define MCS_TO_S 1000000

int nanosleep(const struct timespec *tw, struct timespec *tr);

int clock_gettime(clockid_t clockid, struct timespec *tp);

clock_t clock(void);

unsigned long long __rdtsc(void);

    
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
    long long int delta = end - start;
    return delta;
}

long long int get_by_rdtsc(struct timespec t)
{
    unsigned long long start, end;
    struct timespec tmp;
    start = __rdtsc();
    nanosleep(&t, &tmp);
    end = __rdtsc();
    long long int delta = end - start;
    return delta;
}

void run_gettimeofday(struct timespec t)
{
    printf("...gettimeofday...\n");
    unsigned long long sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum += get_by_gettimeofday(t);
    }
    printf("%lf s\n", (double)sum/N/MCS_TO_S);
}


void run_clock_gettime(struct timespec t)
{
    printf("...clock_gettime...\n");
    unsigned long long sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum += get_by_clock_gettime(t);
    }
    printf("%lf s\n", (double)sum/N/NS_TO_S);
}


void run_clock(struct timespec t)
{
    printf("...clock...\n");
    unsigned long long sum = 0;
    for (int i = 0; i < N; i++)
    {   
        sum += get_by_clock(t);
    }
    printf("%lf ticks\n", (double)sum/N);
}

void run_rdtsc(struct timespec t)
{
    printf("...__rdtsc...\n");
    unsigned long long sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum += get_by_rdtsc(t);
    }
    printf("%lf s\n", (double)sum/N/PROC_TICK);
}


int main()
{
    struct timespec t = TIME_10MSEC, tim2;

    struct timespec times[4] = {TIME_10MSEC, TIME_50MSEC, TIME_100MSEC, TIME_1SEC};
    char strings[4][16] = {"TIME_10MSEC", "TIME_50MSEC", "TIME_100MSEC", "TIME_1SEC"};
    for (int i = 0; i < 4; i++)
    {
        printf("%s\n", strings[i]);
        run_gettimeofday(times[i]);
    
        run_clock_gettime(times[i]);
    
        run_clock(times[i]);
        
        run_rdtsc(times[i]);
    }

    return 0;
}
