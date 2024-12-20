def all_variants(text):
    L_ = len(text)
    sub_str_len = 1
    while sub_str_len <= L_ :
        k = 0 # курсор в строке
        while k <= L_-sub_str_len :
            yield text[k:k+sub_str_len]
            k+=1
        sub_str_len+=1

obj = all_variants('топинамбур')
for i in obj:
    print(i)
