PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list_price = [x.split(' ') for x in PRICE_LIST.split('\n')]
dict_price = {x[0]: int(x[1][:-1]) for x in list_price}
print(dict_price)
