def fibinachi_func():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 0
set_numb = {5, 200, 1000, 100000}
for numb in fibinachi_func():
    count += 1
    if count in set_numb:
        print(f"{count}-е число будет {numb}")
    if count >= max(set_numb):
        break
