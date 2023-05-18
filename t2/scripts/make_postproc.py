import matplotlib.pyplot as plt
import os
import re


data_directory = '../dataset'
types = ('1', '2', '3')
opts = ('O0', 'O2')
sizes = ['1'] + [str(i) for i in range(250, 10000+1, 250)]
datas = []

fig_1, axs_1 = plt.subplots(3, 2)

t_i = 0
for t in types:
    opt_i = 0
    for opt in opts:
        for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
            X = []
            Y = []
            f = open(f"../dataset/data_preproc/preproc_{t}_{opt}_{input_type}.txt", 'r')
            line = f.readline()
            while line:
                X.append(int(list(line.split())[0][:-1]))
                Y.append(int(list(line.split())[3][:-1]))
                line = f.readline()
            axs_1[t_i, opt_i].plot(X, Y)
        axs_1[t_i, opt_i].grid()
        axs_1[t_i, opt_i].set_title(f'type:{t} opt:{opt}')
        opt_i += 1
    t_i += 1
fig_1.legend(('sorted', 'unsorted'))  


fig_2, axs_2 = plt.subplots(3, 2)

t_i = 0
for t in types:
    input_i = 0
    for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
        X = []
        Y_max = []
        Y_avg = []
        Y_min = []
        f = open(f"../dataset/data_preproc/preproc_{t}_{opt}_{input_type}.txt", 'r')
        line = f.readline()
        while line:
            X.append(int(list(line.split())[0][:-1]))
            Y_max.append(int(list(line.split())[7][:-1]))
            Y_avg.append(int(list(line.split())[3][:-1]))
            Y_min.append(int(list(line.split())[9][:-1]))
            line = f.readline()
        axs_2[t_i, input_i].plot(X, Y_max)
        axs_2[t_i, input_i].plot(X, Y_avg)
        axs_2[t_i, input_i].plot(X, Y_min)
        axs_2[t_i, input_i].grid()
        axs_2[t_i, input_i].set_title(f'type:{t} opt:{opt}')
        input_i += 1
    t_i += 1

fig_2.legend(('максимум', 'среднее', 'минимум'))

fig_3, axs_3 = plt.subplots(2, 1)

input_i = 0
for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
    datas = []
    for size in sizes:
        data = []
        f = open(f"../dataset/1/O2/output_{input_type}_{size}.txt", 'r')
        line = f.readline()
        while line:
            el = int(line)
            data.append(el)
            line = f.readline()
        datas.append(data)
    X = []
    Y_avg = []
    Y_min = []
    Y_max = []
    f = open(f"../dataset/data_preproc/preproc_1_O2_{input_type}.txt", 'r')
    line = f.readline()
    while line:
        X.append(int(list(line.split())[0][:-1]))
        Y_max.append(int(list(line.split())[7][:-1]))
        Y_avg.append(int(list(line.split())[3][:-1]))
        Y_min.append(int(list(line.split())[9][:-1]))
        line = f.readline()

    axs_3[input_i].plot(X, Y_max)
    axs_3[input_i].plot(X, Y_avg)
    axs_3[input_i].plot(X, Y_min)
    axs_3[input_i].boxplot(datas, showfliers=False, positions=X, widths = 100)
    axs_3[input_i].set_xticks([1] + [i for i in range(1000, 10000+1, 1000)])
    axs_3[input_i].set_xticklabels([1] + [i for i in range(1000, 10000+1, 1000)])
    axs_3[input_i].grid()
    axs_3[input_i].set_title(input_type)
    input_i += 1

fig_1.set_size_inches(14, 10)
fig_1.savefig('../graphs/graph_1.svg')

fig_2.set_size_inches(14, 10)
fig_2.savefig('../graphs/graph_2.svg')

fig_3.set_size_inches(14, 10)
fig_3.savefig('../graphs/graph_3.svg')
plt.show()

