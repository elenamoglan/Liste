with open ('input.txt','r') as f:
    prenume=f.readline().strip().split(',')
    varsta=list(eval(f.readline()))
print('a)', end=(' '))
for i in range(0,len(prenume)):
    print(f'{prenume[i]} are varsta de {varsta[i]} ani')
    i+=1
prenume.extend(['Andreea', 'Ioan'])
varsta.extend([34,23])
print(f'b) {prenume}\n{varsta}')
del varsta[prenume.index('Ana')]
del prenume[prenume.index('Ana')]
print(f'c) {prenume}\n{varsta}')
print('d)', prenume[:3])
print('e)', prenume[::-1])
print(f'f) {prenume[2]}, {prenume[4]}, {varsta[2]}, {varsta[4]}')
print(prenume[:6])
print(varsta[:6])