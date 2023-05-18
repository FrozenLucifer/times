# types = ('1', '2', '3')
# opts = ('O0', 'O2')
# sizes = ['1'] + [str(i) for i in range(250, 10000+1, 250)]
# sizes_2 = ["1", "500", "1000", "2000", "4000",
#            "5000", "7000", "8000", "9000", "10000",]
# for t in types:
#     for opt in opts:
#         for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
#             print(t, opt, input_type)
#             f = open(
#                 f"../dataset/data_preproc/preproc_{t}_{opt}_{input_type}.txt", 'r')
#             line = f.readline()
#             while line:
#                 if list(line.split())[0][:-1] in sizes_2:
#                     print(list(line.split())[3][:-1])
#                 line = f.readline()
from math import log
sizes = ['1'] + [str(i) for i in range(250, 10000+1, 250)]
sizes_2 = ["1", "500", "1000", "2000", "4000",
           "5000", "7000", "8000", "9000", "10000",]
for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
    print(input_type)
    f = open(
        f"../dataset/data_preproc/preproc_1_O2_{input_type}.txt", 'r')
    line = f.readline()
    t_prev = 10000000
    n_prev = 10000000
    x = -1
    while line:
        n = int(list(line.split())[0][:-1])
        t = int(list(line.split())[3][:-1])
        if t != 0 and t_prev != 0:
            x = (log(t) - log(t_prev))/(log(n) - log(n_prev))
        print(n_prev, t, round(x, 3))
        t_prev = t
        n_prev = n
        line = f.readline()

