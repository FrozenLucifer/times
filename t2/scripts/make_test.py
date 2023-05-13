import matplotlib.pyplot as plt
import os
import re
import numpy as np



data_directory = '../dataset'
types = ('1', '2', '3')
opts = ('O0', 'O2')

fig, axs = plt.subplots(3, 2)
t_i = 0
for t in types:
    opt_i = 0
    for opt in opts:
        programs_dir = "../dataset/"+t+'/'+opt+'/'
        print(f"////////// PROGRAM {programs_dir} ////////////")
        for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
            X = []
            Y = []
            tests_dir = os.path.join(data_directory, programs_dir)
            for test in os.listdir(tests_dir):  # Цикл по всем тестам
                if '_' + input_type in str(test):  # Если подходящий по входным данным тест
                    test_f = os.path.join(tests_dir, test)
                    test_t = int(re.search(r'\d+', test).group(0))
                    print(test)

                    f = open(test_f)
                    line = f.readline()
                    n = 0
                    time_sum = 0
                    while line:
                        n += 1
                        time_sum += int(line)
                        line = f.readline()

                    X.append(test_t)
                    Y.append(time_sum / n)


            X = np.array(X)
            Y = np.array(Y)
            indices = X.argsort()
            X = X[indices]
            Y = Y[indices]


            for z in zip(X, Y):
                print(z)
            axs[t_i, opt_i].plot(X, Y)
        axs[t_i, opt_i].set_title(f'type:{t} opt:{opt}')
        opt_i += 1
    t_i += 1






for ax in axs.flat:
    ax.label_outer()
fig.legend(('sorted', 'unsorted'))

plt.show()