def apply_all_func(int_list,*functions):
    result={}
    for func in functions:
        result.update({func.__name__:func(int_list)})
    return result

int_list =[6, 20, 15, 9]
func_list_1 = [max, min]
func_list_2 = [len, sum, sorted]

print(apply_all_func(int_list,*func_list_1))
print(apply_all_func(int_list,*func_list_2))
