from random import choice

class Magic_Words:
    def __init__(self,*words_):
        self.words = words_
    def __call__(self):
        return choice(self.words)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name,'w',encoding='utf-8') as file:
            for elem in data_set:
                file.write(str(elem)+'\n')
    return write_everything

# Метод __call__
m_words = Magic_Words('Да', 'Нет', 'Наверное','Наверняка','Вряд-ли')
for i in range(0,10):
    print(m_words())

# "Замыкание"
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = map(lambda x,y : x == y , first,second )
print(list(result))
