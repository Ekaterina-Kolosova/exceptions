task = input('Введите через пробел действие и 2 числа')
task_list = task.split(' ')
operators = ['+', '-', '*', '/']

assert task_list[0] in operators, 'Введено неверное арифметическое действие'
assert task_list[2] in task_list, 'Введено менее двух чисел'

try:
    task_list[1] = int(task_list[1])
    task_list[2] = int(task_list[2])
except ValueError:
    print('Введите числа')

if task_list[0] == "*":
    result = task_list[1] * task_list[2]
elif task_list[0] == "/":
    try:
        task_list[2] != 0
        result = task_list[1] / task_list[2]
    except ZeroDivisionError:
        print('На ноль делить нельзя')
elif task_list[0] == "+":
    result = task_list[1] + task_list[2]
elif task_list[0] == "-":
    result = task_list[1] - task_list[2]

print(f'результат: {result}')


