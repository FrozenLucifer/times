import sys
 
from math import sqrt
methods=sys.argv[1].split()
opts=sys.argv[2].split()
arrays=sys.argv[3].split()
sizes=sys.argv[4].split()

print("PREPROC STARTED...")
for method in methods:
    for opt in opts:
        for array in arrays:
            f_preproc = open(f"../preproc/preproc_{method}_{opt}_{array}.txt", 'w')
            f_preproc.write("Размер    Среднне    Минимум   Максимум Ниж.Квантиль   Медиана Верх.Квантиль RSE (%)\n")
            for size in sizes:
                data = []
                f = open(f'../dataset/{method}_{opt}_{array}_{size}.txt', 'r')
                line = f.readline()
                while line:
                    el = int(line)
                    data.append(el)
                    line = f.readline()
                data.sort()
                s = sum(data)
                n = len(data)
                avg = s/n
                s2 = 0
                for el in data:
                    s2 += (el - avg)**2
                s2 /= n - 1
                s = sqrt(s2)
                serr = s / sqrt(n)
                RSE = 0
                try:
                    RSE = serr / avg * 100
                except:
                    pass
                f_preproc.write(f'{size:6} {avg:10.2f} {min(data):10} {max(data):10} {data[n//4]:12} {data[n//2]:9} {data[3*n//4]:13} {RSE:7.3f}\n')

print("PREPROC SUCCES")
