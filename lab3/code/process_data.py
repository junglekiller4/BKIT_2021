import sys
import os
import json
from lab_python_fp import cm_timer_1, Unique, field, print_result, gen_random

# try:
#     path = sys.argv[1]
# except IndexError:
#     raise ValueError("Не указан путь к файлу.")
# else:
path = r"C:\Users\J4ngle\Desktop\lab3\data_light.json"
with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(lst):
    return sorted(list(Unique(field(lst, 'job-name'), ignore_case=True)), key=str.lower)

@print_result
def f2(lst):
    return list(filter(lambda s: str.startswith(str.lower(s), 'программист'), lst))

@print_result
def f3(lst):
    return list(map(lambda s: s + " c опытом Python", lst))

@print_result
def f4(lst):
    return dict(zip(lst, list(f'зарплата {num} руб.' for num in gen_random(len(lst), 1000000, 2000000))))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
os.system('pause')