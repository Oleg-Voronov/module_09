first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x)-len(y)) for x,y in zip(first,second) if len(x) != len(y))
second_result = []

for i in range(0,min(len(first),len(second))):
    if len(first[i]) == len(second[i]):
        second_result.append(True)
    else:
        second_result.append(False)

print(list(first_result))
print(list(second_result))
