# Практика. Задание №4

## Задание 1. Исследование функции nanosleep.
Есть в презентации. Следует гуглить примеры каждой функции, так понятнее.


## Задание 2. Сравнение производительности программы.

1. Разные способы работы с элементами одномерного массива:

(a) использование операции индексации a[i];  
Все понятно.

(b) формальная замена операции индексации на выражение *(a + i);  
Все понятно.

(c) использование указателей для работы с массивом.  
Использование ```int* ptr_start = a``` и ```int* ptr_end = a + n```

2. Разные уровни оптимизации: O0, O2.  
Параметр gcc

3. Разные исходные массивы.  
Генерировать тесты питоном.

### Скрипты
build_apps.sh - циклы + gcc

update_data.sh - прогоняет программу по тестам(много раз), сохраняет это куда-то(для каждого типа входных данных в разное место)

make_preproc.**py** - считает все, что сказано в задании.   
Инфа про эти штуки: https://e-learning.bmstu.ru/iu7/mod/folder/view.php?id=855

make_postproc.**py** - matplotlib (https://www.codecamp.ru/blog/matplotlib-multiple-plots/)

go.sh - тут понятно

