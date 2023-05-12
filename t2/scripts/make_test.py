import matplotlib.pyplot as plt
import os
import re
import numpy as np

data_directory = '../dataset'

for programs_dir in os.listdir(data_directory):  # Цикл по типу программы(a[i], *(a+i), ptr)
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

        plt.plot(X, Y)
        for z in zip(X, Y):
            print(z)
        plt.show()
