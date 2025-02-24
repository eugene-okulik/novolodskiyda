my_dict = {
    'tuple': ('ert', 23, True, 23.5, [True, False]),
    'list': ['dhet', 2, False, 34.5, ['a', 'b', 'c']],
    'dict': {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'},
    'set': {1, 4, 56, 'djf', False}
}
# 1
print(my_dict['tuple'][-1])

# 2
list_in_dict = my_dict['list']
list_in_dict.append('new element')
list_in_dict.pop(1)

# 3
dict_in_dict = my_dict['dict']
dict_in_dict[('i am a tuple',)] = False
dict_in_dict.pop(5)

# 4
set_in_dict = my_dict['set']
set_in_dict.add(999)
set_in_dict.pop()

# 5
print(my_dict)
