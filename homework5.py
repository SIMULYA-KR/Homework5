immutable_var = 1, 2, 3, "dog", False
print(immutable_var)
#immutable_var[0] = 66
#print(immutable_var)    # Кортеж являеться неизменяемой коллекцией.
mutable_list = [1, 3, 4, 2, "cat", True]
print(mutable_list)
mutable_list[0] = 77
mutable_list[1] = 699
mutable_list[2] = 1
mutable_list[3] = 23
print(mutable_list)