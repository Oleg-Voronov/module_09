first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = []
second_result = []

for f_,s_ in zip(first,second):
    k=abs(len(f_) - len(s_))
    if k != 0:
        first_result.append(k)

for i in range(0,min(len(first),len(second))):
    if len(first[i]) == len(second[i]):
        second_result.append(True)
    else:
        second_result.append(False)

print(list(first_result))
print(list(second_result))
