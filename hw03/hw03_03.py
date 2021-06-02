str_obj = 'papa'

sub_set =  {hash(str_obj[i:j]) for i in range(len(str_obj)) for j in range(len(str_obj), i, -1) if str_obj[i:j] != str_obj}
print(sub_set)
print(f'{len(sub_set)} уникальных подстрок')