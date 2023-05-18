import os, re

data_directory = '../dataset'
types = ('1', '2', '3')
opts = ('O0', 'O2')
sizes = ['1'] + [str(i) for i in range(250, 10000+1, 250)]
datas = []
for t in types:
    for opt in opts:
        programs_dir = "../dataset/"+t+'/'+opt+'/'
        print(f"////////// PROGRAM {programs_dir} ////////////")
        for input_type in ('sorted', 'unsorted'):  # Цикл по типу входных данных
            f_output = open(f"../dataset/data_preproc/preproc_{t}_{opt}_{input_type}.txt", 'w')
            for test in sizes:  # Цикл по всем тестам
                print(test)

                f = open(f'../dataset/{t}/{opt}/output_{input_type}_{test}.txt')
                
                data = []
                line = f.readline()
                while line:
                    el = int(line)
                    data.append(el)
                    line = f.readline()
                data.sort()
                n = len(data)
                f_output.write(f"{test}: Среднее ар: {int(sum(data)/n)}, медиана: {data[n//2]}, макс: {max(data)}, мин: {min(data)}, ниж.квант: {data[n//4]}, верх.квант: {data[n*3//4]}\n")
            f_output.close()
