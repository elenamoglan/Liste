a = list(map(int,input('Introduceti numerele listei (prin spatiu): ').split()))
print('lista 1 =', a)
b=sorted(a)
print('lista 2 =', b)
c=sorted(a, reverse=True)
print('lista 3 =', c)
print(f'Numarul de elemente din lista = {len(a)}, elementul MAX = {max(a)}, elementul MIN = {min(a)}')
print('lista 4 =', a + [111])
a[1]=222
print('lista 5 =', a)
