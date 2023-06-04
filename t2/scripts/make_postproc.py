import matplotlib.pyplot as plt
import sys

methods=sys.argv[1].split()
opts=sys.argv[2].split()
arrays=sys.argv[3].split()
sizes=sys.argv[4].split()
lines = ("-", "--", "-.")

#График T_avg(n) для всех вариантов
fig_1, axs_1 = plt.subplots(3, 2)

for t_i, t in enumerate(methods):
    for opt_i, opt in enumerate(opts):
        for a_i, array in enumerate(arrays):
            X = []
            Y = []
            f = open(f"../preproc/preproc_{t}_{opt}_{array}.txt", 'r')
            line = f.readline()
            line = f.readline()
            while line:
                X.append(int(line.split()[0]))
                Y.append(float(line.split()[1]))
                line = f.readline()
            axs_1[t_i, opt_i].plot(X, Y, lines[a_i])
        axs_1[t_i, opt_i].grid()
        axs_1[t_i, opt_i].set_title(f'type: {t}   opt: {opt}')
fig_1.legend(arrays)  
fig_1.set_size_inches(14, 10)

#График T_avg, T_min, T_max(n) для O2
fig_2, axs_2 = plt.subplots(3, 2)

for t_i, t in enumerate(methods):
    for a_i, array in enumerate(arrays):
        X = []
        Y_max = []
        Y_avg = []
        Y_min = []
        f = open(f"../preproc/preproc_{t}_O2_{array}.txt", 'r')
        line = f.readline()
        line = f.readline()
        while line:
            X.append(int(line.split()[0]))
            Y_avg.append(float(line.split()[1]))
            Y_min.append(float(line.split()[2]))
            Y_max.append(float(line.split()[3]))
            line = f.readline()
        axs_2[t_i, a_i].plot(X, Y_avg, lines[0])
        axs_2[t_i, a_i].plot(X, Y_min, lines[1])
        axs_2[t_i, a_i].plot(X, Y_max, lines[2])
        axs_2[t_i, a_i].grid()
        axs_2[t_i, a_i].set_title(f'type: {t}   array: {array}')
fig_2.legend(('среднее', 'минимум', 'максимум'))
fig_2.set_size_inches(14, 10)

#График с усами для a[i] O2
fig_3, axs_3 = plt.subplots(2, 1)

for a_i, array in enumerate(arrays):
    X = []
    Y_max = []
    Y_avg = []
    Y_min = []
    f = open(f"../preproc/preproc_a[i]_O2_{array}.txt", 'r')
    line = f.readline()
    line = f.readline()
    while line:
        info = list(map(float, line.split()))
        X.append(int(info[0]))
        Y_avg.append(float(info[1]))
        Y_min.append(float(info[2]))
        Y_max.append(float(info[3]))

        bp = axs_3[a_i].boxplot([], widths = 100, positions=[info[0]])
        bp['whiskers'][0].set_ydata([info[2], info[4]])
        bp['whiskers'][1].set_ydata([info[6], info[3]])
        bp['caps'][0].set_ydata([info[2]])
        bp['caps'][1].set_ydata([info[3]])
        bp['medians'][0].set_ydata([info[5]])
        bp['boxes'][0].set_ydata([info[4], info[4], info[6], info[6], info[4]])

        line = f.readline()
    axs_3[a_i].plot(X, Y_avg, lines[0])
    axs_3[a_i].plot(X, Y_min, lines[1])
    axs_3[a_i].plot(X, Y_max, lines[2])
    axs_3[a_i].grid()
    xticks = [1] + [i for i in range(1000, 10000+1, 1000)]
    axs_3[a_i].set_xticks(xticks + [10100])
    axs_3[a_i].set_xticklabels(xticks + [""])
    axs_3[a_i].set_title(f'type: a[i]   array: {array}')
fig_3.set_size_inches(14, 10)

fig_1.savefig('../graphs/graph_all.svg')
fig_2.savefig('../graphs/graph_O2.svg')
fig_3.savefig('../graphs/graph_a[i]_O2.svg')
plt.show()
