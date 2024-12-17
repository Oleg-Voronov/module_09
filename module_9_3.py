first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x)-len(y)) for x,y in zip(first,second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(0,min(len(first),len(second))))

print(list(first_result))
print(list(second_result))
