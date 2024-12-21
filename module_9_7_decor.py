def is_print(func):
    def wrapper(*args):
        result = func(*args)
        if isinstance(result,int):
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_print
def sum_three(n1,n2,n3):
    return n1+n2+n3

res1 = sum_three(2,3,6)
print(res1)

res2 = sum_three(2,3,6.5)
print(res2)
