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

            # for z in zip(X, Y):
            #     print(z)
            axs[t_i, opt_i].plot(X, Y)
        axs[t_i, opt_i].grid()
        axs[t_i, opt_i].set_title(f'type:{t} opt:{opt}')

        opt_i += 1
    t_i += 1

for ax in axs.flat:
    ax.label_outer()
fig.legend(('sorted', 'unsorted'))

# plt.show()

fig2, axs2 = plt.subplots(3, 2)

t_i = 0
for t in types:
    programs_dir = "../dataset/"+t+'/O2/'
    print(f"////////// PROGRAM {programs_dir} ////////////")
    input_i = 0
    for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
        X = []
        Y_avg = []
        Y_min = []
        Y_max = []
        tests_dir = os.path.join(data_directory, programs_dir)
        for test in os.listdir(tests_dir):  # Цикл по всем тестам
            if '_' + input_type in str(test):  # Если подходящий по входным данным тест
                test_f = os.path.join(tests_dir, test)
                test_t = int(re.search(r'\d+', test).group(0))

                f = open(test_f)
                line = f.readline()
                n = 0
                time_sum = 0
                min_data = 1e10
                max_data  = 0
                while line:
                    e = int(line)
                    min_data = min(min_data, e)
                    max_data = max(max_data, e)
                    n += 1
                    time_sum += e
                    line = f.readline()

                X.append(test_t)
                Y_avg.append(time_sum / n)
                Y_min.append(min_data)
                Y_max.append(max_data)


        X = np.array(X)
        Y_avg = np.array(Y_avg)
        Y_min = np.array(Y_min)
        Y_max = np.array(Y_max)
        indices = X.argsort()
        X = X[indices]
        Y_avg = Y_avg[indices]
        Y_min = Y_min[indices]
        Y_max = Y_max[indices]

        # for z in zip(X, Y):
        #     print(z)
        axs2[t_i, input_i].plot(X, Y_avg)
        axs2[t_i, input_i].plot(X, Y_min)
        axs2[t_i, input_i].plot(X, Y_max)
        axs2[t_i, input_i].set_title(f'type:{t} input:{("sorted", "unsorted")[input_i]}')
        axs2[t_i, input_i].grid()

        input_i += 1

    t_i += 1
fig2.legend(('среднее', 'минимум', 'максимум'))



fig3, axs3 = plt.subplots(2, 1)

programs_dir = "../dataset/1/O2/"
print(f"////////// PROGRAM {programs_dir} ////////////")
input_i = 0
for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
    X = []
    Y_avg = []
    Y_min = []
    Y_max = []
    Y_cvt1 = []
    Y_cvt2 = []
    Y_cvt3 = []
    tests_dir = os.path.join(data_directory, programs_dir)
    for test in os.listdir(tests_dir):  # Цикл по всем тестам
        if '_' + input_type in str(test):  # Если подходящий по входным данным тест
            test_f = os.path.join(tests_dir, test)
            test_t = int(re.search(r'\d+', test).group(0))

            f = open(test_f)
            line = f.readline()
            n = 0
            time_sum = 0
            min_data = 1e10
            max_data = 0
            data = []
            while line:
                e = int(line)
                data.append(e)
                min_data = min(min_data, e)
                max_data = max(max_data, e)
                n += 1
                time_sum += e
                line = f.readline()
            data.sort()
            X.append(test_t)
            Y_avg.append(time_sum / n)
            Y_min.append(min_data)
            Y_max.append(max_data)
            Y_cvt1.append(data[int(n/4)])
            Y_cvt2.append(data[int(n/2)])
            Y_cvt3.append(data[int(3*n/4)])


    X = np.array(X)
    Y_avg = np.array(Y_avg)
    Y_min = np.array(Y_min)
    Y_max = np.array(Y_max)
    Y_cvt1 = np.array(Y_cvt1)
    Y_cvt2 = np.array(Y_cvt2)
    Y_cvt3 = np.array(Y_cvt3)
    indices = X.argsort()
    X = X[indices]
    Y_avg = Y_avg[indices]
    Y_min = Y_min[indices]
    Y_max = Y_max[indices]
    Y_cvt1 = Y_cvt1[indices]
    Y_cvt2 = Y_cvt2[indices]
    Y_cvt3 = Y_cvt3[indices]

    # for z in zip(X, Y):
    #     print(z)
    axs3[input_i].plot(X, Y_avg)
    axs3[input_i].plot(X, Y_min)
    axs3[input_i].plot(X, Y_max)
    axs3[input_i].plot(X, Y_cvt1)
    axs3[input_i].plot(X, Y_cvt2)
    axs3[input_i].plot(X, Y_cvt3)
    axs3[input_i].set_title(f'type:{1} input:{("sorted", "unsorted")[input_i]}')
    axs3[input_i].grid()

    input_i += 1

fig3.legend(('среднее', 'минимум', 'максимум', '1/4', '1/2', '3/4'))

plt.show()

