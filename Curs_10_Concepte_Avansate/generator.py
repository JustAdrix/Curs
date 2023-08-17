def gen():
    print('Am intrat in functia generator')
    yield 10 # yield - a ceda

    print('Am intrat din nou in functia generator')
    yield 100

    print('Am intrat a treia oara in functia generator')
g= gen()
print(next(g))
print(next(g))
# print(next(g))

print('*'*40)
def even_gen(n):
    generated_nr = 0
    curent = 0
    while generated_nr < n:
        curent += 1
        if curent % 2 == 0:
            yield curent
            generated_nr += 1
g2 = even_gen(10)
for i in g2:
    print(i)
